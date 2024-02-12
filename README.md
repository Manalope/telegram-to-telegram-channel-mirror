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
pip3 install -r requirements.txt
```

## Configuration

Just run the script:  Upon launch, `config.json` is created or updated. Manual editing is OK. Private channels have a negative `-` sign in front of them.

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

During setup, a `telegram_channel_mirror.session` file is generated allowing subsequent connection without re-authentication.


## License

Released under [MIT License](https://opensource.org/license/mit/).

## Acknowledgments

Uses [Telethon library](https://github.com/LonamiWebs/Telethon). Thank you to that project.

