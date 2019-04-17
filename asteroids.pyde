#Menu class which controls the stage of the game
class Menu():
    def __init__(self):
        #setting initial stage as 1(menu)
        self.stage = 1
        
    def change_stage(self, stage):
        #method that changes the stage of the game 
        self.stage = stage
        
#Asteroids class    
class Asteroids():
    def __init__(self):
        #randomly spawning asteroids on the screen
        #x position
        self.x = random(0, 800)
        #y position
        self.y = random(0, 600)
        #x velocity
        self.dx = random(-2, 2)
        #y velocity
        self.dy = random(-2, 2)
        
    def move(self):
        #moving method for asteroids
        self.x += self.dx
        self.y += self.dy
        
        #reset its position if its goes beyond the screen
        if self.x < 0:
            self.x = 800
       
        if self.x > 800:
            self.x = 0
        
        if self.y < 0:
            self.y = 600
       
        if self.y > 600:
            self.y = 0
  
    def render(self):
        #draw the asteroids
        fill(160, 255, 255)
        strokeWeight(0)
        ellipse(self.x, self.y, 16, 16)

class Player():
    #Player class
    #Player has an initial x position and y position
    def __init__(self, x, y):
        #x position
        self.x = x
        #y position
        self.y = y
        #current angle of the player
        self.angle = 0
        #acceleration of player
        self.acceleration = 0
        
    def _rotate(self):
    #rotation method of the player
        if control['a'] or control['A']:
            #if the player pressed a or A, the angle of the player will increase 5 degrees
            self.angle -= 5
        elif control['d'] or control['D']:
            #if the player pressed d or D, the angle of the player will decrease 5 degrees
            self.angle += 5
    
    def accelerate(self):
    #acceleration method of the player
        if control['w'] or control['W']:
             #if the player pressed w or W will increase 5 degrees
            if self.acceleration <= 500:
                #if the current acceleration of the player is less than 500, acceleration number will increase by 10
                self.acceleration += 10
        else:
            #if the player is not holding w or W
            if self.acceleration > 0:
                #if the current acceleration of the player is greater than 0, acceleration will slowly decrease by 8
                self.acceleration -= 8
    
    def move(self):
        #move method of te player
        #formulas for calculating current location of the player
        self.x += sin(radians(self.angle))*self.acceleration/100
        self.y -= cos(radians(self.angle))*self.acceleration/100
    
        #reset its position if its goes beyond the screen
        if self.x < 0:
            self.x = 800
       
        if self.x > 800:
            self.x = 0
        
        if self.y < 0:
            self.y = 600
       
        if self.y > 600:
            self.y = 0
        
    def render(self):
        #draw the ship of current player
        fill(100)
        strokeWeight(0)
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(self.angle))
        triangle(0, -20, -10, 10, 10, 10)
        popMatrix()
   
def setup():  
    global player, control
    size(800, 600)
    player = Player(width/2, height/2)
    control = {'a' : False, 'w': False, 'd': False, 'A' : False, 'W': False, 'D': False, 'p': False}
    
def mouseClicked():
    #while on the menu page...
    if menu.stage == 1:
        if 100 <= mouseX <= 600 and 300 <= mouseY <= 370:
            menu.change_stage(2)  
        if 100 <= mouseX <= 600 and 400 <= mouseY <= 470:
            menu.change_stage(3)     

def keyPressed():
    global control
    #while in game, setting true for when key is pressed
    if menu.stage == 2:
        if key in control:
            control[key] = True

def keyReleased():
    #while in game, setting flase when key is released
    if menu.stage == 2:
        if key in control:
            control[key] = False
        
def draw():
    global player, score
    if menu.stage == 1:
    #while on the menu page
        background(0)
        fill(255)
        myfont1 = createFont("Goudy Stout", 60)
        myfont2 = createFont("Trebuchet MS", 40)
        textFont(myfont1)
        textAlign(CENTER, CENTER)
        text("Asteroids", width/2, 200)
        textFont(myfont2)
        text("Play", width/2, 350)
        text("High Score", width/2, 450)

    if menu.stage == 2:
    #while in game
    #background with stars
        background(0)
        fill(225)
        ellipse(random(width), random(height), 3, 3)
        text("Score: " + str(score), 70, 20)

        for asteroids in asteroids_in_field:
            asteroids.render()
            asteroids.move()
    
        player._rotate()
        player.accelerate()
        player.move()
        player.render()

    if menu.stage == 3:
    #while on high score page
        background(0)
        myfont1 = createFont("Trebuchet MS", 40)
        textFont(myfont1)
        text("High Score", 100, 20)
        myfont4 = createFont("Trebuchet MS", 30)
        textFont(myfont4)
        text("Name: ", 50, 70)
        text("Score: ", 400, 70)
        
#list of asteroids    
asteroids_in_field = []
menu = Menu()
score = 0
#create 10 asteroids
for n in range(10):
    asteroids_in_field.append(Asteroids())  
