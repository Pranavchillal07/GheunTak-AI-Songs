import os
import requests
from dotenv import load_dotenv  # 🛠 dotenv Package Import 

# 🔥 `.env` फाइल Load करतो
if os.path.exists(".env"):
    load_dotenv()
    print("✅ `.env` File Loaded Successfully!")
else:
    print("❌ ERROR: `.env` File Not Found! कृपया `.env` फाइल अपलोड करा.")
    exit()  # 🛑 Script थांबवतो

# 🔑 API Key आता `.env` मधून घेतोय
RIFFUSION_API_KEY = os.getenv("RIFFUSION_API_KEY")

# 📌 API Key Verify करतो
if not RIFFUSION_API_KEY:
    print("❌ ERROR: `.env` मध्ये `RIFFUSION_API_KEY` सापडला नाही! कृपया योग्य Key टाका.")
    exit()  # 🛑 Script थांबवतो

# 🎵 AI Beat Generate (Riffusion)
def generate_ai_beat(prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {RIFFUSION_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"version": "riffusion/riffusion", "input": {"prompt": prompt, "alpha": 0.7}}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("output")
    else:
        print("⚠️ ERROR: API Request Failed", response.text)
        return None

# 🚀 Main Execution
if __name__ == "__main__":
    print("🎵 AI Beat बनवत आहे...")
    beat_url = generate_ai_beat("Marathi dhol-tasha with trap bass")
    
    if beat_url:
        print("🔥 Generated Beat URL:", beat_url)
    else:
        print("❌ Beat Generate करायला अपयश आले.")
