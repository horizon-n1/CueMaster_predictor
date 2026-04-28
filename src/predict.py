from ultralytics import YOLO
import cv2

# 1. Load the model
model = YOLO("resources/model/best.pt")

window_name = "Pool AI - High Performance"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1280, 720)

# 2. Run the prediction with performance tweaks
results = model.predict(
    source="resources/raw/pool_edited.mp4", 
    stream=True, 
    conf=0.1,        # Lowering this helps find the Cue Ball
    vid_stride=2,     # Skips every other frame to eliminate lag
    imgsz=640         # Ensures it stays at the fast internal resolution
)

for r in results:
    # Use r.plot() to get the image with boxes
    # labels=True, boxes=True are default, but we ensure they are on
    annotated_frame = r.plot()
    
    cv2.imshow(window_name, annotated_frame)
    
    # 30ms delay matches a standard 30fps video speed
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()