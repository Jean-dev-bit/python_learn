class Rectangle:
    def __init__(self,largeur,longueur):
        self.largeur = largeur
        self.longueur = longueur
    def Calculer_aire(self):
       aire = self.largeur * self.longueur   
       print("Aire du  rectangle : ", aire)

rect = Rectangle(3,5)
rect.Calculer_aire()
    