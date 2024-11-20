import csv
import re
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import VideoFileClip, AudioFileClip
import os

# Function to sanitize file names
def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

# Load URLs from CSV file
csv_file = input("Enter the path to the CSV file containing URLs: ")

with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    url_list = [row[0] for row in reader]  # Assuming URLs are in the first column

# Process each URL
for i, url in enumerate(url_list):
    try:
        print(f"Processing {i+1}/{len(url_list)}: {url}")
        
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading: {yt.title}")

        # Sanitize the video title for use in a filename
        sanitized_title = sanitize_filename(yt.title)

        # Get video and audio streams
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

        # Download video and audio with fixed filenames
        video_stream.download(filename='video.mp4')
        audio_stream.download(filename='audio.mp4')

        # Combine video and audio
        video_clip = VideoFileClip('video.mp4')
        audio_clip = AudioFileClip('audio.mp4')
        final_clip = video_clip.set_audio(audio_clip)

        # Save the final video file using the sanitized title
        output_filename = f'{sanitized_title}.mp4'
        final_clip.write_videofile(output_filename, codec='libx264')
        print(f"Downloaded and combined video saved as: {output_filename}")

        # Cleanup
        video_clip.close()
        audio_clip.close()

    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")