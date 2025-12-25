from ultralytics import YOLO
import cv2

model = YOLO("yolo11s.pt")

results = model.predict(source="0", show=True)

for k in results:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()