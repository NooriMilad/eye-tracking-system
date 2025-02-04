import cv2

class DrawingTools:
    def __init__(self):
        self.tool = 'brush'
        self.pen_color = (0, 0, 255)  # Default to red
        self.stroke_width = 2

    def set_tool(self, tool):
        self.tool = tool

    def set_pen_color(self, color):
        self.pen_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    def set_stroke_width(self, width):
        self.stroke_width = width

    def draw_on_frame(self, frame, coordinates):
        if coordinates:
            if self.tool == 'brush':
                cv2.circle(frame, coordinates, self.stroke_width, self.pen_color, -1)
            # Add more tool implementations as needed
        return frame