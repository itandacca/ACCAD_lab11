words = []
lenght = []

for user in range(10):
    x = input("Enter a word:")
    words.append(x)
    
    if any(char.isdigit() for char in x):
        print("Error. Please enter a valid word.")
    
while True:
    letters = input("Enter the number of letters:")
    if letters.isdigit():
        letters = int(letters)
        break
    
for word in words:
 #more than
    if len(word) >= letters:
        lenght.append(word)
    
    else:
        continue
    
print(f"\nHere are the words that have {letters} letters: {lenght}")





