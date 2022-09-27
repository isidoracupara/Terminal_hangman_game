import random
from typing import List

possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'device','rocket', 'science','Online', 'piracy','Reinstall', 'programs',
        'search', 'engine','Social', 'media', 'networks', 'technology','Surfing', 'web','click', 'icon','crash','Log','upgrade', 'computer', 'system',
        'Wireless', 'hotspots','Access', 'Internet','Advances','Backup', 'files','rapidly', 'obsolete','literate','Control', 'remotely','Downloading',
        'Electronic', 'Transfer','Emerging', 'technology','screen','Hacking', 'network','access','copy']


class Hangman:
    """A class that will play the hangman game."""

    
    def __init__(self):
        """Method that creates object from class, defines variables.
        self.word_to_find: random string from the list that we will work with and try to guess.
        self.word_letters: string that stores letters from self.word_to_find and check how many letters are left.
        self.well_guessed_letters: list of strings to which correct user inputs (guesses) will be added .
        self.wrongly_guessed_letters: list of strings to which valid but incorrect user inputs (guesses) will be added.
        self.turn_count: an int to which 1 is added every time the user inputs.
        self.lives: an int from which 1 is subtracted every time the user input is incorrect."""
        self.word_to_find: str = random.choice(possible_words).upper()
        self.word_letters: List[str] = list(self.word_to_find) #letters in the word
        self.well_guessed_letters: List[str] = [] #right guess
        self.wrongly_guessed_letters: List [str] = [] #wrong guess
        self.turn_count: int = 0
        self.lives: int = 5


    def play(self):
        """Method that plays the hangman game, calculates wrong or right guess."""
        #checking remaining letters and lives
        while len(self.word_letters) > 0 and self.lives > 0:
            print("You have used these (wrong) letters: ", " ".join(self.wrongly_guessed_letters)) #displaying wrong letters
            print("Remaining lives: " + str(self.lives))

            #revealed letters in the word
            word_preview: List[str] = [letter if letter in self.well_guessed_letters else '_' for letter in self.word_to_find] #calculates guessed letter or -
            print("Your word currently: ", " ".join(word_preview) + "\n") #displays word with revealed letters and -

            #getting user input
            print("This is a game of hangman. Please input a letter.")
            user_letter: str = input("Guess a letter: ").upper()

            #calculation for valid input
            if len(user_letter) == 1 and user_letter.isalpha(): #checking if input is 1 long and a string
                self.turn_count += 1
                if user_letter in self.word_letters:
                    # self.word_letters = list(filter(lambda letter:letter != user_letter, self.word_letters))
                    self.word_letters: List[str] = [letter for letter in self.word_letters if letter != user_letter]
                    self.well_guessed_letters.append(user_letter)
                
                #if already guessed
                elif user_letter in self.well_guessed_letters or user_letter in self.wrongly_guessed_letters:
                    print("You have already guessed that letter. Please input a different letter!\n")
                else:
                    self.wrongly_guessed_letters.append(user_letter)
                    self.lives -= 1
            
            #message for invalid input
            else:
                print("Invalid character. Please type in one letter.\n")
    
    def game_over(self):
        
        print("\n*GAME OVER*\n")
        
    def well_played(self):
        print (f"\n*CONGRATS!* You found the word: {self.word_to_find} in {self.turn_count} turns with {self.lives} lives left!\n")

    def start_game(self):
        """Method that starts or ends the game."""
        self.play()

        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()
            
            

hangman = Hangman()
hangman.start_game()