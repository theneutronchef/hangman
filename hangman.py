import math
import random

f = open("words.txt", "r")

word_dict = []

for line in f:
	word_dict.append(line)

# word_dict = ["word", "hello", "gghaha"]

def check_word(word_list, letter):
	l = []
	while letter in word_list:
		index = word_list.index(letter)
		l.append(index)
		word_list[index] = '-'
	return l

def blanks(word):
	l = []
	for i in range(len(word)):
		l.append('_')
	return l

def run():
	running = True
	index = math.floor(len(word_dict) * random.random())
	word = word_dict[index]
	orig_list = list(word)
	curr_list = blanks(word)
	lives = 10
	print("Number of lives: " + str(lives))
	while running:	
		print(curr_list)
		letter = input("Input letter: ")
		indices = check_word(orig_list, letter)
		if len(indices) == 0:
			lives = lives - 1
			print(letter + " does not exist")
			print("Lives remaining: " + str(lives))
		else:
			for i in indices:
				curr_list[i] = letter
		if '_' not in curr_list:
			running = False
			print("You win!")
		elif lives == 0:
			running = False
			print("You ran out of lives!")
			print("Answer: " + word)

run()