from pyrogram import Client, filters
import random
import asyncio
from shayari_data import get_shayari, get_dialogue

# Bot Token
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
bot_token = 'YOUR_BOT_TOKEN'  # Replace with your Bot Token

app = Client("chatting_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Command to get Shayari
@app.on_message(filters.command("shayari"))
async def send_shayari(client, message):
    shayari = get_shayari()
    await message.reply(shayari)

# Command to get Dialogue
@app.on_message(filters.command("dialogue"))
async def send_dialogue(client, message):
    dialogue = get_dialogue()
    await message.reply(dialogue)

# Command to chat
@app.on_message(filters.text & ~filters.command())
async def chat(client, message):
    user_message = message.text.lower()

    # Predefined responses for certain keywords
    if "hello" in user_message:
        await message.reply("नमस्ते! कैसे हो?")
    elif "how are you" in user_message:
        await message.reply("मैं अच्छा हूँ, धन्यवाद! आप कैसे हैं?")
    elif "what's your name" in user_message:
        await message.reply("मेरा नाम चैटिंग बोट है।")
    elif "bye" in user_message:
        await message.reply("अलविदा! फिर मिलेंगे।")
    else:
        await message.reply("मुझे समझ में नहीं आया, कृपया फिर से प्रयास करें।")

# Start the bot
if __name__ == "__main__":
    app.run()
