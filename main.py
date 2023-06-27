import openai
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())
  # префикс для команд ботa

openai.api_key = ''  # API ключ от OpenAI
model_engine = "davinci"  # имя модели GPT

@client.event
async def on_ready():
  print('Бот запущен. Готов к работе')

# Создаем команду для работы с GPT
@client.command()
async def chat(ctx, *, message):
  # Выполняем запрос к OpenAI GPT API
  response = openai.Completion.create(
    prompt=message,
    model=model_engine,
    temperature=0.9,
    max_tokens=100,
    n=1,
    stop=None,
    )
  
  # Получаем текст ответа от GPT модели
  bot_reply = response.choices[0].text
  # Отправляем ответ в Discord-чат
  await ctx.send(bot_reply)

# Запускаем бота
client.run('')  # Токен вашего бота в Discord
