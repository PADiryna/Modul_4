word = "oko"
def palindrome(word):
  '''takes one argument (string type) 
  and returns a boolean value: True/False 
  indicating whether the given text is a palindrome,
  by comparing the indexes of the beginning and end of the string 
  in the range of half the string'''
  letters = len(word)//2
  for letter in range(letters):
    if word[letter] != word[-letter - 1]:
      return False
  return True   
print(f"{word} is palindrome" if palindrome(word) else "{word} is not palindrome") 



word = "oko"
def palindrome(word):
  '''takes one argument (string type) 
  and returns a boolean value: True/False 
  indicating whether the given text is a palindrome,
  by comparing the original string with the reversed'''
  if word == word [::-1]:
    return True
  return False
print(f"{word} is palindrome" if palindrome(word) else "{word} is not palindrome")  