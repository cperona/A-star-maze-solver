import time

import pyamaze as maze
from queue import PriorityQueue

ROWS = 20
COLS = 20

def h(cell1, cell2):
    (x1, y1) = cell1
    (x2, y2) = cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m):
    # Definim les caselles d'start i goal
    start = (1,1)
    end = (m.rows, m.cols)

    #Camí recorregut. En cada casella guardem la casella de la que procedeix
    camins = {}

    #Creem el set on guardem els gscore(cami_recorregut)
    #Omplim les seves caselles de infinits
    cami_recorregut = {}
    for cell in m.grid:
        cami_recorregut[cell] = float('inf')

    cami_recorregut[start] = 0

    #Creem la proprity queue
    pq = PriorityQueue()

    # Introduim el start al priority queue pq.put(fscore, gscore, cell)
    pq.put((0+h(start,end), start))

    #Creem el path on guardarem el path més rapid
    path = {}


    #Mentra la priority queue no estigui buida
    while not pq.empty():
        point = pq.get()
        fscore_current = point[0]
        currentCell = point[1]

        #Si hem arribat al goal, parem
        if fscore_current > cami_recorregut[end]:
            break

        #Recorrem les posicions colindants a la current cell
        for direction in 'ESNW':
            if m.maze_map[currentCell][direction]==True:
                if direction == 'E':
                    adjacentCell = (currentCell[0], currentCell[1] + 1)
                if direction == 'W':
                    adjacentCell = (currentCell[0], currentCell[1] - 1)
                if direction == 'N':
                    adjacentCell = (currentCell[0] - 1, currentCell[1])
                if direction == 'S':
                    adjacentCell = (currentCell[0] + 1, currentCell[1])

                #Si es trova un gscore (cami_recorregut) de la adjacentCell és més petit que el anterior actualitza els valors de camiRecorregut i guarda el nou cami a camins
                temp_recorregut = cami_recorregut[currentCell]+1
                if temp_recorregut < cami_recorregut[adjacentCell]:
                    cami_recorregut[adjacentCell] = temp_recorregut
                    camins[adjacentCell] = currentCell
                    pq.put((cami_recorregut[adjacentCell]+h(adjacentCell,end),adjacentCell))
    cell = end
    while cell != start:
        path[cell] = camins[cell]
        cell = camins[cell]

    print(path)
    return path

m=maze.maze(ROWS,COLS)
m.CreateMaze()
pre_Astar = time.time()
path = aStar(m)
post_Astar = time.time()
print(post_Astar - pre_Astar)
a=maze.agent(m,footprints=True)
m.tracePath({a:path},delay=5)
m.run()
