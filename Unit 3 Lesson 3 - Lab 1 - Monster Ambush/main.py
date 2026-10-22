import random
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Ambush")
font = pygame.font.Font(None, 34)
large_font = pygame.font.Font(None, 48)

states = ["Graveyard",
          "Haunted House",
          "Dark Forest",
          "Pumpkin Patch"]

transition_matrix = [
    [0.10, 0.45, 0.30, 0.15],
    [0.35, 0.10, 0.40, 0.15],
    [0.25, 0.35, 0.15, 0.25],
    [0.40, 0.20, 0.20, 0.20]
]




def draw_quadrants():
    pygame.draw.rect(screen, (222,31,18), (0, 0, WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, (24, 44, 222), (WIDTH // 2, 0, WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, (24, 222, 41), (0, HEIGHT // 2, WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, (222, 169, 24), (WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2))

    screen.blit(large_font.render("Graveyard", True, (255, 255, 255)), ((20,20)))
    screen.blit(large_font.render("Haunted House", True, (255, 255, 255)), (420,20))
    screen.blit(large_font.render("Dark Forest", True, (255, 255, 255)), (20,320))
    screen.blit(large_font.render("Pumpkin Patch", True, (255, 255, 255)), (420,320))

current_state = 2
current_round = 0
max_rounds = 10
score = 0
ambush_state = None
next_state = None
valid_choice = False
message = "Pick a quadrant 1-4 to ambush the monster!"
running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                ambush_state = 0
                valid_choice = True
            elif event.key == pygame.K_2:
                ambush_state = 1
                valid_choice = True
            elif event.key == pygame.K_3:
                ambush_state = 2
                valid_choice = True
            elif event.key == pygame.K_4:
                ambush_state = 3
                valid_choice = True

            if valid_choice:
                next_state = random.choices(
                    range(4),
                    weights=transition_matrix[current_state],
                    k=1
                )[0]

                if ambush_state == next_state:
                    score += 1
                    message = "AMBUSH SUCCESSFUL!"
                else:
                    message = "The monster escaped!"
                current_state = next_state
                current_round += 1
                valid_choice = False
                if current_round >= max_rounds:
                    message = "Game over! Final Score: " + str(score)
                    running = False

    draw_quadrants()

    panel = pygame.Surface((WIDTH, 180))
    panel.fill((128, 128, 128))
    panel.set_alpha(150)

    if ambush_state == None:
        ambush_text = "Waiting for monster to move..."
    else:
        ambush_text = states[ambush_state] 

    if next_state == None:
        move_text = "Waiting for monster to move..."
    else:
        move_text = states[next_state]


    location_text = font.render("Current Location: " + states[current_state], True, (255, 255, 255))
    ambush_text = font.render("Your Ambush: " + ambush_text, True, (255, 255, 255))
    move_text = font.render("Monster Moved To: " + move_text, True, (255, 255, 255))
    message_text = font.render(message, True, (255, 255, 255))
    score_text = font.render("Score: " + str(score) + " / " + str(max_rounds), True, (255, 255, 255))

    panel.blit(location_text, (20, 10))
    panel.blit(ambush_text, (20, 45))
    panel.blit(move_text, (20, 75))
    panel.blit(message_text, (20, 105))
    panel.blit(score_text, (20, 135))

    screen.blit(panel, (0, HEIGHT - 180))
    pygame.display.flip()

pygame.quit()
sys.exit()
