import networkx as nx
data=pd.read_csv("gitcoin-grant/GR15_contributions.csv")
# create directed graph
G = nx.DiGraph()

# Add edges to the graph
for i, row in data.iterrows():
    G.add_edge(row['address'], row['tx_id'], weight=row['amount_in_usdt'])

# calculate the degree of each node
# calculate the in-degree of each node
in_degree = dict(G.in_degree())

# calculate the out-degree of each node
out_degree = dict(G.out_degree())

# calculate the in-degree centrality of each node
in_degree_centrality = nx.in_degree_centrality(G)

# calculate the out-degree centrality of each node
out_degree_centrality = nx.out_degree_centrality(G)

# calculate the PageRank of each node
pagerank = nx.pagerank(G)

# calculate the HITS of each node
hits = nx.hits(G)

# add the calculated features to the dataframe
data['in_degree'] = data['address'].map(in_degree)
data['out_degree'] = data['address'].map(out_degree)
data['in_degree_centrality'] = data['address'].map(in_degree_centrality)
data['out_degree_centrality'] = data['address'].map(out_degree_centrality)
data['pagerank'] = data['address'].map(pagerank)
data['hubs'] = data['address'].map(hits[0])
data['authorities'] = data['address'].map(hits[1])


from sklearn.cluster import KMeans

# select the graph-based features as input for the clustering
X = data[["in_degree", "out_degree", "in_degree_centrality", "out_degree_centrality", "pagerank", "hubs", "authorities"]]

# initialize the K-Means model
kmeans = KMeans(n_clusters=3)

# fit the model to the data
kmeans.fit(X)

# get the cluster labels for each data point
labels = kmeans.labels_

# add the cluster labels as a column to the data
data["cluster"] = labels

# analyze the clusters to detect any suspicious patterns
for i in range(3):
    cluster_data = data[data["cluster"] == i]
    print("Cluster ", i)
    print("Number of points: ", cluster_data.shape[0])
    print("Unique addresses: ", len(cluster_data["address"].unique()))
    print("Mean in-degree: ", cluster_data["in_degree"].mean())
    print("Mean out-degree: ", cluster_data["out_degree"].mean())
    print("Mean in-degree centrality: ", cluster_data["in_degree_centrality"].mean())
    print("Mean out-degree centrality: ", cluster_data["out_degree_centrality"].mean())
    print("Mean pagerank: ", cluster_data["pagerank"].mean())
    print("Mean hubs: ", cluster_data["hubs"].mean())
    print("Mean authorities: ", cluster_data["authorities"].mean())
data.to_csv("Result_G15.csv")
