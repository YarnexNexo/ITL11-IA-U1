#Librerias importadasa
from tablero import tablero
from registro import registro
from random import random

import time 

#Bloque principal
base = 70 #Base para las dimenciones del bloque "ancho y alto"
casilla_H = 10 #Nuemro de bloque para los "Renglones"
casilla_W = 10 #Nuemro de bloque para las "Columnas"

#LEYENDA DEL: "Robot_IA_v1"
x_Leyenda = 0
y_Leyenda = 20
medida_Leyenda = 15
espacio_Leyenda = 300
contenido_Leyenda = ""

#Mundo Princiapal
axi_M_Matriz = []
lis_cordenadas_M_Matriz_XY = []
lis_cordenadas_Libres_M_Matriz_XY = []
lis_cordenadas_obstaculos_M_Matriz_XY = []
lis_cordenadas_objetivo_M_Matriz_XY = []
lis_cordenadas_bateria_M_Matriz_XY = []
num_obstaculos = 150
aximat = []

#Robot
robot = []
x_robot = 0
y_robot = 0
estado_robot = ""     
energuia_robot = 200
base_robot = 4
cuerpo =[[0,0,1,0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,0,1,1,1,0,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,1,1,1,1,0,1],[1,0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,0,0]]

#Objetivo
objetivo = [[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,0]]
r_objetivo = [[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,255,255,255,255,255,1,0,0],[0,1,255,255,255,255,255,255,255,1,0],[1,255,255,255,1,1,1,255,255,255,1],[1,255,255,255,1,255,255,255,255,255,1],[1,255,255,255,255,1,255,255,255,255,1],[1,255,255,255,255,255,1,255,255,255,1],[1,255,255,255,1,1,1,255,255,255,1],[0,1,255,255,255,255,255,255,255,1,0],[0,0,1,255,255,255,255,255,1,0,0],[0,0,0,1,1,1,1,1,0,0,0]]
g_objetivo = [[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,255,255,255,255,255,1,0,0],[0,1,255,255,255,255,255,255,255,1,0],[1,255,255,255,1,1,1,255,255,255,1],[1,255,255,255,1,255,255,255,255,255,1],[1,255,255,255,255,1,255,255,255,255,1],[1,255,255,255,255,255,1,255,255,255,1],[1,255,255,255,1,1,1,255,255,255,1],[0,1,255,255,255,255,255,255,255,1,0],[0,0,1,255,255,255,255,255,1,0,0],[0,0,0,1,1,1,1,1,0,0,0]]
b_objetivo = [[0,0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,0,0,0]]

#Bateria
bateria = [[0,0,0,0,1,1,1,1,0,0,0,0],[0,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1]]
r_bateria = [[0,0,0,0,1,1,1,1,0,0,0,0],[0,1,1,1,1,200,200,1,1,1,1,0],[1,200,200,200,200,200,200,200,200,200,200,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,255,255,255,255,255,255,255,255,255,255,1],[1,255,255,1,1,1,1,1,1,255,255,1],[1,255,1,255,255,255,255,255,1,1,255,1],[1,255,1,255,255,1,1,255,255,1,255,1],[1,255,1,255,255,255,255,255,1,1,255,1],[1,255,1,255,255,1,1,255,255,1,255,1],[1,255,1,255,255,255,255,255,1,1,255,1],[1,255,255,1,1,1,1,1,1,255,255,1]]
g_bateria = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,200,200,1,1,1,1,0],[1,200,200,200,200,200,200,200,200,200,200,1],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,255,255,0,0,255,255,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,255,255,0,0,255,255,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
b_bateria = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,200,200,1,1,1,1,0],[1,200,200,200,200,200,200,200,200,200,200,1],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,255,255,0,0,255,255,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,255,255,0,0,255,255,0,0,0],[0,0,0,255,255,255,255,255,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]

#Robot
Obstaculos = []
x_Obstaculos = 0
y_Obstaculos = 0
bandere_estado = False
contador_movimientos = 0

#
xxrespaldo = 0
yyrespaldo = 0
def setup():
    
    #Configuracion del "Leyenda"
    global x_Leyenda
    global contenido_Leyenda
    global leyenda
    global energuia_robot
    #global estado_robot
    global x_robot
    global y_robot
    
    #
    global lis_cordenadas_M_Matriz_XY
    global lis_cordenadas_Libres_M_Matriz_XY
    global lis_cordenadas_obstaculos_M_Matriz_XY
    global lis_cordenadas_objetivo_M_Matriz_XY
    global lis_cordenadas_bateria_M_Matriz_XY
    global num_obstaculos
    global aximat
    
    #Iniciando tableros
    global Obstaculos
    
    reg = registro(casilla_W,casilla_H,"Matriz mundo") 
    reg.reiniciar_M_Mat()
    
    #Se obtienen todas las cordenadas posibles sin repetir
    lis_cordenadas_M_Matriz_XY = reg.lista_cordena_mat(reg.get_M_Matriz())
     
    #Se coloca Obstaculos
    (lis_cordenadas_M_Matriz_XY,lis_cordenadas_obstaculos_M_Matriz_XY) = reg.cordenadas_selecion_obstaculos(lis_cordenadas_M_Matriz_XY,int((casilla_H*casilla_W)*0.10))
    reg.set_M_Matriz(reg.colocar_num(reg.get_M_Matriz(),lis_cordenadas_obstaculos_M_Matriz_XY,1))
    lis_cordenadas_Libres_M_Matriz_XY = lis_cordenadas_M_Matriz_XY
    print "Obstaculos",lis_cordenadas_obstaculos_M_Matriz_XY

    #Se coloca objetivo
    (lis_cordenadas_M_Matriz_XY,lis_cordenadas_objetivo_M_Matriz_XY) = reg.cordenadas_selecion_obstaculos(lis_cordenadas_M_Matriz_XY,1)
    reg.set_M_Matriz(reg.colocar_num(reg.get_M_Matriz(),lis_cordenadas_objetivo_M_Matriz_XY,2))
    print "Objetivo",lis_cordenadas_objetivo_M_Matriz_XY
    
    #Se coloca bateria
    (lis_cordenadas_M_Matriz_XY,lis_cordenadas_bateria_M_Matriz_XY) = reg.cordenadas_selecion_obstaculos(lis_cordenadas_M_Matriz_XY,1)
    reg.set_M_Matriz(reg.colocar_num(reg.get_M_Matriz(),lis_cordenadas_bateria_M_Matriz_XY,3))
    print "Bateria",lis_cordenadas_bateria_M_Matriz_XY
        
    #Se coloca robot
    (lis_cordenadas_M_Matriz_XY,lis_cordenadas_avatar_M_Matriz_XY) = reg.cordenadas_selecion_obstaculos(lis_cordenadas_M_Matriz_XY,1)
    reg.set_M_Matriz(reg.colocar_num(reg.get_M_Matriz(),lis_cordenadas_avatar_M_Matriz_XY,0))

    x_robot = lis_cordenadas_avatar_M_Matriz_XY[0][0]
    y_robot = lis_cordenadas_avatar_M_Matriz_XY[1][0]
    
    Obstaculos = reg.get_M_Matriz()
    
    #Dimencion de la ventana principal
    size((base*casilla_W+1)+espacio_Leyenda,base*casilla_H+1)
    x_Leyenda = base*casilla_W+1

def limpiar_Ventana():
    stroke(0,0,0) #Color de borde "Negro<"
    fill(255,255,255) #Color de fondo "Blanco"
    rect(0,0,(base*casilla_W+1),(base*casilla_H+1))

def reset_MatrizWordV():
    #CONTENIDO DE LA MATRIZ "matrizWordV"
    axi = []
    for i in range(casilla_H):
        for j in range(casilla_W):
            axi.append(0);
        matrizWordV.append(axi)
        axi = []

def infoProgram():
    #Dibuja fondo
    stroke(0,0,0)#Color de borde "Negro"
    fill(0,0,0)#Color de fondo "Negro"
    rect((base*casilla_W+1),1,(espacio_Leyenda),(base*casilla_H+1))
    
    #Dibuja leyenda
    fill(0,255,0) #Color de la fuente "Verde"
    textSize(medida_Leyenda) #Tamño de la fuente
    contenido_Leyenda = str(int(frameRate))
    contenido_Leyenda += str("\nEnerguia del robot: ")
    contenido_Leyenda += str(energuia_robot)
    contenido_Leyenda += str("\nEstodo: ")
    contenido_Leyenda += estado_robot
    contenido_Leyenda += "\nNumero mov: "
    contenido_Leyenda += str(contador_movimientos) 
    #print estado_robot
    text(("Robot_IA_V21\nFPS: " + contenido_Leyenda),x_Leyenda ,y_Leyenda)

def play():
    #robot 1
    global robot
    robot = [[5,0],[0,0]]

    #Objeto
    global wordV
    wordV = tablero(casilla_W,casilla_H,"Matriz mundo")
    
    wordV.reiniciar_M_Mat()
    
    
    if(bandere_estado):
        wordV.add_M_Matriz(robot,x_robot,y_robot)
        wordV.add_M_Matriz(Obstaculos,x_Obstaculos,y_Obstaculos)
        wordV.set_Element_M_Matriz(x_robot,y_robot,5)
    else:
        wordV.add_M_Matriz(robot,x_robot,y_robot)
        wordV.add_M_Matriz(Obstaculos,x_Obstaculos,y_Obstaculos)

def draw():
    #Variables globales
    global axi_M_Matriz
    global x_robot
    global y_robot
    global energuia_robot
    global estado_robot
    global bandere_estado
    global xxrespaldo
    global yyrespaldo
    global contador_movimientos
    #Ejecuta la aplicacion
    play()
    
    #Estado buscado
    if(energuia_robot>0 and bandere_estado == False):
        #Posibles movimientos
        movimientos = registro(casilla_W,casilla_H,"Movimieto")
        mov = movimientos.cordenadas_XY_Rey(x_robot,y_robot,lis_cordenadas_obstaculos_M_Matriz_XY,casilla_W,casilla_H)
        #print "\nPunto de partida x: ",x_robot," y: ",y_robot
        #print "Lista de movimientos: ",mov
        #---------------------------
        for esCordenada in range(len(mov[0])):
            if (mov[0][esCordenada] == lis_cordenadas_objetivo_M_Matriz_XY[0][0] and mov[1][esCordenada] == lis_cordenadas_objetivo_M_Matriz_XY[1][0]):
                x_robot = lis_cordenadas_objetivo_M_Matriz_XY[0][0]
                y_robot = lis_cordenadas_objetivo_M_Matriz_XY[1][0]
                xxrespaldo = x_robot
                yyrespaldo = y_robot
                #energuia_robot-=1
                break
            else:
                dec_mov = int((len(mov[0])) * random())
                xxrespaldo = x_robot
                yyrespaldo = y_robot
                x_robot  = mov[0][dec_mov]
                y_robot = mov[1][dec_mov]
                #energuia_robot-=1
        #print "x :",len(mov[0]) 
        #print "y :",mov[1][0]
        #print "x :",lis_cordenadas_objetivo_M_Matriz_XY[0][0]
        #print "y :",lis_cordenadas_objetivo_M_Matriz_XY[1][0]
        
        #
        contador_movimientos+=1
        #print "DEC: ",dec_mov
        #print "Moviendo x: ",mov[0][dec_mov]," y: ",mov[1][dec_mov]
        
        
        #---------------------------------
        energuia_robot-=1
        estado_robot = "Buscando"
        infoProgram()
        if(x_robot == lis_cordenadas_objetivo_M_Matriz_XY[0][0] and y_robot == lis_cordenadas_objetivo_M_Matriz_XY[1][0]):
            wordV.set_Element_M_Matriz(x_robot,y_robot,5)
            wordV.set_Element_M_Matriz(xxrespaldo,yyrespaldo,0)
            bandere_estado = True
            estado_robot = "Objetivo encontrado"
            print "SE encontro objeto"
        elif(x_robot == lis_cordenadas_bateria_M_Matriz_XY[0][0] and y_robot == lis_cordenadas_bateria_M_Matriz_XY[1][0]):
            estado_robot = "Recargando bateria"
            energuia_robot +=  100
            wordV.set_Element_M_Matriz(x_robot,y_robot,5)
            wordV.set_Element_M_Matriz(xxrespaldo,yyrespaldo,0)
            print "Recargando bateria"
            
    #Estado robot sin energuia
    elif(energuia_robot==0):
        estado_robot = "Robot sin energuia..."
        infoProgram()
        
    #Estado del programa
    infoProgram()
    
    #Comprueva si se realisaron cambios
    if(axi_M_Matriz!=wordV.get_M_Matriz()):
        limpiar_Ventana()
        #Se recore la matris "wordV.get_M_Matriz()" para dibujar los bloques
        for i in range(wordV.get_Ren()):
            for j in range(wordV.get_Col()):
                
                #Dibuja "Casillas libres"
                if(wordV.get_Element_M_Matriz(i,j) == 0):
                    stroke(220,220,220)
                    fill(255,255,255)
                    rect(base*(j),base*(i),base*1,base*1)
                
                #Dibuja "Obstaculos"
                elif(wordV.get_Element_M_Matriz(i,j) == 1):
                    stroke(0,0,0)
                    fill(0,0,0)
                    rect(base*(j),base*(i),base*1,base*1)
                
                #Dibuja "Objetivos"
                elif(wordV.get_Element_M_Matriz(i,j) == 2):
                    for i_r in range(len(objetivo)):
                        for j_r in range(len(objetivo[i_r])):
                            if(objetivo[i_r][j_r] !=0):
                                stroke(r_objetivo[i_r][j_r],g_objetivo[i_r][j_r],b_objetivo[i_r][j_r])
                                fill(r_objetivo[i_r][j_r],g_objetivo[i_r][j_r],b_objetivo[i_r][j_r])
                                rect((base_robot*(j_r))+(base*(j))+10,(base_robot*(i_r))+(base*(i))+10,base_robot*1,base_robot*1)
                
                #Dibuja "bateria"
                elif(wordV.get_Element_M_Matriz(i,j) == 3):
                    for i_r in range(len(bateria)):
                        for j_r in range(len(bateria[i_r])):
                            if(bateria[i_r][j_r] !=0):
                                stroke(r_bateria[i_r][j_r],g_bateria[i_r][j_r],b_bateria[i_r][j_r])
                                fill(r_bateria[i_r][j_r],g_bateria[i_r][j_r],b_bateria[i_r][j_r])
                                rect((base_robot*(j_r))+(base*(j))+10,(base_robot*(i_r))+(base*(i))+10,base_robot*1,base_robot*1)
                #Dibuja al "Robot"
                elif(wordV.get_Element_M_Matriz(i,j) == 9):
                    for i_r in range(len(cuerpo)):
                        for j_r in range(len(cuerpo[i_r])):
                            if(cuerpo[i_r][j_r] !=0):
                                stroke(255,0,0)
                                fill(255,0,0)
                                rect((base_robot*(j_r))+(base*(j))+10,(base_robot*(i_r))+(base*(i))+10,base_robot*1,base_robot*1)
                
                #Dibuja al "Robot prueva movimieto"
                elif(wordV.get_Element_M_Matriz(i,j) == 5):
                    for i_r in range(len(cuerpo)):
                        for j_r in range(len(cuerpo[i_r])):
                            if(cuerpo[i_r][j_r] !=0):
                                stroke(255,0,0)
                                fill(255,0,0)
                                rect((base_robot*(j_r))+(base*(j))+10,(base_robot*(i_r))+(base*(i))+10,base_robot*1,base_robot*1)

        #Actualismos el Matriz AXILIAR                    
        axi_M_Matriz = wordV.get_M_Matriz()

        #Tiempo de espera para el siguiente movimiento
        time.sleep(.1)
        
        
