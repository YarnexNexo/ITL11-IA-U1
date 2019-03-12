class tablero(object):

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

    #Regresa un elemento de la lista con las cordenadas espesificadas
    def get_Element_M_Matriz(self,i,j):
        return self.m_matriz[i][j]

    #Modifica un elemento de la lista con las cordenadas espesificadas    
    def set_Element_M_Matriz(self,i,j,elemento):
        self.m_matriz[i][j] = elemento
    
    #Metodos
    
    #Imprimie el contenido de la matriz "m_matria"
    def imprimir_Consola_M_Matriz(self):
        for i in range(self.ren):
            print self.m_matriz[i]

    #REINICIA EL CONTENIDO DE LA MATRIZ A CERO "0" 
    def reiniciar_M_Mat(self):
        axi = []
        for i in range(self.ren):
            for j in range(self.col):
                axi.append(0);
            self.m_matriz.append(axi)
            axi = []

    #Agrega un "lists de lista" a la lista princiapla
    def add_M_Matriz(self,m_mat,x_mat,y_mat):
        for i in range(len(m_mat)):
            for j in range(len(m_mat[i])):
                if(m_mat[i][j]>0):            
                    self.m_matriz[i+x_mat][j+y_mat] = m_mat[i][j]

    #Object                
    def __str__(self):
        return (self.name)
