from random import random

class registro(object):

    #Costructor
    def __init__(self,col,ren,name):
        self.col = col
        self.ren = ren
        self.name = name;
        self.m_matriz = []

    #Metodos "Get y Set"    
    def get_Name(self):
        return self.name
    
    def set_Name(self,newName):
        self.name = newName

    def get_Ren(self):
        return self.ren
    
    def get_Col(self):
        return self.col

    def get_M_Matriz(self):
        return self.m_matriz
    
    def set_M_Matriz(self,mat):
        self.m_matriz = mat
    
    #REINICIA EL CONTENIDO DE LA MATRIZ A CERO "0" 
    def reiniciar_M_Mat(self):
        axi = []
        for i in range(self.ren):
            for j in range(self.col):
                axi.append(0);
            self.m_matriz.append(axi)
            axi = []
            
    def IMC(self,mat):
        for i in range(len(mat)):
            print(mat[i])

    def cordenadas_selecion_obstaculos(self,lista,num):
        axi_X = lista[0]
        axi_Y = lista[1]
        cadx = []
        cady = []

        lisXY_Sobrante = []
        lisXY_Selecionada = []
    
        for i in range(num):
            num_ran = int(len(axi_X) * random())
            cadx.append(axi_X.pop(num_ran))
            cady.append(axi_Y.pop(num_ran))
    
        lisXY_Selecionada.append(cadx)
        lisXY_Selecionada.append(cady)
    
        lisXY_Sobrante.append(axi_X)
        lisXY_Sobrante.append(axi_Y)
    
        return lisXY_Sobrante,lisXY_Selecionada

    def lista_cordena_mat(self,mat):
        axi_X = []
        axi_Y = []
        lista_XY = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                axi_X.append(i)
                axi_Y.append(j)

        lista_XY.append(axi_X)
        lista_XY.append(axi_Y)
        return lista_XY

    def colocar_num(self,mat,lisXY,num):
        #print("go",len(lisXY[0]))
        for i in range(len(lisXY[0])):
            ren = lisXY[0][i]
            col = lisXY[1][i]
            mat[ren][col] = num
        return mat

    def colocar_Elemento(self,mat,num_obs,num,):
        for i in range(num_obs):
            mat[int(ren * random())][int(col * random())] = num
        return mat

    def cordenadas_XY_Rey(self,x,y,lista_Obstaculos_XY,col,ren):
        a_x = []
        a_y = []
        a = []

        l_x = [x,x-1,x+1,x-1,x,x-1,x+1,x+1]
        l_y = [y-1,y,y,y+1,y+1,y-1,y+1,y-1]
        for g in range(len(l_x)):
            if(l_x[g] >= 0 and l_x[g] < ren and l_y[g] >= 0 and l_y[g] < col):
                a_x.append(l_x[g])
                a_y.append(l_y[g])
        l_x = a_x
        l_y = a_y
        
        t_x = []
        t_y = []
        
        bandera = True
        for h in range(len(l_x)):
            for f in range(len(lista_Obstaculos_XY[1])):
                if(l_x[h] == lista_Obstaculos_XY[0][f] and l_y[h] == lista_Obstaculos_XY[1][f]):
                    #print l_x[h],lista_Obstaculos_XY[0][f],l_y[h],lista_Obstaculos_XY[1][f]
                    t_x.append(l_x[h])
                    t_y.append(l_y[h])
                    
        for q in range(len(t_x)):
            for w in range(len(a_x)):
                if(t_x[q] == l_x[w] and t_y[q] == l_y[w]):
                    l_x.pop(w)
                    l_y.pop(w)
                    break            
        a_x = l_x
        a_y = l_y 
    
        a.append(a_x)
        a.append(a_y)
        return a
    
    def cordenadas_XY_Torre(self,x,y,lista_Obstaculos_XY,col,ren):
        a_x = []
        a_y = []
        a = []

        #l_x = [x,x-1,x+1,x-1,x,x-1,x+1,x+1]
        #l_y = [y-1,y,y,y+1,y+1,y-1,y+1,y-1]
        
        l_x = [x-1,x,x,x+1]
        l_y = [y,y-1,y+1,y]
        
        for g in range(len(l_x)):
            if(l_x[g] >= 0 and l_x[g] < ren and l_y[g] >= 0 and l_y[g] < col):
                a_x.append(l_x[g])
                a_y.append(l_y[g])
        l_x = a_x
        l_y = a_y
        
        t_x = []
        t_y = []
        
        bandera = True
        for h in range(len(l_x)):
            for f in range(len(lista_Obstaculos_XY[1])):
                if(l_x[h] == lista_Obstaculos_XY[0][f] and l_y[h] == lista_Obstaculos_XY[1][f]):
                    #print l_x[h],lista_Obstaculos_XY[0][f],l_y[h],lista_Obstaculos_XY[1][f]
                    t_x.append(l_x[h])
                    t_y.append(l_y[h])
                    
        for q in range(len(t_x)):
            for w in range(len(a_x)):
                if(t_x[q] == l_x[w] and t_y[q] == l_y[w]):
                    l_x.pop(w)
                    l_y.pop(w)
                    break            
        a_x = l_x
        a_y = l_y 
    
        a.append(a_x)
        a.append(a_y)
        return a
    
    
    def IMC_E(self,mat):
        mat_obstaculo = ""
        mat_libre = ""
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(mat[i][j]!=0):
                    mat_obstaculo+=str(mat[i][j])
                    mat_libre+=" "
                else:
                    mat_obstaculo+=" "
                    mat_libre+=str(mat[i][j])
            mat_obstaculo +="\n"
            mat_libre +="\n"
        
        return mat_obstaculo,mat_libre

    def tiene_solucion(self,mat):
        i_inicio = 0
        j_inicio = 0
        resultado = True

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                i_inicio+=1
                break
        return resultado,i_inicio

    #Object                
    def __str__(self):
        return (self.name)
