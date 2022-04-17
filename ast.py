import pygame
import time

pygame.init()

display_width = 500
display_height = 500
background_square_color = (154, 168, 128)
foreground_square_color = (72, 84, 57)
white = (255, 255, 255)

image = pygame.image.load(r'C:\Users\Iniya\PycharmProjects\SonomaHacks\plane.png')



places = [{"name": "- London", "type": "explore", "community": "city", "continent": "europe"},
        {"name": "- Paris", "type": "explore", "community": "city", "continent": "europe"},
        {"name": "- Tokyo", "type": "explore", "community": "city", "continent": "asia"},
        {"name": "- Dubai", "type": "explore", "community": "city", "continent": "asia"},
        {"name": "- New York City", "type": "explore", "community": "city", "continent": "nsamerica"},
        {"name": "- Rio de Janeiro", "type": "explore", "community": "city", "continent": "nsamerica"},
        {"name": "- Sydney", "type": "explore", "community": "city", "continent": "other"},
        {"name": "- Lagos", "type": "explore", "community": "city", "continent": "other"},
        {"name": "- Swiss Alps", "type": "explore", "community": "nature", "continent": "europe"},
        {"name": "- Durmitor National Park", "type": "explore", "community": "nature", "continent": "europe"},
        {"name": "- Mount Fuji", "type": "explore", "community": "nature", "continent": "asia"},
        {"name": "- Huanglong", "type": "explore", "community": "nature", "continent": "asia"},
        {"name": "- Andes Mountains", "type": "explore", "community": "nature", "continent": "nsamerica"},
        {"name": "- Grand Canyon", "type": "explore", "community": "nature", "continent": "nsamerica"},
        {"name": "- Great Barrier Reef", "type": "explore", "community": "nature", "continent": "other"},
        {"name": "- Kenyan Safari", "type": "explore", "community": "nature", "continent": "other"},
        {"name": "- Tsavo National Park", "type": "explore", "community": "nature", "continent": "other"},
        {"name": "- Athens", "type": "culture", "community": "city", "continent": "europe"},
        {"name": "- Madrid", "type": "culture", "community": "city", "continent": "europe"},
        {"name": "- Seoul", "type": "culture", "community": "city", "continent": "asia"},
        {"name": "- Taipei", "type": "culture", "community": "city", "continent": "asia"},
        {"name": "- Washington DC", "type": "culture", "community": "city", "continent": "nsamerica"},
        {"name": "- Bogotá", "type": "culture", "community": "city", "continent": "nsamerica"},
        {"name": "- Cairo", "type": "culture", "community": "city", "continent": "other"},
        {"name": "- Melbourne", "type": "culture", "community": "city", "continent": "other"},
        {"name": "- Greek Islands", "type": "culture", "community": "nature", "continent": "europe"},
        {"name": "- Eisriesenwelt", "type": "culture", "community": "nature", "continent": "europe"},
        {"name": "- Himalayas", "type": "culture", "community": "nature", "continent": "asia"},
        {"name": "- Indonesian Islands", "type": "culture", "community": "nature", "continent": "asia"},
        {"name": "- Machu Picchu", "type": "culture", "community": "nature", "continent": "nsamerica"},
        {"name": "- Hawaiian Islands", "type": "culture", "community": "nature", "continent": "nsamerica"},
        {"name": "- Madagascar", "type": "culture", "community": "nature", "continent": "other"},
        {"name": "- New Zealand", "type": "culture", "community": "nature", "continent": "other"},
        {"name": "- Lisbon", "type": "relax", "community": "city", "continent": "europe"},
        {"name": "- Zagreb", "type": "relax", "community": "city", "continent": "europe"},
        {"name": "- Batad", "type": "relax", "community": "city", "continent": "asia"},
        {"name": "- Hanoi", "type": "relax", "community": "city", "continent": "asia"},
        {"name": "- Cancun", "type": "relax", "community": "city", "continent": "nsamerica"},
        {"name": "- Orillia", "type": "relax", "community": "city", "continent": "nsamerica"},
        {"name": "- Gold Coast", "type": "relax", "community": "city", "continent": "other"},
        {"name": "- Kenya", "type": "relax", "community": "city", "continent": "other"},
        {"name": "- Sicily", "type": "relax", "community": "nature", "continent": "europe"},
        {"name": "- Algarve", "type": "relax", "community": "nature", "continent": "europe"},
        {"name": "- Tahiti", "type": "relax", "community": "nature", "continent": "asia"},
        {"name": "- Bali", "type": "relax", "community": "nature", "continent": "asia"},
        {"name": "Finger Lakes", "type": "relax", "community": "nature", "continent": "nsamerica"},
        {"name": "Punta del Este", "type": "relax", "community": "nature", "continent": "nsamerica"},
        {"name": "Jervis Bay", "type": "relax", "community": "nature", "continent": "other"},
        {"name": "Tarrafal beach", "type": "relax", "community": "nature", "continent": "other"}]


answers = []
destinations = []

def get_places():
    for place in places:
        if place["type"] == answers[0] and place["community"] == answers[1] and place["continent"] == answers[2]:
            destinations.append(place["name"])
    print(destinations)


screen = pygame.display.set_mode((display_width, display_height))

TitleFont = pygame.font.SysFont("Courier New", 35, True, False)
Title2Font = pygame.font.SysFont("Corbel", 35, bold=False, italic=False)
Title3Font = pygame.font.SysFont("Segoe Print", 35, bold=False, italic=False)
SubTitleFont = pygame.font.SysFont("Corbel", 18, bold=False, italic=False)
MediumFont = pygame.font.SysFont("Courier New", 28, bold=True, italic=False)
SmallFont = pygame.font.SysFont("Corbel", 23, bold=False, italic=False)
SmallFont2 = pygame.font.SysFont("Courier New", 20)

def plane_screen(bg_color):
    screen.fill(bg_color)
    screen.blit(image, (300, 200))
    pygame.display.update()
    time.sleep(0.2)

    screen.fill((bg_color))
    screen.blit(image, (250, 200))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(370, 220, 10, 10))
    pygame.display.update()
    time.sleep(0.2)

    screen.fill((bg_color))
    screen.blit(image, (200, 200))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(370, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(320, 220, 10, 10))
    pygame.display.update()
    time.sleep(0.2)

    screen.fill((bg_color))
    screen.blit(image, (150, 200))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(370, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(320, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(270, 220, 10, 10))
    pygame.display.update()
    time.sleep(0.2)

    screen.fill((bg_color))
    screen.blit(image, (100, 200))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(370, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(320, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(270, 220, 10, 10))
    pygame.draw.rect(screen, (184, 154, 99), pygame.Rect(220, 220, 10, 10))
    pygame.display.update()


def question_screen2(question, option1, option2):
    SubTitle = SubTitleFont.render(question, True, foreground_square_color)
    text_rect = SubTitle.get_rect(center=(display_width / 2, 100))
    screen.blit(SubTitle, text_rect)

    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 160, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 260, 280, 50))

    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 150, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 250, 280, 50))

    Medium = SmallFont2.render(option1, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 175))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option2, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 275))
    screen.blit(Medium, text_rect)

    Small = SmallFont.render("(Press 1)", True, foreground_square_color)
    screen.blit(Small, (210, 215))

    Small = SmallFont.render("(Press 2)", True, foreground_square_color)
    screen.blit(Small, (210, 315))

    pygame.display.flip()


def question_screen3(question, option1, option2, option3):
    SubTitle = SubTitleFont.render(question, True, foreground_square_color)
    text_rect = SubTitle.get_rect(center=(display_width / 2, 100))
    screen.blit(SubTitle, text_rect)

    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 160, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 260, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 360, 280, 50))

    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 150, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 250, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 350, 280, 50))

    Medium = SmallFont2.render(option1, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 175))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option2, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 275))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option3, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 375))
    screen.blit(Medium, text_rect)

    Small = SmallFont.render("(Press 1)", True, foreground_square_color)
    screen.blit(Small, (210, 215))

    Small = SmallFont.render("(Press 2)", True, foreground_square_color)
    screen.blit(Small, (210, 315))

    Small = SmallFont.render("(Press 3)", True, foreground_square_color)
    screen.blit(Small, (210, 415))

    pygame.display.flip()

def question_screen4(question, option1, option2, option3, option4):
    SubTitle = SubTitleFont.render(question, True, foreground_square_color)
    text_rect = SubTitle.get_rect(center=(display_width / 2, 50))
    screen.blit(SubTitle, text_rect)

    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 110, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 210, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 310, 280, 50))
    pygame.draw.rect(screen, background_square_color, pygame.Rect(100, 410, 280, 50))

    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 100, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 200, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 300, 280, 50))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(110, 400, 280, 50))

    Medium = SmallFont2.render(option1, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 125))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option2, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 225))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option3, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 325))
    screen.blit(Medium, text_rect)

    Medium = SmallFont2.render(option4, True, white)
    text_rect = Medium.get_rect(center=(display_width / 2, 425))
    screen.blit(Medium, text_rect)

    Small = SmallFont.render("(Press 1)", True, foreground_square_color)
    screen.blit(Small, (210, 165))

    Small = SmallFont.render("(Press 2)", True, foreground_square_color)
    screen.blit(Small, (210, 265))

    Small = SmallFont.render("(Press 3)", True, foreground_square_color)
    screen.blit(Small, (210, 365))

    Small = SmallFont.render("(Press 4)", True, foreground_square_color)
    screen.blit(Small, (210, 465))

    pygame.display.flip()

def last_screen():
    pygame.draw.rect(screen, background_square_color, pygame.Rect(18, 90, 450, 70))
    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(28, 80, 450, 70))
    SubTitle = SmallFont2.render("Here are some possible destinations", True, white)
    text_rect = SubTitle.get_rect(center=(display_width / 2, 100))
    screen.blit(SubTitle, text_rect)
    SubTitle = SmallFont2.render("that you may enjoy! :-)", True, white)
    text_rect = SubTitle.get_rect(center=(display_width / 2, 130))
    screen.blit(SubTitle, text_rect)

    y = 220
    for destination in destinations:
        suggestion = TitleFont.render(destination, True, white)
        text_rect = suggestion.get_rect(center=(display_width / 2, y))
        screen.blit(suggestion, text_rect)
        y += 70



    pygame.display.flip()


def render_question_screen(type):
    global current_page
    current_page = type

    if type == '1':
        screen.fill((232, 228, 211))
        question_screen3("What do you want to do the most during your trip?", "Explore the location", "Indulge in the culture", "Rest & Relax")

    elif type == '2':
        screen.fill((227, 226, 200))
        question_screen2("What do you prefer more?", "Urban City", "Nature")

    elif type == '3':
        screen.fill((217, 219, 189))
        question_screen4("What continent do you want to travel to?", "Europe", "Asia", "North or South America", "Other")

    elif type == "last":
        screen.fill((200, 209, 176))
        last_screen()


def home_screen():
    screen.fill((210, 220, 210))

    title = TitleFont.render("-----", True, (0, 0, 0))
    text_rect = title.get_rect(center=(display_width / 2, 80))
    screen.blit(title, text_rect)

    title = TitleFont.render("dream", True, (0, 0, 0))
    text_rect = title.get_rect(center=(display_width / 2, 110))
    screen.blit(title, text_rect)

    title = Title2Font.render("DESTINATION", True, (0, 0, 0))
    text_rect = title.get_rect(center=(display_width / 2, 150))
    screen.blit(title, text_rect)

    title = Title3Font.render("locator", True, (0, 0, 0))
    text_rect = title.get_rect(center=(display_width / 2, 180))
    screen.blit(title, text_rect)

    title = Title3Font.render("-----", True, (0, 0, 0))
    text_rect = title.get_rect(center=(display_width / 2, 200))
    screen.blit(title, text_rect)

    subtitle = SubTitleFont.render("Take this short quiz to find an idea travel spot", True, (0, 0, 0))
    text_rect = subtitle.get_rect(center=(display_width / 2, 255))
    screen.blit(subtitle, text_rect)

    subtitle = SubTitleFont.render("for your next trip!  :-)", True, (0, 0, 0))
    text_rect = subtitle.get_rect(center=(display_width / 2, 280))
    screen.blit(subtitle, text_rect)

    pygame.draw.rect(screen, foreground_square_color, pygame.Rect(55, 380, 390, 40))
    space_message = SmallFont2.render("Click the space bar to continue", True, white)
    text_rect = space_message.get_rect(center=(display_width / 2, 400))
    screen.blit(space_message, text_rect)

    subtitle = SubTitleFont.render("(created by iniya saravanan)", True, (0, 0, 0))
    text_rect = subtitle.get_rect(center=(display_width / 2, 480))
    screen.blit(subtitle, text_rect)




home_screen()

running = True
current_page = 'HOME'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                plane_screen((210, 220, 210))
                time.sleep(0.35)
                render_question_screen(type='1')
            elif event.key == pygame.K_1:
                if current_page == "1":
                    answers.append("explore")
                    plane_screen((232, 228, 211))
                    time.sleep(0.35)
                    render_question_screen(type='2')
                elif current_page == "2":
                    answers.append("city")
                    plane_screen((227, 226, 200))
                    time.sleep(0.35)
                    render_question_screen(type='3')
                elif current_page == "3":
                    answers.append("europe")
                    plane_screen((217, 219, 189))
                    time.sleep(0.35)
                    get_places()
                    render_question_screen(type='last')

            elif event.key == pygame.K_2:
                if current_page == "1":
                    answers.append("culture")
                    plane_screen((232, 228, 211))
                    time.sleep(0.35)
                    render_question_screen(type='2')
                elif current_page == "2":
                    answers.append("nature")
                    plane_screen((227, 226, 200))
                    time.sleep(0.35)
                    render_question_screen(type='3')
                elif current_page == "3":
                    answers.append("asia")
                    plane_screen((217, 219, 189))
                    time.sleep(0.35)
                    get_places()
                    render_question_screen(type='last')

            elif event.key == pygame.K_3:
                if current_page == "1":
                    answers.append("relax")
                    plane_screen((232, 228, 211))
                    time.sleep(0.35)
                    render_question_screen(type='2')
                elif current_page == "3":
                    answers.append("nsamerica")
                    plane_screen((217, 219, 189))
                    time.sleep(0.35)
                    get_places()
                    render_question_screen(type='last')

            elif event.key == pygame.K_4:
                if current_page == "3":
                    answers.append("other")
                    plane_screen((217, 219, 189))
                    time.sleep(0.35)
                    get_places()
                    render_question_screen(type='last')

    pygame.display.flip()

pygame.quit()