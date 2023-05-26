import discord, openai
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents = intents)
openai.api_key = ""

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author != bot.user:
      print(message.content.startswith(">"))
      if message.content.startswith(">"):
        content = message.content.replace(">", "").strip()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=content,
            max_tokens=500,
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        await message.reply(reply)


bot.run("")
