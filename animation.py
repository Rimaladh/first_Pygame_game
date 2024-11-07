import pygame
#definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
    #definir les choses à faire à la création de l'entité
    def __init__(self,sprite_name,size=(200,200)):
        super().__init__()
        self.size=size
        self.image=pygame.image.load(f'C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/{sprite_name}.png')
        self.image=pygame.transform.scale(self.image,size)
        self.current_image=0;#commencer l'anim à l'image 0
        self.images=animations.get(sprite_name)#recuperer les images de sprite de clé mummy ou ...
        self.animation=False

                
    #definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation=True

        
    #definir une methode pour animer le sprite
    def animate(self,loop=False):
        #verifier si l'animation est active
        if self.animation: 
            #passe à l'image suivante
            self.current_image +=1

            #verifier si on a atteint la fin de l'animation
            if self.current_image >=len(self.images):
                #remettre l'animation au depart
                self.current_image=0

                #verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    
                    #desactiver l'annimation
                    self.animation=False
                
            #modifier l'image précedente par la suivante
            self.image=self.images[self.current_image]
            self.image=pygame.transform.scale(self.image,self.size)

        
#definir une fonction pour charger les images d'un sprite
def load_animation_image(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images=[]#creer une liste pour stocker tous les images de sprites
    #recuperer le chemin du dossier pour ce sprite
    path=f"C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1,24):
        image_path=path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png,...mummy2.png,...]
# player-> [...player.png,...player.png,...]
animations={
    'mummy':load_animation_image('mummy'),
    'player':load_animation_image('player'),
    'alien':load_animation_image('alien')
    }
