from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run detection on an example image
results = model("https://ultralytics.com/images/bus.jpg")

# Display the result
results[0].show()

print("Detection complete!")
