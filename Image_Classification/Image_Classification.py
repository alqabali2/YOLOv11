from ultralytics import YOLO

# تحميل نموذج تصنيف الصور
model = YOLO("yolo11n-cls.pt")  # تأكد من أنك تستخدم النموذج الصحيح
