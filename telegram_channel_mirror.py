import asyncio
import json
from telethon import TelegramClient, events, errors

CONFIG_FILE = 'config.json'

# Prints a pretty header for different sections
def print_header(title):
    print("\n" + "#" * 50)
    print(f"{' ' * ((50 - len(title)) // 2)}{title}")
    print("#" * 50 + "\n")

# Loads configuration from a JSON file
def load_config():
    try:
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print_header("Configuration Not Found")
        return None
    except json.JSONDecodeError:
        print_header("Configuration Error")
        print("Configuration file is invalid.\n")
        return None

# Lists available channels and prompts the user to choose one
async def select_channel(client):
    await client.start()
    print_header("Select Source Channel")
    async for dialog in client.iter_dialogs():
        print(f"{dialog.id}: {dialog.name}")
    channel_id = input("\nEnter the SOURCE Channel ID: ")
    return channel_id

# Confirms current settings with the user or reconfigures them
async def confirm_or_reconfigure(config):
    print_header("Current Configuration")
    print(f"API ID: {config['api_id']}")
    print(f"API Hash: {config['api_hash']}")
    print(f"Source Channel ID: {config['source_channel_id']}")
    print(f"Target Channel ID: {config['target_channel_id']}")
    choice = input("\nReconfigure these settings? (yes/no): ").lower()
    if choice in ['yes', 'y']:
        return await configure()
    return config

# Configures the script by asking the user for necessary details
async def configure():
    print_header("Configuration Setup")
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")
    async with TelegramClient('telegram_channel_mirror', api_id, api_hash) as client:
        source_channel_id = await select_channel(client)
        target_channel_id = input("Enter the TARGET Channel ID: ")
        config = {
            "api_id": api_id,
            "api_hash": api_hash,
            "source_channel_id": source_channel_id,
            "target_channel_id": target_channel_id
        }
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file)
    return config

# Runs the forwarder, listening for new messages and forwarding them
async def run_forwarder(config):
    async with TelegramClient('telegram_channel_mirror', config['api_id'], config['api_hash']) as client:
        @client.on(events.NewMessage(chats=int(config['source_channel_id'])))
        async def handler(event):
            try:
                await client.forward_messages(int(config['target_channel_id']), event.message)
            except errors.FloodWaitError as e:
                print(f"Rate limited... Sleeping for {e.seconds} seconds...")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Failed to forward message: {e}")

        await client.start()
        print_header("Mirror Active")
        print("Listening for messages...\n")
        await client.run_until_disconnected()

# Main function to load config, confirm/reconfigure if needed, and run the forwarder
async def main():
    config = load_config()
    if not config:
        config = await configure()
    else:
        config = await confirm_or_reconfigure(config)

    while True:
        try:
            await run_forwarder(config)
        except (ConnectionError, errors.ConnectionError):
            print("Connection error... attempting to reconnect...\n")
            await asyncio.sleep(5)
        except KeyboardInterrupt:
            print("\nExited by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}\n")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
