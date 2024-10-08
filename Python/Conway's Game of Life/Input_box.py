"""Requirements"""

import pygame as py


py.init()
screen = py.display.set_mode((640, 480))
screen.fill((128, 128, 128))
COLOR_INACTIVE = py.Color("lightskyblue3")
COLOR_ACTIVE = py.Color("dodgerblue2")
FONT = py.font.Font(None, 32)


class InputBox:
    """Input Box."""

    def __init__(self, x, y, w, h, text=""):
        self.rect = py.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """Handles input event."""
        if event.type == py.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == py.KEYDOWN:
            if self.active:
                if event.key == py.K_RETURN:
                    print(self.text)
                    self.text = ""
                elif event.key == py.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        """Resize the box if text is too long."""
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """Blit the text and rect."""
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        py.draw.rect(screen, self.color, self.rect, 2)


def run():
    """Main."""
    clock = py.time.Clock()
    input_box = InputBox(100, 100, 140, 32)
    done = False

    while not done:
        for event in py.event.get():
            input_box.handle_event(event)
            input_box.update()

            if event.type == py.KEYDOWN:
                if event.key == py.K_DOWN:
                    done = True

        input_box.draw(screen)

        py.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    run()
    py.quit()
