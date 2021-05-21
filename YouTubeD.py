import moviepy
from pytube import YouTube
from moviepy.editor import *
import time
print("Welcome to YouTubeD ! Note: please check your internet connection first;)")
link = input("enter the link => ")
yl = YouTube(link)
print("collecting data")
print("Title :" , yl.title)
print("Length :" , yl.length)
print("Data collected")
h_or_l=input("If you want to download the video with the hoghest resolutoin you can write | highest | or | h |\n and for downloading the video with the lowest resolution you have to write | lowest | or | low | \n also you can download video and audio with diffrent resolution Separately, just write |dr| : ")
fname = input("Enter your video name : ")
faname = input("enter your audio name : ")
if h_or_l == "low" or h_or_l == "lowest" or h_or_l == "lower":
    fpath = input("enter your file path :")
    ys = yl.streams.get_lowest_resolution()
    print("Start downloading")
    ys.download(output_path=fpath,filename=fname)
    print("Download finished")
    print("Made by amin")
    time.sleep(10)
elif h_or_l == "high" or h_or_l == "highest" or h_or_l == "higher":
    fpath = input("enter your file path :")
    ys = yl.streams.get_highest_resolution()
    print("start downloading")
    ys.download(output_path=fpath,filename=fname)
    print("Download finished")
    print("Made by amin")
    time.sleep(10)
elif h_or_l == "dr":
    reso=input("enter your ressolution number|720p,480p,360p,240p,144p| :")
    fpath = ''
    if fpath == '':
        fpath = None

    if reso == "720px" or reso == "720" or reso == "720p":
        reso = "720p"
    elif reso == "480px" or reso == "480" or reso == "480p":
        reso = "480p"
    elif reso == "360px" or reso == "360" or reso == "360p":
        reso = "360p"
    elif reso == "240px" or reso == "240" or reso == "240p":
        reso = "240p"
    elif reso == "144px" or reso == "144" or reso == "144p":
        reso = "144p"
    else:
        reso = "720p"

    print("Collecting data")
    print(yl.streams.filter(res=reso))
    print("Data collected")
    itag = input("Enter your itag number : ")
    ysv = yl.streams.get_by_itag(itag)
    print("Collecting your audio data")
    print(yl.streams.filter(only_audio=True))
    itag = input("Enter your itag number : ")
    ysa = yl.streams.get_by_itag(itag)
    print("start downloading video")
    ysv.download(output_path=fpath,filename=fname)
    print("video downloaded")
    print("start downloading audio")
    ysa.download(output_path=fpath,filename=faname)
    print("audio downloaded")
else:
    fpath = input("enter your file path")
    ys = yl.streams.get_highest_resolution()
    print("Start downloading")
    ys.download(output_path=fpath,filename=fname)
    print("Download finished")
    print("Made by amin")
    time.sleep(10)

temp=input("also you can have one file the it has both seprated audio and video together! \n just write |combine| note:you have to download both files in the program folder for this action : ")
if temp == "combine":
    videoclip = VideoFileClip(fname+".mp4")
    audioclip = AudioFileClip(faname+".mp4")
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("new_filename.mp4")
print("Made by:pRANk3shTAIn Date:2021/3/23")