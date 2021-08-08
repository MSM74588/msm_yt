from art import *
# from termcolor import colored
from pyfiglet import Figlet
from rich.console import Console
import pytube
from pytube import Playlist
from rich.prompt import Prompt
# from rich.progress import track
from pytube import Channel
from rich.console import Console
from rich.markdown import Markdown
# from tqdm import tqdm  
# import time
# CODE to INHIBIT SLEEP
import os
import ctypes

class WindowsInhibitor:
    '''
    Prevent OS sleep/hibernate in windows; code from:
    https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
    API documentation:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx
    '''
    ES_CONTINUOUS        = 0x80000000
    ES_SYSTEM_REQUIRED   = 0x00000001
    ES_AWAYMODE_REQUIRED = 0x00000040

    def __init__(self):
        pass

    def inhibit(self):
        if os.name == 'nt': #Prevent Windows from going to sleep
            try:
                ctypes.windll.kernel32.SetThreadExecutionState(
                    WindowsInhibitor.ES_CONTINUOUS | \
                    WindowsInhibitor.ES_SYSTEM_REQUIRED)
            except:
                return False
            return True
        else:
            return False

    def uninhibit(self):
        import ctypes
        #print("")
        if os.name == 'nt': #Allow Windows to go to sleep
            try:
                ctypes.windll.kernel32.SetThreadExecutionState(
                    WindowsInhibitor.ES_CONTINUOUS)
            except:
                return False
            return True
        else:
            return False



    ####

# //CODE to INHIBIT SLEEP

console = Console()


# tprint("MSM Youtube Downloader","cybermedum")


######## HD Single video Download Function ###############

def singlevid():
    console.print("\n Enter the Path name to which you want to Download to:", style="reverse #F1ECC3")
    SAVE_PATH = input() #to_do 
    console.print("Enter the Video Link:", style="reverse #F1ECC3")
    link = input()
    yt = pytube.YouTube(link)
    console.print('\n[reverse white]Downloading Video: [/reverse white] \n' + yt.title, style= "bold #F8485E underline")
    # stream = yt.streams.filter(file_extension='mp4').order_by('resolution').desc() #later mutated for download
    # print(stream)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH) 
    console.print('\n Downloaded! \n', style= "reverse #B3E283 underline")

def playlistvid():
    # p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
    console.print("\n Enter the Path name to which you want to Download to:", style="reverse #F1ECC3")
    SAVE_PATH = input() #to_do 
    console.print("Enter the Playlist Link:", style="reverse #F1ECC3")
    link = input()
    p = Playlist(link)
    print('Number of videos in playlist: %s' % len(p.video_urls))
    # p.download_all(SAVE_PATH)
    console.print("\n [#FF4848 blink]DOWNLOADING, PLEASE WAIT[/#FF4848 blink] \n This might take a while, So sitback and Relax \n", style="white bold")
    # for i in trange(len(p.video_urls)):
    # for n in tqdm(range(len(p.video_urls)), desc="Downloading :"):
    for video in p.videos:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            # n+=1
        console.print('     Video Downloaded: ' + video.title, style='bold #5dbdf0')
    console.print('\n Downloaded! \n', style= "reverse #B3E283 underline")

def channelvid():
    console.print("\n Enter the Path name to which you want to Download to:", style="reverse #F1ECC3")
    SAVE_PATH = input() #to_do 
    console.print("Enter the Channel Link:", style="reverse #F1ECC3")
    link = input()
    c = Channel(link)
    print('Number of videos in the Channel: %s' % len(c.video_urls))
    console.print("\n [#FF4848 blink]DOWNLOADING, PLEASE WAIT[/#FF4848 blink] \n This might take a while, So sitback and Relax \n", style="white bold")
    for video in c.videos:
        video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
        console.print('     Video Downloaded: ' + video.title, style='bold #5dbdf0')
    console.print('\n Downloaded! \n', style= "reverse #B3E283 underline")




def main():
    mode = Prompt.ask("Video Download Mode?", choices=["SingleVideo", "FullPlaylist", "WholeChannel"], default="SingleVideo")
    if mode == 'SingleVideo':
        singlevid()
    elif mode == 'FullPlaylist':
        playlistvid()
    elif mode == 'WholeChannel':
        channelvid()
    else:
        console.print('error: Please enter the correct option', style='red reverse')
    







# f = Figlet(font='isometric3')
f2 = Figlet(font='standard')

# print(f.renderText('MSM'))
print(f2.renderText('MSM - YT Downloader'))
decor("barcode1")


# Rich Imported Later as it affects the Banner Text
from rich import print, style

# print("Hello :thumbs_up:")
# console.print("Hello", "World!")
console.print("Download Youtube Videos using this utlity made fully in Python 🤟", style="bold #C9D8B6")
console.print("Made with :coffee:  by [reverse] MandraSaptak Mandal [/reverse]", style="bold #F1ECC3")

# console.print("\n Click [#FF4848]ENTER[/#FF4848] to continue", style=" #FFD371  blink bold")

MARKDOWN = """
# Usage intructions

Youtube Downloader Utility
There are 3 download modes:

1. Single Video:- To download a Single video [You will require the video share link of the specific video]
2. Full Playlist:- To download all the video in a playlist [You will reqire the link of the playlist]
3. Whole Playlist:- To download all the video by a specific a channel [You will require link of the specific channel]

Location:- the location where you want to save the video [you will require the path to the specific folder]
- for Linux, example structure: /home/user/folder
- for Windows, example structure: C:/Users/usr/Videos
- for MacOS, example structure /Users/usr

:: Replace "usr" with your username, and folder with your specific folder 

by MSM > https://mandrasaptak.netlify.app 
"""

md = Markdown(MARKDOWN)

print('\n')
console.print(md, style="bold #EFB1FF")
print('\n')






# MAIN EXECUTION....


while True:
    main() #Code Run First time    
# while True:
#     main()
    loop = Prompt.ask("Download Another Video?", choices=["y", "n"])
    if loop=='y':
        main()
    else:
        quit()















# Use rich prompt

# Current issue is Videos are downloaded in 3ggp format > Solved