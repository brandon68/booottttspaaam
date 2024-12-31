import telebot
import time
from spammer import send_spam_deia, send_spam_slack, send_spam_emarketingsd, send_recuperar_emarkeyin, \
    send_spam_mexicox, send_spam_lagranbodega, reset_password_mexicox, enviar_naturacloud, enviar_elpais, \
    recuperar_naturacloud, enviar_recuperar_elpais_v2, registrar_usuario_petco, enviar_suscripcion_axelspringer, \
    enviar_email_ibm, registrar_virgin, start_gandhi_login, send_gandhi_access_key, enviar_nanopay, \
    enviar_codigo_freecodecamp, enviar_registro_outdooractive, registrar_strikingly, enviar_heb, start_elektra_login, \
    send_elektra_access_key, start_doto_login, send_doto_access_key, registrar_macstore, registrar_clip, registrar_puntoferta, registrar_ynab, pectov2_restablecer, virginv22_recuperar_contrasena, outdooractivev2_recuperar_contrasena, strikinglyv2_recuperar_contrasena, hebv2_recuperar_cuenta, macstorev2_recuperar_cuenta, puntoofertav2_recuperarcontraseña, ynabv2_recuperarcontraseña         

# Reemplaza con tu token de BotFather
API_TOKEN = '7119344534:AAGloICq0pD5RWhDM-lQYUcKzDZ3uZ912LA'

bot = telebot.TeleBot(API_TOKEN)

# Diccionario para almacenar la información de los usuarios
users_data = {}

# Leer las keys desde el archivo y cargarlas en un diccionario
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

# Lista global de keys cargadas desde el archivo
keys = load_keys()

# Función para verificar si la key es válida
def validate_key(user_key):
    if user_key in keys and keys[user_key] > 0:
        return True
    return False

# Función para guardar las keys de vuelta en el archivo después de actualizarlas
def save_keys(keys, filename="keys.txt"):
    with open(filename, "w") as file:
        for key, credits in keys.items():
            file.write(f"{key},{credits}\n")

# Manejo del comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "¡Hola! Para comenzar, por favor ingresa tu 'key' de acceso. adquire con @juanper33z")
    bot.register_next_step_handler(message, get_key)

# Función para recibir y verificar la key
def get_key(message):
    user_key = message.text.strip()
    if validate_key(user_key):
        # Reduce el crédito de la key utilizada
        keys[user_key] -= 1
        save_keys(keys)  # Guardar los cambios en el archivo
        users_data[message.chat.id] = {'key': user_key, 'credits': keys[user_key]}
        bot.send_message(message.chat.id, "Key validada. Ahora, ingresa tu correo electrónico.")
        bot.register_next_step_handler(message, get_email)
    else:
        bot.send_message(message.chat.id, "Key inválida o sin créditos. Por favor, intenta con una nueva key. compra con @juanper33z")
        bot.register_next_step_handler(message, get_key)

# Función para recibir el correo y registrar
def get_email(message):
    email = message.text.strip()
    users_data[message.chat.id]['email'] = email
    bot.send_message(message.chat.id, "Correo registrado. ¡ENVIANDO SPAM!")

    # Llamamos a las funciones del archivo spammer.py
    result_deia = send_spam_deia(email)
    result_slack = send_spam_slack(email)
    result_macstore = registrar_macstore(email)
    result_emarketing = send_spam_emarketingsd(email)
    result_emarkeyin = send_recuperar_emarkeyin(email)
    result_virgin = registrar_virgin(email)
    result_mexicox = send_spam_mexicox(email)
    result_lagranbodega = send_spam_lagranbodega(email)
    result_mexicox_reset = reset_password_mexicox(email)
    result_naturacloud = enviar_naturacloud(email)
    result_elpais = enviar_elpais(email)
    result_naturacloud_recuperar = recuperar_naturacloud(email)
    result_elpais_v2 = enviar_recuperar_elpais_v2(email)
    result_petco = registrar_usuario_petco(email)
    result_axelspringer = enviar_suscripcion_axelspringer(email)
    result_ibm = enviar_email_ibm(email)
    result_nanopay = enviar_nanopay(email)
    result_freecodecamp = enviar_codigo_freecodecamp(email)
    result_outdooractive = enviar_registro_outdooractive(email)
    result_strikingly = registrar_strikingly(email)
    result_clip = registrar_clip(email)
    result_puntoferta = registrar_puntoferta(email)
    result_ynab = registrar_ynab(email)
    result_pectov2 = pectov2_restablecer(email)
    result_virginv22 = virginv22_recuperar_contrasena(email)
    result_outdooractivev2 = outdooractivev2_recuperar_contrasena(email)
    result_strikinglyv2 = strikinglyv2_recuperar_contrasena(email)
    result_hebv2 = hebv2_recuperar_cuenta(email)
    result_macstorev2 = macstorev2_recuperar_cuenta(email)
    result_puntoofertav2 = puntoofertav2_recuperarcontraseña(email)
    result_ynabv2 = ynabv2_recuperarcontraseña(email)
    result_heb = enviar_heb(email)

    # Iniciar el proceso de Elektra
    session_elektra = start_elektra_login(email)  # Guardamos la sesión de Elektra
    if session_elektra:
        result_elektra_login = "Inicio de sesión en Elektra exitoso."
        result_access_key_elektra = send_elektra_access_key(email, session_elektra)  # Pasamos la sesión aquí
    else:
        result_elektra_login = "Error al iniciar sesión en Elektra."
        result_access_key_elektra = "No se pudo obtener la clave de acceso de Elektra."

    # Iniciar el proceso de Gandhi
    session_gandhi = start_gandhi_login(email)  # Guardamos la sesión de Gandhi
    if session_gandhi:
        result_gandhi_login = "Inicio de sesión en Gandhi exitoso."
        result_access_key_gandhi = send_gandhi_access_key(email, session_gandhi)  # Pasamos la sesión aquí
    else:
        result_gandhi_login = "Error al iniciar sesión en Gandhi."
        result_access_key_gandhi = "No se pudo obtener la clave de acceso de Gandhi."

    # Iniciar el proceso de Doto
    session_doto = start_doto_login(email)  # Guardamos la sesión de Doto
    if session_doto:
        result_doto_login = "Inicio de sesión en Doto exitoso."
        result_access_key_doto = send_doto_access_key(email, session_doto)  # Pasamos la sesión aquí
    else:
        result_doto_login = "Error al iniciar sesión en Doto."
        result_access_key_doto = "No se pudo obtener la clave de acceso de Doto."  # Asegúrate de que esta variable también se defina


    # Enviar los resultados a Telegram
    bot.send_message(message.chat.id, result_deia)
    bot.send_message(message.chat.id, result_slack)
    bot.send_message(message.chat.id, result_emarketing)
    bot.send_message(message.chat.id, result_emarkeyin)
    bot.send_message(message.chat.id, result_virgin)
    bot.send_message(message.chat.id, result_mexicox)
    bot.send_message(message.chat.id, result_lagranbodega)
    bot.send_message(message.chat.id, result_mexicox_reset)
    bot.send_message(message.chat.id, result_naturacloud)
    bot.send_message(message.chat.id, result_elpais)
    bot.send_message(message.chat.id, result_naturacloud_recuperar)
    bot.send_message(message.chat.id, result_elpais_v2)
    bot.send_message(message.chat.id, result_petco)
    bot.send_message(message.chat.id, result_axelspringer)
    bot.send_message(message.chat.id, result_ibm)
    bot.send_message(message.chat.id, result_nanopay)
    bot.send_message(message.chat.id, result_freecodecamp)
    bot.send_message(message.chat.id, result_outdooractive)
    bot.send_message(message.chat.id, result_strikingly)
    bot.send_message(message.chat.id, result_heb)
    bot.send_message(message.chat.id, result_elektra_login)
    bot.send_message(message.chat.id, result_access_key_elektra)
    bot.send_message(message.chat.id, result_gandhi_login)
    bot.send_message(message.chat.id, result_access_key_gandhi)
    bot.send_message(message.chat.id, result_doto_login)
    bot.send_message(message.chat.id, result_access_key_doto)
    bot.send_message(message.chat.id, result_clip)
    bot.send_message(message.chat.id, result_puntoferta)
    bot.send_message(message.chat.id, result_ynab)
    bot.send_message(message.chat.id, result_pectov2)
    bot.send_message(message.chat.id, result_virginv22)
    bot.send_message(message.chat.id, result_outdooractivev2)
    bot.send_message(message.chat.id, result_strikinglyv2)
    bot.send_message(message.chat.id, result_hebv2)
    bot.send_message(message.chat.id, result_macstorev2)
    bot.send_message(message.chat.id, result_puntoofertav2)
    bot.send_message(message.chat.id, result_ynabv2)
    bot.send_message(message.chat.id, result_macstore)

    # Finaliza el proceso
    bot.send_message(message.chat.id, "¡Gracias por usar el bot, Autor @juanper33z!")

# Iniciar el bot con polling
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Error ocurrido: {e}")
        time.sleep(15)  # Esperar un poco antes de volver a intentar