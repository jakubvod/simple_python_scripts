from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path
import random

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


def get_artist_id_name(artist_name: str) -> tuple[str, str] | None:
    searched = sp.search(q=artist_name, type="artist", limit=1)
    if not searched["artists"]["items"]:
        print("Couldn't find any artist with that name.")
        return None
    return searched["artists"]["items"][0]["id"], searched["artists"]["items"][0]["name"]

def play_top_track_random(artist_name: str) -> None:
    result = get_artist_id_name(artist_name)
    if not result:
        return None
    artist_id, name  = result
    top_tracks = sp.artist_top_tracks(artist_id)["tracks"]

    if not top_tracks:
        print("Artist has no tracks.")
        return None
    
    track = random.choice(top_tracks)
    print(f"\n------------------------------------------\nPlaying {track['name']} by {name}\n------------------------------------------\n")

    devices = sp.devices()
    if not devices["devices"]:
        print("\n------------------------------------------\nNo active devices found. Open spotify on a device and try again.\n------------------------------------------\n")
        return
    device_id = devices["devices"][0]["id"]
    sp.start_playback(device_id=device_id, uris=[track["uri"]])

def main() -> None:
    chosen_artist = input("\n------------------------------------------\nEnter the name of the artist: ")
    play_top_track_random(chosen_artist)

if __name__ == "__main__":
    main()