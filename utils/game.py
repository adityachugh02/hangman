import random
from typing import List, Union

class Hangman:
	"""
	Hangman class containing start_game(), play(), game_over(), well_played() methods
	"""
	def __init__(self):
		self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
		self.word_to_find: List[str] = []
		self.lives: int = 5
		self.correctly_guessed_letters: List[str] = []
		self.wrongly_guessed_letters: List[str] = []
		self.turn_count: int = 0
		self.error_count: int = 0

		random.shuffle(self.possible_words)	#randomize word list
		self.word_to_find = self.possible_words[0] #take the first random word from the list

		for letter in self.word_to_find:			   #for every letter in word_to_find
			self.correctly_guessed_letters.append("_") #add one _ to correctly_guessed_letters for every letter 

	def start_game(self):
		"""
		Will call play() until the game is over (because the use guessed the word or because of a game over).
		Will call game_over() if lives is equal to 0.
		Will call well_played() if all the letter are guessed.
		Will print well_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn.
		"""
		while ("_" in self.correctly_guessed_letters) and (self.lives != 0): #do while there are still _ in correctly_guessed_letters
			self.play()														 #and while lives are still left
			print(f"Correctly guessed letters: {self.correctly_guessed_letters}")
			print(f"Wrongly guessed letters: {self.wrongly_guessed_letters}")
			print(f"Lives: {self.lives}, Errors: {self.error_count}, Turn: {self.turn_count}")
			print()

		if self.lives == 0: #game over when no lives are left
			self.game_over()
		if list(self.word_to_find) == self.correctly_guessed_letters: #if word to find is equal to correcly guessed letters
			self.well_played()
		
	
	def play(self):
		"""
		Method that asks the player to enter a letter. 
		Player is not allowed to type something else than a letter, and not more than a letter. 
		If the player guessed a letter well, add it to the well_guessed_letters list. 
		If not, add it to the wrongly_guessed_letters list and add 1 to error_count
		"""
		buffer = input("Enter a letter:")
		if buffer.isalpha() == True and len(buffer) == 1 and buffer not in self.correctly_guessed_letters and buffer not in self.wrongly_guessed_letters: 
		#check if input is alpha, length is 1, is not in correctly/ wrongly guessed letters
			self.turn_count += 1																		   
			if buffer in self.word_to_find: #if input letter is in word to find
				for i in range(len(list(self.word_to_find))): #for the index of every letter in word to find
					if list(self.word_to_find)[i] == buffer: # check if the letter of index i in words to find is equal to input letter
						self.correctly_guessed_letters[i] = buffer #if yes write the letter in the same position i in correctly_guessed_letters
			else:
				self.error_count += 1
				self.lives -= 1
				self.wrongly_guessed_letters.append(buffer) #if input letter not in word to find, add input to wrongly guessed letters
		else:
			print("Err not letter or already entered")

	def game_over(self):
		"""
		Method that will stop the game and print game over...
		"""
		print("Game over...")

	def well_played(self):
		"""
		Method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!
		"""
		print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")


	
		
