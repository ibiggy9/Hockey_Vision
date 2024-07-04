import cv2

def read_video():
    cap = cv2.VideoCapture('input_videos/game_7.mp4')
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output_videos/output.avi', fourcc, 24.0, (output_video_frames[0].shape[1],output_video_frames[0].shape[0]))
    for frame in read_video():
        out.write(frame)
    out.release()