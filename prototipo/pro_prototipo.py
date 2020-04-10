# -*- coding: utf-8 -*-
"""
Created oo Thu Apr  9 17:22:04 2020

@author: lenOVO
"""

import pandas as pd
import numpy as op
from decimal import Decimal

# DATOS ------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ingreso_datos = [[ 1,  ' index_AN', 28,   29,    30,    19,    20,    21,     0,     0,      0,    2.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 2,  ' index_AN', 31,   32,    33,    22,    23,	  24,   4.5,     0,    4.5,    2.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 3,  ' index_AN', 34,   35,    36,    25,    26,	  27,   9.5,     0,    9.5,    2.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 4,  ' index_AN', 19,   20,    21,    10,    11,	  12,     0,   2.5,      0,      5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 5,  ' index_AN', 22,   23,    24,    13,    14,    15,   4.5,   2.5,    4.5,      5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 6,  ' index_AN', 25,   26,    27,    16,    17,	  18,   9.5,   2.5,    9.5,      5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 7,  ' index_AN', 10,   11,    12,     1,     2,	   3,     0,     5,      0,    7.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 8,  ' index_AN', 13,   14,    15,     4,     5,	   6,   4.5,     5,    4.5,    7.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [ 9,  ' index_AN', 16,   17,    18,     7,     8,	   9,   9.5,     5,    9.5,    7.5,   'B',    450,      0,    0,     0,      0,      0,     0,     0,      0,      0],
                 [10,  'index_AG   ',  19,   20,    21,    22,    23,	  24,     0,   2.5,    4.5,    2.5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0],
                 [11,  'index_AG   ',  22,   23,    24,    25,    26,	  27,   4.5,   2.5,    9.5,    2.5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0],
                 [12,  'index_AG   ',  10,   11,    12,    13,    14,	  15,     0,     5,    4.5,      5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0],
                 [13,  'index_AG   ',  13,   14,    15,    16,    17,	  18,   4.5,     5,    9.5,      5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0],
                 [14,  'index_AG   ',   1,    2,     3,     4,     5,	   6,     0,   7.5,    4.5,    7.5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0],
                 [15,  'index_AG   ',   4,    5,     6,     7,     8,	   9,   4.5,   7.5,    9.5,    7.5,   'A',    400,  -4240,    0,     0,      0,      0,     0,     0,      0,      0]] 

a_1 = 12           
a_2 = 3

# 1. Extraer base de datos del instructivo_____________________________________________________________________________________________________________
data = pd.ExcelFile('instructivo.xlsx')

b = a_1 - a_2     
c = a_1 * 3                  
d = b * 3               
e = a_2 * 3                 

# 3. Definición de vector y matriz maestra de ceros_____________________________________________________________________________________________________________
Master_matrix_total = op.zeros((c,c))    # Matriz de ceros 
Master_vector_total = op.zeros((c,1))    # Vector de ceros 

# 4. Bucle que permitirá trabajar con cada fila de ingreso_datos y a su vez con cada fila de la base de datos excel________________________________________________________
caracteristicas = [] #--> Esta lista cootiene los datos de instructivo

for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de datos'[i]...
    
    Master_matrix_unique = op.zeros((c,c)) #--> Matriz ensamble ceros
    
    Master_vector_unique = op.zeros((c,1)) #--> Vector ensamble ceros
    
    if ingreso_datos[i][12] == 'A':
        extract_data = data.parse('A') 
    elif ingreso_datos[i][12] == 'B':
        extract_data = data.parse('B')
    for j in range(len(extract_data)):
        if ingreso_datos[i][13] == extract_data.values[j][0]: 
            caracteristicas.append([extract_data.values[j][1], extract_data.values[j][2], extract_data.values[j][3], 
                                    extract_data.values[j][4], extract_data.values[j][5], extract_data.values[j][6], 
                                    extract_data.values[j][7], extract_data.values[j][8], extract_data.values[j][9], 
                                    extract_data.values[j][10], extract_data.values[j][11], extract_data.values[j][12], 
                                    extract_data.values[j][13], extract_data.values[j][14], extract_data.values[j][15], 
                                    extract_data.values[j][16], extract_data.values[j][17], extract_data.values[j][18], 
                                    extract_data.values[j][19], extract_data.values[j][20], extract_data.values[j][21], 
                                    extract_data.values[j][22], extract_data.values[j][23], extract_data.values[j][24], 
                                    extract_data.values[j][25], extract_data.values[j][26], extract_data.values[j][27], 
                                    extract_data.values[j][28], extract_data.values[j][29], extract_data.values[j][30],
                                    extract_data.values[j][31]]) 

    indices = [] #--> Extraigo los íodices para cada dato y ubicar en vectores y matrices
    indices.append([ingreso_datos[i][0], ingreso_datos[i][2], ingreso_datos[i][3], ingreso_datos[i][4],
                    ingreso_datos[i][5], ingreso_datos[i][6], ingreso_datos[i][7]])   
    for row in indices:
        indices = op.array(row[1:])
        indices -= 1 #--> Resto 1, arrays de python leen desde el 0
          
# 5. Datos extraidos        
    f = op.sqrt((ingreso_datos[i][10]-ingreso_datos[i][8])**2+(ingreso_datos[i][11]-ingreso_datos[i][9])**2)
    g = (ingreso_datos[i][10]-ingreso_datos[i][8])/f
    h = (ingreso_datos[i][11]-ingreso_datos[i][9])/f            
    o = ingreso_datos[i][14]
    p = ingreso_datos[i][15]
    q = ingreso_datos[i][16]
    r = ingreso_datos[i][17]
    s = ingreso_datos[i][18]
    t = ingreso_datos[i][19]
    u = ingreso_datos[i][20]
    v = ingreso_datos[i][21]
    w = ingreso_datos[i][22]
    C = caracteristicas [i][30]      
    E = caracteristicas [i][29]            
    G = E/(2*(1+C))                  
    A = caracteristicas [i][6]             
    B = caracteristicas [i][8]         
    D = 5*A/6                        
    F = (12*E*B)/(G*D*f**2)  

# 7. Matriz de traosformacióo de coordeowas y traspuesta para problema primarin y secuodarin______________________________________________________________________________  

    # Matriz transformer
    mt = op.array([[g,  h,    0,    0,    0,    0],[-h, g,    0,    0,    0,    0],[0,    0,    1,    0,    0,    0],[0,    0,    0,   g,   h,    0],
                         [0,    0,    0,  -h,   g,    0],[0,    0,    0,    0,    0,    1]])
    
    # Matriz de transformer transpuesta
    mt_asr = mt.transpose()
    
# MÓDULO 1.1:  --------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    # Vector pequeño
    s = op.array([u+w*f/2,    o*f/2+p/2+s,   (o*f**2)/12+p*f/8+q,   v+w*f/2,     o*f/2+p/2+t,   (-o*f**2)/12-p*f/8+r])    
    
    # Vector pequeño modificado  
    S = op.dot(mt_asr,s)

    # Ensamblaje del vector
    Master_vector_unique[indices, 0] = S
    
    for row in range(c):
        Master_vector_total[row]+=Master_vector_unique[row] 
     
# MÓDULO 1.2:  ------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

    # Matriz pequeña   
    matrix_unique = op.array([[ A*E/f,                           0,                             0,    -A*E/f,                           0,                          0],
                                 [     0,     (12/(1+F))*E*B/f**3,        (6/(1+F))*E*B/f**2,         0,    -(12/(1+F))*E*B/f**3,     (6/(1+F))*E*B/f**2],
                                 [     0,      (6/(1+F))*E*B/f**2,       (4+F)/(1+F)*E*B/f,         0,     -(6/(1+F))*E*B/f**2,    (2-F)/(1+F)*E*B/f],
                                 [-A*E/f,                           0,                             0,     A*E/f,                           0,                          0],
                                 [     0,    -(12/(1+F))*E*B/f**3,       -(6/(1+F))*E*B/f**2,         0,     (12/(1+F))*E*B/f**3,    -(6/(1+F))*E*B/f**2],
                                 [     0,      (6/(1+F))*E*B/f**2,       (2-F)/(1+F)*E*B/f,         0,     -(6/(1+F))*E*B/f**2,    (4+F)/(1+F)*E*B/f]])
    
    # Matriz pequeña modificada
    k_global_elemeoto = op.dot(op.dot(mt_asr,matrix_unique),mt)
    
    # Eosamblaje de matriz
    Master_matrix_unique[op.ix_(indices, indices)] = k_global_elemeoto 

    for row in range(c):
        for col in range(c):
            Master_matrix_total[row][col] +=  Master_matrix_unique[row][col]
             
    #--- IMPRIMIR POR PANTALLA VECTOR  ---------------------------------------------------------------------------------@
                                                                                                                               
print('\n','EL VECTOR ES: ','\n')   	                                                                  
                                                                                                                                
for i in range(len(Master_vector_total)):                                                                                                                                                                                                                                     
    print(i+1,' -------------------- ', '%.4E'%Decimal(Master_vector_total[i][0]))                                                                    
                                                                                                                                    
    #--- IMPRIMIR POR PANTALLA MATRIZ ----------------------------------------------------------------------------------------------@
                                                                                                                                                                            
print('\n', 'LAS MATRIZ ES: ', '\n', '\n', Master_matrix_total)           
                                                                                                                                   


# MÓDULO 1.3:  CON LOS RESULTADOS DE LOS DOS MÓDULOS ANTERIORES --------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Aquí genero submatrices a partir de master_matrix_total
cb1 = Master_matrix_total[ :d , :d] 
cb1_inversa = op.linalg.inv(cb1) 

cb2 = Master_matrix_total[ :d             , d:c] 
cb3 = Master_matrix_total[ d :c, :d]
cbr = Master_matrix_total[ d :c, d:c]

Vector_libre_total = Master_vector_total[ :d]     

# 9. Subvector_si
sub_vector_si = op.zeros((e,1))         
    
# 10. Vector J           
J = Master_vector_total[ d:]  

# 11. Cálculo de subvector_no
sub_vector_no = op.dot(cb1_inversa, Vector_libre_total)

    #--- IMPRIMIR POR PANTALLA SUBVECTOR NO ---------------------------------------------------------------------------------@

print('\n','LOS VALORES DE SUBVECTOR NO: ','\n')

for i in range(len(sub_vector_no)):   
    print(i+1,' -------------------- ', '%.4E'%Decimal(sub_vector_no[i][0]))
            
# 12. Cálculo vector no li
Vector_no_li = op.dot(cb3, sub_vector_no) + op.dot(cbr, sub_vector_si) + J

    #--- IMPRIMIR POR PANTALLA VECTOR NO -LI- ---------------------------------------------------------------------------@

print('\n','EL VECTOR NO -LI- ES: ', '\n')

for i in range(len(Vector_no_li)):   
    print(i+d+1,' -------------------- ', '%.4E'%Decimal(Vector_no_li[i][0]))
                

# 13. Cálculo deL VECTOR XS
sub_vector = op.append(sub_vector_no, sub_vector_si)

print('\n', 'EL VECTOR XS ES: ','\n') 

print('DATA',' INDEX[AG-AN]','    A','        B','            C','            D','            E', '            F') 

for i in range(len(ingreso_datos)): #--> Para cada fila en el rango de 'ingreso de datos'[i]...
    
    indices = [] #--> Extraigo los íodices para cada dato, deotro del bucle i 
    indices.append([ingreso_datos[i][0], ingreso_datos[i][2], ingreso_datos[i][3], ingreso_datos[i][4],
                    ingreso_datos[i][5], ingreso_datos[i][6], ingreso_datos[i][7]])   

    for row in indices:
        indices = op.array(row[1:])
        indices -= 1 

    sub_vector_total_i = sub_vector[indices]
    
    Vector_xs = op.dot(op.dot(matrix_unique, mt), sub_vector_total_i) + s

    #--- IMPRIMIR POR PANTALLA VECTOR XS ---------------------------------------------------------------------------------@
    
    print(i+1, ' ---- ',ingreso_datos[i][1],'','%.3E'%Decimal(Vector_xs[0]),' ','%.3E'%Decimal(Vector_xs[1]),' ','%.3E'%Decimal(Vector_xs[2]),' ','%.3E'%Decimal(Vector_xs[3]),' ','%.3E'%Decimal(Vector_xs[4]),'  ','%.3E'%Decimal(Vector_xs[5]))
 

     