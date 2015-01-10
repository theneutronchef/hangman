import math
import random

f = open("words.txt", "r")
chars = []
for i in range(8):
	chars.append(" ")
chars_lib = ["|", "0", "| |", "/", "\\", "A", "/", "\\"]

def create_image():
	return """
 _______
|   """ + chars[0] + """
|   """ + chars[1] + """
| """ + chars[3] + chars[2] + chars[4] + """
|   """ + chars[5] + """
|  """ + chars[6] + " " + chars[7] + """ 
|
|_______
""" 

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
	for i in range(len(word)-1):
		l.append('_ ')
	return l

def run():
	running = True
	index = int(math.floor(len(word_dict) * random.random()))
	word = word_dict[index]
	orig_list = list(word)
	curr_list = blanks(word)
	count = 0
	while running:	
		print("".join(curr_list))
		letter = input("Input letter: ")
		indices = check_word(orig_list, letter)
		if len(indices) == 0:
			chars[count] = chars_lib[count]
			count = count + 1
			print(letter + " does not exist")
			print(create_image())
		else:
			for i in indices:
				curr_list[i] = letter + " "
		if '_ ' not in curr_list:
			running = False
			print("You win!")
		elif count == 8:
			running = False
			print("You died!")
			print("Answer: " + word)

run()