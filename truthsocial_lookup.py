import cloudscraper
import json

requests = cloudscraper.create_scraper()

username = input(" • Enter Your Username: ")

url = f"https://truthsocial.com/api/v1/accounts/lookup?acct={username}"

HEADERS = {"User-Agent": "Mozilla;"}

response = requests.get(url, headers=HEADERS)
# print(response.text)
try:
    data = response.json()

    if data.get("username"):
        print(json.dumps(data, indent=2, ensure_ascii=False))

    elif "errors" in data:
        try:
            error = data["errors"][0].get("error_message", "Unknown error")
            print("Error:", error)
        except:
            print("Error:", data)

    else:
        print("HTTP Error:", response.status_code)

except Exception as e:
    print("Parse Error:", str(e))
