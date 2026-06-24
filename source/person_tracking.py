import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

if not cap:
    print("Camera not accessible.")
    exit

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive frame.")
        break

    # track ppl only with classes=0
    results = model.track(frame, persist=True, classes=[0], tracker="bytetrack.yaml")

    annotated_frame = results[0].plot()
    cv2.imshow("Person tracker", annotated_frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()