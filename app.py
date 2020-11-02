from phrasehunter.game import Game

if __name__ == "__main__":
    choice = 'y'
    while choice == 'y':
        game = Game()
        game.start()
        choice = input("Would you like to play again? (y / n)").lower()
    input("Thanks for playing!! Press ENTER to exit...")
