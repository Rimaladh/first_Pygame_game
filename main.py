import pygame
import math
from game import Game


pygame.init()

# generer la fenetre
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080, 720))
# importer l image
background = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/bg.jpg')

#importer (charger) notre bannière
banner=pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/banner.png')
banner=pygame.transform.scale(banner,(500,500))
banner_rect=banner.get_rect()
banner_rect.x=math.ceil(screen.get_width()/4)#pour que l'mage soit deplacer au centre(la fonction ceil fait l'arronsissement de le reste de devision) 

#importer charger notre bouton pour lancer la partie
play_button=pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/button.png')
play_button=pygame.transform.scale(play_button,(350,100))
play_button_rect=play_button.get_rect()
play_button_rect.x=math.ceil(screen.get_width()/3)
play_button_rect.y=math.ceil(screen.get_height()/2)+50
#credits button
credits_button = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/credits.png')
credits_button = pygame.transform.scale(credits_button, (400,220))
credits_button_rect = credits_button.get_rect()
credits_button_rect.x = math.ceil(screen.get_width() / 3.2)
credits_button_rect.y = math.ceil(screen.get_height() / 2) + 95
#charger le deux boutons mut et volume
mute_button = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/mute.png')
volume_button=pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/volume.png')

# Redimensionner les boutons
button_size = (50, 50)  # Taille des boutons
volume_button = pygame.transform.scale(volume_button, button_size)
mute_button = pygame.transform.scale(mute_button, button_size)

# Positionner les boutons à droite de l'arrière-plan
volume_button_rect = volume_button.get_rect()
mute_button_rect = mute_button.get_rect()
# Positionnement des boutons de volume et de sourdine à droite
volume_button_rect.x = screen.get_width() - 100
mute_button_rect.x = screen.get_width() - 200
# Même hauteur pour les deux boutons
volume_button_rect.y = mute_button_rect.y = 20
#exit button
exit_button = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/exit.png')
exit_button = pygame.transform.scale(exit_button, (400,220))
exit_button_rect = exit_button.get_rect()
exit_button_rect.x = math.ceil(screen.get_width() / 3.2)
exit_button_rect.y = math.ceil(screen.get_height() / 2) + 200
#boutton quitter
quit_button = pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/quit.png')
quit_button = pygame.transform.scale(quit_button, (65, 35))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 2) - 35
quit_button_rect.y = math.ceil(screen.get_height() / 2) + 60

game= Game()
clock = pygame.time.Clock()
running = True
show_credits = False

# boucle tant que cette condition est vrai
while running:
    clock.tick(60)
    # appliquer larriere plan (0 0 largeur et hauteur )
    screen.blit(background, (0, -200))
    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        #declancher les instructions de la partie
        game.update(screen)
        #game.update_current_best_score()  # Update current best score during the game

    #verifier si notre jeu n'a pas commencé
    else:
        if not show_credits:
            
            #ajouter mon ecran de bienvenue
            screen.blit(play_button,play_button_rect)
            screen.blit(banner,banner_rect)
            screen.blit(volume_button, volume_button_rect)
            screen.blit(mute_button, mute_button_rect)
            screen.blit(credits_button, credits_button_rect)
            screen.blit(exit_button, exit_button_rect)
            
        if show_credits:
            # Afficher les crédits
            game.show_credits(screen)
            screen.blit(quit_button, quit_button_rect)
            
    # mettre a jour l  ecran
    pygame.display.flip()
    
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN: #ken shtaaml  event.type == pygame.K_right le deplacement n est pas fluide et je serai appui sur la touche
            game.pressed[event.key]=True #touche est active
            #detecter si la touche espace est enclanchée pour lancer notre projectiles
            if event.key == pygame.K_SPACE:#si le joueur touche à key espace
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.sound_manager.stop_music()
                    game.start()
                    #jouer le son
                    game.sound_manager.play('click')
            if event.key == pygame.K_c:
                show_credits = True
        elif event.type== pygame.KEYUP: #touche n est plus utilise
            game.pressed[event.key]=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                game.sound_manager.stop_music()
                #mettre le jeu en mode lancé
                game.start()
                #jouer le son
                game.sound_manager.play('click')
            elif credits_button_rect.collidepoint(event.pos):
                show_credits = True
            if quit_button_rect.collidepoint(event.pos):
                game.is_playing = False
                show_credits = False
                # Retourner au menu principal lorsque le bouton "Exit" est cliqué
            elif exit_button_rect.collidepoint(event.pos):
                game.sound_manager.play('click')
                running = False
                pygame.quit()
            elif volume_button_rect.collidepoint(event.pos):
                game.sound_manager.unmute_all()
                print("Volume activated")
            elif mute_button_rect.collidepoint(event.pos):
                game.sound_manager.toggle_mute()
                print("Mute activated")
            if show_credits and quit_button_rect.collidepoint(event.pos):
                show_credits = False
            
            
# After the main loop, update the best score across sessions
game.update_best_score()














