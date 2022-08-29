officer, untreated = 0, 0
n = int(input())
events = [int(x) for x in input().split()]


'''
av_officers = 0
untreated = 0
event happens:
      is it a crime or recuit an officer? 
          if it is a crime and we do not have offices
              so it's untreated ++
          else if it's a crime and we have officers
              each officer can solve one case in his life
              officers who would work in this case would be busy
              and not available 
              so:
              officers = officers - crimes
              
'''
for i in range(len(events)):
    if events[i] < 0 and officer <= 0:
        untreated += abs(events[i])
    elif events[i] < 0 and officer > 0:
        officer -= abs(events[i])
    elif events[i] > 0:
        officer += abs(events[i])

print(untreated)



