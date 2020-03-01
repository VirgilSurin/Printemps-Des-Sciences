import umage
import sys
from docopt import docopt
import copy
import math
import random

def normaliser(mat):
    """
    Divise une matrice par la somme de ses termes.
    Le but est d'avoir une somme des valeurs égale à 1 et par conséquent,
    les valeurs de chaque pixel reste entre 0 et 255.

    Fonctionne désormais aussi pour les listes.
    """
    total = 0
    for line in range(len(mat)):
        if type(mat[0]) != list:
            total += mat[line]
        else:
            for column in range(len(mat[0])):
                total += mat[line][column]

    for line in range(len(mat)):
        if type(mat[0]) != list:
            mat[line] /= total
        else:
            for column in range(len(mat[0])):
                mat[line][column] /= total
    return mat

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

def modifier_couleurs(mat_img, listeR, listeV, listeB):
    """
    Les paramètres "listeR, listeV, listeB" sont des listes de 3 float.
    Les listes doivent être passées par la fonction normaliser auparavant.
    """
    new_img = copy.deepcopy(mat_img)
    for i in range(len(mat_img)) :
        for j in range(len(mat_img[i])) :
            new_img[i][j] = (int(mat_img[i][j][0] * listeR[0] + mat_img[i][j][1] * listeR[1] + mat_img[i][j][2] * listeR[2]),
                             int(mat_img[i][j][0] * listeV[0] + mat_img[i][j][1] * listeV[1] + mat_img[i][j][2] * listeV[2]),
                             int(mat_img[i][j][0] * listeB[0] + mat_img[i][j][1] * listeB[1] + mat_img[i][j][2] * listeB[2]))
    return new_img

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

def randomListGenerator() :
    """
    create a random list of 3 items, ready to be used for modifier_couleurs
    """
    newlist = []
    for i in range(3) :
        randomInt = random.randint(1,10)
        newlist.append(randomInt)
    normaliser(newlist)
    return newlist

def randomMatrixGenerator(basic = True) :
    """
    Génère matrice pour appliquer avec multiMatrix
    """
    if basic:
        n = 3
    else:
        n = random.randint(1, 10) * 2 + 1
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append([])
    for i in range(n):
        for j in range(n):
            mat[i][j] = random.randint(1, 100)
    normaliser(mat)
    return mat

if __name__ == "__main__" :

    for i in range(5) :
        convo1 = [[-2,0,0],[0,1,0],[0,0,2]]
        convo2 = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
        convo3 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
        sobel_1A = [[-1,0,1],[-2,0,2],[-1,0,1]]
        sobel_1B = [[-1,-2,-1],[0,0,0],[1,2,1]]
        randomSobel_A = randomMatrixGenerator()
        randomSobel_B = randomMatrixGenerator()
        #t1 = randomListGenerator()
        #t2 = randomListGenerator()
        #t3 = randomListGenerator()
        path = "C:/Users/Bernadette/Desktop/Virgil/Printemps-Des-Sciences/ressources/"
        name = "test"+str(i)
        image = umage.load(path + "shrek.png")
        new = Sobel(image, randomSobel_A, randomSobel_B)
        umage.save(new, name)
        #print(name + " :  " + str(t1) + "  "+ str(t2) + "  "+ str(t3))
        print(name + " :  " + str(randomSobel_A) + "  " + str(randomSobel_B))
        print("--------------------------------------")

        """
        modifier_couleurs :
        style sépia : [0.5333333333333333, 0.22777777777777777, 0.2388888888888889]  [0.06779661016949153, 0.6779661016949152, 0.2542372881355932]  [0.3380281690140845, 0.29577464788732394, 0.36619718309859156]
        pink panther : [0.20689655172413793, 0.5655172413793104, 0.22758620689655173]  [0.0410958904109589, 0.0821917808219178, 0.8767123287671232]  [0.5260115606936416, 0.1676300578034682, 0.3063583815028902]
        I'm blue : [0.16363636363636364, 0.32727272727272727, 0.509090909090909]  [0.3888888888888889, 0.36363636363636365, 0.2474747474747475]  [0.7936507936507936, 0.16666666666666666, 0.03968253968253968]
        very green : [0.055900621118012424, 0.6086956521739131, 0.33540372670807456]  [0.4305555555555556, 0.4791666666666667, 0.09027777777777778]  [0.03968253968253968, 0.30952380952380953, 0.6507936507936508]
        strange peps' : [0.5, 0.16666666666666666, 0.3333333333333333]  [0.47368421052631576, 0.3157894736842105, 0.21052631578947367]  [0.058823529411764705, 0.35294117647058826, 0.5882352941176471]
        turquoise : [0.11764705882352941, 0.35294117647058826, 0.5294117647058824]  [0.42857142857142855, 0.5, 0.07142857142857142]  [0.3125, 0.625, 0.0625]
        -----------------------------------------------------------------------------------

        sobel :

        """
    

