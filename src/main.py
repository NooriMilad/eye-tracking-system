import pygame
from eye_tracking import EyeTracker
from drawing import DrawingApp

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 800))
    pygame.display.set_caption("Eye Art System")

    eye_tracker = EyeTracker()
    drawing_app = DrawingApp(screen, eye_tracker)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            drawing_app.handle_event(event)

        drawing_app.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()