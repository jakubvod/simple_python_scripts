# python_scripts
**❗FOR LEARNING PURPOSES❗**
- Small and simple Python scripts I wrote while learning and refreshing my skills.
- These are just practice projects to explore libraries and concepts like filesystem handling or API usage.
## 📂 SUFFIX READER - Reads all suffixes in a directory (with optional filtering). The script must be placed inside the target directory.
**Skills used:**
- Working with the file system using pathlib.
- Handling user input.
## 🎵 SPOTIPY SCRIPT - Given an artist input, the script randomly plays one of their 10 most popular songs (Spotify premium required).
**Skills used:**
- Managing sensitive data with ".env" and ".gitignore".
- Working with Spotipy and OAuth.

> ⚠️ Note
To use it, follow these steps.
1. Create `.env` file with the following format:
```
CLIENT_ID = 'xxxxxxxxx'
CLIENT_SECRET = 'xxxxxxxxx'
REDIRECT_URI = 'http://localhost:8888/callback'
```
2. Get your ID and SECRET from [Spotify's Dashboard](https://developer.spotify.com/dashboard)
   > (you need to create an app) and replace the xxxxxxxxx values with your credentials.
