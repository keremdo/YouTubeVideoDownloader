import pytube

url = input("Enter Video Url : ")
path = "\YouTubeVideos"

pytube.YouTube(url).streams.get_highest_resolution().download(path)