#!/usr/bin/env

A=[[5,0],[0,1],[3,0]]
B=[[4,3],[3,4],[6,3]]
data=[]
for i1 in range(3):
    for i2 in range(3):
        for j1 in range(2):
            for j2 in range(2):
                data.append([A[i1][j1]+A[i2][j2],B[i1][j1]+B[i2][j2]])
p=list_plot(data,axes_labels=['Player 1','Player 2'],size=30)
p.save("HW3-P02.png")
