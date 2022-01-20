from exceptions.snake_and_ladder_exceptions import InitException


class Snake:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @head.setter
    def head(self, head):
        print("head")
        self._head = head

    @tail.setter
    def tail(self, tail):
        print("tail")
        if tail >= self._head:
            raise InitException("Tail position should be lesser than head position")
        self._tail = tail
