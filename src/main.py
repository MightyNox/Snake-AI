from game.Game import Game
from ai import Model

if __name__ == "__main__":
    game = Game("bot", 1)
    model = Model()
    model.create_neural_network_model()

    ''' 3 modes user/bot/ai '''
    #game.start()
