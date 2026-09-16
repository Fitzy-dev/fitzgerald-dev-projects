# Jordan Fitzgerald
# 4/7/2026
# Player Interface Project


from abc import ABC
from abc import abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)

        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]

        self.position = (new_x, new_y)
        self.path.append(self.position)

        return self.position
    
    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),   # up
            (0, -1),  # down
            (1, 0),   # right
            (-1, 0)  # left
        ]
    
    def level_up(self):
        self.moves.extend([
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ])
    



