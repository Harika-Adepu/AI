class State:
    def __init__(self, current_state):
        self.current_state = current_state
        
    def goalTest(self):
        return self.current_state == ['R','R','R','_','L','L','L']
        
    def moveGen(self):
        children = []
        for i in range(len(self.current_state))
            if self.current_state[i]=='L':
                if i+1<7 and self.current_state[i+1]=='_':
                    new_state = self.current_state.copy()
                    new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                    children.append(State(new_state))
                if i+2<7 and self.current_state[i+1]=='R' and self.current_state[i+2]=='_':
                    new_state = self.current_state.copy()
                    new_state[i], new_state[i+2] = new_state[i+2], new_state[i]
                    children.append(State(new_state))
                    
            if self.current_state[i]=='R':
                if i-1>=0 and self.current_state[i-1]=='_':
                    new_state = self.current_state.copy()
                    new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
                    children.append(State(new_state))
                if i-2>=0 and self.current_state[i-1]=='L' and self.current_state[i-2]=='_':
                    new_state = self.current_state.copy()
                    new_state[i], new_state[i-2] = new_state[i-2], new_state[i]
                    children.append(State(new_state))          
        return children
                    
    def __str__(self):
        return str(self.current_state) 
    
    def __hash__(self):
        return hash(tuple(self.current_state))
    
    def __eq__(self, value):
        return self.current_state==value.current_state
        
    def __repr__(self):
        return f"{self.current_state}\n"
    
def findPath(current_state, visited, Path) :
    if current_state.goalTest():
        return Path + [current_state]
    visited.add(current_state)
    for child in current_state.moveGen():
        if child not in visited:
            result = findPath(child, visited, Path + [current_state])
            if result:
                return result 
    return None 

def dfs(state, visited, path):
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
    open_nodes = [node for node,parent in OPEN]
    closed_nodes = [node for node,parent in CLOSED]
    new_nodes = [node for node in children if node not in open_nodes and node not in closed_nodes]
    return new_nodes 

def makePair(new_nodes, N):
    return [(node,N) for node in new_nodes]

def reconstructPath(node_pair, CLOSED):
    parent_map = {}
    for node,parent in CLOSED:
        parent_map[node] = parent 
    N,parent = node_pair 
    parent = parent_map[N]
    path = [N]
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    path.reverse()
    #print('->'.join(map(str,path)))
    return path 

def bfs(state):
    OPEN = [(state, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N,parent = node_pair 
        CLOSED.append(node_pair)
        if N.goalTest():
            return reconstructPath(node_pair, CLOSED)
        
        children = N.moveGen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        new_pairs = makePair(new_nodes, N)
        OPEN = OPEN + new_pairs
    return []

        
initial_state = ['L','L','L','_','R','R','R']
start_state = State(initial_state)
visited = set() 
path = findPath(start_state, visited, [])
if path:
    print('Path found: ',path)
else:
    print('Path not found')
    
print('BFS: ', bfs(start_state))

visited = set()
path = []
if dfs(start_state, visited, path):
    print('DFS: ',path)
else:
    print('No DFS Found')

