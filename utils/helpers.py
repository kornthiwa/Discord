import re
import urllib.parse
import urllib.request

yt_dl_song_options = {
    'format': 'bestaudio',  # เปลี่ยนเป็น 'bestaudio' เพื่อให้ได้คุณภาพเสียงที่ดีที่สุด
    'extractaudio': True,  # ระบุให้ดึงเฉพาะเสียง
    'audioformat': 'mp3',  # กำหนดรูปแบบเสียงเป็น MP3
    'noplaylist': True,  # ไม่อนุญาตให้ดาวน์โหลดเพลย์ลิสต์
    'nocheckcertificate': True,  # ปิดการตรวจสอบใบรับรอง SSL
    'ignoreerrors': False,  # หยุดกระบวนการหากเกิดข้อผิดพลาด
    'quiet': True,  # ปิดการแสดงข้อความ
    'no_warnings': True,  # ปิดการแสดงข้อความเตือน
    'default_search': 'auto',  # ใช้การค้นหาอัตโนมัติหากไม่มี URL
    'extract_flat': False  # ไม่เปิดใช้งานการดึงข้อมูลเพลย์ลิสต์แบบเร็ว
}

yt_dl_playlist_options = {
    'extract_flat': True,
    'skip_download': True,
    'quiet': True,
}
# yt_dl_options = {"format": "bestaudio/best",'noplaylist': True,}
ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.25"'}
youtube_base_url = 'https://www.youtube.com/'
youtube_results_url = youtube_base_url + 'results?'
youtube_watch_url = youtube_base_url + 'watch?v='

def get_youtube_link(search_query):
    """ค้นหาและส่งกลับลิงก์ YouTube สำหรับคำค้นหาที่กำหนด"""
    # ตรวจสอบว่าคำค้นหาเป็น URL YouTube ประเภทต่าง ๆ หรือไม่
    if is_url_youtube(search_query):
        # ถ้าเป็นลิงก์ YouTube วิดีโอ ให้ส่งกลับลิงก์นั้นโดยตรง
        return search_query
    elif is_url_youtube_music(search_query):
        # ถ้าเป็นลิงก์ YouTube Music ให้ส่งกลับลิงก์นั้น
        return search_query
    elif is_url_youtube_playlist(search_query):
        # ถ้าเป็นลิงก์เพลย์ลิสต์ YouTube ให้ส่งกลับลิงก์นั้น
        return search_query
    else:
        # ถ้าไม่ใช่ลิงก์ YouTube ให้ค้นหาวิดีโอด้วยคำค้นหา
        return is_url_query(search_query)

def is_url_query(search_query):
    """ค้นหาวิดีโอ YouTube โดยใช้คำค้นหาและส่งกลับลิงก์วิดีโอ"""
    query_string = urllib.parse.urlencode({'search_query': search_query})
    content = urllib.request.urlopen(youtube_results_url + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})', content.read().decode())
    if search_results:
        return youtube_watch_url + search_results[0]
    return None

def is_url_youtube(url):
    """ตรวจสอบว่าลิงก์เป็น YouTube วิดีโอหรือไม่"""
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_regex, url) is not None

def is_url_youtube_music(url):
    """ตรวจสอบว่าลิงก์เป็น YouTube Music หรือไม่"""
    youtube_music_regex = re.compile(
        r'(https?://)?(music\.)?(youtube)\.(com)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return re.match(youtube_music_regex, url) is not None

def is_url_youtube_playlist(url):
    """ตรวจสอบว่าลิงก์เป็นเพลย์ลิสต์ YouTube หรือไม่"""
    youtube_playlist_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(playlist\?list=)([a-zA-Z0-9-_]+)')
    return re.match(youtube_playlist_regex, url) is not None

def create_youtube_watch_url(video_id):
    """รับ ID ของวิดีโอ YouTube และส่งกลับลิงก์วิดีโอ"""
    return youtube_watch_url + video_id

def create_youtube_music_url(video_id):
    """รับ ID ของวิดีโอ YouTube และส่งกลับลิงก์ YouTube Music"""
    youtube_music_base_url = 'https://music.youtube.com/watch?v='
    return youtube_music_base_url + video_id
