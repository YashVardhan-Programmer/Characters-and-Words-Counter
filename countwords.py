sentence = input("Enter The Sentence: ")
characterCount = 0
wordsCount = 1

for i in sentence:
    characterCount = characterCount+1
    if i == ' ':
        wordsCount = wordsCount+1
print("No. of words in the sentence are:", wordsCount)
print("No. of characters in the sentence are:", characterCount)