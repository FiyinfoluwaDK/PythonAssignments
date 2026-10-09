def word_length(word):
	return len(word)
	
def word_first_last_two_letters(word):
	if len(word) < 2: 	
		return ""
	else:
		return word[0] + word[1] + word[-2] + word[-1]
	
def word_add_ing(word):
	if len(word) > 2:
		if word[-3] == "i" and word[-2] == "n" and word[-1] == "g":
			return word + "ly"
		else:
			return word + "ing"
	else:
		return word
		
def largest_word_in_list(words):
	largest = len(words[0])
	largest_word = words[0]
	for count in words:
		if len(count) > largest:
			largest = len(count)
			largest_word = count
	return largest_word, largest
			
def odd_index(word):
	odd_letters = []
	for count in range(len(word)):
		if count % 2 != 0:
			odd_letters.append(word[count])
	return odd_letters
	
def smallest_number(numbers):
	smallest = numbers[0]
	for count in numbers:
		if count < smallest:
			smallest = count
	return smallest
	
def largest_number(numbers):
	largest = numbers[0]
	for count in numbers:
		if count > largest:
			largest = count
	return largest
	
def repeated_words(word, number):
	if word.isalpha() and str(number).isdigit():
		return word * int(number)
	else:
		return word
		
def squared_list(numbers):
	square = []
	for count in numbers:
		square.append(count * count)
	return square
	
def squared_list_sum(numbers):
	total = 0
	for count in numbers:
		total += count * count
	return total

numbers = [2,4,6,8,10]	
number = 5
word = "concatination"
games = ["Farcry","Palsworld","Minecraft","Skyrim","Crysis"] 	


print(word_length(word))
print(word_first_last_two_letters(word))
print(word_add_ing(word))
print(largest_word_in_list(games))
print(odd_index(word))
print(smallest_number(numbers))
print(largest_number(numbers))
print(repeated_words(word,number))
print(squared_list(numbers))
print(squared_list_sum(numbers))		
		
		
		
		
		
		
		
