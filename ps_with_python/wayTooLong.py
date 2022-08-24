# Way Too Long Words
# n words
#Let's consider a word too long, if its length is strictly more than 10 characters.
numOfWords = int(input())
words = []
output = []
for i in range(numOfWords):
   word = str(input())
   words.append(word)

output = [w if len(w)<=10 else (w[0]+str(len(w)-2)+w[len(w)-1]) for w in words]

#print(output[0])
for j in range(numOfWords):
   print(output[j])
