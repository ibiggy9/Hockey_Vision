from utils import read_video, save_video

def main():
    frames = read_video('input_videos/game_7.mp4')
    save_video(frames, 'output_videos/output.avi')

if __name__ == '__main__':
    print("Hi")