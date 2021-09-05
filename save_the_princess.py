#!/usr/bin/python

def displayPathtoPrincess(n, grid, mcol, mrow, pcol, prow):
    row_change = prow - mrow
    col_change = pcol - mcol
    printer(row_change, 'LEFT', 'RIGHT')
    printer(col_change, 'UP', 'DOWN')


def printer(change, neg, pos):
    if change < 0:
        for _ in range(abs(change)):
            print(neg)
    else:
        for _ in range(change):
            print(pos)


m = int(input())
grid = []
count = 0
mcol = 0
mrow = 0
pcol = 0
prow = 0
for i in range(0, m):
    elements = input().strip()
    if 'm' in elements:
        mcol = count
        mrow = elements.index('m')

    if 'p' in elements:
        pcol = count
        prow = elements.index('p')

    grid.append(elements)
    count += 1



displayPathtoPrincess(m,grid, mcol, mrow, pcol, prow)
