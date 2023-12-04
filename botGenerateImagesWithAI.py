import asyncio
from telebot.async_telebot import AsyncTeleBot
import random
import requests
TELEGRAM_API_BOT = ''
DEEPAI_API_TOKEN = ''
bot = AsyncTeleBot(TELEGRAM_API_BOT)  # Oculta el token del bot

async def generate_image(message, generator_url, command):
    prompt = message.text[len(command) + 1:]
    if not prompt:
        await bot.reply_to(message, f"Por favor, ingresa una frase después de {command}.")
    else:
        await bot.reply_to(message, "Tu imagen se está procesando, espera unos segundos...")
        r = requests.post(
            generator_url,
            data={
                'text': str(prompt),
                'grid-size': '1',
                'image_generator_version': 'hd'
            },
            headers={'api-key': DEEPAI_API_TOKEN}
        )
        image_result = r.json()['output_url']
        await bot.send_photo(message.chat.id, image_result)

async def verify_message_generator(message, generator_url, command, response_text):
    if message.text.startswith(command):
        await generate_image(message, generator_url, command)
    else:
        await bot.reply_to(message, response_text)

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, "Hola. Los comandos disponibles son: ")
    await bot.reply_to(message, "/random, /creature, /chibi, /pixelWorld, /pixelArt, /cartoon3d, /alien, /animeWorld")

@bot.message_handler(commands=['random'])
async def send_random(message):
    await bot.reply_to(message, "Aqui tienes tu imagen aleatoria")
    await bot.send_photo(message.chat.id, f"https://picsum.photos/seed/{random.randint(1, 100)}/400/600")

@bot.message_handler(commands=['creature'])
async def send_imaginacion(message):
    await verify_message_generator(message, "https://api.deepai.org/api/cute-creature-generator", '/creature', "Por favor, utiliza el comando /creature seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['chibi'])
async def send_chibi(message):
    await verify_message_generator(message, "https://api.deepai.org/api/chibi-character-generator", '/chibi', "Por favor, utiliza el comando /chibi seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['pixelWorld'])
async def send_pixel(message):
    await verify_message_generator(message, "https://api.deepai.org/api/pixel-world-generator", '/pixel', "Por favor, utiliza el comando /pixel seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['pixelArt'])
async def send_pixelArt(message):
    await verify_message_generator(message, "https://api.deepai.org/api/pixel-art-generator", '/pixelArt', "Por favor, utiliza el comando /pixelArt seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['cartoon3d'])
async def send_cartoon3d(message):
    await verify_message_generator(message, "https://api.deepai.org/api/3d-cartoon-generator", '/cartoon3d', "Por favor, utiliza el comando /cartoon3d seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['alien'])
async def send_alien(message):
    await verify_message_generator(message, "https://api.deepai.org/api/alien-civilization-generator", '/alien', "Por favor, utiliza el comando /alien seguido de una frase para generar una imagen.")

@bot.message_handler(commands=['animeWorld'])
async def send_animeWorld(message):
    await verify_message_generator(message, "https://api.deepai.org/api/anime-world-generator", '/animeWorld', "Por favor, utiliza el comando /animeWorld seguido de una frase para generar una imagen.")

asyncio.run(bot.polling())  # Esto es para que el bot esté siempre activo
