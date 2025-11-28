from random import choice, randint
import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
# === CLASSES DU JEU ===

class GameObject:
    def __init__(self):
        super().__init__()
        self.position = [0, 0]
        self.body_color = (255, 255, 255)
    
    def draw(self, surface):
        pass

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.body_color = SNAKE_COLOR
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
    
    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None
    
    def move(self):
        self.update_direction()
        x, y = self.position
        dx, dy = self.direction
        new_x = (x + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (y + dy * GRID_SIZE) % SCREEN_HEIGHT
        
        self.last = self.position
        self.position = [new_x, new_y]
        self.positions.insert(0, self.position)
        if len(self.positions) > 1:
            self.positions.pop()
    
    def draw(self, screen):
        for position in self.positions[:-1]:
            rect = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        
        # Tête
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)
        
        # Effacer dernier segment
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

class Apple(GameObject):
    def __init__(self):
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()
    
    def randomize_position(self):
        self.position = [
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        ]
    
    def draw(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# === FIN DES CLASSES ===
def main():
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Змейка')
    clock = pygame.time.Clock()
    
    # Créer les instances
    snake = Snake()
    food = Apple()

    # while True:
    while True:
        # clock.tick(SPEED)
        clock.tick(SPEED)
        
        # Тут опишите основную логику игры.
        # Gestion des événements
        handle_keys(snake)
        
        # Mouvement du serpent
        snake.move()
        
        # Vérifier collision avec la nourriture
        if snake.positions[0] == food.position:
            food.randomize_position()
            # Agrandir le serpent
            snake.positions.append(snake.positions[-1])
        
        # Dessin
        screen.fill(BOARD_BACKGROUND_COLOR)
        food.draw(screen)
        snake.draw(screen)
        
        # Mettre à jour l'affichage
        pygame.display.update()
# Метод draw класса Apple
def draw(self):
     rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
     pygame.draw.rect(screen, self.body_color, rect)
     pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# # Метод draw класса Snake
def draw(self):
     for position in self.positions[:-1]:
         rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
         pygame.draw.rect(screen, self.body_color, rect)
         pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

     # Отрисовка головы змейки
     head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
     pygame.draw.rect(screen, self.body_color, head_rect)
     pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

# Затирание последнего сегмента
     if self.last:
         last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
         pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

# Функция обработки действий пользователя
def handle_keys(game_object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                 game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                 game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                 game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                 game_object.next_direction = RIGHT

# Метод обновления направления после нажатия на кнопку
def update_direction(self):
    if self.next_direction:
         self.direction = self.next_direction
         self.next_direction = None

if __name__ == '__main__':
    main()
