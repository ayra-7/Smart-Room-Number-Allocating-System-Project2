#************************** SMART ROOM NUMBER ALLOCATING SYSTEM **************************
'''
Q.A building has 5 floors. Each 20 rooms. You have to assign the room numbers as per given rule:

1. If user ask for floor one room number must be 101, 102, 103----- (except 113)
2.if user ask for floor 5 room number must be 501, 502, 503----- (except 513)

'''

print("Enter 1 for first floor")
print("Enter 2 for second floor")
print("Enter 3 for third floor")
print("Enter 4 for fourth floor")
print("Enter 5 for fifth floor")
i1=0
i2=0
i3=0
i4=0
i5=0
while(i1==0 or i2==0 or i3==0 or i4==0 or i5==0):
    print("\nEnter floor no.")
    ch=int(input())
    if(ch==1):
        i1+=1
        ch=ch*100+1
        while(ch<=121):
            print(ch,end=" ")
            ch+=1
            if(ch==113):
                ch+=1
    elif(ch==2):
        i2+=1
        ch=ch*100+1
        while(ch<=221):
            print(ch,end=" ")
            ch+=1
            if(ch==213):
                ch+=1
    elif(ch==3):
        i3+=1
        ch=ch*100+1
        while(ch<=321):
            print(ch,end=" ")
            ch+=1
            if(ch==313):
                ch+=1
    elif(ch==4):
        i4+=1
        ch=ch*100+1
        while(ch<=421):
            print(ch,end=" ")
            ch+=1
            if(ch==413):
                ch+=1
    elif(ch==5):
        i5+=1
        ch=ch*100+1
        while(ch<=521):
            print(ch,end=" ")
            ch+=1
            if(ch==513):
                ch+=1
    else:
        print("Enter correct floor no.")

