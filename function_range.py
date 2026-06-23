# =========================
# RANGE
# =========================

# range() permet de générer une suite de nombres entiers
# sans créer directement une liste en mémoire
# Syntaxes :
# range(stop) → de 0 à stop-1
# range(start, stop) → de start à stop-1
# range(start, stop, step) → avec un pas (step)
r = range(10)

print(r)

for i in r:
    print(i)

# =========================

r = range(5, 15)
print(r)

for i in r:
    print(i)

# =========================

r = range(5, 15, 2)
print(r)

for i in r:
    print(i)

# =========================
# Conversion en liste
# =========================

r = range(5, 15)
print(r)

print(list(r))

for i in r:
    print(i)