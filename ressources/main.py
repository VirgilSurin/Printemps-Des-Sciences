import umage
import sys
from docopt import docopt
import copy
import math

def convolution(mat_img, mat) :
    new_img = copy.deepcopy(mat_img)
    for i in range(len(mat_img)) :
        for j in range(len(mat_img[i])) :
            new_img[i][j] = appliquer_convolution(mat_img, mat, i, j)
    return new_img

def appliquer_convolution(img, mat, i, j) :
    """
    mat doit être une matrice impaire et carrée
    """
    ligne = -len(mat) // 2
    R = 0
    G = 0
    B = 0
    for line in range(len(mat)) :
        colonne = -len(mat[line]) // 2 #se réinitialise à la fin d'une ligne de pixel voisin
        for column in range(len(mat[line])) :
            pixel_value = pixel(img, i+ligne, j+colonne)
            r, g, b = pixel_value
            R += mat[line][column] * r 
            G += mat[line][column] * g
            B += mat[line][column] * b
            colonne += 1
            
        ligne += 1
    #les lignes suivantes empêchent les valeurs de dépasser les valeurs autorisées.
    if R > 255 :
        R = 255
    if R < 0 :
        R = 0
    if G > 255 :
        G = 255
    if G < 0 :
        G = 0
    if B > 255 :
        B = 255
    if B < 0 :
        B = 0
    return R, G, B

def pixel(img, i, j, default=(0,0,0)) :

    '''
    les paramètres i et j représentent les indices du pixel recherché.
    '''
    if i in range(len(img)) and j in range(len(img[i])) : #le pixel est-il dans l'image ?
        return img[i][j]
    else : 
        return default

def Sobel(img, Gx, Gy) :
    new_image = copy.deepcopy(img)
    for i in range(len(img)) :
        for j in range(len(img[i])) :
            a = appliquer_convolution(img, Gx, i, j)
            b = appliquer_convolution(img, Gy, i, j)
            Ra, Ga, Ba = a
            Rb, Gb, Bb = b
            Rg = int(math.sqrt(Ra ** 2 + Rb ** 2))
            Gg = int(math.sqrt(Ga ** 2 + Gb ** 2))
            Bg = int(math.sqrt(Ba ** 2 + Bb ** 2))
            gradient = Rg, Gg, Bg
            
            #Ro = int(math.atan2(Ra, Rb))
            #Go = int(math.atan2(Ga, Gb))
            #Bo = int(math.atan2(Ba, Bb))
            #gradient = Ro, Go, Bo
            new_image[i][j] = gradient
            
    return new_image