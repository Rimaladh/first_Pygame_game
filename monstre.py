import pygame
import random
import animation
#créer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):
    
    def __init__(self,game,name,size,offset=0):#c'est un constructeur qui contient l'attribut self qui contient les caracteristiques de classe monster

        super().__init__(name,size)#appel la super classe Animatesprite pour le charger
        self.game=game
        self.health=100 #le nombre de vie actuelle de monster
        self.max_health=100 #le nombre de vie maximum de monstre
        self.attack=0.3 #le degat infiguéé a ce joueur(5 monsters)
        self.rect=self.image.get_rect()#pour la positionnement (on peut le positionner sur l'axe x ou sur l'axe y)
        self.rect.x=1000 + random.randint(0,300)#pour avoir l'image de monstre  au droit(1000)
        self.rect.y=540-offset#le monstre avoir presque le meme  positionnement de le player sur l'axe de y
        self.loot_amount=10
        self.start_animation()

    def set_speed(self,speed):
        self.default_speed=speed
        self.velocity=random.randint(1,3)# elle definir le vitesse de deplacement de monstre

    def set_loot_amount(self,amount):
        self.loot_amount = amount

    #fonction pour diminuer le health
    def damage(self,amount):
        #infliger les degats
        self.health -= amount#amount dans notre cas:9adach min nombre de vie bach yon9sou lil monster
        #verifier si son nouveau nombre de points de vie est < à 0
        if self.health <= 0:
            self.game.sound_manager.play('death')
            #reapparaitre comme un nouveau monstre
            self.rect.x=1000 + random.randint(0,300)
            self.velocity=random.randint(1,self.default_speed)
            self.health = self.max_health#réinitialiser le nombre de vie au maximum
            #ajouter le nombre de points
            self.game.add_score(self.loot_amount)
            #si la barre d'evenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)
                #appel de la méthode pour essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    #creation d'une methode qui gere l'animation de monster
    def update_animation(self):
        self.animate(loop=True)
    def update_health_bar(self,surface):
        #definir une couleur pour notre jauge de vie(vert claire)
        bar_color=(111,210,46)#un variable pour stocké le couleur
        #definir une couleur pour l'arriére plan de la jauge(gris foncé)
        back_bar_color=(60,63,60)
        #definir la position de notre jauge de vie ainsi que sa largeuret son épaisseur
        bar_position=[self.rect.x+10,self.rect.y-20,self.health,5]#[x,y,width,hite]
        #definir la position de l'arriére plan de notre de jauge de vie
        back_bar_position=[self.rect.x+10,self.rect.y-20,self.max_health,5]#[x,y,width,hite]
        #dessiner notre barre de vie
        pygame.draw.rect(surface,back_bar_color, back_bar_position)
         #dessiner notre barre de vie maximum
        pygame.draw.rect(surface,bar_color,bar_position)
        
        
    
    def forward(self):
        #le deplacement ne se fait que si il n'y a pas de collision avec un group de  joueur
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity#pour le monstre avancer ver le joueur
        #si le monster est en collision avec le joueur
        else:
            #infliger des degats(au joueur)
            self.game.player.damage(self.attack)


#definir une classe pour le momie
class Mummy(Monster):

    def __init__(self,game):
        super().__init__(game,"mummy",(130,130))
        self.set_speed(3)
        self.set_loot_amount(20)
#definir une classe pour l'alien
class Alien(Monster):
    def __init__(self,game):
        super().__init__(game,"alien",(300,300),130)
        self.health=250
        self.max_health=250
        self.attack=0.8
        self.set_speed(1)
        self.set_loot_amount(80)

