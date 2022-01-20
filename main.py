from models.snake import Snake
from models.ladder import Ladder
from models.player import Player
from models.board import Board
from services.game_service.game import Game

if __name__ == '__main__':
    dice_size = int(input("Enter value of dice you are using: "))
    board_size = int(input("Enter the board size: "))
    no_of_snakes = int(input("Enter the number of snake to be added in board: "))
    snake_list = []
    for n in range(no_of_snakes):
        head_tail = input("Enter head followed by tail position: ").split()
        snake = Snake()
        snake.head = int(head_tail[0])
        snake.tail = int(head_tail[1])
        snake_list.append(snake)

    no_of_ladders = int(input("Enter the number of ladder to be added in board: "))
    ladder_list = []
    for n in range(no_of_ladders):
        start_end = input("Enter start followed by end position: ").split()
        ladder = Ladder()
        ladder.start = int(start_end[0])
        ladder.end = int(start_end[1])
        ladder_list.append(ladder)

    no_of_players = int(input("Enter the number of players: "))
    player_list = []
    for n in range(no_of_players):
        player_name = input("Enter name of player: ")
        player = Player(player_name)
        player_list.append(player)

    board = Board(snake_list, ladder_list)
    game = Game(board, player_list, dice_size, board_size)
    game.start()
