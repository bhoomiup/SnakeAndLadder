from exceptions.snake_and_ladder_exceptions import InitException


class Ladder:
    def __init__(self):
        self._start = None
        self._end = None

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @start.setter
    def start(self, start):
        self._start = start

    @end.setter
    def end(self, end):
        if end <= self._start:
            raise InitException("End position should we greater than start position")
        self._end = end
