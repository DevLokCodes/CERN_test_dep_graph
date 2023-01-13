# CERN_test dep_graph


This script is a method to implement a full dependency graph using a recursion logic. The task was to create a graph for the dependency inputs which as taken as input.

#### *Dependencies:*

  - System Windows
  - Language Python 3.6.10 or greater
  
  sub dependencies/ modules for running the script
  
      - os 
      - json
      - pathlib




#### *time and space complexity:* 

The nested for loop, which currently contributes to the time complexity of the scripts, has a worst-case time complexity of O(N * M). where N represents the keys in the json list and M is the size of the dictionary's values. Recursion logic is used in this particular solution, which saves time, however using a graph or dfs tree would be far more effective and take up less time because it can traverse directly across data it has already visited and does not need to recalculate the graph.
  
The implementation of a BFS tree would function much better in terms of space complexity than a recursive approach with the comparable goal of not overloading memory while saving the same data and instead saving the nodes as a list.

#### *additional work to be done:*

More test cases that were discovered need to be worked on as well as attempts to construct it using a dfs tree and ultimately a graph method.

#### *basic working:* 

The program iterates over the dependencies in a linear loop until we locate a dependency that satisfies the requirement of also being a parent dependency to another child dependency. This is how it works in its simplest form. A recursive function is used anytime this condition is met, and separate, smaller dependence checks are triggered. This keeps running until we exhaust the list completely.
