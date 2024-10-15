import pygame  # necessaire pour charger les images et les sons
import random
import math
import time
class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 1
        self.score = 0
        self.coeur=3   
    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + 1
    def perdrecoeur(self):
        self.coeur-=1

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
    
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:
            self.etat = "chargee"
                
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
    def toucher2(self, bossvaisseau):
        if (math.fabs(self.hauteur - bossvaisseau.hauteur) < 200) and (math.fabs(self.depart - (bossvaisseau.x+55)) < 125):
            self.etat = "chargee"
            return True
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.2
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.4
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.2
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.4
class Boss:
    def __init__(self):
        self.image=pygame.image.load("finalboss copy.png")
        self.hauteur = -50
        self.x = 100
        self.vitesse = round(random.uniform(0.1, 4.0),1)
        self.sens = "droite"
        self.vie=10
        self.tirs=[]#aider par chatgpt
    def avancer(self):
        if self.sens=="droite" and self.x < 800-373+105:
            self.x = self.x + self.vitesse
            self.vitesse = round(random.uniform(0.1, 4.0),1)
            """forum"""
            if self.x>=800-373-1+105:
                self.sens="gauche"
        elif self.sens=="gauche" and self.x>0-373+105:
            self.x = self.x - self.vitesse
            self.vitesse = round(random.uniform(0.1, 4.0),1)
            if self.x<=0-153+1+105:
                self.sens="droite"
    def perdrevie(self):
        
        self.vie-=1
    def tirer(self):
        """aider par chatgpt"""
        # Crée une nouvelle balle et l'ajoute à la liste
        balle_boss = BalleBoss(self)
        self.tirs.append(balle_boss)
class BalleBoss:
    def __init__(self,tireur):
        self.tireur = tireur
        self.depart = tireur.x + round(random.uniform(20.0, 250.0),1)
        self.hauteur = 40
        self.image = pygame.image.load("missile.png")
        self.vitesse = round(random.uniform(0.1, 3.0),1)
        self.etat = "chargee"
    def bouger(self):
        if self.etat == "chargee":
            self.hauteur += self.vitesse  # Déplacement vers le bas
            if self.hauteur > 600:  # Si la balle sort de l'écran
                self.etat = "chargee"  # Reset l'état
        elif self.etat == "tiree":
            self.hauteur += self.vitesse

    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - 500) < 40) and (math.fabs(self.depart - vaisseau.position) < 40):
            return True
        return False

def getSurface(t, clip, srf=None):
    frame = clip.get_frame(t=t)  # t is the time in seconds
    
    if srf is None:
        # Transpose the array and create the Pygame surface
        return pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    else:
        pygame.surfarray.blit_array(srf, frame.swapaxes(0, 1))
        return srf