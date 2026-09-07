"""
Algoritmo “Organización y automatización de correos electrónicos”

1.	INICIO
2.	INGRESAR a correo electrónico del usuario
3.	DEFINIR opciones = “ 1. Buscar
		                 2. Escribir correo
		                 3. Salir “
4.	IMRPIMIR opciones
5.	PEDIR al usuario que ingrese un número
6.	GUARDAR en opcion_elegida
"""
opciones = "1. Buscar \n2. Escribir correo \n3. Salir"
print(opciones)
opcion_elegida = input("Ingrese un número: ")
"""""


7.	SI opcion_elegida == '1'
    a.	PEDIR al usuario palabras clave 
    b.	GUARDAR en palabras_clave
    c.	DEFINIR total_palabras_clave = 0
    """
palabras_clave = list(input("Ingrese palabras clave separadas por comas: ").split(","))
total_palabras_clave = 0
"""
    d.	LEER bandeja de entrada
    e.	SI correo electrónico contiene cualquier palabra de palabras_clave
        i.	SUMAR total_palabras_clave += 1
        """
total_palabras_clave = total_palabras_clave + 1
antiguedad = fecha_entrada - fecha_actual
"""
        ii.	IMPRIMIR correo electrónico
    g.	SINO
        i.	IMPRIMIR “No se encontraron las palabras ingresadas”
    h.  IMPRIMIR total_palabras_clave
8.	SI opción elegida == '2'
    a.	PEDIR el destinatario
    b.	PEDIR el asunto
    c.	PEDIR el mensaje
    d.	PREGUNTAR si el usuario lo desea enviar
    e.	GUARDAR en desea_enviar
    f.	SI desea enviar == 'si'
        i.	ENVIAR correo
    g.	SINO
        i.	GUARDAR correo
9.	SINO
    a.	PREGUNTAR si desea salir
    b.	GUARDAR en desea_salir
c.	SI desea_salir == 'si'
    i.	FIN
d.	SINO
    i.	REGRESAR a paso 4
10.	FIN
"""