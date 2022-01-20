class Player:
    def __init__(self, name):
        self._name = name
        self.current_dice_val = 0
        self.current_position = 0
        self.has_won = False

    @property
    def name(self):
        return self._name

    @property
    def current_dice_val(self):
        return self.current_dice_val

    @property
    def current_position(self):
        return self._current_position

    @property
    def has_won(self):
        return self._has_won

    @name.setter
    def name(self, name):
        self._name = name

    @current_dice_val.setter
    def current_dice_val(self, current_dice_val):
        self._current_dice_val = current_dice_val

    @current_position.setter
    def current_position(self, current_position):
        self._current_position = current_position

    @has_won.setter
    def has_won(self, has_won):
        self._has_won = has_won
