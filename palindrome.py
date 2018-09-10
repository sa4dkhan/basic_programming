string = str(input("Enter the word: "))

string = string.casefold()

rev_string = reversed(string)

print(list(rev_string))

if list(string) == list(rev_string):
	print("It is palindrome")
else:
	print("It is not palindrome")