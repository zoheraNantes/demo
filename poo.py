class Chat:
    """Description d'un Chat"""

    def __init__(self, nom):
        self._nom = nom

    def __str__(self):
        return "Le chat " + self._nom


ella = Chat("Ella")

print(ella.__doc__)
print(ella)
print(ella.__str__())