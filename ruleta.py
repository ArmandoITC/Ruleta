# ruleta
#integrantes:
# FIGUEROA MARTINEZ ARMANDO
# MARTINEZ VALENCIA LUIS EDUARDO
# HERNANDEZ TOVAR ANDRES
# GARCIA GARCIA SALVADOR

from tkinter import *
import random
from PIL import Image
import time
global tipo,Juga,i,turno,Apuesta,minimo,Napuesta,eleccion,cantidad,Numero,Apostado,Apuestas1,Ok,Aceptar,doble

minimo=0
Napuesta=0
Apuestas=[""]
doble=[""]
Apuestas1=[[0,0]]
IApuesta=0
turno=0
i=0
tipo=""
def Apuesta_minima ():
    global IApuesta
    L=minimo.get()
    IApuesta=int(L)
    if(IApuesta>=10):
        apuesta()

        
def apuesta():
    global eleccion,IApuesta
    l=Label(ventana,text="Los datos que hayas ingresando se mostraran cronologicanente en pantallan solo de tu ultima apuesta hecha ").place(x=300,y=70)
    l=Label(ventana,text=IApuesta).place(x=800,y=100)
    eleccion=StringVar()
    l=Label(ventana,text="tipo de apuesta (en minusculas) ").grid(column=0,row=0)
    cuadro00=Entry(ventana,textvariable=eleccion,state="normal",width=2,bg="blue")
    cuadro00.place(width=90,height=30)
    cuadro00.place(x=0, y=25)
    B3=Button(ventana,text="aceptar",command=tipo_apuesta,bg="white",width=30)
    B3.place(x=100, y=25)



def tipo_apuesta ():
    global tipo,Napuesta,Apuestas,cantidad
    L=eleccion.get()
    tipo=L
    Apuestas[Napuesta]=str(tipo)
    l=Label(ventana,text=Apuestas[Napuesta]).place(x=800,y=120)
    cantidad=StringVar()
    l=Label(ventana,text="                                                           ").grid(column=0,row=0)
    l=Label(ventana,text="cantidad").grid(column=0,row=0)
    cuadro00=Entry(ventana,textvariable=cantidad,state="normal",width=2,bg="blue")
    cuadro00.place(width=90,height=30)
    cuadro00.place(x=0, y=25)
    B1=Button(ventana,text="aceptar",command=Cantidad_apostada,bg="white",width=30)
    B1.place(x=100, y=25)

def Cantidad_apostada():
    global tipo,Napuesta,Apuestas,IApuesta,cantidad,Numero,Aceptar
    L=cantidad.get()
    Tapostado=""
    Tapostado=L
    Apuestas1[Napuesta][0]=0
    Apuestas1[Napuesta][0]=int(Tapostado)
    l=Label(ventana,text=Apuestas1[Napuesta][0]).place(x=800,y=150)
    IApuesta=IApuesta-int(Tapostado)
    l=Label(ventana,text=IApuesta).place(x=800,y=180)
    Numero=StringVar()
        
    cuadro01=Entry(ventana,textvariable=Numero,state="normal",bg="blue")
    cuadro01.place(width=90,height=30)
    cuadro01.place(x=0, y=25)
    
    Aceptar=Button(ventana,text="aceptar",command=numeros_apostados,bg="white",width=30)
    Aceptar.place(x=100, y=25)
    if(Apuestas[Napuesta]=="simple"):
        l=Label(ventana,text="                                                           ").grid(column=0,row=0)
        l=Label(ventana,text="elige el numero entre 0 y 36").grid(column=0,row=0)
        
    if(Apuestas[Napuesta]=="fila"):
        l=Label(ventana,text="                                                           ").grid(column=0,row=0)
        l=Label(ventana,text="introduzca los numeros de la fila segidos sin espacios").grid(column=0,row=0)
        
          
            
    if(Apuestas[Napuesta]=="docena"):
        l=Label(ventana,text="                                                           ").grid(column=0,row=0)
        l=Label(ventana,text="introduzca 1,2,3 segun la docena que desea elegir").grid(column=0,row=0)
    
    if(Apuestas[Napuesta]=="color"):
        l=Label(ventana,text="                                                                                 ").grid(column=0,row=0)
        l=Label(ventana,text="introduzca 1 para negro 0 para rojo").grid(column=0,row=0)
        
    if(Apuestas[Napuesta]=="mitades"):
        l=Label(ventana,text="                                                           ").grid(column=0,row=0)
        l=Label(ventana,text="introduzca 0 para los primeros 18,  1 para los ultimos 18").grid(column=0,row=0)
    if(Apuestas[Napuesta]=="par"):
        cuadro01=Entry(ventana,textvariable=Numero,state="normal",bg="blue")
        cuadro01.place(width=90,height=30)
        cuadro01.place(x=0, y=25)
    if(Apuestas[Napuesta]=="doble"):
        cuadro01=Entry(ventana,textvariable=Numero,state="normal",bg="blue")
        cuadro01.place(width=90,height=30)
        cuadro01.place(x=0, y=25)
    
        Aceptar=Button(ventana,text="aceptar",command=caso_doble,bg="white",width=30)
        Aceptar.place(x=100, y=25)
        l=Label(ventana,text="                                                           ").grid(column=0,row=0)
        l=Label(ventana,text="introduzca la pareja separada por una coma y de menor a mayor ").grid(column=0,row=0)


def caso_doble():
    global doble
    L=Numero.get()
    doble[Napuesta]=str(L)
    l=Label(ventana,text=doble[Napuesta]).place(x=800,y=200)
    if(IApuesta>=10):
        B1=Button(ventana,text="deseas realizar otra apuesta",command=creacion_lista,bg="white")
        B1.place(x=100, y=25)
        Ok=Button(ventana,text="    Mantener solo apuestas actuales  ",command=rotar,bg="white")
        Ok.place(x=250, y=25)
        
    else:
        rotar()
    
def numeros_apostados  ():
    global tipo,Napuesta,Apuestas,IApuesta,cantidad,Numero,Ok,Aceptar
    L=Numero.get()
    Apuestas1[Napuesta][1]=int(L)
    l=Label(ventana,text=Apuestas1[Napuesta][1]).place(x=800,y=200)
    if(IApuesta>=10):
        B1=Button(ventana,text="deseas realizar otra apuesta",command=creacion_lista,bg="white")
        B1.place(x=100, y=25)
        Ok=Button(ventana,text="    Mantener solo apuestas actuales  ",command=rotar,bg="white")
        Ok.place(x=250, y=25)
        
    else:
        rotar()
    
        

def creacion_lista():
    global Apuestas,Napuesta,Ok,doble
    Ok.destroy()
    Apuestas.append("")
    doble.append("")
    Apuestas1.append([0,0])
    Napuesta=Napuesta+1
    apuesta()

    
def Volver_jugar():
    global Napuesta
    Napuesta=0
    Apuesta_minima()












def ganador():
    global Napuesta,Apuestas,Ganador,IApuesta,Apuestas1,doble
    i=0
    l=Label(ventana,text=("El numero ganador es ",Ganador)).place(x=900,y=150)
    while(Napuesta>=i):
        #l=Label(ventana,text=("hola "+str(Napuesta))).place(x=900,y=100)
        com=""
        com=str(Apuestas[i])
        compn=0
        compn=Apuestas1[i][1]
        if (com=="color"):
            if (Apuestas1[i][1]==0 and Ganador==2 or Ganador==4 or Ganador==6 or Ganador==8 or Ganador==10 or Ganador==11 or Ganador==13 or Ganador==15 or Ganador==17 or Ganador==20 or Ganador==22 or Ganador==24 or Ganador==26 or Ganador==28 or Ganador==29 or Ganador==11 or Ganador==33 or Ganador==35 or Ganador==31):
                l=Label(ventana,text="felicidades ganas con colores negros 1").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*2+IApuesta
            if(Apuestas1[i][1]==1 and Ganador==1 or Ganador==3 or Ganador==5 or Ganador==7 or Ganador==9 or Ganador==12 or Ganador==14 or Ganador==16 or Ganador==18 or Ganador==19 or Ganador==21 or Ganador==23 or Ganador==25 or Ganador==27 or Ganador==30 or Ganador==31 or Ganador==32 or Ganador==34 or Ganador==36):
                IApuesta=Apuestas1[i][0]*2+IApuesta
                l=Label(ventana,text="felicidades ganas con colores rojos 0").place(x=900,y=300)



        if(com=="simple" and Apuestas1[i][1]==Ganador):
            IApuesta=Apuestas1[i][0]*35+IApuesta


        if (com=="docena"):
            if (compn==1 and (13>Ganador>=0)):
                l=Label(ventana,text="felicidades ganas con docena 1").place(x=900,y=300)
                IApuesta=Apuestas1[o][0]*8+IApuesta
            if (compn==2 and 25>Ganador >12):
                l=Label(ventana,text="felicidades ganas con docena 2").place(x=900,y=300)
                IApuesta=Apuestas1[o][0]*8+IApuesta
            if (compn==3 and 37>Ganador >26):
                l=Label(ventana,text="felicidades ganas con docena 3").place(x=900,y=300)
                IApuesta=Apuestas1[o][0]*8+IApuesta
                
        if (com=="mitades"):
            if (19>Ganador >-1 and compn==0):
                l=Label(ventana,text="felicidades ganas con primera mitad").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*2+IApuesta
            if (36>Ganador >18  and compn==1):
                l=Label(ventana,text="felicidades ganas con segunda mitad").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*2+IApuesta


        if (com=="fila"):
            if((Ganador==1 or Ganador==2 or Ganador==3)and compn==123 ):
                l=Label(ventana,text="felicidades ganas con la fila 1,2,3").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==4 or Ganador==5 or Ganador==6)and compn==456 ):
                l=Label(ventana,text="felicidades ganas con la fila 456").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==7 or Ganador==8 or Ganador==9)and compn==789 ):
                l=Label(ventana,text="felicidades ganas con la fila 789").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==10 or Ganador==11 or Ganador==12)and compn==101112 ):
                l=Label(ventana,text="felicidades ganas con la fila 10,11,12").place(x=900,y=300)
                IApuesta=Apuestas[i][0]*17+IApuesta
            if((Ganador==13 or Ganador==14 or Ganador==15)and compn==131415 ):
                l=Label(ventana,text="felicidades ganas con la fila 13,14,15").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==16 or Ganador==17 or Ganador==18)and compn==161718):
                l=Label(ventana,text="felicidades ganas con la fila 16,17,18").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==19 or Ganador==20 or Ganador==21)and compn==192021 ):
                l=Label(ventana,text="felicidades ganas con la fila 19,20,21").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==22 or Ganador==23 or Ganador==24)and compn==222324 ):
                l=Label(ventana,text="felicidades ganas con la fila 22,23,24").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==25 or Ganador==26 or Ganador==27)and compn==252627 ):
                l=Label(ventana,text="felicidades ganas con la fila 25,26,27").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if( (Ganador==28 or Ganador==29 or Ganador==30)and compn==282930 ):
                l=Label(ventana,text="felicidades ganas con la fila 28,,29,30").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==31 or Ganador==32 or Ganador==33)and compn==313233 ):
                l=Label(ventana,text="felicidades ganas con la fila 31,32,33").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if((Ganador==34 or Ganador==35 or Ganador==36)and compn==343536 ):
                l=Label(ventana,text="felicidades ganas con la fila 34,35,36").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
        if(com=="par"):
            if(compn==0 and Ganador%2==0 and Ganador!=0):
                l=Label(ventana,text="felicidades ganas con pares").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*2+IApuesta
            if(compn==1 and Ganador%2!=0 and Ganador!=0):
                l=Label(ventana,text="felicidades ganas con pares").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*2+IApuesta

        if(com=="doble"):
            if(doble[i]=="1,2" and (Ganador==1 or Ganador==2) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="2,3" and (Ganador==2 or Ganador==3) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="4,5" and (Ganador==4 or Ganador==5) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="5,6" and (Ganador==5 or Ganador==6) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="7,8" and (Ganador==7 or Ganador==8) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="11,12" and (Ganador==11 or Ganador==12) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="13,14" and (Ganador==13 or Ganador==14) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="14,15" and (Ganador==14 or Ganador==15) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="17,18" and (Ganador==17 or Ganador==18) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="19,20" and (Ganador==19 or Ganador==20) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="20,21" and (Ganador==20 or Ganador==21) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="22,23" and (Ganador==22 or Ganador==23) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="23,24" and (Ganador==23 or Ganador==24) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="25,26" and (Ganador==25 or Ganador==26) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="26,27" and (Ganador==26 or Ganador==27) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="28,29" and (Ganador==28 or Ganador==29) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="29,30" and (Ganador==29 or Ganador==30) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="31,32" and (Ganador==31 or Ganador==32) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="32,33" and (Ganador==32 or Ganador==33) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="34,35" and (Ganador==34 or Ganador==35) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="35,36" and (Ganador==35 or Ganador==36) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta  
            if(doble[i]=="1,4" and (Ganador==4 or Ganador==1) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="4,7" and (Ganador==4 or Ganador==7) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="7,10" and (Ganador==7 or Ganador==10) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="10,13" and (Ganador==10 or Ganador==13) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="13,16" and (Ganador==13 or Ganador==16) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="16,19" and (Ganador==16 or Ganador==19) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="19,22" and (Ganador==19 or Ganador==22) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="22,25" and (Ganador==22 or Ganador==25) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="25,28" and (Ganador==25 or Ganador==28) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="28,31" and (Ganador==28 or Ganador==31) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="31,33" and (Ganador==31 or Ganador==34) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="1,5" and (Ganador==2 or Ganador==5) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="5,8" and (Ganador==5 or Ganador==8) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="8,11" and (Ganador==8 or Ganador==11) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="11,14" and (Ganador==11 or Ganador==14) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="14,17" and (Ganador==14 or Ganador==17) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="17,20" and (Ganador==17 or Ganador==20) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="20,23" and (Ganador==20 or Ganador==23) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="23,26" and (Ganador==23 or Ganador==26) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="26,29" and (Ganador==26 or Ganador==29) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="29,32" and (Ganador==29 or Ganador==32) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="32,35" and (Ganador==32 or Ganador==35) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="3,6" and (Ganador==3 or Ganador==6) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="6,9" and (Ganador==6 or Ganador==9) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="9,12" and (Ganador==9 or Ganador==12) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="12,15" and (Ganador==12 or Ganador==15) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="15,18" and (Ganador==15 or Ganador==18) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="18,21" and (Ganador==18 or Ganador==21) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="21,24" and (Ganador==21 or Ganador==24) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="24,27" and (Ganador==24 or Ganador==27) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="27,30" and (Ganador==27 or Ganador==30) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="30,33" and (Ganador==30 or Ganador==33) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
            if(doble[i]=="33,36" and (Ganador==33 or Ganador==36) ):
                l=Label(ventana,text="felicidades ganas con doble").place(x=900,y=300)
                IApuesta=Apuestas1[i][0]*17+IApuesta
             
        #if(com="linea"): 
        i=i+1
    l=Label(ventana,text=("tu saldo ahora es  ",IApuesta),bg="white").place(x=900,y=280)






def rotar ():#funcion que rota la imagen mediante un ciclo
    global Imagen0,Imagen1,Imagen,Ganador,Napuesta,l
    Ganador=0
    A=random.randint(5,25)
    for e in range (0,A):
        ImagenT=PhotoImage(file="tablero.gif") #se extrae la imagen para label
        l=Label(ventana,image=ImagenT).place(x=700, y=500)
        Imagen0=Image.open("A.gif") #se lee la imagen normal
        Imagen1=Imagen0.rotate(1*e,fillcolor="black") #se rota la imagen
        Imagen1.save("rotada.gif") # se guarda la imagen que se ha rotado
        Imagen=PhotoImage(file="rotada.gif") #se extrae la imagen para label
        l=Label(ventana,image=Imagen).place(x=0, y=0) #se imprime la imagen
        ventana.update() #se actualiza cada evento de la imagen
        time.sleep(0.2) #tiempo de espera para notar el cambio y controlar la velocidad
    Ganador=random.randint(0,36)
    ganador()





def retirarse ():
    ventana.destroy()




ventana=Tk()
ventana.geometry("1100x1000")
ventana.config(bg="black")
minimo=StringVar()
l=Label(ventana,text="inserta tu apuesta minimo 10").grid(column=0,row=0)
cuadro00=Entry(ventana,textvariable=minimo,state="normal",width=2,bg="blue")
cuadro00.place(width=90,height=30)
cuadro00.place(x=0, y=25)
B1=Button(ventana,text="aceptar",command=Apuesta_minima,bg="white",width=30)
B1.place(x=100, y=25)
B2=Button(ventana,text="retirarse",command=retirarse,bg="white",height=5,width=10)
B2.place(x=900,y=10)
BL=Button(ventana,text="volver a jugar",command=Volver_jugar,bg="white",height=5,width=10)
BL.place(x=900,y=90)


ventana.mainloop()








