import pygame
import cv2
import numpy as np

class DrawingCanvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = pygame.Surface((width, height))
        self.canvas.fill((255, 255, 255))  # White background

    def draw_circle(self, position, radius=10, color=(255, 0, 0)):  # Red color
        pygame.draw.circle(self.canvas, color, position, radius)

    def clear_canvas(self):
        self.canvas.fill((255, 255, 255))  # Reset to white background

    def get_surface(self):
        return self.canvas

class DrawingApp:
    def __init__(self, screen, eye_tracker):
        self.screen = screen
        self.eye_tracker = eye_tracker
        self.canvas = DrawingCanvas(screen.get_width(), screen.get_height())
        self.cursor_pos = (400, 300)
        self.cap = cv2.VideoCapture(0)
        self.drawing = False
        self.pen_color = (255, 0, 0)  # Default to red
        self.pen_size = 2  # Default pen size

        # Define buttons
        self.buttons = {
            "start": pygame.Rect(10, 10, 100, 50),
            "stop": pygame.Rect(120, 10, 100, 50),
            "erase": pygame.Rect(230, 10, 100, 50),
            "color_red": pygame.Rect(340, 10, 100, 50),
            "color_blue": pygame.Rect(450, 10, 100, 50),
        }

    def draw_buttons(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.buttons["start"])  # Green
        pygame.draw.rect(self.screen, (255, 0, 0), self.buttons["stop"])  # Red
        pygame.draw.rect(self.screen, (255, 255, 255), self.buttons["erase"])  # White
        pygame.draw.rect(self.screen, (255, 0, 0), self.buttons["color_red"])  # Red
        pygame.draw.rect(self.screen, (0, 0, 255), self.buttons["color_blue"])  # Blue

        font = pygame.font.Font(None, 36)
        self.screen.blit(font.render("Start", True, (0, 0, 0)), (20, 20))
        self.screen.blit(font.render("Stop", True, (0, 0, 0)), (130, 20))
        self.screen.blit(font.render("Erase", True, (0, 0, 0)), (240, 20))
        self.screen.blit(font.render("Red", True, (0, 0, 0)), (360, 20))
        self.screen.blit(font.render("Blue", True, (0, 0, 0)), (470, 20))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons["start"].collidepoint(event.pos):
                self.drawing = True
            elif self.buttons["stop"].collidepoint(event.pos):
                self.drawing = False
            elif self.buttons["erase"].collidepoint(event.pos):
                self.canvas.clear_canvas()
            elif self.buttons["color_red"].collidepoint(event.pos):
                self.pen_color = (255, 0, 0)
            elif self.buttons["color_blue"].collidepoint(event.pos):
                self.pen_color = (0, 0, 255)

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            self.screen.blit(frame, (0, 0))

        eye_pos = self.eye_tracker.get_eye_position()
        if eye_pos and self.drawing:
            self.cursor_pos = (int(eye_pos[0] * self.screen.get_width()), int(eye_pos[1] * self.screen.get_height()))
            self.canvas.draw_circle(self.cursor_pos, color=self.pen_color)

        self.screen.blit(self.canvas.get_surface(), (0, 0))
        self.draw_buttons()

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()