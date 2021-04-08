import math
import random

"""
REFERENCIAS
http://dgeiawf.semarnat.gob.mx:8080/ibi_apps/WFServlet?IBIF_ex=D3_R_AIRE01_04&IBIC_user=dgeia_mce&IBIC_pass=dgeia_mce
http://www.edomexico.gob.mx/calidaddelaire/html/conceptos_imeca.htm

"""
#Tendriamos tres variables fijas para dividir los valores

opcion = input("¿Que opcion escoges?")

#a sera el random generado para ozono, azufre y nitrogeno
a= round(random.uniform(0,0.5),3)

if opcion == "ozono" or opcion == "azufre" or opcion == "nitrogeno":
    print("El valor de la variable a es: ", a)

#ozono = round(random.uniform(0,0.5),3)

#Calculo para los 3
a= (a * 100)
calidad=0
if opcion == "ozono":
    #este es ozono
    calidad= a / 0.11
    print("La calidad del aire en base a Ozono es:", round(calidad))
    print("\n")

if opcion == "azufre":
    #este es azufre
    calidad= a / 0.13
    print("La calidad del aire en base a Azufre es: ", round(calidad))
    print("\n")
if opcion == "nitrogeno":
    calidad= a / 0.21
    print("La calidad del oxigeno es: ", round(calidad))
    print("\n")
if opcion == "monoxido":
    mono=round(random.uniform(1,70),3)
    print("El valor de mono es:", mono)
    mono= (mono * 100) / 11
    calidad= mono
    print("La calidad del aire en base a Monoxido de Carbono es: ", round(calidad))
    print("\n")
if opcion == "particulas":
    p=round(random.uniform(1,500))
    print("El valor de P es: ", p)
    #DE 0 A 120 µ/m3 IMECA PM10 = CONCENTRACIÓN DE PM10 * 0.833
    if p >= 0 and p  <= 120:
        p= p * 0.833
    #DE 121 A 320 µ/m3 IMECA PM10 = (CONCENTRACIÓN DE PM10 * 0.5) + 40
    if p >= 121 and p  <= 320:
        p= (p * 0.5) + 40
    #MAYOR A 320 µ/m3 IMECA PM10 = CONCENTRACIÓN DE PM10 *  0.625
    if p > 320: 
        p= p *  0.625
    calidad=p
    print("La calidad del aire en base a PARTÍCULAS SUSPENDIDAS es:", round(calidad))
    print("\n")

#CALCULO DE LA CALIDAD DEL AIRE

if calidad >= 0 and calidad  <= 50:
    print("\n")
    print("La calidad del Aire es BUENA!!!")
if calidad >= 51 and calidad  <= 100:
    print("\n")
    print("La calidad del Aire es REGULAR!!!")
if calidad >= 101 and calidad  <= 150:
    print("\n")
    print("La calidad del Aire es MALA!!!")
if calidad >= 151 and calidad  <= 200:
    print("\n")
    print("La calidad del Aire es MUY MALA!!!")
if calidad >= 201:
    print("\n")
    print("La calidad del Aire es EXTREMADAMENTE MALA!!!")









