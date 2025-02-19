from ultralytics import YOLO


model = YOLO("yolo11n-seg.pt")  


results = model("video.mp4", task="segment", save=True)


print("The segmented video has been saved in:", results[0].save_dir)
