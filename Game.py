import random
import csv

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.game_count = 0
        self.terminated = False
        self.player1_wins = 0
        self.player2_wins = 0
        self.player1_cumulative = 0
        self.player2_cumulative = 0
        self.leaderBoard = dict()
        self.leaderBoard[str(self.player1)] = (self.player1_wins, self.player1_cumulative)
        self.leaderBoard[str(self.player2)] = (self.player2_wins, self.player2_cumulative)
        self.retrieveLeaderBoard()
        if str(self.player1) in self.leaderBoard:
            self.player1_wins = self.leaderBoard[str(self.player1)][0]
            self.player1_cumulative = self.leaderBoard[str(self.player1)][1]
        if str(self.player2) in self.leaderBoard:
            self.player2_wins = self.leaderBoard[str(self.player2)][0]
            self.player2_cumulative = self.leaderBoard[str(self.player2)][1]
        print(self.leaderBoard)


    def start(self):
        print("Starting Game " + str(self.game_count))
        game_over = False
        player1_score = 0
        player2_score = 0
        server = True
        serve = input("Do you want to serve first? Y/N\n")
        if serve == "N": server = False
        round = 0
        points_to_win = 11
        while not (self.terminated or game_over):
            round += 1
            if server: print("You are serving this round.")
            if not server: print("Your opponent is serving this round.")
            player1_score, player2_score = self.oneRound(player1_score, player2_score)
            choice = input("Do you wish to terminate? Y/N\n")
            if choice == "Y":
                self.terminated = True
                self.saveLeaderBoard()
                break
            if player1_score == points_to_win-1 and player2_score == points_to_win-1: points_to_win += 1
            if max(player1_score, player2_score) == points_to_win:
                game_over = True
                print("Game " + str(self.game_count) + " is over!")
                if player1_score == points_to_win:
                    print("You won this game " + str(player1_score) + ":" + str(player2_score))
                    print("Winner: " + str(self.player1))
                    self.player1_wins += 1
                    self.player1_cumulative += player1_score
                elif player2_score == points_to_win:
                    print("You lost this game " + str(player1_score) + ":" + str(player2_score))
                    print("Winner: " + str(self.player2))
                    self.player2_wins += 1
                    self.player2_cumulative += player2_score
                self.game_count += 1
                self.leaderBoard[str(self.player1)] = (self.player1_wins, self.player1_cumulative)
                self.leaderBoard[str(self.player2)] = (self.player2_wins, self.player2_cumulative)
                leaderBoard = sorted(self.leaderBoard.items(),
                                          key=lambda k:(-k[1][0], k[1][1]))
                print("LEADERBOARD")
                for item in leaderBoard:
                    print("Player: " + item[0] + ", " +
                          "Wins: " + str(item[1][0]) + ", " +
                          "Cumulative points: " + str(item[1][1]))


            if round % 2 == 0: server = not server


    def oneRound(self, player1_score, player2_score):
        winner = input("Who wins the round? "
                       + str(self.player1) + " or " + str(self.player2) + "?\nInput name: \n")
        if winner == str(self.player1):
            print("You won this round!")
            player1_score += 1
        elif winner == str(self.player2):
            print("You lost this round!")
            player2_score += 1
        print("Current score: " + str(player1_score) + ":" + str(player2_score))
        return player1_score, player2_score

    def saveLeaderBoard(self):
        with open('leaderBoard.csv', mode="w") as f_out:
            writer = csv.writer(f_out)
            writer.writerows(self.leaderBoard.items())

    def retrieveLeaderBoard(self):
        with open('leaderBoard.csv', mode="r") as f_in:
            reader = csv.reader(f_in)
            data = [row for row in reader]
            for player in data:
                self.leaderBoard[player[0]] = eval(player[1])
