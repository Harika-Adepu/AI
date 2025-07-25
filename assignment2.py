class State:
    def __init__(self, umbrella, Amogh, Ameya, grandmother, grandfather, total_time=0):
        self.umbrella = umbrella 
        self.Amogh = Amogh
        self.Ameya = Ameya
        self.grandmother = grandmother
        self.grandfather = grandfather
        self.total_time = total_time
        
    def goalTest(self):
        return self.umbrella == self.Amogh == self.Ameya == self.grandmother == self.grandfather == 'R'
    
    def moveGen(self):
        children = []
        people = ['Amogh', 'Ameya', 'grandmother', 'grandfather']
        positions = {
            'Amogh': self.Amogh,
            'Ameya': self.Ameya,
            'grandmother': self.grandmother,
            'grandfather': self.grandfather
        }
        times = {
            'Amogh': 5,
            'Ameya': 10,
            'grandmother': 20,
            'grandfather': 25
        }
        current_side = self.umbrella
        new_side = 'R' if current_side == 'L' else 'L' 

        if current_side == 'L':
            for i in range(4):
                for j in range(i + 1, 4):
                    p1, p2 = people[i], people[j]
                    if positions[p1] == positions[p2] == 'L':
                        new_pos = positions.copy()
                        new_pos[p1] = 'R'
                        new_pos[p2] = 'R'
                        new_time = self.total_time + max(times[p1], times[p2])
                        if new_time <= 60:
                            children.append(State(new_side, new_pos['Amogh'], new_pos['Ameya'], new_pos['grandmother'], new_pos['grandfather'], new_time))

        else:
            for i in range(4):
                p = people[i]
                if positions[p] == 'R':
                    new_pos = positions.copy()
                    new_pos[p] = 'L'
                    new_time = self.total_time + times[p]
                    if new_time <= 60:
                        children.append(State(new_side, new_pos['Amogh'], new_pos['Ameya'], new_pos['grandmother'], new_pos['grandfather'], new_time))

        return children
                
    def __repr__(self):
        return f"(umbrella: {self.umbrella}) (Amogh: {self.Amogh}), (Ameya: {self.Ameya}), (grandmother: {self.grandmother}), (grandfather: {self.grandfather}), Total Time: {self.total_time}\n"
    
    def __hash__(self):
        return hash((self.umbrella, self.Amogh, self.Ameya, self.grandmother, self.grandfather))
    
    def __eq__(self, other):
        return (self.umbrella, self.Amogh, self.Ameya, self.grandmother, self.grandfather) == \
               (other.umbrella, other.Amogh, other.Ameya, other.grandmother, other.grandfather)


def printResult(current_state, visited, result):
    if current_state.total_time > 60:
        return None
    if current_state.goalTest():
        return result + [str(current_state)]
    visited.add(current_state)
    for child in current_state.moveGen():
        if child not in visited:
            path = printResult(child, visited, result + [str(current_state)])
            if path:
                return path
    return None 


def dfs(state, visited, path):
    if state.total_time > 60:
        return False
    if state in visited:
        return False
    visited.add(state)
    path.append(state)

    if state.goalTest():
        return True

    for child in state.moveGen():
        if dfs(child, visited, path):
            return True

    path.pop()
    return False


def removeSeen(children, OPEN, CLOSED):
    open_nodes = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [node for node in children if node not in open_nodes and node not in closed_nodes]
    return new_nodes 


def makePair(new_nodes, N):
    return [(node, N) for node in new_nodes]


def reconstructPath(node_pair, CLOSED):
    parent_map = {}
    for node, parent in CLOSED:
        parent_map[node] = parent 
    N, parent = node_pair 
    parent = parent_map[N]
    path = [N]
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    path.reverse()
    return path 


def bfs(current_state):
    OPEN = [(current_state, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair 
        CLOSED.append(node_pair)
        if N.goalTest():
            return reconstructPath(node_pair, CLOSED)
        
        children = N.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        new_pairs = makePair(new_nodes, N)
        OPEN = OPEN + new_pairs
    return []


start_state = State('L', 'L', 'L', 'L', 'L', 0)
visited = set() 
path = printResult(start_state, visited, [])
if path:
    print('Path Found:\n', '->'.join(map(str, path)))
else:
    print('Path not found (recursive)')

print('\nBFS Path:')
bfs_path = bfs(start_state)
if bfs_path:
    for step in bfs_path:
        print(step)
    print("Total Time:", bfs_path[-1].total_time)
else:
    print("No BFS Path Found")
  
print('\nDFS Path:')
visited = set()
path = []
if dfs(start_state, visited, path):
    for step in path:
        print(step)
    print("Total Time:", path[-1].total_time)
else:
    print('No DFS Path Found')
