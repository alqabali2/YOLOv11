from ultralytics import YOLO

# تحميل النموذج
model = YOLO("yolo11n-cls.pt")

# تنفيذ اكتشاف الأجسام على الصورة
results = model("image.jpg")

# عرض النتائج
results[0].show()
