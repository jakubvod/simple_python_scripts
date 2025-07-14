from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path

script_dir = Path(__file__).parent
cache_path = script_dir / ".cache"

client_id = "12e742c3462e46e982c9985b856d8b94"
client_secret = "1a612e4b00a34822997a41a451196b27"
redirect_uri = "http://localhost:8888/callback"
scope = "user-modify-playback-state,user-read-playback-state"
sp = Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               cache_path=cache_path))


track_uri = "spotify:track:6mFkJmJqdDVQ1REhVfGgd1" # Pink Floyd - Wish You Were Here

def play_pink_floyd():
    devices = sp.devices()
    print("Devices:", devices)
    if not devices["devices"]:
        print("No active devices found. Open spotify on a device and try again.")
        return
    device_id = devices["devices"][0]["id"]
    sp.start_playback(device_id=device_id, uris=[track_uri], position_ms=94000)  # Start playback at 1:34:00

def main():
    print("\n-----------------------------------\nPlaying Pink Floyd - Wish You Were Here\n-----------------------------------\n")
    play_pink_floyd()

if __name__ == "__main__":
    main()