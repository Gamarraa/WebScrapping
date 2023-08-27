import requests
from bs4 import BeautifulSoup
import re

# Send a GET request to the webpage
url = "https://founderz.com/program_lessons"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the iframe element
iframe_element = soup.find('iframe', {'id': 'founderzvideo'})

# Extract the video URL from the iframe source attribute
video_src = iframe_element['src']

# Extract the Vimeo video ID from the video URL
video_id = re.search(r'video/(\d+)', video_src).group(1)

# Construct the final video URL
video_url = f"https://vimeo.com/{video_id}"

print("Video URL:", video_url)



