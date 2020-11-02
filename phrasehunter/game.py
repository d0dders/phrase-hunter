from phrasehunter.phrase import Phrase
import random

class Game:

    STARTING_LIVES = 5

    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('A New Hope'),
                        Phrase('The Empire Strikes Back'),
                        Phrase('Return of the Jedi'),
                        Phrase('The Force Awakens'),
                        Phrase('The Last Jedi')]
        self.active_phrase = None
        #guesses contains space to simply win checking
        self.guesses = [' ']
    
    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        #print(self.active_phrase)
        still_playing = True
        while still_playing:
            self.active_phrase.display(self.guesses)
            self.get_guess()
            if self.active_phrase.check_complete(self.guesses) == True:
                still_playing = False
                self.game_over('win')
            elif self.missed >= self.STARTING_LIVES:
                still_playing = False
                self.game_over('lose')

    def get_random_phrase(self):
        return self.phrases[random.randint(0, 4)]

    def welcome(self):
        """ Prints a short welcome message to console        
        """
        print("""
  ___| |_ __ _ _ __  __      ____ _ _ __ ___ 
 / __| __/ _` | '__| \ \ /\ / / _` | '__/ __|
 \__ \ || (_| | |     \ V  V / (_| | |  \__ \\
 |___/\__\__,_|_|      \_/\_/ \__,_|_|  |___/
        """)
        print("           Welcome to PHRASEHUNTER")
        print("\nGuess the Star Wars movie title...")

    def get_guess(self):
        valid_guess = False
        while valid_guess == False:
            try:
                guess = input("\nGuess a letter:  ")
                if len(guess) > 1:
                    raise ValueError("You can only guess one letter at a time")
                elif guess < 'a' or guess > 'z':
                    raise ValueError("You must only make alphabet guesses (a-z)")
            except ValueError as err:
                print(err)
            else:
                valid_guess = True

        self.guesses.append(guess)
        if not self.active_phrase.check_letter(guess):
            self.missed += 1
            print(f"\nYou have {self.STARTING_LIVES - self.missed} out of {self.STARTING_LIVES} lives remaining!")
        
    def game_over(self, win_or_lose):
        if win_or_lose == 'win':
            print("\nCongratulations, you won! The force is strong in you!\n")
        else:
            print("\nLost you did. More trainng you will need.\n")