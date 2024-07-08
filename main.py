import random

class Game:
    def __init__(self):
        self.first_dice = 0
        self.second_dice = 0
        self.curr_sum = 0
        self.goal_sum = 0

    def roll_dice(self):
        print('Rolling the dice...', flush=True)
        self.first_dice = random.randint(1,6)
        self.second_dice = random.randint(1,6)
        self.curr_sum = self.first_dice +  self.second_dice
        print(f'The sum is {self.first_dice} + {self.second_dice} = {self.curr_sum}')
    
    def set_goal(self):
        print(f'Setting {self.curr_sum} as a goal', flush=True)
        self.goal_sum = self.curr_sum

    def is_win(self):
        if self.curr_sum in [7, 11]:
            return True
        return False
    
    def is_lose(self):
        if self.curr_sum in [2, 3, 12]:
            return True
        return False
    
    def start_game(self):
        self.roll_dice()
        if self.is_win():
            print('Apres, you won!', flush=True)
        elif self.is_lose():
            print('Craps, you lost', flush=True)
        else:
            self.set_goal()
            while True:
                self.roll_dice()
                if self.curr_sum == 7:
                    print('Craps, you lost', flush=True)
                    break
                elif self.curr_sum == self.goal_sum:
                    print('Apres, you won!', flush=True)
                    break

game_obj = Game()
game_obj.start_game()