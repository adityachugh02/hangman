import random

class Hangman():
	"""
	Hangman class containing start_game(), play(), game_over(), well_played() methods
	"""
	possible_words = ['becode', 'learning', 'mathematics', 'sessions']
	word_to_find = []
	lives = 5
	correctly_guessed_letters = []
	wrongly_guessed_letters = []
	turn_count = 0
	error_count = 0

	random.shuffle(possible_words)
	word_to_find = possible_words[0]

	for letter in word_to_find:
		correctly_guessed_letters.append("_")

	def start_game():
		"""
		will call play() until the game is over (because the use guessed the word or because of a game over).
		will call game_over() if lives is equal to 0.
		will call well_played() if all the letter are guessed.
		will print well_guessed_letters, bad_guessed_letters, life, error_count and turn_count at the end of each turn.
		"""
		while ("_" in Hangman.correctly_guessed_letters) and (Hangman.lives != 0):
			Hangman.play()
			print(f"Correctly guessed letters: {Hangman.correctly_guessed_letters}")
			print(f"Wrongly guessed letters: {Hangman.wrongly_guessed_letters}")
			print(f"Lives: {Hangman.lives}, Errors: {Hangman.error_count}, Turn: {Hangman.turn_count}")
			print()

		if Hangman.lives == 0:
			Hangman.game_over()
		if sorted(list(Hangman.word_to_find)) == sorted(Hangman.correctly_guessed_letters):
			Hangman.well_played()
		
	
	def play():
		"""
		method that asks the player to enter a letter. 
		Player is not allowed to type something else than a letter, and not more than a letter. 
		If the player guessed a letter well, add it to the well_guessed_letters list. 
		If not, add it to the wrongly_guessed_letters list and add 1 to error_count
		"""
		buffer = input("Enter a letter:")
		if buffer.isalpha() == True and len(buffer) == 1 and buffer not in Hangman.correctly_guessed_letters:
			Hangman.turn_count += 1
			if buffer in Hangman.word_to_find:
				for i in range(len(list(Hangman.word_to_find))):
					if list(Hangman.word_to_find)[i] == buffer:
						Hangman.correctly_guessed_letters[i] = buffer
			else:
				Hangman.error_count += 1
				Hangman.lives -= 1
				Hangman.wrongly_guessed_letters.append(buffer)
		else:
			print("Err not letter or already entered")

	def game_over():
		"""
		method that will stop the game and print game over...
		"""
		print("Game over...")
		return 0

	def well_played():
		"""
		method that will print You found the word: {word_to_find_here} in {turn_count_here} turns with {error_count_here} errors!
		"""
		print(f"You found the word: {Hangman.word_to_find} in {Hangman.turn_count} turns with {Hangman.error_count} errors!")


	
		
