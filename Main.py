from pytube import YouTube
from sys import argv
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

url = input("Your URL: ")
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download('file path after download your video.')
