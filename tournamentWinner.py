"""
time complexity o(n), space complexity o(n) for dict
input=[['python','C#'],['C#','Java'],['python,Java']], result=[1,0,1] 
python => 6 pts
Java => 3 pts
C# => 0 pts
output=> python
1- loop to add all teams to hashtable
2-loop on result array to add point to the teams 
3-loop on the hashtable to return the teams with max points

"""
def getWinner(competitions,result):
    resulttable={}
    for item in competitions:
        if item[0] not in resulttable:
            resulttable[item[0]]=0
        if item[1] not in resulttable:
            resulttable[item[1]]=0
    
    for i in range(0,len(result)):
        if (result[i]==1):
            resulttable[competitions[result[i]][1]]= resulttable[competitions[result[i]][1]]+3
        if (result[i]==0):
            resulttable[competitions[result[i]][0]]= resulttable[competitions[result[i]][0]]+3

    winnerTeam=''
    maxPoints=0
    for item in resulttable:
        if resulttable[item]>maxPoints:
            maxPoints=resulttable[item]
            winnerTeam=item
    
    return winnerTeam




print(getWinner([['python','C#'],['C#','Java'],['python','Java']],[1,0,1]))

