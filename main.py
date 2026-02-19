import discord
import os

# Get the token from environment variables
# You can set this in the Secrets tool (lock icon) as DISCORD_TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("Error: DISCORD_TOKEN environment variable not set.")
    print("Please set the DISCORD_TOKEN secret in the Tools > Secrets pane.")
    exit(1)

# Set up intents to read message content
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == client.user:
        return

    # Respond to "hi" with "hi"
    if message.content.lower() == 'hi':
        await message.channel.send('hi')

client.run(TOKEN)
