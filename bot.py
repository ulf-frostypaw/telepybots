import telebot
import tweepy
#from tweepy.errors import TweepyException

bot = telebot.TeleBot('6740701036:AAFGgqTZnIP7fzz558gd201HY2Le_ARTd0Y')

def verify_user(username, message):
    if username is not None:
        consumer_key = '' 
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        # Autenticación con las credenciales de la API de Twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Crear una instancia del API de Twitter
        api = tweepy.API(auth)

        def verify_user(username):
            try:
                user = api.get_user(username)
                return True
            except BaseException as e:
                return str(e)

        # Ejemplo de uso
        #username = 'nombre_de_usuario'
        if verify_user(username):
            bot.reply_to(message, "El usuario existe")
            #print(f"El usuario {username} existe en Twitter.")
        else:
            bot.reply_to(message, "El usuario no existe")
            #print(f"El usuario {username} no existe en Twitter.")


    else:
        bot.reply_to(message, "El usuario no existe")
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message): #saludo inicial o ayuda
    bot.reply_to(message, "Hola. Soy un bot que te permite acceder a tu cuenta de Twitter desde Telegram. Para comenzar, escribe /twitter")

@bot.message_handler(commands=['twitter'])
def check_twitter(message):
    if message.text.startswith('/twitter'):
        username = message.text[9:]  # Extract the username from the message
        if not username:
            bot.reply_to(message, "Por favor, ingresa tu nombre de usuario de Twitter después de /twitter.")
        else:
            verify_user(username, message) #verificar si el usuario existe en twitter. Parece que no esta respondiendo la funcion. RESOLVER
    else:
        bot.reply_to(message, "Por favor, responde al mensaje anterior para continuar.")
 
@bot.message_handler(func=lambda message: True)
def myMessage(message): # esto responde con el mensaje que el mismo usuario envia
    bot.reply_to(message, message.text)




bot.infinity_polling() # esto es para que el bot este siempre activo

# PSEUDOCODIGO XD
# 1. recibir mensaje y solicitar el username del twitter del usuario
# 2. buscar el username en twitter
# 3. si existe, darle acceso
# 4. si no existe, enviar mensaje de error
# 5. solicitar el token de acceso de autorizacion del propietario
# 6. Si existe el token de acceso, darle acceso
# 7. Si no existe, enviar mensaje de error
# 8. Si todo esta bien, darle acceso al twitter del usuario
