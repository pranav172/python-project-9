import requests
from requests.auth import HTTPBasicAuth

Client_id = "cdf81c2b2fe741dca008ae9963d68e38"
Client_secret = "db460a18445e44d482bbb1ee1b3ba182"

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(Client_id, Client_secret)

response = requests.post(url, data=data, auth=auth)

# Check for successful token retrieval
if response.status_code != 200:
    print("Error getting access token:", response.json())
    exit()

accessToken = response.json()["access_token"]

artist = input("Artist: ").lower()
artist = artist.replace(" ", "%20")

url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {accessToken}"}
search = f"?q=artist%3A{artist}&type=track&limit=5"

fullURL = f"{url}{search}"
print("Full URL:", fullURL)  # Debugging print

response = requests.get(fullURL, headers=headers)

# Check for successful search request
if response.status_code != 200:
    print("Error during search:", response.json())
    exit()

data = response.json()

# Check if tracks were found
if "tracks" not in data or "items" not in data["tracks"]:
    print("No tracks found for the artist.")
    exit()

for track in data["tracks"]["items"]:
    print(track["name"])
    print(track["external_urls"]["spotify"])



# print(response.ok)
# print(response.json())
# print(response.status_code)