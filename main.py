import requests
import time
import json

with open("config.json", "r") as f:
    config = json.load(f)

token = config["token"]
delay = config["time_until_next_change"]

headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.607 Chrome/134.0.6998.179 Electron/35.1.5 Safari/537.36",
    "Origin": "https://canary.discord.com",
    "Referer": "https://canary.discord.com/discovery/quests",
}

response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
if response.status_code != 200:
    print("❌ Failed to get guilds:", response.text)
    exit()

guilds = response.json()
guilds_with_tags = [g for g in guilds if "GUILD_TAGS" in g.get("features", [])]

print(f"🔍 Found {len(guilds_with_tags)} guild(s) with GUILD_TAGS.")

while True:
    for guild in guilds_with_tags:
        payload = {
            "identity_guild_id": guild["id"],
            "identity_enabled": True
        }

        put_response = requests.put(
            "https://discord.com/api/v9/users/@me/clan",
            headers=headers,
            json=payload
        )

        if put_response.status_code == 200:
            print(f"✅ Successfully updated clan for guild: {guild['name']} ({guild['id']})")
            time.sleep(delay)

        elif put_response.status_code == 403:
            print(f"❌ Rate Limited. Sleeping 1 minute", put_response.text)
            time.sleep(60)
        else:
            print(f"❌ Failed for {guild['name']} ({guild['id']}):", put_response.status_code, put_response.text)
            time.sleep(delay)
