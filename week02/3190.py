N = int(input())
K = int(input())

apples = []
moves = []
snake = [(0, 0)]

for _ in range(K):
    row, col = map(int, input().split())
    apples.append((row - 1, col - 1))

L = int(input())

for _ in range(L):
    x, c = input().split()
    x = int(x)
    moves.append((x, c))

board = [["X" for _ in range(N)] for _ in range(N)]


time = 0
move_direction = (0, 1)
tail = (0, 0)


def snake_move(move_direction):
    global snake
    global tail
    dx, dy = move_direction
    current_x, current_y = snake[-1]

    x, y = current_x + dx, current_y + dy

    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if (x, y) in snake:
        return False

    board[x][y] = "O"
    snake.append((x, y))
    tail = snake[0]
    return True


def get_apple():
    x, y = snake[-1]
    for apple in apples:
        if apple[0] == x and apple[1] == y:
            apples.remove(apple)
            return True
    return False


def turn_snake(move_direction, c):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = directions.index(move_direction)

    new_idx = 0

    if c == "L":
        new_idx = (idx - 1) % 4
    if c == "D":
        new_idx = (idx + 1) % 4

    return directions[new_idx]


while True:
    time += 1
    """
    for row in board:
        print(" ".join(item for item in row))
    print()
    """
    if not snake_move(move_direction):
        break

    if not get_apple():
        board[tail[0]][tail[1]] = "X"
        snake = snake[1:]

    for x, c in moves:
        if time == x:
            move_direction = turn_snake(move_direction, c)


print(time)
