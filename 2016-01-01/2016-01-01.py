'''
https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

Description: 
You were hired to create words for a new language. However, your boss wants these words to follow a strict pattern of consonants and vowels. You are bad at creating words by yourself, so you decide it would be best to randomly generate them.
Your task is to create a program that generates a random word given a pattern of consonants (c) and vowels (v).

Input Description:
Any string of the letters c and v, uppercase or lowercase.

Output Description:
A random lowercase string of letters in which consonants (bcdfghjklmnpqrstvwxyz) occupy the given 'c' indices and vowels (aeiou) occupy the given 'v' indices.

Sample Inputs:
cvcvcc
CcvV
cvcvcvcvcvcvcvcvcvcv

Sample Outputs:
litunn
ytie
poxuyusovevivikutire

Bonus:
Error handling: make your program react when a user inputs a pattern that doesn't consist of only c's and v's.
When the user inputs a capital C or V, capitalize the letter in that index of the output.
'''

import random
import sys

letters = {
	'c': 'bcdfghjklmnpqrstvwxyz',
	'v': 'aeiou'
}

def validate(pattern):
	for char in pattern:
		if char not in ['c', 'v', 'C', 'V']:
			return False
	return True

def replace(char):
	new_char = random.choice(letters.get(char.lower(), char))
	return new_char if char.islower() else new_char.upper()
	
if __name__ == '__main__':
	pattern = sys.argv[1]
	if validate(pattern):
		print(''.join(replace(char) for char in pattern))
	else:
		print('Invalid input. Pattern must consist only of \'c\', \'v\', \'C\', or \'V\'.')