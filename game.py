import pygame
from player import Player
from monstre import Monster
from monstre import Mummy
from monstre import Alien
from comet_event import CometFallEvent
from sounds import SoundManager
import math

#classe qui va represente notre jeu
class Game():
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing=False
        #creer un group de joueur vierge
        self.all_players=pygame.sprite.Group()
        #generer notre jeueur
        self.player = Player(self)#lorsque il ya une creation d'un joueur, le classe game donne l'acces au classe joueur d'utiliser leur attribut et leur methode en ajoutant self
        self.all_players.add(self.player)
        #generer l'evenement
        self.comet_event=CometFallEvent(self)
        #creer un group de monstre qui est vierge(vide)
        self.all_monsters=pygame.sprite.Group()
        #gerer le son
        self.sound_manager=SoundManager()
        #contenir tous les touches qui seront acitfs pour le joueur
        #mettre le score à 0
        self.font=pygame.font.Font("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/my_custom_font.ttf",25)
        self.score=0
         # Load the best score from a file
        self.load_best_score()
        self.pressed = {} #contenir tous cle touche qui sont actuelement actifs par le joueur
        #Initialise un dictionnaire vide appelé pressed. Ce dictionnaire sera utilisé pour contenir les touches du clavier qui sont actuellement enfoncées par le joueur.


 #si le joueur clique sur le bouton play la fonction permet de charger le monsters
    def start(self):
        self.is_playing=True
        self.spawn_monster(Mummy)#generer automatiquement un exemplaire de monstre lors de demarrage de jeu
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

   
    def show_credits(self, screen):
            # Ouvrir le fichier en mode lecture
        with open("best_score.txt", "r") as file:
                # Lire le contenu du fichier
            valeur = file.read()
            # Création de la fenêtre pour afficher le meilleur score
        best_score_window = pygame.Surface((300, 250))
        best_score_window.fill((0, 0, 0))
            # Affichage du meilleur score
        best_score_text = self.font.render(f"Best Score: {valeur}", True,(255, 255, 255))
        best_score_rect = best_score_text.get_rect(center=(150, 100))
        best_score_window.blit(best_score_text, best_score_rect)
            # Affichage de la fenêtre sur l'écran principal
        screen.blit(best_score_window, (screen.get_width() // 2 - 150, screen.get_height() // 2 - 100))
        pygame.display.flip()
    def add_score(self,points=10):
        self.score += points
        self.update_best_score()
    def save_best_score(self):
        with open("best_score.txt", "w") as file:
            file.write(str(self.best_score))

    def update_best_score(self):
        if self.score > self.best_score:
            self.best_score = self.score
            self.save_best_score()


    def game_over(self):

        # remettre le jeu à neuf, retirer les monstres,remettre le joueur à 100 de vie,jeu en attente
        self.all_monsters=pygame.sprite.Group()
        self.comet_event.all_comets=pygame.sprite.Group()
        self.player.health = self.player.max_health#remettre le nombre de health de joueur au maximum
        self.comet_event.reset_percent()
        self.is_playing=False
        self.score=0
        #jouer le son
        
        self.sound_manager.play('game_over')
        self.sound_manager.stop_music()
        self.sound_manager.play_home_music()
    

    def update(self,screen):
        #afficher le score surl'ecran
        score_text=self.font.render(f"Score : {self.score} ",1,(0,0,0))
        screen.blit(score_text,(20,20))
        #appliquer l'image de mon joueur
        screen.blit(self.player.image,self.player.rect)
        #actualier la barre de vie de joueur
        self.player.update_health_bar(screen)

        #actualiser l'animation du joueur
        self.player.update_animation()
        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)
        #recuperer les projectiles du joueur:
        for projectile in self.player.all_projectiles:
            projectile.move()
        #appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)
        #recuperer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        #appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        #recuperer les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()
        # appliquer l'ensemble des images de mon groupe de commettes
        self.comet_event.all_comets.draw(screen)
    
    

        #verifier si le joueuer souhaite aller a gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width<screen.get_width(): #game.player.rect.width:largeur image de joueur
            self.player.move_right()
        elif  self.pressed.get(pygame.K_LEFT) and self.player.rect.x>0:
            self.player.move_left()


    def load_best_score(self):
        try:
            with open("best_score.txt", "r") as file:
                content = file.read()
                if content.strip():  # Check if content is not empty
                    self.best_score = int(content)
                else:
                    self.best_score = 0  # Set default value if file is empty
        except FileNotFoundError:
            self.best_score = 0  # Set default value if file doesn't exist
        except ValueError:
            self.best_score = 0  # Set default value if file contains invalid data



        

    #ajouter le principe de collision
    def check_collision(self,sprite,group):
        #comparer est ce que le sprite entre en collision avec un group de sprite
        # en utilisant pygame.sprite.spritecollide(sprite,group,dokill(est ce que il tuer l'entité courante lorsque il entre en collision),type de collision)
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)#on metfalse dans le dokill car le sprite lorsque il entre en collision avec le monstre il mort automatiquement
        

    def spawn_monster(self,monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
