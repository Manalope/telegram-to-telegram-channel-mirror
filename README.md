# Telegram to Telegram Channel Mirror

This Python script mirrors messages from one Telegram channel to another. It's designed to be simple and easy to use.


## Prerequisites

Get your `api_id` and `api_hash` from [Telegram's Developer Page](https://my.telegram.org/apps).


## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/manalope/telegram-to-telegram-channel-mirror.git

cd telegram-to-telegram-channel-mirror
```


2. **Install Dependencies**

```bash
pip install -r requirements.txt
```


## Configuration

Upon launch, the script creates or refreshes the `config.json` with your preferences. Manual editing is optional; to initiate the setup just run the script. Ensure you input the full numeric ID for both `source_channel_id` and `target_channel_id`, including the initial `-` for private channels or groups. Enter everything in quotes as strings.

Example of `config.json`:

```json
{
  "api_id": "your_api_id",
  "api_hash": "your_api_hash",
  "source_channel_id": "-123456789",
  "target_channel_id": "-987654321"
}
```

## Running the Script

```bash
python3 telegram_channel_mirror.py
```

During the initial authentication process, a `telegram_channel_mirror.session` file will be generated allowing the script to connect to Telegram without needing to re-authenticate each time.

## License

This project is released under the [MIT License](https://opensource.org/license/mit/).

## Acknowledgments

- This project uses the [Telethon library](https://github.com/LonamiWebs/Telethon) to interact with the Telegram API. Thank you to that project.

