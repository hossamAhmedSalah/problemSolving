# n participants
# k arrangment

n, k = [int(x) for x in input().split()]
scores = []
scores = [int(y) for y in input().split()]


toNextRound = [score for score in scores if score>=scores[k-1] and score>0]
print(len(toNextRound))

#k is not a score
