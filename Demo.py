import pygame

#GLOBAL VARIABLES !IMPORTANT!
WALL_SIZE = 20
SCREEN_SIZE_X = 400
SCREEN_SIZE_Y = 400
CELL_ROW_COUNT_X = SCREEN_SIZE_X // WALL_SIZE
CELL_ROW_COUNT_Y = SCREEN_SIZE_Y // WALL_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
clock = pygame.time.Clock()
running = True
dt = 0

#creates list for collision
obj_list = []
goal = []

def draw_maze(surface, Maze):
        for X in range(len(Maze)):
            for Y in range(len(Maze)):
                rect = pygame.Rect(Y * WALL_SIZE, X * WALL_SIZE, WALL_SIZE, WALL_SIZE)
                if Maze[X][Y] == 1:
                    pygame.draw.rect(surface, "white", rect)
                    obj_list.append(rect)
                if Maze[X][Y] == 2:
                    pygame.draw.rect(surface, "green", rect)
                    goal.append(rect)

player_pos = pygame.Vector2(25,25)

player_pos_last = player_pos.xy

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #Drawing the bounding box for the Gar
    Gar_bounding_box = pygame.rect.Rect(player_pos.x, player_pos.y, 10, 10)
    pygame.draw.rect(screen, "red", Gar_bounding_box)

    #drawing the maze
    Maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1],
            [1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1],
            [1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1],
            [1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1],
            [1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1],
            [1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1],
            [1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,1,1],
            [1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1],
            [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,0,2,0,1],
            [1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
    draw_maze(screen, Maze)
    
    #checking for wall colision
    if Gar_bounding_box.collideobjects(obj_list):
        player_pos.xy = player_pos_last
    if Gar_bounding_box.x <= 0:
        player_pos.x = player_pos_last.x

    #goal system
    if Gar_bounding_box.collideobjects(goal):
        pygame.quit()
        print("You won!")

    #movement system
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]:
        speed = 100
    else:
        speed = 30
    
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt
   
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    #saves player pos from last frame
    if not Gar_bounding_box.collideobjects(obj_list):
        player_pos_last = player_pos.xy

pygame.quit()