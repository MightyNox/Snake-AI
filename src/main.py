import argparse

from game.Game import Game

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--game_mode', dest='game_mode', type=str, default='user', help="'bot' or 'user'")
    parser.add_argument('--latency', dest='latency', type=int, default=100, help='Latency of the snake')
    args = parser.parse_args()

    game_mode= args.game_mode
    latency = args.latency
    game = Game(game_mode, latency)

    game.start()
