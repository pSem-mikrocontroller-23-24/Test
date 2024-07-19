import speech_recognition as sr
import pygame
import time

# pib Farben in RGB
color_pink = (230, 0, 126)
color_blue = (0, 159, 227)
color_purple = (149, 27, 129)
black = (0, 0, 0)

# Initialisierung von pygame
pygame.init()

# Fenstermaße festlegen
width, height = 1024, 600
screen = pygame.display.set_mode((width, height))

# Titel des Fensters setzen
pygame.display.set_caption("pib")

# Funktion, um das Fenster zu aktualisieren
def draw_eyes(color):
    screen.fill(black)
    # Zeichne zwei Ellipsen für farbige Augen
    pygame.draw.ellipse(screen, color, (156, 100, 200, 400))
    pygame.draw.ellipse(screen, color, (668, 100, 200, 400))
    # Pupillen
    pygame.draw.ellipse(screen, black, (186, 130, 140, 340))
    pygame.draw.ellipse(screen, black, (698, 130, 140, 340))
    pygame.draw.rect(screen, black, pygame.Rect(0, 285, 1024, 30))
    pygame.display.flip()

def draw_eyes_closed(color):
    screen.fill(black)    
    # Zeichne kleinere Ellipsen (Augen zu)
    pygame.draw.ellipse(screen, color, (181, 200, 150, 200))
    pygame.draw.ellipse(screen, color, (693, 200, 150, 200))
    pygame.draw.rect(screen, black, pygame.Rect(0, 285, 1024, 30))
    pygame.display.flip()

# Funktion zum Blinzeln
def blink(color):
    draw_eyes(color)
    time.sleep(0.5)
    draw_eyes_closed(color)
    time.sleep(0.5)
    draw_eyes(color)
    time.sleep(0.5)
    draw_eyes_closed(color)
    time.sleep(0.5)
    draw_eyes(color)

# Funktion, um Sprachbefehle zu erkennen
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hallo, was kann ich tun? Sprechen Sie jetzt...")
        audio = recognizer.listen(source)

        try:
            # Erkenne Sprache
            text = recognizer.recognize_google(audio, language="de-DE")
            print(f"Erkannter Text: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Entschuldigung, ich habe das nicht verstanden.")
        except sr.RequestError:
            print("Entschuldigung, der Sprachdienst ist derzeit nicht verfügbar.")
    return ""

def main():
    running = True
    current_color = color_blue # Startzustand: Augen blau und offen
    draw_eyes(current_color)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False            

        # Erkennen Sie den Sprachbefehl
        command = recognize_speech()

        if "augen zu" in command:
            draw_eyes_closed(current_color)
        elif "augen auf" in command:
            draw_eyes(current_color)
        elif "augen pink" in command:
            current_color = color_pink
            draw_eyes(current_color)
        elif "augen blau" in command:
            current_color = color_blue
            draw_eyes(current_color)
        elif "augen lila" in command:
            current_color = color_purple
            draw_eyes(current_color)
        elif "blinzeln" in command:
            blink(current_color)
        elif "ende" in command:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()