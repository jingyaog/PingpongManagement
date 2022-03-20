import Game
import Player


if __name__ == '__main__':
    player1 = Player.Player(1)
    player2 = Player.Player(2)
    game_management = Game.Game(player1, player2)
    while not game_management.terminated:
        game_management.start()



