import cloudscraper, json

requests = cloudscraper.create_scraper()

url = "https://truthsocial.com/api/v1/accounts/107780257626128497/statuses" # User Id

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
		acc = data[0]["account"]
		print("username:", acc.get("username"))
		print("display_name:", acc.get("display_name"))
		print("avatar:", acc.get("avatar"))
		print("header:", acc.get("header"))
		print("created_at:", acc.get("created_at"))
		print("followers_count:", acc.get("followers_count"))
		print("following_count:", acc.get("following_count"))
		print("statuses_count:", acc.get("statuses_count"))
		print("---------------------")

	for post in data:
		print("---------------------")
		content = post.get("content")
		print("content:", content if content else None)

		print("last_status_at:", post.get("created_at"))

		media = post.get("media_attachments", [])
		if media:
			for m in media:
				print("type:", m.get("type"))
				print("url:", m.get("url"))
				print("preview_url:", m.get("preview_url"))
		else:
			print("type: None")

	input(" Next.. ")

	if not data:
		break

	id = data[-1]["id"]
	max_id = id
