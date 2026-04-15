import cloudscraper, json

requests = cloudscraper.create_scraper()

url = "https://truthsocial.com/api/v1/accounts/update_credentials"

payload = {
  'display_name': "Welcome", # Name
  'note': "This is Bio", # Bio
  'website': "t.me/z_0_g", # Url
  'location': "" # Location 
  
  # -- Update Profile and Cover --
  # 'avatar': 'data:image/jpg;base64,/', 
  # 'header': 'data:image/jpg;base64,/',  
}

headers = {
  'User-Agent': "TruthSocialAndroid/okhttp/5.1.0/1230",
  'authorization': "Bearer idk**", # Token
  'accept-language': "en-US"
}

response = requests.patch(url, data=payload, headers=headers)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))
