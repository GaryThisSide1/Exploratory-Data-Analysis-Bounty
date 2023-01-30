# Exploratory-Data-Analysis-Bounty

### 1. Using the graph based approach
In this method of graph based approach addresses are nodes and transactions are edges.It can be used to get the features such as :-
* In-degree: number of incoming edges for each node
* Out-degree: number of outgoing edges for each node
* In-degree centrality: normalized in-degree of a node
* Out-degree centrality: normalized out-degree of a node
* PageRank: a measure of the importance of a node in a graph
* HITS: a measure of the authority and hubness of a node

I implemented this approach in the Graph.py file where i used the python and its library NetworkX to implement this.
NetworkX is a Python library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It provides data structures for representing graphs, as well as algorithms for graph analysis and visualization.

In this case, NetworkX is being used to create a graph representation of the transactions in the data. Each address is represented as a node, and each transaction is represented as a directed edge from the source address to the target address. This allows us to study the relationships between the addresses in the network, such as the number of incoming and outgoing transactions and the centrality measures of the addresses.

The NetworkX library is useful for this task because it provides a convenient way to represent and manipulate graph data, as well as a variety of algorithms for graph analysis and visualization. This makes it easier to study the patterns in the data and identify any potential sybil attacks.

On applying this approach on the Gitcoin Gr15 data i got this as the analysis:-
   ![This is an image](images/)
