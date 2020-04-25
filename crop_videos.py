from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--video_path", type = str, required = True)
parser.add_argument("--smin", type = int , required = True)
parser.add_argument("--ssec", type = int, required = True)
parser.add_argument("--emin", type = int, required = True)
parser.add_argument("--esec", type = int, required = True)
parser.add_argument("--output_path", type = str, required = True)
args = parser.parse_args()


video_path = args.video_path
video_name = os.path.basename(video_path)

start_min = args.smin
start_sec = args.ssec
end_min = args.emin
end_sec = args.esec

start_time = (start_min*60 + start_sec) - 3
if(start_time < 0):
    start_time = 0

end_time = end_min*60 + end_sec

ffmpeg_extract_subclip("{}".format(video_path), start_time, end_time, targetname= os.path.join(args.output_path, "{}_cropped.mp4".format(video_name[:-4])))