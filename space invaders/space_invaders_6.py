import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application
import random
from moviepy.editor import VideoFileClip
import numpy as np
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('Earth.png')
menu = pygame.image.load('menu.png')
fin = pygame.image.load('gameover.png')
# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)

tir.etat = "chargee"
# creation des ennemis
Boss=space.Boss()
bosstir=space.BalleBoss(Boss)
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
bossvaisseau=space.Boss()
police = pygame.font.Font(None, 36)
def score():
    texte_score = police.render(f'Score: {player.score}', True, (255, 255, 255))
    screen.blit(texte_score, (10, 10))
def bossvie():
    texte_score = police.render(f'SuperPaul: {Boss.vie}', True, (255, 3, 0))
    screen.blit(texte_score, (200, 10))
def bossvie2():
    texte_score = police.render(f'SuperPaul: {Boss.viephase2}', True, (255, 3, 0))
    screen.blit(texte_score, (200, 10))
def persocoeur():
    texte_score = police.render(f'coeur :x{player.coeur}', True, (255, 255, 255))
    screen.blit(texte_score, (10, 550))
police2 = pygame.font.Font(None, 50)
def gameover():
    texte_score = police2.render('SUPER PAUL VOUS A TERRASSE', True, (100, 0, 0))
    screen.blit(texte_score, (120, 300))
def gamelose():
    texte_score = police2.render('SUPER PAUL S EST ECRASE SUR TERRE', True, (100, 0, 0))
    screen.blit(texte_score, (120, 300))
def win():
    texte_score = police.render('VOUS AVEZ VAINCU SUPER PAUL', True, (255, 255, 255))
    screen.blit(texte_score, (180, 500))
def obj():
    texte_score = police.render('DETRUISEZ SUPERPAUL', True, (0, 200, 100))
    screen.blit(texte_score, (400, 10))

pause=False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 74)
text_pause = font.render("PAUSE", True, WHITE)
resume_text = font.render("Reprendre", True, WHITE)
quit_text = font.render("Quitter", True, WHITE)
def draw_pause_menu():
    screen.fill(BLACK)
    screen.blit(text_pause, (300, 150))
    screen.blit(resume_text, (300, 300))
    screen.blit(quit_text, (300, 400))
video_playing = False
### BOUCLE DE JEU  ###
def display_text(text, font, color, x, y):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

"""def menu_principal():
    menu_running=True
    font = pygame.font.Font(None, 74)
    while menu_running==True:
        screen.fill(BLACK)
        display_text("Space Invaders", font, WHITE, 220, 150)
        display_text("Jouer", police2, WHITE, 350, 300)
        display_text("Quitter", police2, WHITE, 350, 400)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 450 and 300 <= y <= 350:  # Coordonnées pour "Jouer"
                    return 
                if 350 <= x <= 450 and 400 <= y <= 450:  # Coordonnées pour "Quitter"
                    pygame.quit()
                    sys.exit()"""

niveau=1
running = True # variable pour laisser la fenêtre ouverte
menu_active=True
clock = pygame.time.Clock()
while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    

    if menu_active:
        # Affichage du menu principal
        screen.blit(menu,(0,0))
        screen.blit(Boss.image,[500,50 ])
        display_text("Paul Invaders", pygame.font.Font(None, 74), WHITE, 220, 150)
        display_text("Jouer", police2, WHITE, 350, 300)
        display_text("Quitter", police2, WHITE, 350, 400)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 450 and 300 <= y <= 350:  # Coordonnées pour "Jouer"
                    menu_active = False  # Passe du menu au jeu
                elif 350 <= x <= 450 and 400 <= y <= 450:  # Coordonnées pour "Quitter"
                    running = False
                    sys.exit()
    
    else:
        screen.blit(fond,(0,0))
        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement
           
           # gestion du clavier
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer()
                    tir.etat = "tiree"
                if event.key == pygame.K_p:
                    pause = not pause
        
        if pause:
                draw_pause_menu()
        else:
              
        
            ### Actualisation de la scene ###
            # Gestions des collisions
            player.deplacer()
            screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
                # la balle
            tir.bouger()
            screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
            persocoeur()
            if niveau==1:
                for ennemi in listeEnnemis:
                    if tir.toucher(ennemi):
                        ennemi.disparaitre()
                        player.marquer()
                print(f"Score = {player.score} points")
                # placement des objets
                # le joueur
                # les ennemis
                for ennemi in listeEnnemis:
                    ennemi.avancer()
                    screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
                score()
                if ennemi.hauteur>=550 :
                    ennemi.hauteur=10
                    player.perdrecoeur()
                if player.score>=5:
                    niveau=2
            
            elif niveau ==2:
                
                bossvie()
                for balle in Boss.tirs:
                    balle.bouger()
                    screen.blit(balle.image, [balle.depart, balle.hauteur])
                   
                    if balle.toucher(player):
                        balle.hauteur=40
                        player.perdrecoeur()
                screen.blit(Boss.image,[Boss.x,Boss.hauteur ])
                bosstir.bouger()
                Boss.avancer()
                if tir.toucher2(Boss) and Boss.vie>=1:
                    Boss.perdrevie()
                elif Boss.vie<1:
                    niveau=3
                elif player.coeur <= 0 and not video_playing:
                    running=False
                    running=False
                if random.random() < 0.018:  # Ajustez la probabilité de tir
                    Boss.tirer()
                    """chatgpt/google"""
            elif niveau ==3:
                
                if tir.toucher2(Boss) and Boss.viephase2>=1:
                    Boss.perdrevie2()
                screen.blit(Boss.image,[Boss.x,Boss.hauteur ])
                Boss.avancer2()
                obj()
                bossvie2()
                if Boss.viephase2<=0:
                    screen.blit(fin,(0,0))
                    win()
                    print("vous avez gagnez")
                    running=False
            # Bouger et dessiner les balles tirées par le boss
                
            pygame.display.update() # pour ajouter tout changement à l'écran

        if player.coeur<=0:
        # Chargement de la vidéo
            clip = VideoFileClip('nuke.mp4')
            frame_count = clip.fps * clip.duration +100 # Nombre total de frames

            surface = space.getSurface(0, clip)

            screen = pygame.display.set_mode(surface.get_size(), 0, 32)

            # Run the Pygame loop to keep the window open
            running = True
            t = 0
            while running:
                # Draw the surface onto the window
                
                screen.blit(space.getSurface(t, clip, surface), (0, 0))
                gameover()
                pygame.display.flip()
                
                t += 1/60 # use actual fps here
                pygame.time.delay(10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
        if Boss.hauteur>=300:
        # Chargement de la vidéo
            clip = VideoFileClip('crash_1.mp4')
            frame_count = clip.fps * clip.duration +100 # Nombre total de frames

            surface = space.getSurface(0, clip)

            screen = pygame.display.set_mode(surface.get_size(), 0, 32)

            # Run the Pygame loop to keep the window open
            running = True
            t = 0
            while running:
                # Draw the surface onto the window
                
                screen.blit(space.getSurface(t, clip, surface), (0, 0))
                gamelose()
                pygame.display.flip()
                
                t += 1/60 # use actual fps here
                pygame.time.delay(10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        sys.exit()
               
                
            # Quit Pygame
            pygame.quit()
