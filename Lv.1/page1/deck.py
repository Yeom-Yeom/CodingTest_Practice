def deck(cards1, cards2, goal):
    answer = "Yes"

    card1_idx, card2_idx = 0,0

    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx+=1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx+=1
        else:
            answer="No"
            break
    return answer

# another solution
# def solution(cards1, cards2, goal):
#   for g in goal:
#       if len(card1)>0 and g==cards1[0]:
#           cards1.pop(0)
#       elif len(card2)>0 and g==cards2[0]:
#           cards2.pop(0)
#       else:
#           return "No"
#   return "Yes"