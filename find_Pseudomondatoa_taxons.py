import pandas as pd
import numpy as np
import sys

def traverse_dfs_all_nodes(node):
    if node in Tree:
        children = []
        for child in Tree[node]:
            children += [child]
            children += traverse_dfs_all_nodes(child)
        return children
    else:
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the tree (nodes.dmp) file")
        print("Usage: python find_Pseudomondatoa_taxons.py <tree file>")
        sys.exit(1)

    tree_file = sys.argv[1]

    tree_df = pd.read_csv(tree_file,  sep="\t", header=None)
    tree_df.head()

    children = tree_df[0]
    parents = tree_df[2]

    Tree = {}
    for i in range(len(tree_df[0])):
        parent = parents[i]
        child = children[i]
        if parent in Tree:
            Tree[parent].add(child)
        else:
            Tree[parent] = {child}
    
    all_pseudomanadat = traverse_dfs_all_nodes(1224)
    with open("all_pseudomanadat.taxa.ids", "w") as f:
        for item in all_pseudomanadat:
            f.write(f"{item}\n")