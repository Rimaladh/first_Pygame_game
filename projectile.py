import pygame


#definir la classe qui va gérer le projectile de notre  joueur
class Projectile(pygame.sprite.Sprite):


    #definit le constructeur de cette classe  hérite de la classe pygame.sprite.Sprite.
    def __init__(self,player):
        super().__init__()
        self.velocity=7
        self.player=player#pour accéder au attribut de player
        self.image=pygame.image.load('C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/projectile.png')
        #redimensionner l'image de projectile en utilisant pygame.transform.scale(image,(largeur,hauteur))
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        #le projectiles ont le meme cordonnees que le player
        self.rect.x=player.rect.x+120
        self.rect.y=player.rect.y+80
        self.origin_image=self.image#l'origin_image garde le meme origine de l'image iniale càd sans rotation
        self.angle=0#la angle de rotation qui est inialement 0
    def rotate(self):
        #tourner le projectile
        self.angle +=8
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)#redimensionner l'image apres la rotation avec pygame.transform.rotozoom(surface ,angle,scale
        self.rect=self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)#self est l'objet courant
        
    #la fonction qui fait le mouvement de projectiles sur l'axe de x
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        #verifier si le prijectile entre en collision avec un monster
        #tous les monsters qui entre en collision avec le ball de feu sont subi à une diminuation dans le nombre de vie (health)
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #supprimer le projectile en appelant la methode remove()
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)
        #verifier si notre projectile n'est pas présent sur l'ecran
        if self.rect.x>1080:
            #supprimer le projectile (en dehors de l'ecran)
            self.remove()
            print("projetile supprimé!")
            
    
    
