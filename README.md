# Discord Tag Changer

This script automates updating your discord tag

## 🔧 Features

- Fetches your current joined guilds.
- Filters out only guilds with `GUILD_TAGS`.
- Sends regular PUT requests to update your identity clan.
- Fully configurable via `config.json`.

## 🛠 Configuration

Edit the `config.json` file:

```json
{
  "token": "YOUR_DISCORD_TOKEN_HERE",
  "time_until_next_change": 10
}
```
`token`: Your Discord user token (see WARNING below).

`time_until_next_change`: Delay between updates in seconds.

## 🚀 How to Run
```bash
python clan_updater.py
```

## ⚠️ WARNING: RISK OF BAN
This script uses your Discord user token, which is strictly against Discord’s Terms of Service.
Using selfbots, scripts, or automated access via a user token can result in:

- Permanent account bans
- IP bans in some cases
- Removal from servers or guilds

⚠️ USE AT YOUR OWN RISK. THIS IS FOR EDUCATIONAL PURPOSES ONLY.

🧠 Disclaimer
This project is provided as-is, without any guarantees. The author is not responsible for any bans or damage that may occur through the use of this code.

📜 License
Apache 2.0 License
