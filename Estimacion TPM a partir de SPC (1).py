# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:55:09 2019

@author: gvera
"""


import numpy  as np
import matplotlib.pyplot as mpl


import datetime 



def tpm(fecha_ultima_reunion, tasa_ultima_reunion, fecha_hoy,tspc3,tspc6,tspc12):
    fur=datetime.datetime.strptime(fecha_ultima_reunion,"%d-%m-%Y").date()
    hoy=datetime.datetime.strptime(fecha_hoy,"%d-%m-%Y").date()

    fur=datetime.datetime.strptime(fecha_ultima_reunion,"%d-%m-%Y").date()
    hoy=datetime.datetime.strptime(fecha_hoy,"%d-%m-%Y").date()
    #las fechas empieza 1 mes despues de la fecha de hoy
    fr_1=datetime.datetime.strptime("10-04-2021","%d-%m-%Y").date()
    fr_2=datetime.datetime.strptime("10-05-2021","%d-%m-%Y").date()
    fr_3=datetime.datetime.strptime("10-06-2021","%d-%m-%Y").date()
    fr_4=datetime.datetime.strptime("10-07-2021","%d-%m-%Y").date()
    fr_5=datetime.datetime.strptime("10-08-2021","%d-%m-%Y").date()
    fr_6=datetime.datetime.strptime("10-09-2021","%d-%m-%Y").date()
    fr_7=datetime.datetime.strptime("10-10-2021","%d-%m-%Y").date()
    fr_8=datetime.datetime.strptime("10-11-2021","%d-%m-%Y").date()
    fr_9=datetime.datetime.strptime("10-12-2021","%d-%m-%Y").date()
    fr_10=datetime.datetime.strptime("10-01-2022","%d-%m-%Y").date()
    fr_11=datetime.datetime.strptime("10-02-2022","%d-%m-%Y").date()
    
    fechas=[]
    variacion_dias=[]
    coeficientes3=[]
    coeficientes6=[]
    coeficientes12=[]
    spc=[]
    
    fechas.append(fur)
    fechas.append(hoy)
    fechas.append(fr_1)
    fechas.append(fr_2)
    fechas.append(fr_3)
    fechas.append(fr_4)
    fechas.append(fr_5)
    fechas.append(fr_6)
    fechas.append(fr_7)
    fechas.append(fr_8)
    fechas.append(fr_9)
    fechas.append(fr_10)
    fechas.append(fr_11)
    
    
    for j in range(len(fechas)):
        dias=fechas[j]-fechas[j-1] 
        variacion_dias.append(dias.days)
        
    
    variacion_dias.pop(0)
    
    for i in range(0,3):
        coef_1=variacion_dias[i]/(variacion_dias[0]+variacion_dias[1]+variacion_dias[2])
        coeficientes3.append(coef_1)
    for i in range(0,6):
        coef_1=variacion_dias[i]/(variacion_dias[0]+variacion_dias[1]+variacion_dias[2]+variacion_dias[3]+variacion_dias[4]+variacion_dias[5])
        coeficientes6.append(coef_1)
    for i in range(0,12):
        coef_1=variacion_dias[i]/(variacion_dias[0]+variacion_dias[1]+variacion_dias[2]+variacion_dias[3]+variacion_dias[4]+variacion_dias[5]+variacion_dias[6]+variacion_dias[7]+variacion_dias[8]+variacion_dias[9]+variacion_dias[10]+variacion_dias[11])
        coeficientes12.append(coef_1)
        
    coeficientes3[0]=float(coeficientes3[0])*(tasa_ultima_reunion/100)
    coeficientes6[0]=float(coeficientes6[0])*(tasa_ultima_reunion/100)
    coeficientes12[0]=float(coeficientes12[0])*(tasa_ultima_reunion/100)
    
    spc.append((tspc3/100)-coeficientes3[0])
    spc.append((tspc6/100)-coeficientes6[0])
    spc.append((tspc12/100)-coeficientes12[0])
    
    
    
    #Ahora tenemos que llenar con zero lo que faltan en las matrices
    for i in range(len(coeficientes3),len(coeficientes12)):
        coeficientes3.append(0)
        
    for i in range(len(coeficientes6),len(coeficientes12)):
        coeficientes6.append(0)
    
    print('variacion_dias : ',variacion_dias)

    coef=np.array([coeficientes3,
                  coeficientes6,
                  coeficientes12,              
                  ])
    spc=np.array(spc)
    
    res= np.linalg.lstsq(coef,spc)
    res[0][0]=tasa_ultima_reunion/100
    print(res)
    print(len(fechas))
    fechas_para_grafico=fechas
    del fechas_para_grafico[1]
    print(len(fechas_para_grafico))
    mpl.figure(figsize=(10,5))
    mpl.plot(fechas_para_grafico,res[0]*100,"bo")
    mpl.ylabel("TPM")
    mpl.xlabel("Fechas")
    mpl.ylim(top=3,bottom=0)
   

    
    mpl.title("Estimación de la TPM implícita en las tasa swap promedio cámara para 3m, 6m y 1y al {0}".format(fecha_hoy))
    mpl.grid(True)
    print("¿CORREGISTE LAS FECHAS PROYECTADAS?")
    print(fechas_para_grafico)
    mpl.show()


tpm(fecha_ultima_reunion='27-01-2021',tasa_ultima_reunion=0.5, fecha_hoy='10-03-2021',tspc3=0.35,tspc6=0.425,tspc12=0.635)

