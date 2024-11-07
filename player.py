import pygame
from projectile import Projectile
import animation
class Player(animation.AnimateSprite):
 # Définit le constructeur de la classe Player. Le constructeur est appelé lors de la création d'une instance de Player.
    def __init__(self,game): #appeler au chargement du classe Player
                             # on utilise game dans la fonction init pour acceder au attribut et le methode de game
#Appelle le constructeur de la classe mère (pygame.sprite.Sprite). Cela est nécessaire pour initialiser correctement la classe Player en tant que sous-classe de Sprite.
        super().__init__('player') #'player' passé au constructeur de la classe mère AnimateSprite est utilisé pour identifier le joueur dans le contexte de l'animation. Il peut être utilisé pour charger différentes animations spécifiques au joueur à partir d'un fichie
        self.game=game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5 #vitesse
        self.all_projectiles=pygame.sprite.Group()
        self.rect = self.image.get_rect() #recupere les 4 coins de l image
        self.rect.x=400
        self.rect.y=500
    def damage(self,amount):
        if self.health - amount >amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de points de vie
            self.game.game_over()
    # fonction qui gere l'animation de player   
    def update_animation(self):
        self.animate()
    def update_health_bar(self,surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface,(60,63,60), [self.rect.x+50,self.rect.y+20,self.max_health,7])
        #dessiner notre barre de vie maximum
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+50,self.rect.y+20,self.health,7])
    
    #lancer leboul de feu(projectiles)
    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile et l'ajouter au groupe all_projectiles 
        self.all_projectiles.add(Projectile(self))#on passe le player comme paramétre lors de la construction d'une nouvelle instance de projectile pour que le projectiles accéde au dimension de player
        # demarrer l'animation de lancer
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')
    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not  self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity#le joueur avancer avance

    def move_left(self):
        self.rect.x -= self.velocity



