import os
from pytube import YouTube
import geocoder
import requests
import functions as func


def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        os.system('color 4')
    return False
    
def check_ip(check_connection):
    if check_connection == True :
        g =geocoder.ip('me')
        ip_info = str(g.geojson)
        if 'IR' in ip_info:
            os.system('color 4')
            print('As you live in Iran please turn on your VPN or connect to a proxy and restart the program')
            os.system.sleep(10)
            exit()
        else:
            os.system('color 2')
            print("Ready to use")
    else:
        os.system('color 4')
        print("please check your internet connection first and run the app again!")
        os.system.sleep(10)
        exit()

def ULR_VALIDATION(ULR_VALIDATION):
    while ULR_VALIDATION == 0:
        try:
            link = input("enter the link => ")
            os.system('color 7')
            # make ready the link to Collecting data from youtube 
            yl = YouTube(link)
            ULR_VALIDATION = 1
            return yl
        except:
            print("please enter a valid url")
def check_reso(reso):
    if "1080" in reso:
        reso = "1080p"
    elif "720" in reso :
        reso = "720p"
    elif "480" in reso :
        reso = "480p"
    elif "360" in reso :
        reso = "360p"
    elif "144" in reso :
        reso = "144p"
    else:
        reso = "720p"
    
    return reso

def download_video(final_reso , youtube_video):
    print("Start downloading")
    youtube_video.streams.filter(res=final_reso).first().download()
    print("Download finished")

def download_separately(video_choosen , audio_choosen , video_file_name , path , audio_file_name ):
    print("start downloading video")
    video_choosen.download(output_path=path,filename=video_file_name)
    print("video downloaded")
    print("start downloading audio")
    audio_choosen.download(output_path=path,filename=audio_file_name)
    print("audio downloaded")