#Import Libraries
import webbrowser
import tkinter
import pytube
import requests
import pyshorteners
import os
#Functions
def shortenURL():
    url=input("Enter the URL you would like to shorten: ")
    newurl=pyshorteners.Shortener().tinyurl.short(url)
    print("Your new URL is ", newurl)
def downloadYouTube():
    videourl=input("Input the video URL of your YouTube video: ")
    youtube=pytube.YouTube(videourl)
    video=youtube.streams.get_highest_resolution()
    video.download()
    print("Video downloaded")
def downloadFavicon():
    url=input("Enter the ROOT of the URL of the website you would like to download the favicon icon of (e.g. https://www.example.com): ")
    newurl=url + '/favicon.ico'
    x=requests.get(newurl)
    ico = open('favicon.ico', 'wb').write(x.content)
    print("favicon.ico downloaded")
def downloadHTML():
    url=input("Enter the ROOT of the URL of the website you  would like to download index.html from (e.g. https://www.example.com): ")
    newurl=url + '/index.html'
    x=requests.get(newurl)
    html1=open('index.html', 'wb').write(x.content)
    print("Index.html downloaded")
#Tkinter Window
window=tkinter.Tk()
shorturl=tkinter.Button(window, text="Shorten a URL", command=shortenURL).pack()
youtube=tkinter.Button(window, text="Download YouTube video", command=downloadYouTube).pack()
favicon=tkinter.Button(window, text="Download Favicon Icon from Website", command=downloadFavicon).pack()
html=tkinter.Button(window, text="Download index.html file from a website", command=downloadHTML).pack()
window.mainloop()