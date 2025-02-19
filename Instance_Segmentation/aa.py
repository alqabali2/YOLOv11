from ultralytics import YOLO


model = YOLO("yolo11n-seg.pt")  


results = model("image.jpg", task="segment")


results[0].show()
