import cloudscraper, json
# from urllib.parse import urlencode

requests = cloudscraper.create_scraper()

username = input(" ~ Enter your username: ")
password = input(" ~ Enter your password: ")

payload = {
  'client_id': "dKEZb2UwazKgg_gtQ7j-6Rr_AfE3Gs05oGPMV_Oh1pw",
  'client_secret': "C9xyBLoQvL3fhIBtVO0fJ1Z3gN73-ZpWurP73yJmi2U",
  'scope': "read write follow push",
  'grant_type': "password",
  'username': username,
  'password': password
}

url = "https://truthsocial.com/oauth/v2/token" # ? + urlencode(payload) 

acc = "https://truthsocial.com/api/v1/accounts/verify_credentials"

headers = {
  'User-Agent': "TruthSocialAndroid",
  'accept-language': "en-US"
}

response = requests.post(url,data=payload, headers=headers)

try:
    data = response.json()
    if data.get("errors"):
        try:            
            error = data["errors"][0].get("error_message", "Unknown error")
            print("Error:", error)
        except:
            print("Error:", data)
            
    if data.get("access_token"):
        token = data.get("access_token")
                
        headers.update({
         'authorization':
          f"Bearer {token}",
         'x-truth-device-name':
          "UmVkbWkgTm90ZSA5",
        })
        info = requests.get(acc, headers=headers)
        print(json.dumps(info.json(), indent=2, ensure_ascii=False))

    else:
        print("HTTP Error:", response.status_code)
        
except Exception as e:
    print("Parse Error:", str(e))
