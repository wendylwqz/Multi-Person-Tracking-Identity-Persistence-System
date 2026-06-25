import cv2
import torchreid
from ultralytics import YOLO
from torch.nn.functional import cosine_similarity

# configuration variable
SIMILARITY_THRESHOLD = 0.72

memory_bank = {}                                # memory bank of IDs and features

cap = cv2.VideoCapture(0)                       # webcam
detector = YOLO("yolov8n.pt")                   # model
extractor = torchreid.utils.FeatureExtractor(   # feature extractor
    model_name="osnet_x1_0",
    device="cpu"
)

if not cap:
    print("Camera not accessible.")
    exit

next_persistent_id = 1

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive frame.")
        break

    results = detector.track(frame, persist=True, classes=[0], tracker="bytetrack.yaml")

    annotated = frame.copy()

    boxes = results[0].boxes

    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()
            person_crop = frame[y1:y2, x1:x2]

            if person_crop.size == 0:
                continue

            embedding = extractor(person_crop)

            # attempt to find person match in memory bank
            best_id = None
            best_score = 0

            for person_id, person_embedding in memory_bank.items():
                score = cosine_similarity(embedding, person_embedding).item()

                if score > best_score:
                    best_score = score
                    best_id = person_id

            # if person is similar enough, id them; otherwise add person to memory bank
            if best_score >= SIMILARITY_THRESHOLD:
                persistent_id = best_id
            else:
                persistent_id = next_persistent_id
                memory_bank[persistent_id] = embedding
                next_persistent_id += 1
            
            # draw tracker box 
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated, f"ID: {persistent_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Persistant Tracker", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()




