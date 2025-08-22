# AI
ASSIGNMENT 1_1
The Rabbit Leap Problem

Three east-bound rabbits stand in a line blocked by three-west bound rabbits.  
They are crossing a stream with stones places in the east west direction in a line. 
There is one empty stone between them.  
The rabbits can only move forward one step or two steps. 
The solution is implemented using both BFS and DFS approaches.

***************************************************************************
ASSIGNMENT 1_2
Bridge-crossing over the river within one hour to catch the train

It is raining and Amogh, Ameya and their grandparents have only one umbrella which can be shared by two people.
Amogh can cross the bridge in 5 minutes, Ameya in 10, their grandmother in 20 and their grandfather in 25.
The code finds valid sequences using BFS and DFS to ensure everyone crosses safely within the time limit.

***************************************************************************
ASSIGNMENT 2_1
Pathfinding in an n×n Binary Matrix: Best First Search vs A* Search

The task is to explore and compare two search algorithms for pathfinding in an n × n binary matrix. The objective is to determine a path from the top-left cell (0, 0) to the bottom-right cell (n-1, n-1) under the following conditions:

- A valid path may only pass through cells with value 0.
- Movements are allowed in 8 possible directions — horizontally, vertically, and diagonally.
- The length of the path is defined as the total number of visited cells.

Part A — Best First Search (Greedy Search):
Implement Best First Search using an admissible heuristic (Manhattan distance to the goal). This approach may not guarantee the shortest path. 

Part B — A* Search:
Implement the A* Search algorithm with the same heuristic. This approach guarantees the shortest path length if one exists, or returns text message as "No Path Found" if no valid path can be found.

Comparison Between Best First Search and A* Search:
Best First Search (Greedy Search):
  - Uses only the heuristic (e.g., Euclidean or Manhattan distance) to guide the search.
  - Fast in practice since it prioritizes nodes closest to the goal.
  - Does not guarantee the shortest path, as it ignores the cost already traveled.
  - May get trapped in exploring locally optimal paths.

A* Search:
  - Combines the actual cost so far (g(n)) with the heuristic estimate to the goal (h(n)), i.e., f(n) = g(n) + h(n).
  - Guarantees the shortest path if the heuristic is admissible.
  - More computationally expensive than Best First Search due to expanded search space.
  - Considered optimal and complete for this type of problem.

***************************************************************************
