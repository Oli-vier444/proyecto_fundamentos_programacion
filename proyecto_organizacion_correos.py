
#Algoritmo “Organización y automatización de correos electrónicos”
#Autor: Olivier Gaytán
"""
Descripción: El programa lee la bandeja de entrada para poder buscar
palabras clave en correos, además de poder redactar y enviarlos periódicamente.
Para envio de correos: smtplib
Para revisión de bandeja de entrada: imaplib, email
Para manejo de tiempo: time
"""
import imaplib
import email
import smtplib
from email.header import decode_header
from time import sleep
#Pide el usuario y la contraseña del correo electrónico
usuario = input("USUARIO: ")
contraseña = input("CONTRASEÑA DE APLICACIÓN GOOGLE: ")

servidor = "imap.gmail.com"

def mostrar_menu():
    #muestra el menú de opciones al usuario
    opciones = "1. Buscar \n2. Escribir correo \n3. Salir"
    print(opciones)

def escribir_correo():
    correo = usuario
    clave = contraseña
    destinatario = input("Destinatario: ")
    asunto = input("Asunto: ")
    mensaje = input("Mensaje: ")
    desea_enviar = input("¿Deseas enviarlo?: ")
    texto = f"subject: {asunto} \n\n {mensaje}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.starttls

    server.login(correo, clave)
    
    if desea_enviar == "si":

        envio_periodico = input("¿Deseas enviarlo periodicamente?: ")
        envio_periodico.strip().lower()
        if envio_periodico == "si":
            frecuencia = int(input("¿Cada cuántos días?: "))
            repetir = int(input("¿Durante cuántos días?: "))
            segundos = frecuencia*86400
            print(f"Correo enviado. se enviará cada {frecuencia} días por {repetir} días")
            for _ in range(repetir):
                server.sendmail(correo, destinatario, texto)
                sleep(segundos)
                
        elif envio_periodico == "no":
            server.sendmail(correo, destinatario, texto)
            print("Correo enviado")

#def leer_bandeja():
  
mostrar_menu()

opcion_elegida = input("Ingrese un número: ")

if opcion_elegida == "1":
    palabras_clave = list(input("Ingrese palabras clave separadas por comas: ").split(","))
    total_palabras_clave = 0

    imap = imaplib.IMAP4_SSL(servidor)
    imap.login(usuario, contraseña)

    imap.select("Inbox")

    _, msjs = imap.search(None, "ALL")

    nums_msjs = msjs[0].split()

    hasta = int(input("Revisar los últimos correos: "))
    hasta = hasta * -1

    ultimos_correos = nums_msjs[hasta:]
    todos = []
    for nums_msjs in ultimos_correos:
        _, datos = imap.fetch(nums_msjs, '(RFC822)')

        for parte in datos:
            if isinstance(parte, tuple):
                msj = email.message_from_bytes(parte[1])
                subject, encoding = decode_header(msj["Subject"])[0]

                asunto = msj.get('Subject')
                emisor = msj.get('From')
                todos.append(asunto)
                todos.append(emisor)
                
    for palabras_clave in todos:
        total_palabras_clave += 1
    print(f"Palabras clave encontradas: {total_palabras_clave}")
elif opcion_elegida == "2":
    escribir_correo()
elif opcion_elegida == "3":
    print("Adios!")



