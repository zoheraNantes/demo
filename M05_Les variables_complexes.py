# =========================
# COPIE SIMPLE vs COPIE PROFONDE
# =========================

# copy = copie superficielle (shallow copy)
# deepcopy = copie complète (deep copy)

from copy import copy, deepcopy

# =========================
# COPIE SIMPLE
# =========================

l = [1, 2, 3]

# On crée une copie de la liste
l4 = copy(l)

# On modifie la liste originale
l.append('autre élément pour la liste l')

# Affichage
print(l)   # liste modifiée
print(l4)  # copie non modifiée (car valeurs simples)


# =========================
# COPIE PROFONDE
# =========================

# liste contenant des sous-listes
l = [['a', 'b', 'c'], ['z']]

# deepcopy = copie complète (même les sous-listes)
l2 = deepcopy(l)

# On modifie une sous-liste dans la copie
l2[0].append('d')

# Affichage
print(l2)  # la copie est modifiée
print(l)   # l originale reste intacte


# Chaîne de caractères
s = 'test'

# Centre la chaîne sur une largeur de 30 caractères
# Des espaces sont ajoutés à gauche et à droite
print(s.center(30))

# Aligne la chaîne à droite sur une largeur de 30 caractères
# Des espaces sont ajoutés à gauche
print(s.rjust(30))

# Complète la chaîne à gauche avec des zéros
# jusqu'à obtenir une longueur totale de 30 caractères
print(s.zfill(30))


# Ajoute des zéros à gauche jusqu'à obtenir une longueur de 4 caractères
print('42'.zfill(4))

# Supprime au début et à la fin les caractères :
# espace, tiret (*) et astérisque (*)
print(' -* test -* '.strip(' -*'))