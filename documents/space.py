import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.image=pygame.image.load('vaisseau.png')
        self.vitesse=0.5
        self.position=400
        self.sens="centre" 
    def deplacer(self):
        if self.sens=="droite"and self.position<800-64:
            
            self.position+=self.vitesse
            
            
        elif self.sens=="gauche"and self.position>0:
            self.position-=self.vitesse
            
class Balle():
    def __init__(self):
        self.tireur=tireur
        self.image=pygame.image.load("balle.png")
        self.depart=self.tireur + 16
        self.hauteur=492
        
        
        
