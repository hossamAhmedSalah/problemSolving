n = int(input())
ser,dim = 0,0
cards = [int(x) for x in input().split()]

for i in range(len(cards)):
    if i%2 == 0:
        if cards[0] > cards[len(cards) - 1]:
            ser += cards[0]
            cards.remove(cards[0])
        else:
            ser += cards[len(cards) - 1]
            cards.remove(cards[len(cards)-1])


    else:
        if cards[0] > cards[len(cards) - 1]:
            dim += cards[0]
            cards.remove(cards[0])
        else:
            dim += cards[len(cards) - 1]
            cards.remove(cards[len(cards) - 1])


print(ser, dim, end=' ')
