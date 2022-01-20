class Board:
    def __init__(self, snakes, ladders):
        self.board_size = 0
        self._snakes = snakes
        self._ladders = ladders

    @property
    def snakes(self):
        return self._snakes

    @property
    def ladders(self):
        return self._ladders

    @snakes.setter
    def snakes(self, snakes):
        self._snakes = snakes

    @ladders.setter
    def ladders(self, ladders):
        self._ladders = ladders
