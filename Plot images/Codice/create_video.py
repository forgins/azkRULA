import subprocess
import os

# Replace these paths with your actual image file names and output video file name
image_folder = 'immagini'
output_video = 'video.mp4'

# Get a list of image filenames in the folder
#image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])

image_files = [f"frame_{i}.png" for i in range(len(os.listdir(image_folder)))]
# FFmpeg command to create the video
ffmpeg_cmd = [
    'ffmpeg',           # FFmpeg executable
    '-framerate', '60', # Frame rate of the video (frames per second)
    '-i', '-',          # Input from pipe
    '-c:v', 'libx264',  # Video codec
    '-pix_fmt', 'yuv420p',  # Pixel format
    output_video        # Output video file name
]

# Run FFmpeg and provide the list of images as input
with subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE) as proc:
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        with open(image_path, 'rb') as f:
            proc.stdin.write(f.read())

# Close the input stream
proc.stdin.close()
proc.wait()
