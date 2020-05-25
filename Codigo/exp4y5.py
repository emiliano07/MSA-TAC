import Grasp.grasp as gr
import Programacion_Dinamica.programacionDinamica as pd
from timeit import default_timer
import numpy as np
import copy as c

#-------------------------------------------------------------------------------------------------

A = "A"
C = "C"
G = "G"
T = "T"
_ = "_"

# 4 SECUENCIAS DE 4 NUCLEOTIDOS
S0 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G]]
# 5 SECUENCIAS DE 4 NUCLEOTIDOS
S1 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G],[A,T,G,G]]
# 6 SECUENCIAS DE 4 NUCLEOTIDOS
S2 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G],[A,T,G,G],[G,T,C,G]]
# 7 SECUENCIAS DE 4 NUCLEOTIDOS
S3 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G],[A,T,G,G],[G,T,C,G],[G,T,G,G]]
# 8 SECUENCIAS DE 4 NUCLEOTIDOS
S4 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[G,T,C,G],[G,T,G,G]]
# 9 SECUENCIAS DE 4 NUCLEOTIDOS
S5 = [[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,C,G],[A,T,G,G],[A,T,G,G],[G,T,C,G],[G,T,G,G],[A,T,G,G]]

#-------------------------------------------------------------------------------------------------

def calcularScore(secuencias):
  score = 0
  for u in range(0,len(secuencias)):
    for v in range(u+1,len(secuencias)):
      score += scorePar(secuencias[u],secuencias[v])
  return score

def scorePar(u,v):
  score = 0
  for i in range(0,len(u)):
    score += costoComparacion(u[i],v[i])
  return score

def costoComparacion(u,v):
  match = 3
  missmatch = -1
  gap = 1
  if (u == v):
    if(u == "_"):
      return 0
    return match
  else:
    if(u == "_" or v == "_"):
      return gap
    return missmatch

def executeGrasp(secAux,nExe):
  ejecuciones = nExe
  #print("---------------------")
  print("Grasp")
  #print("---------------------")
  promTiempo = 0
  for x in range(ejecuciones):
      #print("Ejecucion N°: " + str(x+1))
      ti = default_timer() 
      grAux = gr.grasp(30,secAux)
      tf = default_timer()
      tiempo = tf - ti
      promTiempo += tiempo
      secFinal = grAux["PROFILE"]["SECUENCIAS"]
      #print("---------------------")
      #print("Secuencias Iniciales:")
      #for i in range(0,len(secAux)):
      #    print(' '.join(map(str, secAux[i])))
      #print("---------------------")
      #print("Alineamiento Final:")
      #for i in range(0,len(secFinal)):
      #    print(' '.join(map(str, secFinal[i])))
      #print("---------------------")
      tiempo = round(tiempo,2)
      print("Tiempo " + str(x+1) + " = " + str(tiempo) + " segundos")
      scoreGR = calcularScore(secFinal)
      print("Score Grasp " + str(x+1) + " = " + str(scoreGR))
      #print("---------------------")
  promTiempo = promTiempo / ejecuciones
  promTiempo = round(promTiempo,2)
  print("Tiempo promedio = " + str(promTiempo) + " segundos")
  print("---------------------")
  return (grAux,scoreGR)

def executePD(secAux,nExe):
  ejecuciones = nExe
  print("---------------------")
  print("Programacion Dianmica")
  #print("---------------------")
  promTiempo = 0
  for x in range(ejecuciones):
    #print("Ejecucion N°: " + str(x+1))
    ti = default_timer() 
    pdAux = pd.alineamiento(secAux)
    tf = default_timer()
    tiempo = tf - ti
    promTiempo += tiempo
    #print("---------------------")
    #print("Secuencias Iniciales:")
    #for i in range(0,len(secAux)):
    #    print(' '.join(map(str, secAux[i])))
    #print("---------------------")
    #print("Alineamiento Final:")
    #for i in range(0,len(pdAux)):
    #    print(' '.join(map(str, pdAux[i])))
    #print("---------------------")
    tiempo = round(tiempo,2)
    print("Tiempo " + str(x+1) + " = " + str(tiempo) + " segundos")
    scorePD = calcularScore(pdAux)
    print("Score PD " + str(x+1) + " = " + str(scorePD))
    #print("---------------------")
  promTiempo = promTiempo / ejecuciones
  promTiempo = round(promTiempo,2)
  print("Tiempo promedio = " + str(promTiempo) + " segundos")
  print("---------------------")
  return (pdAux,scorePD)

#-------------------------------------------------------------------------------------------------

print("------------------------------------------------------")
print("------------------------------------------------------")
print("Experimento N° 3")
print("------------------------------------------------------")
print("------------------------------------------------------")
print("Secuencias Iniciales:")
print("------------------------------------------------------")
secuencias = [S0,S1,S2,S3,S4,S5]
secuenciasC = [S0,S1,S2]
secuenciasM = [S3,S4]
secuenciasL = [S5]
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    for i in range(0,len(secuencias[sec])):
        print(' '.join(map(str, secuencias[sec][i])))
    escenario += 1
    print("---------------------")
print("------------------------------------------------------")
print("Ejecuciones:")
print("------------------------------------------------------")
resultadosPD = []
resultadosGRASP = []
escenario = 1
for sec in range(0,len(secuenciasC)):
    print("Escenario N° " + str(escenario))
    resultadosPD.append(executePD(secuenciasC[sec],8))
    resultadosGRASP.append(executeGrasp(secuenciasC[sec],8))
    escenario += 1
    print("---------------------")
for sec in range(0,len(secuenciasM)):
    print("Escenario N° " + str(escenario))
    resultadosPD.append(executePD(secuenciasM[sec],4))
    resultadosGRASP.append(executeGrasp(secuenciasM[sec],4))
    escenario += 1
    print("---------------------")
for sec in range(0,len(secuenciasL)):
    print("Escenario N° " + str(escenario))
    resultadosPD.append(executePD(secuenciasL[sec],2))
    resultadosGRASP.append(executeGrasp(secuenciasL[sec],2))
    escenario += 1
    print("---------------------")
print("------------------------------------------------------")
print("Alineamiento Final:")
print("------------------------------------------------------")
escenario = 1
for sec in range(0,len(secuencias)):
    print("Escenario N° " + str(escenario))
    print("---------------------")
    print("Programacion Dinamica")
    for i in range(0,len(resultadosPD[sec][0])):
        print(' '.join(map(str, resultadosPD[sec][0][i])))
    print("Score Final PD = " + str(resultadosPD[sec][1]))
    print("---------------------")
    print("Grasp")
    for i in range(0,len(resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"])):
        print(' '.join(map(str, resultadosGRASP[sec][0]["PROFILE"]["SECUENCIAS"][i])))
    print("Score Final Grasp = " + str(resultadosGRASP[sec][1]))
    escenario += 1
    print("---------------------")
    print("---------------------")