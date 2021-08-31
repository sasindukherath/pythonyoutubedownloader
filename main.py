'''
YouTube Video Downloader
Author: Sasindu K Herath
'''

#import the package
from pytube import YouTube grijighhhjgjkrji gjyrhhfjjsjuthhgjrgyrurii igurp

url = 'your url'
my_video = YouTube(url)

print("*********************Video Title************************")
#get Video Title
print(my_video.title)

print("********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)

