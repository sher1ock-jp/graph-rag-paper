import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Path to your .parquet file
file_path = 'output/20240810-150058/artifacts/create_final_nodes.parquet'

# df = pd.read_parquet(file_path)
# print(df)

# G = nx.read_graphml("output/20240810-150058/artifacts/embedded_graph.0.graphml")
G = nx.read_graphml("output/20240810-150058/artifacts/clustered_graph.1.graphml")
# G = nx.read_graphml("output/20240810-150058/artifacts/merged_graph.graphml")

nx.draw(G, with_labels=True)
plt.show()