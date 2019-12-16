"""
Pyg Latin
Remove first letter of any word
Add letter to end of word
Lastly add 'ay' to the end of the letter
that was appended to end of word

Example: Pancake = ancakepay, telephone = elephonetay
"""

#declare variable with ending of pyg latin word
pyg = 'ay' 

#retrieve word from user to be converted
users_word = input("Please enter a word to be translated to pyg latin: ")

#slice off first letter
single_letter = users_word[0] 

#keep all letters except for first
new_word = users_word[1:len(users_word)] 

#concatenate all strings together
pyg_word = new_word + single_letter + pyg 

print(pyg_word)
