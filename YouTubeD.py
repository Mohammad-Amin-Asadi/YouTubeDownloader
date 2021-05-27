import os
from pytube import YouTube
import geocoder
import requests
import functions as func


# try:
while True:
    ULR_VALIDATION = 0
    check_connection=func.check_internet()
    func.check_ip(check_connection)
    youtube_video = func.ULR_VALIDATION(ULR_VALIDATION)

    #Get the link from user
    print("collecting data")
    
    # show the video title
    print("Title :" ,youtube_video.title )
    
    #show the video length
    videoLength =youtube_video.length
    print("Length :" , f"{videoLength} " + "second")
    print("Data collected")
    
    #Lets let the user choose the quality of his video 
    User_menu_choice=input("If you want to download the video with the hoghest resolutoin you can write | highest | or | h |\n and for downloading the video with the lowest resolution you have to write | lowest | or | low  | \n you can download video with any resolution you want to with typing |dvr| or |different rent video resolutions| \n also you can download video and audio with different nt resolution Separately, just write |dr| : ")
    
    if User_menu_choice == "low" or User_menu_choice == "lowest" or User_menu_choice == "lower":

        # get the name of video that the user want to have with it in his dirctory
        fname = input("Enter your video name : ")
        fpath = input("enter your file path :")

        # choose the lowest quality for the user with the pytube library
        ys = youtube_video.streams.get_lowest_resolution()
        print("Start downloading")
        ys.download(output_path=fpath,filename=fname)
        print("Download finished")

    elif User_menu_choice == "high" or User_menu_choice == "highest" or User_menu_choice == "higher":

        # choose the highest quality for the user with the pytube library
        fname = input("Enter your video name : ")
        fpath = input("enter your file path :")
        ys = youtube_video.streams.get_highest_resolution()
        print("start downloading")
        ys.download(output_path=fpath,filename=fname)
        print("Download finished")

    elif User_menu_choice == "dr":

        # choose the favorite quality for the user with the pytube library
        fname = input("Enter your video name : ")
        faname = input("Enter your audio name : ")
        reso=input("enter your resolution number|720p,480p,360p,240p,144p| :")
        fpath = input("enter your file path :")
        if fpath == '':
            fpath = None

        func.check_reso(reso)

        # showing video itags to user for choosing favorie quality
        print("Collecting data")
        print(youtube_video.streams.filter(only_video=True))
        print("Data collected")  
        itag = input("Enter your itag number : ")
        video_choosen = youtube_video.streams.get_by_itag(itag)

        # showing audio itags to user for choosing favorie quality
        print("Collecting your audio data")
        print(youtube_video.streams.filter(only_audio=True))
        itag = input("Enter your itag number : ")
        audio_choosen = youtube_video.streams.get_by_itag(itag)
       
        func.download_separately(video_choosen , audio_choosen , fname, fpath , faname)

    elif User_menu_choice == "dvr" or User_menu_choice == "different  video resolutions":
        reso=input("enter your resolution : ")
        reso_final=func.check_reso(reso)
        func.download_video(reso_final , youtube_video)
    else:
        fpath = input("enter your file path")
        ys = youtube_video.streams.get_highest_resolution()
        print("Start downloading")
        ys.download(output_path=fpath,filename=fname)
        print("Download finished")          
# except:
#     print("App closed ")
    
#     print("Made by:pRANk3shTAIn  created in  :2021/3/23")