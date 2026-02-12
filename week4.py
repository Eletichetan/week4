
import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x = (val-1)//3
                goal_y = (val-1)%3
                distance += abs(i-goal_x) + abs(j-goal_y)
    return distance

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def a_star(start):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    parent = {}
    g_cost = {state_to_tuple(start): 0}

    while pq:
        _, current = heapq.heappop(pq)
        current_t = state_to_tuple(current)

        if current == goal:
            path = []
            while current_t in parent:
                path.append(current)
                current = parent[current_t]
                current_t = state_to_tuple(current)
            path.append(start)
            return path[::-1]

        visited.add(current_t)
        x,y = find_zero(current)

        for dx,dy in moves:
            nx,ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                new_state = [row[:] for row in current]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_t = state_to_tuple(new_state)

                if new_t in visited:
                    continue

                new_g = g_cost[current_t] + 1
                g_cost[new_t] = new_g
                f = new_g + manhattan(new_state)

                heapq.heappush(pq, (f, new_state))
                parent[new_t] = current

    return None

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

solution = a_star(start)

for step in solution:
    for row in step:
        print(row)
    print()
