import random

from services.game_service import constants as service_constants
from models.board import Board
from models.player import Player


class Game:
    """
    Game: This class is used to build services based on requirement
    """
    def __init__(self, board: Board, players: list[Player], dice_val, board_size):
        self.board = board
        self.players = players
        self.dice_val = dice_val
        self.board.board_size = board_size
        self.winner = False

    def start(self):
        """
        Game execution
        """
        while not self.winner:
            for player in self.players:
                input(f"{player.name}, {service_constants.ROLL_DICE_MSG}")
                dice_value = self.roll_dice()
                self.move_player(player, dice_value)
                if player.current_position == self.board.board_size:
                    player.hasWon = True
                    self.winner = True
                    print(f"{player.name} {service_constants.WIN_MSG}")
                    break

    def roll_dice(self):
        """
        This method is used to get the value on dice roll
        :return:
        dice value (int)
        """
        return random.randint(1, self.dice_val)

    def move_player(self, player: Player, value):
        """
        This method is to move the player based on the value
        :param player: player making the move
        :param value: value of dice
        """
        current_pos = player.current_position
        new_pos = player.current_position + value
        snake_pos = self.check_snake(new_pos)
        ladder_pos = self.check_ladder(new_pos)
        if snake_pos:
            new_pos = snake_pos
        elif ladder_pos:
            new_pos = ladder_pos
        if new_pos <= self.board.board_size:
            player.current_position = new_pos
            print(f"{player.name} rolled a {value} and moved from {current_pos} to {player.current_position}")

    def check_snake(self, position):
        """
        This method is to check if there is a snake in the position
        :param position: current position
        :return: snake tail position
        """
        for snake in self.board.snakes:
            if snake.head == position:
                print(service_constants.MET_SNAKE)
                return snake.tail

    def check_ladder(self, position):
        """
        This method is to check if there is a ladder in the position
        :param position: current position
        :return: ladder end position
        """
        for ladder in self.board.ladders:
            if ladder.start == position:
                print(service_constants.MET_LADDER)
                return ladder.end
