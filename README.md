# Telegram to Telegram Channel Mirror

This Python script allows you to mirror messages from one Telegram channel to another automatically. It's designed to be simple and easy to use, leveraging the Telethon library to interact with the Telegram API.


## Prerequisites

Prior to using this script, secure your API ID and API Hash from [Telegram's Developer Page](https://my.telegram.org/apps), essential for Telegram API interactions.


## Installation

1. **Clone the Repository**

```git clone https://github.com/manalope/telegram-to-telegram-channel-mirror.git```
```cd telegram-to-telegram-channel-mirror```


2. **Install Dependencies**

```pip install -r requirements.txt```


## Configuration

On startup, the script automatically generates or updates the config.json file, offering an option to modify existing settings or create new ones, including listing and selecting channel IDs you're part of for easy configuration.

```json
{
  "api_id": "Your_API_ID",
  "api_hash": "Your_API_Hash",
  "source_channel_id": "Your_Source_Channel_ID",
  "target_channel_id": "Your_Target_Channel_ID"
}
```

Each field holds the respective information as a string. The source_channel_id and target_channel_id should include the entire numeric ID, even if it begins with a -, indicating a private channel or group.

## Running the Script

```python3 telegram_channel_mirror.py```


The script will load your configuration, and if everything is set up correctly, it will start listening for new messages in your source channel and automatically forward them to your target channel.

## License

This project is released under the [MIT License](https://opensource.org/license/mit/).

## Acknowledgments

- This project uses the [Telethon library](https://github.com/LonamiWebs/Telethon) to interact with the Telegram API. Thank you to that project.

