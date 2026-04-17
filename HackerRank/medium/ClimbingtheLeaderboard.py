def climbingLeaderboard(ranked,player):
    leaderBoard = sorted(set(ranked),reverse=True)
    result = []
    length = len(leaderBoard) - 1
    for score in player:
        while length >= 0 and score >= leaderBoard[length]:
            length -= 1
        result.append(length+1)
    return result
print(climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120]))



#  n = leaderBoard.index(min(leaderBoard))+1
#     for score in player:
#         for rank in leaderBoard:
#             if score < min(leaderBoard):
#                 result.append(n+1)
#                 break
#             elif score >= rank:
#                 result.append(leaderBoard.index(rank)+1)
#                 break     
#         n += 1
