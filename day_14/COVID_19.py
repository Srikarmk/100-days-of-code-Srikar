'''
Mr. Chef is the manager of the Code cinemas and after a long break, the theatres are now open to the public again. To compensate for the loss in revenue due to Covid-19, Mr. Chef wants to maximize the profits for every show from now on and at the same time follow the guidelines set the by government. The guidelines are:

If two people are seated in the same row, there must be at least one empty seat between them.
If two people are seated in different rows, there must be at least one completely empty row between them. That is, if there are people seated in rows i and j where i<j, there must be some row k such that i<k<j and nobody is seated in row k.
Given the information about the number of rows and the number of seats in each row, find the maximum number of tickets Mr. Chef can sell.

'''
t=int(input())
for i in range(t):
    r,s=map(int,input().split())
    if r%2==0:
        nr=r/2
        if s%2==0:
            ns=s/2
        else:
            ns=int(s/2)+1
    else:
        nr=int(r/2)+1
        if s%2==0:
            ns=s/2
        else:
            ns=int(s/2)+1
    print(int(ns*nr))