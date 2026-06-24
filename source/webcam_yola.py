import cv2 
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# open webcam, 0 = default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not accessible.")
    exit

while True:
    # capture frame by frame
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive frame.")
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO webcam", annotated_frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    