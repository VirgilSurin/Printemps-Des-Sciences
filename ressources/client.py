def normaliser(mat):
    """
    Divise une matrice par la somme de ses termes.
    Le but est d'avoir un somme des valeurs égale à 1 et par conséquent,
    les valeurs de chaque pixel reste entre 0 et 255.
    """
    total = 0
    for line in range(len(mat)):
        for column in range(len(mat[0])):
            total += mat[line][column]
    
    for line in range(len(mat)):
        for column in range(len(mat[0])):
            mat[line][column] /= total
    return mat

def filtre_de_Gauss():
    """
    Pas encore implémenté
    Toujours pas implémenté
    """
    mat = []
    return mat
def multiMatrix(matList) :
    """
    Applique une matrice différente par couleur d'un pixel 
    en choississant parmis une liste de matrice
    """
    
"""
Idées:

- Appliquer une matrice différente par couleur d'un pixel

- Appliquer une matrice 1x3 régissant les valeurs d'un pixel
EX : Pixel(50, 50, 50)
     Matrice(1, 2, 1/2)
     => Pixel(50, 100, 25)
"""
