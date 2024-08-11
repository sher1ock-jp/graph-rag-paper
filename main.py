import networkx as nx
import matplotlib.pyplot as plt

# Load the .graphml file
G = nx.read_graphml("output/20240811-142618/artifacts/merged_graph.graphml")

# Draw the graph
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_size=50, font_size=8, node_color="skyblue", edge_color="gray")
plt.savefig("graph_visualization.png", format="PNG")  # Save as an image file
plt.show()

# G = nx.read_graphml("output/20240810-150058/artifacts/embedded_graph.0.graphml")
# G = nx.read_graphml("output/20240811-142618/artifacts/merged_graph.graphml")
# G = nx.read_graphml("output/20240810-150058/artifacts/merged_graph.graphml")

# nx.draw(G, with_labels=True)
# plt.show

# import pandas as pd
# import os

# # Define the output file
# readme_path = "README.md"

# # List of file paths to process
# file_paths = [
#     'output/20240811-142618/artifacts/create_base_extracted_entities.parquet',
#     'output/20240811-142618/artifacts/create_base_entity_graph.parquet',
#     'output/20240811-142618/artifacts/create_final_community_reports.parquet',
#     'output/20240811-142618/artifacts/create_final_entities.parquet',
#     'output/20240811-142618/artifacts/create_final_nodes.parquet',
#     'output/20240811-142618/artifacts/create_final_relationships.parquet',
#     'output/20240811-142618/artifacts/create_summarized_entities.parquet'
# ]

# # Open README.md for appending
# with open(readme_path, "a") as readme_file:
#     # Iterate over each file path
#     for file_path in file_paths:
#         # Load the parquet file into a DataFrame
#         df = pd.read_parquet(file_path)
        
#         # Print the contents or a summary of the DataFrame
#         content = df.to_string()
        
#         # Write the content to README.md
#         readme_file.write(f"\n## {os.path.basename(file_path)}\n")
#         readme_file.write(content)
#         readme_file.write("\n\n")