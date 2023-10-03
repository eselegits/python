import random

MOVES = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        return random.choice(MOVES)

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_last_move = None

    def move(self):
        if self.my_last_move:
            index = (MOVES.index(self.my_last_move) + 1) % len(MOVES)
            return MOVES[index]
        return random.choice(MOVES)

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


class HumanPlayer(Player):
    def move(self):
        while True:
            user_input = input("Enter your move "
                               "(rock, paper, or scissors): ").lower()
            if user_input in MOVES:
                return user_input
            else:
                print("Invalid input. Please enter rock, paper, or scissors.")


def determine_winner(move1, move2):
    if move1 == move2:
        return 0
    if (
        (move1 == 'rock' and move2 == 'scissors') or
        (move1 == 'scissors' and move2 == 'paper') or
        (move1 == 'paper' and move2 == 'rock')
    ):
        return 1
    return 2


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rounds = 3
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        winner = determine_winner(move1, move2)

        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("Player 1 wins this round!")
            self.p1_score += 1
        else:
            print("Player 2 wins this round!")
            self.p2_score += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(self.rounds):
            print(f"Round {round + 1}:")
            self.play_round()

            if self.p1_score >= 2 or self.p2_score >= 2:
                break

        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        else:
            print("It's a draw!")


if __name__ == '__main__':
    player1 = HumanPlayer()
    player2 = RandomPlayer()
    game = Game(player1, player2)
    game.play_game()
