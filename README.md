# CERN_test dep_graph


This script is a method to implement a full dependency graph using a recursion logic. The task was to create a graph for the dependency inputs which as taken as input.

Dependencies:

System Windows
Language Python 3.6.10 or greater
  sub dependencies/ modules for running the script
      os 
      json
      pathlib




time and space complexity 

  Currently the time complexity of the scripts comes from the nested for loop which could take at worst O(N * M) time complexity. where N is the keys in the json list and M is the length of the values in the dictionary. In this specific implementation a recursion logic is implement which cuts down sometime but using a dfs tree or a graph would be much more efficient and twould consume less time as it can directly traverse through the values it has already visited and does not require to calculate the graph again.
  
  The space

additional work to be done

basic working 

