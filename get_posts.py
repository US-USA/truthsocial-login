import cloudscraper, json
from datetime import datetime

requests = cloudscraper.create_scraper()

def format_time(iso_time_str):
    if not iso_time_str:
        return "Unknown time"
    try:
        dt = datetime.fromisoformat(iso_time_str.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return iso_time_str
        
url = "https://truthsocial.com/api/v1/accounts/107780257626128497/statuses"  # Trump User ID

params = {
    'page': "1",
    'limit': "20",
    'pinned': "false",
    'exclude_reblogs': "false",
    'exclude_replies': "true",
    'only_replies': "false",
    'only_media': "false"
}

headers = {
    'User-Agent': "TruthSocialAndroid",
    'authorization': "None",
    'accept-language': "en-US",
}

max_id = None

while True:
    params["max_id"] = max_id
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    # print(json.dumps(data, indent=2, ensure_ascii=False)) 

    if data:
        print("👤 Profile:")
        acc = data[0]["account"]
        print("username:", acc.get("username"))
        print("display_name:", acc.get("display_name"))
        print("avatar:", acc.get("avatar"))
        print("header:", acc.get("header"))
        print("created_at:", acc.get("created_at"))
        print("followers_count:", acc.get("followers_count"))
        print("following_count:", acc.get("following_count"))
        print("statuses_count:", acc.get("statuses_count"))
        
        print("\n")
        print("👇 Posts:")

    for post in data:
        print("---------------------")
        
        is_retruth = post.get("reblog") is not None
        if is_retruth:
            content = post["reblog"].get("content")
            created_at = post["reblog"].get("created_at")
            reblogs_count = post["reblog"].get("reblogs_count", 0)
            likes_count = post["reblog"].get("favourites_count", post["reblog"].get("upvotes_count", 0))
            replies_count = post["reblog"].get("replies_count", 0)
            print("🔁 ReTruthed:", acc.get("display_name"), "ReTruthed")
        else:
            content = post.get("content")
            created_at = post.get("created_at")
            reblogs_count = post.get("reblogs_count", 0)
            likes_count = post.get("favourites_count", post.get("upvotes_count", 0))
            replies_count = post.get("replies_count", 0)

        print("📄 Content:", content if content else None)
        print("⌚ Posted:", format_time(created_at))
        
        print(f"🔁 ReTruths: {reblogs_count:,}")
        print(f"❤️ Likes: {likes_count:,}")
        print(f"💬 Replies: {replies_count:,}")

        media = post.get("media_attachments", [])
        if media:
            for m in media:
                print("🟥 Media type:", m.get("type"))
                print("🟩 Media URL:", m.get("url"))
                print("🟦 Preview URL:", m.get("preview_url"))
        else:
            print("🟥 Media: None")

    input("Next.. ")

    if not data:
        break
    max_id = data[-1]["id"]
