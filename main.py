import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Path to your .parquet file
file_path = 'output/20240811-142618/artifacts/create_final_relationships.parquet'

df = pd.read_parquet(file_path)
print(df)

# G = nx.read_graphml("output/20240810-150058/artifacts/embedded_graph.0.graphml")
# G = nx.read_graphml("output/20240811-142618/artifacts/merged_graph.graphml")
# G = nx.read_graphml("output/20240810-150058/artifacts/merged_graph.graphml")

# nx.draw(G, with_labels=True)
# plt.show()