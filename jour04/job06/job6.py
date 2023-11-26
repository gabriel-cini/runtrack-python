liste = [1, 5, 7, 12, 16]
temporaire = liste[0]
liste[0] = liste[-1]
liste[-1] = temporaire
print(liste)



