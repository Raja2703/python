num=input('Enter a number:')
lst=['one','two','three','four','five','six','seven']

for i in range(len(lst)):
    count=0
    if(len(lst[i]) == len(num)):
        
        for j in range(len(num)):
            
            if(num[j] == lst[i][j]):
                count=count+1
            
            if(count>=len(num)-1):
                print('Correct answer is ',lst[i])
                break
