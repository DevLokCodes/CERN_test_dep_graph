# CERN_test dep_graph


This script is a method to implement a full dependency graph using a recursion logic. The task was to create a graph for the dependency inputs which as taken as input.

#####*Dependencies:*

  - System Windows
  - Language Python 3.6.10 or greater
  
  sub dependencies/ modules for running the script
  
      - os 
      - json
      - pathlib




#####*time and space complexity:* 

Currently the time complexity of the scripts comes from the nested for loop which could take at worst O(N * M) time complexity. where N is the keys in the json list and M is the length of the values in the dictionary. In this specific implementation a recursion logic is implement which cuts down sometime but using a dfs tree or a graph would be much more efficient and twould consume less time as it can directly traverse through the values it has already visited and does not require to calculate the graph again.
  
The space complexity would work significantly better for the implementation of BFS tree rather than recursive approach with the similar idea of not haveing the overload of memory saving the same data and instead saving the nodes as a list.

#####*additional work to be done:*

Working on some more test cases which were found
trying to implement it using dfs tree and eventually a graph approach.

#####*basic working:* 

the basic gist of the program is that it iterates though the dependencies in a linear loop until we find a dependency which satifies a condidition of also being a parent dependecy to another child dependency. whenever this condition is fulfilled a recursive function is called upon and a seperate smaller dependency checks are made to run. this keeps running until we exhaust the list completly.
