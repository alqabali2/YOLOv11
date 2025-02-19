from ultralytics import YOLO


model = YOLO("yolo11n.pt")

results = model("video.mp4", save=True)


print("The output video has been saved in:", results[0].save_dir)
