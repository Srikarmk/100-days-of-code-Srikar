'''Chef wants to store some important numerical data on his personal computer. He is using a new data type that can store values only from 0 till N both inclusive. If this data type receives a value greater than N then it is cyclically converted to fit into the range 0 to N. For example:

Value N+1 will be stored as 0.
Value N+2 will be stored as 1.
and so on…

Given X, the value chef wants to store in this new data type. Determine what will be the actual value in memory after storing X.'''

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if x<=n:
        print(x)
    else:
        while x>n:
            x=x-n-1
        print(x)
