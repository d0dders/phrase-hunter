class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __str__(self):
        return self.phrase
    
    def display(self, guesses):
        """Takes a list of the guessed letters.
        Displays phrase to console showing corrctly guessed letters
        """
        display_string_list = []
        for character in self.phrase:
            if character == ' ':
                display_string_list.append(character)
            elif character >= 'a' and character <= 'z':
                if character in guesses:
                    display_string_list.append(character)
                else:
                    display_string_list.append('_')
        display_string = ' '.join(display_string_list)
        print("\n" + display_string)

    def check_letter(self, letter):
        if letter in self.phrase:
            return True

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
