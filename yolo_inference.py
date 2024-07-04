from ultralytics import YOLO

model = YOLO('models/best.pt')


results = model.predict("input_videos/game_7.mp4", save=True, device="mps")  

#First Frame
print(results[0])

for box in results[0].boxes:
    print(box)

