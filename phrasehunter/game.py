from phrasehunter.phrase import Phrase
import random

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('A New Hope'),
                        Phrase('The Empire Strikes Back'),
                        Phrase('Return of the Jedi'),
                        Phrase('The Force Awakens'),
                        Phrase('The Last of the Jedi')]
        self.active_phrase = None
        self.guesses = []
    
    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        print(self.active_phrase)
        #get_guess()
        #process guess

    def get_random_phrase(self):
        return self.phrases[random.randint(0, 4)]

    def welcome(self):
        """ Prints a short welcome message to console        
        """
        print("Welcome to PHRASEHUNTER")