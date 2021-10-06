import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        
    def update(self):
        self.rect.centerx += self.speed
    
    def win_state(self):
        self.win_state = False

class Button(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.clicked = False

pygame.init() # Initiate pygame
screen = pygame.display.set_mode((480, 360)) # Create display surface
clock = pygame.time.Clock() # Create clock object

bg = pygame.image.load('images/bg.png')   

button1 = Button('images/Player_1_button.png', 90, 330)
button1_group = pygame.sprite.GroupSingle()
button1_group.add(button1)

button2 = Button('images/Player_2_button.png', 370, 330)
button2_group = pygame.sprite.GroupSingle()
button2_group.add(button2)

cat = Player('images/cat1.png', 40, 155, 25)
cat_group = pygame.sprite.GroupSingle()
cat_group.add(cat)

dog = Player('images/dog1.png', 40, 250, 25)
dog_group = pygame.sprite.GroupSingle()
dog_group.add(dog)

cat_win = pygame.image.load('images/cat_win.png')
dog_win = pygame.image.load('images/dog_win.png')

while True: # Game loop
    for event in pygame.event.get(): #Check for events / player input
        if event.type == pygame.QUIT: # Close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.rect.collidepoint(event.pos):
                cat.update()
                print(f'cat x_pos: {cat.rect.centerx} y_pos: {cat.rect.centery}')
            if cat.rect.centerx >= 465:
                cat.win_state = True
                print("THE CAT WINS")
                
            if button2.rect.collidepoint(event.pos):
                dog.update()
                print(f"dog x_pos: {dog.rect.centerx} y_pos: {dog.rect.centery}")
            if dog.rect.centerx >= 465:
                dog.win_state = True
                print("THE DOG WINS")
    
    screen.blit(bg,(0,0))
    cat_group.draw(screen)
    dog_group.draw(screen)
    button1_group.draw(screen)
    button2_group.draw(screen)
    
    if cat.win_state == True:
        screen.blit(cat_win, (0,0))
    if dog.win_state == True:
       screen.blit(dog_win, (0,0)) 
    
    pygame.display.update() # Draw frame
    clock.tick(120) # Control the framerate