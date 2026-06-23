# =========================
# DICTIONNAIRE
# =========================

# Création d'un dictionnaire à partir d'une liste de tuples
d = dict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
])

# Récupère la valeur associée à la clé "d"
# Comme la clé n'existe pas, get() renvoie None
print(d.get("d"))

# =========================
# Récupérer les clés
# =========================

# Parcourt toutes les clés du dictionnaire
for k in d.keys():
    print(k)

# =========================
# Récupérer les valeurs
# =========================

# Parcourt toutes les valeurs du dictionnaire
for v in d.values():
    print(v)

# =========================
# Récupérer les clés et les valeurs
# =========================

# Parcourt les couples (clé, valeur)
for k, v in d.items():
    print(k, ':', v)

# =========================
# Deuxième dictionnaire
# =========================

d2 = {
    'truc': 36,
    'machin': 72,
    'bidule': 42,
}

# Module permettant d'utiliser des fonctions utilitaires
import operator

# =========================
# Trier le dictionnaire par clé
# =========================

# d2.items() renvoie les couples (clé, valeur)
# itemgetter(0) indique de trier selon l'élément d'indice 0 (la clé)
for k, v in sorted(d2.items(), key=operator.itemgetter(0)):
    print(k, ':', v)


# =========================
# CONFIGURATION
# =========================

def read_configuration(filename):
    return {
        "host": "localhost",
        "port": 5432
    }


def f(**kwargs):
    conf = read_configuration("config.json")  # lecture config par défaut
    conf.update(kwargs)  # écrase / complète avec kwargs
    print(conf)


# appel de la fonction (EN DEHORS de la fonction)
f(host="127.0.0.1", port=5432, user='root', pwd='')


# =========================
# LISTE
# =========================

l = [1, 2, 3, 4, 5]

# slicing avec pas de 2
print(l[::2])  # prend 1 élément sur 2 → [1, 3, 5]


# =========================
# STRING
# =========================

s = "je suis une string"

# découpe avec pas de 2 entre index 4 et -2
print(s[4:-2:2])

# les 5 premiers caractères
print(s[:5])