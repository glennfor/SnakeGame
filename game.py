from tkinter.tix import DirTree
from constants import *


class Snake():
    def __init__(self,x,y):
        self.bodyPoints = []
        self.head = (x, y)
        self.changeX , self.changeY = DIRECTIONS['RIGHT']
        self.bodyPoints.append(self.head)
        self.prevPoint = None

    def move(self):
        x, y = self.head
        self.head = x+ self.changeX, y+self.changeY
        self.bodyPoints.insert(0, self.head)
        self.prevPoint =  self.bodyPoints.pop()

    def turn(self, direction):
        #cant turn in oposite directions
        x, y = direction
        if (x == self.changeX) or (y == self.changeY):
            return

        self.changeX, self.changeY = direction
    
    def grow(self, point):
        if self.head == point:
            self.bodyPoints.append(self.prevPoint)
            return True
        return False

    def getBody(self,):
        return self.bodyPoints

    
class Game():
    def __init__(self, window) -> None:
        self.window = window
        self.snake = Snake(5,5)
        self.boxPoints = [] 
        self.food = None

        self.init()  

    def init(self,):
        for x in range(GRID_WIDTH):
            rowPoints = []
            for y in range(GRID_HEIGHT):
                rowPoints.append((WINDOW_MARGIN_X + x*BOX_SIZE, WINDOW_MARGIN_Y+y*BOX_SIZE))
            self.boxPoints.append(rowPoints)

    def detectCollision(self,):
        x, y = self.snake.head
        body = self.snake.getBody()
        hittingWall = (x < 0  or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT)
        hittingSelf = any([point for point in body if body.count(point) > 1])
        if hittingSelf or hittingWall:
            return True
        return False

    def createFood(self,)->tuple:
        snakeBody = self.snake.getBody()
        spot = None
        emptySpots = []
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if (x, y) not in snakeBody:
                    emptySpots.append((x,y))
        self.food = random.choice(emptySpots)

        return self.food

    def drawFood(self,):
        if self.food is None:
            return
        row, col = self.food
        row, col = self.boxPoints[row][col]
        pygame.draw.rect(self.window, FOOD_COLOR, 
            (row, col, BOX_SIZE, BOX_SIZE))

    def drawSnake(self, ):
        points = self.snake.getBody()
        for point in points:
            x, y = point
            row, col= self.boxPoints[x][y]
            pygame.draw.rect(self.window, SNAKE_COLOR, 
            (row, col, BOX_SIZE, BOX_SIZE))

    def drawBoard(self, ):
        pygame.draw.rect(self.window, BORDER_COLOR, 
        (WINDOW_MARGIN_X - GRID_BORDER, WINDOW_MARGIN_Y - GRID_BORDER, 
        BOX_SIZE*GRID_WIDTH + GRID_BORDER*2, BOX_SIZE*GRID_HEIGHT + GRID_BORDER*2))

        pygame.draw.rect(self.window, BACKGROUND_COLOR, 
        (WINDOW_MARGIN_X, WINDOW_MARGIN_Y, 
        BOX_SIZE*GRID_WIDTH, BOX_SIZE*GRID_HEIGHT))

        #draw horizontal lines
        for row in range(GRID_HEIGHT):
            pygame.draw.line(self.window, LINE_COLOR, 
            (WINDOW_MARGIN_X, WINDOW_MARGIN_Y+row*BOX_SIZE), (WINDOW_MARGIN_X + BOX_SIZE*GRID_WIDTH, WINDOW_MARGIN_Y+row*BOX_SIZE))

        #draw vevrtical lines
        for col in range(GRID_WIDTH):
            pygame.draw.line(self.window, LINE_COLOR, 
            (WINDOW_MARGIN_X + col*BOX_SIZE, WINDOW_MARGIN_Y), (WINDOW_MARGIN_X + col*BOX_SIZE, WINDOW_MARGIN_Y + BOX_SIZE*GRID_HEIGHT))
  
    def updateUI(self,):
        self.drawBoard()
        self.drawSnake()
        self.drawFood()



def runGame():

    running = True
    score = 0
    game = Game(WINDOW)
    timeDelta = time.time()
    food = game.createFood()
    while running:
        WINDOW.fill(BLACK)
        surf = pygame.transform.rotate(font.render('Score: %d'%score, 1, YELLOW), 90)
        WINDOW.blit(surf, (2, WINDOW_HEIGHT//3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.snake.turn(DIRECTIONS['RIGHT'])
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.snake.turn(DIRECTIONS['LEFT'])
                elif event.key == pygame.K_DOWN or event.key == pygame.K_a:
                    game.snake.turn(DIRECTIONS['DOWN'])
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.snake.turn(DIRECTIONS['UP'])

        
        if time.time()-timeDelta > SNAKE_SPEED:
            game.snake.move()
            timeDelta = time.time()
        
        if game.detectCollision():
            print(game.snake.bodyPoints)
            running = False
            break
            
        game.updateUI()
        eaten = game.snake.grow(food)
        if eaten:
            score += 1
            MUNCH.play()
            food = game.createFood()

        pygame.display.update()
    pygame.quit()