
# A A A B B B A B A B

# A B B B

def check_winner(colors:str)->bool:
    a,b,i=0,0,0
    while i<len(colors):
        j,count=i,0
        while j<len(colors) and colors[j]==colors[i]:
            count+=1
            j+=1
        if count>=3:
            if colors[i]=='A':
                a+=(count-2)
            else:
                b+=(count-2)
        i=j

    return a>b

print(check_winner("AAABAAB"))
        
        
        