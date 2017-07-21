

class TurnstileController:

    def __init__(self):
        self.is_coin = False
        self.is_turn = False

    def coin(self):
        self.is_coin = True

    def turn(self):
        self.is_turn = True
