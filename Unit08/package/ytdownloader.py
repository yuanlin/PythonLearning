from pytube import YouTube

def download(url):
    yt = YouTube()
    yt.url = url
    video = yt.get('mp4', '360p')
    video.download('./')
    return yt.filename