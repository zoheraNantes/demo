# =========================
# TUPLE (n-uplet)
# =========================

# Fonction qui retourne 2 valeurs (donc un tuple)
def my_function(a: int, b: int, /):
    return a * 3, b * 3   # retourne un tuple (a*3, b*3)

# -------------------------
# Retour multiple (tuple)
# -------------------------

# Décomposition du tuple dans deux variables
r1, r2 = my_function(10, 20)

# Affichage du type de la variable r1/r2
print(type(r1))  # int car on a décomposé le tuple

# Affichage des résultats
print(r1)  # 30
print(r2)  # 60


# =========================
# TUPLE EXEMPLE
# =========================

# Création d'un tuple
t = (10, 20, 30, 20, 40)

# -------------------------
# count()
# -------------------------
# Compte combien de fois une valeur apparaît
print(t.count(20))  # 2 → le 20 apparaît 2 fois

# -------------------------
# index()
# -------------------------
# Donne la position (indice) de la première occurrence
print(t.index(30))  # 2 → 30 est à la position 2


def make_sum(*integers):
    total = 0
    for integer in integers:
        total += integer
    return total

t= (1,2,3,4,5,6,7,8,9,10)
print(t[3])