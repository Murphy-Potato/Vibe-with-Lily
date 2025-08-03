import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Vibe with Lily")

font = pygame.font.SysFont('arial', 20)  
text_surface = font.render("Choose an emotion for Lily", True, (0, 0, 0))  

# Load images
images = {
    "idle1": pygame.image.load("assests/pictures/idle-handsup.png"),
    "idle2": pygame.image.load("assests/pictures/idle-handsdown.png"),
    "happy": pygame.image.load("assests/pictures/happy.png"),
    "sad": pygame.image.load("assests/pictures/sad.png"),
    "hype": pygame.image.load("assests/pictures/hype.png"),
    "angry": pygame.image.load("assests/pictures/angry.png"),
    "lovely": pygame.image.load("assests/pictures/lovely.png")
}

# Resize all images to same size
for key in images:
    images[key] = pygame.transform.scale(images[key], (500, 500))

# Load music
music = {
    "chill": "assests/music/chill.mp3",
    "happy": "assests/music/happy.mp3",
    "sad": "assests/music/sad.mp3",
    "hype": "assests/music/hype.mp3",
    "angry": "assests/music/angry.mp3",
    "lovely": "assests/music/lovely.mp3"
}

def play_music(track):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music[track])
    pygame.mixer.music.play(-1)

# Button setup
font = pygame.font.SysFont(None, 36)
def make_button(text, x, y):
    return {
        "text": text,
        "rect": pygame.Rect(x, y, 120, 40)
    }

buttons = [
    make_button("Happy", 50, 500),
    make_button("Sad", 200, 500),
    make_button("Hype", 350, 500),
    make_button("Angry", 500, 500),
    make_button("Lovely", 650, 500)
]

current_state = "idle1"
is_idle = True

character_rect = pygame.Rect(150, 50, 300, 300)

play_music("chill")

# Main loop
while True:
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (260, 20))  

    # Draw character
    screen.blit(images[current_state], character_rect.topleft)

    # Draw buttons
    for btn in buttons:
        pygame.draw.rect(screen, (200, 200, 200), btn["rect"])
        label = font.render(btn["text"], True, (0, 0, 0))
        screen.blit(label, (btn["rect"].x + 10, btn["rect"].y + 5))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Character click: toggle idle and play chill music
            if character_rect.collidepoint(mouse_pos):
                if is_idle:
                    current_state = "idle2" if current_state == "idle1" else "idle1"
                    play_music("chill")
                is_idle = True

            # Check emotion buttons
            for btn in buttons:
                if btn["rect"].collidepoint(mouse_pos):
                    emotion = btn["text"].lower()
                    current_state = emotion
                    play_music(emotion)
                    is_idle = False
