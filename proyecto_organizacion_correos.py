
#Algoritmo “Organización y automatización de correos electrónicos”
#Autor: Olivier Gaytán
"""
Descripción: El programa lee la bandeja de entrada para poder buscar
palabras clave en correos, además de poder redactar y enviarlos periódicamente.
Para envio de correos: smtplib (solo gmail)
"""
import smtplib

#Pide el usuario y la contraseña del correo electrónico
usuario = input("USUARIO: ")
contraseña = input("CONTRASEÑA DE APLICACIÓN GOOGLE: ")

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
            server.sendmail(correo, destinatario, texto)
            print(f"Correo enviado. se enviará cada {frecuencia} días")
        elif envio_periodico == "no":
            server.sendmail(correo, destinatario, texto)
            print("Correo enviado")


mostrar_menu()

opcion_elegida = input("Ingrese un número: ")

if opcion_elegida == "1":
    palabras_clave = list(input("Ingrese palabras clave separadas por comas: ").split(","))
    total_palabras_clave = 0
    total_palabras_clave = total_palabras_clave + 1
elif opcion_elegida == "2":
    escribir_correo()
elif opcion_elegida == "3":
    print("Adios!")



