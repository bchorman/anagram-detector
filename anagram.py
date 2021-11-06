def LoadDict():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letterDict = {}
  for letter in alphabet:
    letterDict.update({letter: 0})
  return letterDict

userWord1 = input("Type a word: ")
userWord2 = input("Type another word: ")
print("\nYour words are", userWord1, "and", userWord2, "\n")

word1 = userWord1.lower().replace(" ", "")
word2 = userWord2.lower().replace(" ", "")

letterDict = LoadDict()

for letter in word1:
  count = letterDict.get(letter)
  letterDict.update({letter: count+1})

for letter in word2:
  count = letterDict.get(letter)
  letterDict.update({letter: count-1})

allCounts = letterDict.values();
areAnagrams = True

for num in allCounts:
  if num != 0:
    areAnagrams = False

if areAnagrams:
  print(userWord1, "and", userWord2, "are anagrams\n")
else:
  print(userWord1, "and", userWord2, "are not anagrams\n")
