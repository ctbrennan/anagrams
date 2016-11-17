import sys
word_dict = {} #mapping of sorted_words -> tuple of words


def process(filename):
	"""
	Reads in and processes file, making each word lowercase and sorting it
	Calls add_word_to_dict with the sorted word and 

	ARG1 - filename of line separated dictionary
	RETURNS - None
	"""
	with open(filename) as f:
		for line in f:
			word = line.strip()
			sorted_word = "".join(sorted(word.lower()))
			add_word_to_dict(sorted_word, word)


def add_word_to_dict(sorted_word, word):
	"""
	Takes a sorted word and the input word. 
	If the sorted word is not yet a key in the word dictionary, adds the mapping from sorted word to word to the dictionary.
	Otherwise, pulls the tuple/word from inside in dictionary, converts it to a list, and appends the new word, and puts the new tuple back in

	ARG1 - the sorted word
	ARG2 - the original word
	RETURNS - None
	"""
	if sorted_word not in word_dict:
		word_dict[sorted_word] = tuple([word])
	else:
		word_tup = word_dict[sorted_word]
		word_list = list(word_tup)
		word_list.append(word)
		word_list = sorted(word_list)
		word_dict[sorted_word] = tuple(word_list)


def online():
	"""
	Indefinitely takes input words and prints their anagrams contained in word dict.
	Does so by sorting the word, and looking it up in the hashtable. If the sorted word is not a key in the hashtable, prints('-')
	Exits when the user hits enter (inputs empty string)

	ARGS - n/a
	RETURNS - None
	"""
	while(True):
		word = input().lower()
		if word == "":
			exit()
		sorted_word = "".join(sorted(word))
		if sorted_word not in word_dict:
			print('-')
		else:
			words = word_dict[sorted_word]
			output_str = " ".join(words)
			print(output_str)



if __name__ == "__main__":
	filename = sys.argv[1]
	process(filename)
	online()