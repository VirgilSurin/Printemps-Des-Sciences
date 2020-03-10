import copy
import umage
import math
import random
import docopt
from science import *

#Convolution

flou_de_Gauss = normaliser([[1, 4, 6, 4, 1],
                            [4, 16, 24, 16, 4],
                            [6, 24, 36, 24, 6],
                            [4, 16, 24, 16, 4],
                            [1, 4, 6, 4, 1]])
convo1 = [[-2,0,0],[0,1,0],[0,0,2]]
convo2 = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
convo3 = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
sobel_1A = [[-1,0,1],[-2,0,2],[-1,0,1]]
sobel_1B = [[-1,-2,-1],[0,0,0],[1,2,1]]

#Couleurs

sepia = [[0.5333333333333333, 0.22777777777777777, 0.2388888888888889], [0.06779661016949153, 0.6779661016949152, 0.2542372881355932], [0.3380281690140845, 0.29577464788732394, 0.36619718309859156]]
pink_panther = [[0.20689655172413793, 0.5655172413793104, 0.22758620689655173], [0.0410958904109589, 0.0821917808219178, 0.8767123287671232], [0.5260115606936416, 0.1676300578034682, 0.3063583815028902]]
blue = [[0.16363636363636364, 0.32727272727272727, 0.509090909090909], [0.3888888888888889, 0.36363636363636365, 0.2474747474747475], [0.7936507936507936, 0.16666666666666666, 0.03968253968253968]]
very_green = [[0.055900621118012424, 0.6086956521739131, 0.33540372670807456], [0.4305555555555556, 0.4791666666666667, 0.09027777777777778], [0.03968253968253968, 0.30952380952380953, 0.6507936507936508]]
strange_peps = [[0.5, 0.16666666666666666, 0.3333333333333333], [0.47368421052631576, 0.3157894736842105, 0.21052631578947367], [0.058823529411764705, 0.35294117647058826, 0.5882352941176471]]
turquoise = [[0.11764705882352941, 0.35294117647058826, 0.5294117647058824], [0.42857142857142855, 0.5, 0.07142857142857142], [0.3125, 0.625, 0.0625]]
joconde = [[0.2, 0.1, 0.7], [0.9, 0.05, 0.05], [0.3, 0.4, 0.3]]

def client(args):
    if args[1] == "SHREK":
        mat_img = umage.load("shrek.png")
        for i in range(1, 11):
            umage.save(modifier_couleurs(mat_img, randomListGenerator(), randomListGenerator(), randomListGenerator()), "new" + str(i))
            print("Image \"new" + str(i) + ".jpg\" enregistrée.")
        print("Traitement des images terminé.")
        return

    file = args[-1]
    mat_img = umage.load(file)
    if args[1] == "-c":
        if args[2] == "r":
            n = 10 #Nombre de photos à créer
            if args[3] != file:
                n = int(args[3])
            for i in range(1, n + 1):
                umage.save(convolution(mat_img, randomMatrixGenerator(basic = False)), "new" + str(i))
                print("Image \"new" + str(i) + ".jpg\" enregistrée.")
            print("Traitement des images terminé.")
            return
        else:
            conv = [convo1, convo2, convo3]
            for i in range(1, len(conv)+1):
                umage.save(convolution(mat_img, conv[i-1]), "new" + str(i))
                print("Image \"new" + str(i) + ".jpg\" enregistrée.")
            print("Traitement des images terminé.")
            return
    if args[1] == "-k":
        if args[2] == "r":
            n = 10 #Nombre de photos à créer
            if args[3] != file:
                n = int(args[3])
            for i in range(1, n + 1):
                umage.save(modifier_couleurs(mat_img, randomListGenerator(), randomListGenerator(), randomListGenerator()), "new" + str(i))
                print("Image \"new" + str(i) + ".jpg\" enregistrée.")
            print("Traitement des images terminé.")
            return
        else:
            color = [sepia, pink_panther, blue, very_green, strange_peps, turquoise, joconde]
            for i in range(1, len(color)+1):
                umage.save(modifier_couleurs(mat_img, color[i-1][0], color[i-1][1], color[i-1][2]), "new" + str(i))
                print("Image \"new" + str(i) + ".jpg\" enregistrée.")
            print("Traitement des images terminé.")
            return
    if args[1] == "-s":
        umage.save(Sobel(mat_img, sobel_1A, sobel_1B), "new1")
        print("Image \"new1.jpg\" enregistrée.")
        print("Traitement des images terminé.")
        return