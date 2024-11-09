class MusicQueue:
    def __init__(self):
        self.queues = {}  # Dictionary to hold queues for each guild
        self.playlists = {}  # Dictionary to hold playlists for each guild
        self.current_songs = {}  # Dictionary to hold current song for each guild

    def add_queue(self, guild_id, song):
        """เพิ่มเพลงลงในคิวเพลงของ guild"""
        if song:
            if guild_id not in self.queues:
                self.queues[guild_id] = []
            self.queues[guild_id].append(song)
            print(f"Added song to queue for guild ")

    def add_playlist(self, guild_id, playlist):
        """เพิ่มลิสต์ของเพลงลงในเพลย์ลิสต์ของ guild"""
        if isinstance(playlist, list) and all(isinstance(song, dict) for song in playlist):
            if guild_id not in self.playlists:
                self.playlists[guild_id] = []
            self.playlists[guild_id].extend(playlist)
            print(f"Added playlist to guild ")

    def add_current_song(self, guild_id, song):
        """ตั้งค่าเพลงปัจจุบันของ guild"""
        if song:
            self.current_songs[guild_id] = song
            print(f"Set current song for guild ")

    def pop_queue(self, guild_id):
        """ลบและคืนค่าเพลงแรกจากคิวเพลงของ guild"""
        song = self.queues[guild_id].pop(0) if guild_id in self.queues and self.queues[guild_id] else None
        print(f"Popped song from queue for guild")
        return song
    
    def pop_playlist(self, guild_id):
        """ลบและคืนค่าเพลงแรกจากเพลย์ลิสต์ของ guild"""
        song = self.playlists[guild_id].pop(0) if guild_id in self.playlists and self.playlists[guild_id] else None
        print(f"Popped song from playlist for guild ")
        return song
     
    def clear_queue(self, guild_id):
        """ล้างคิวเพลงของ guild ให้ว่างเปล่า"""
        if guild_id in self.queues:
            self.queues[guild_id].clear()
            print(f"Cleared queue for guild ")

    def clear_playlist(self, guild_id):
        """ล้างเพลย์ลิสต์ของ guild ให้ว่างเปล่า"""
        if guild_id in self.playlists:
            self.playlists[guild_id].clear()
            print(f"Cleared playlist for guild ")

    def move_playlist_to_queue(self, guild_id):
        """ย้ายเพลงแรกจากเพลย์ลิสต์ไปยังคิวเพลงของ guild"""
        if guild_id in self.playlists and self.playlists[guild_id]:
            if guild_id not in self.queues:
                self.queues[guild_id] = []
            song = self.playlists[guild_id].pop(0)
            print(song)
            self.queues[guild_id].append(song)
            print(f"Moved song from playlist to queue for guild ")



