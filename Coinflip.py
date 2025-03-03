import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coinflip Game")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Police
font = pygame.font.Font(None, 50)

# Texte d'intro
title_text = font.render("Coinflip Game", True, BLACK)
title_rect = title_text.get_rect(center=(WIDTH // 2, 50))

# Résultat
result_text = None

def flip_coin():
    return random.choice(["Pile", "Face"])

# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    # Affichage du titre
    screen.blit(title_text, title_rect)

    # Dessiner les boutons Pile et Face
    pile_rect = pygame.draw.rect(screen, GREEN, (150, 150, 120, 60))
    face_rect = pygame.draw.rect(screen, RED, (330, 150, 120, 60))

    pile_text = font.render("Pile", True, WHITE)
    face_text = font.render("Face", True, WHITE)

    screen.blit(pile_text, (pile_rect.x + 30, pile_rect.y + 10))
    screen.blit(face_text, (face_rect.x + 30, face_rect.y + 10))

    # Afficher le résultat si dispo
    if result_text:
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 300))

    pygame.display.flip()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pile_rect.collidepoint(event.pos):
                choice = "Pile"
            elif face_rect.collidepoint(event.pos):
                choice = "Face"
            else:
                choice = None
            if choice:
                flip = flip_coin()
                if flip == choice:
                    result_text = font.render(f"Gagné ! C'était {flip}", True, GREEN)
                else:
                    result_text = font.render(f"Perdu ! C'était {flip}", True, RED)

# Quitter Pygame
pygame.quit()
