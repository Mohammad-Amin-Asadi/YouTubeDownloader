import os
from pytube import YouTube
import geocoder
import requests
def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        os.system('color 4')
    return False

try:
    while True:
        check_connection=check_internet()
        if check_connection == True :
            g =geocoder.ip('me')
            ip_info = str(g.geojson)
            if 'IR' in ip_info:
                os.system('color 4')
                print('As you live in Iran please turn on your VPN or connect to a proxy and restart the program')
                print("app closed!")
                break
            else:
                os.system('color 2')
                print("Ready to use")
        else:
            os.system('color 4')
            print("please check your internet connection first and run the app again!")
            print("app closed!")
            break

        # A Welcome text

        #Get the link from user
        l=1
        while l == 1:
            try:
                link = input("enter the link => ")
                os.system('color 7')
                # make ready the link to Collecting data from youtube 
                yl = YouTube(link)
                l = 2
            except:
                print("please enter a valid url")
        
        print("collecting data")
        # show the video title

        print("Title :" , yl.title)

        #show the video length

        videoLength =int(yl.length)
        print("Length :" , f"{int(videoLength / 60)+1} " + "min")
        print("Data collected")

        #Lets let the user choose the quality of his video 

        h_or_l=input("If you want to download the video with the hoghest resolutoin you can write | highest | or | h |\n and for downloading the video with the lowest resolution you have to write | lowest | or | low  | \n you can download video with any resolution you want to with typing |dvr| or |diffrerent video resolutions| \n also you can download video and audio with diffrent resolution Separately, just write |dr| : ")
        

        if h_or_l == "low" or h_or_l == "lowest" or h_or_l == "lower":

            # get the name of video that the user want to have with it in his dirctory

            fname = input("Enter your video name : ")
            fpath = input("enter your file path :")

            # choose the lowest quality for the user with the pytube library

            ys = yl.streams.get_lowest_resolution()
            print("Start downloading")
            ys.download(output_path=fpath,filename=fname)
            print("Download finished")

        elif h_or_l == "high" or h_or_l == "highest" or h_or_l == "higher":

            # choose the highest quality for the user with the pytube library

            fname = input("Enter your video name : ")
            fpath = input("enter your file path :")
            ys = yl.streams.get_highest_resolution()
            print("start downloading")
            ys.download(output_path=fpath,filename=fname)
            print("Download finished")

        elif h_or_l == "dr":

            # choose the favorite quality for the user with the pytube library


            fname = input("Enter your video name : ")
            faname = input("Enter your video name : ")
            reso=input("enter your ressolution number|720p,480p,360p,240p,144p| :")
            fpath = input("enter your file path :")
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

            # showing itags to user for choosing favorie quality

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

        elif h_or_l == "dvr" or h_or_l == "diffrerent video resolutions":
            reso=input("enter your resolution : ")
            if reso == "720px" or reso == "720" or reso == "720p":
                reso = "720p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
            elif reso == "480px" or reso == "480" or reso == "480p":
                reso = "480p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
            elif reso == "360px" or reso == "360" or reso == "360p":
                reso = "360p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
            elif reso == "240px" or reso == "240" or reso == "240p":
                reso = "240p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
            elif reso == "144px" or reso == "144" or reso == "144p":
                reso = "144p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
            else:
                reso = "720p"
                print("Start downloading")
                yl.streams.filter(res=reso).first().download()
                print("Download finished")
        else:
            fpath = input("enter your file path")
            ys = yl.streams.get_highest_resolution()
            print("Start downloading")
            ys.download(output_path=fpath,filename=fname)
            print("Download finished")          
except:
    print("App closed ")
    
    print("Made by:pRANk3shTAIn  created in  :2021/3/23")