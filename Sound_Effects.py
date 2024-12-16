import pygame
### Αυτός είναι ο φάκελος που θα αρχικοποιήσουμε τα ηχητικα εφε για το παιχνίδι μας###

pygame.mixer.init()


Backround_Sound = pygame.mixer.Sound('Sounds/entry-of-the-gladiators-op.ogg')
Impact_Sound = pygame.mixer.Sound('Sounds/cajun-kick-hit-15.ogg')
Point_Sound = pygame.mixer.Sound('Sounds/hitting-a-tin.ogg')
Win_Sound = pygame.mixer.Sound('Sounds/jingle_win_00.ogg')

def Check_Sound():
    return pygame.mixer.get_busy()