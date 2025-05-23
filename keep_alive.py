import requests
import datetime

url = "https://prototype-lbvkcopyxbnjstheegz3qn.streamlit.app/"  # Replace with your Streamlit URL

try:
    response = requests.get(url)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Visited {url} - Status: {response.status_code}")
except Exception as e:
    print(f"[!] Failed to reach {url}: {e}")
