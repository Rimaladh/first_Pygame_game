import pygame

class SoundManager:
    def __init__(self):

        self.sounds={
            'click': pygame.mixer.Sound("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/tir.ogg"),
            'death':pygame.mixer.Sound("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/death.ogg")
                       }
        
        pygame.mixer.music.load("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/acceuil.mp3")
        pygame.mixer.music.play(-1)
        self.is_muted = False
    def play_home_music(self):
        if not self.is_muted:
        # Charger et jouer la musique de la page d'accueil
            pygame.mixer.music.load("C:/Users/rimal/OneDrive/Documents/game/PygameAssets-main/sounds/acceuil.mp3")
            pygame.mixer.music.play(-1)

    def play(self,name):
        if not self.is_muted:
            self.sounds[name].play()
        
    def stop_music(self):
        # Arrêter la musique d'ambiance
        pygame.mixer.music.stop()


    def toggle_mute(self):
        # Inverser l'état du mute
        self.is_muted = not self.is_muted

        # Ajuster le volume de tous les sons en fonction de l'état du mute
        if self.is_muted:
            # Mute tous les sons
            for sound in self.sounds.values():
                sound.set_volume(0)
            pygame.mixer.music.set_volume(0)  # Mute la musique de fond
        else:
            # Rétablir les volumes des sons à leur valeur d'origine
            for sound in self.sounds.values():
                sound.set_volume(1)
            pygame.mixer.music.set_volume(1)  # Rétablir le volume de la musique de fond

    def unmute_all(self):
        # Rétablir les volumes des sons à leur valeur d'origine
        for sound in self.sounds.values():
            sound.set_volume(1)
        pygame.mixer.music.set_volume(1)  # Rétablir le volume de la musique de fond
        self.is_muted = False
