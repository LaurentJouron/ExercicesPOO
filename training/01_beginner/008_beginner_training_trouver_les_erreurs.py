"""
Trouver les erreurs
	Dans cet exercice, vous devez modifier le code de base pour qu'il ne
	retourne plus d'erreur et qu'il affiche les coordonnées x, y et z de
	l'instance sphere avec des valeurs respectivement de 9, 2 et 5
	(pour x, y et z).
	Votre script doit donc afficher :
	9
	2
	5
"""


class Geometry:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z


sphere = Geometry(x=9, y=2, z=5)
print(sphere.x)
print(sphere.y)
print(sphere.z)
