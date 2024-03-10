import networkx as nx
import pygraphviz as pgv
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

# Course data with prerequisites
courses = {
    "Cálculo I": None,
    "Lógica Matemática": None,
    "Introdução à Ciência da Computação": None,
    "Programação I": ["Lógica Matemática", "Introdução à Ciência da Computação"],
    "Estrutura de Dados": ["Cálculo I"],
    "Algoritmos": ["Cálculo I", "Estrutura de Dados"],
    "Programação II": ["Programação I"],
    "Banco de Dados": ["Estrutura de Dados"],
    "Redes de Computadores": ["Introdução à Ciência da Computação"],
    "Sistemas Operacionais": ["Programação II", "Estrutura de Dados"],
    "Arquitetura de Computadores": ["Cálculo I", "Estrutura de Dados"],
    "Engenharia de Software": ["Programação II"],
    "Compiladores": ["Programação II", "Arquitetura de Computadores"],
    "Inteligência Artificial": ["Algoritmos"],
    "Computação Gráfica": ["Programação II", "Matemática Discreta"],  # Assuming Matemática Discreta is a prerequisite
    "Projeto de Software": ["Engenharia de Software", "Banco de Dados"],
    "Tópicos Especiais em Ciência da Computação": ["Algoritmos", "Programação II"],
    "Técnicas de Pesquisa": None,
}

# Create a directed graph object
grafo = nx.DiGraph(overlap=False, splines='true')

# Add nodes (courses)
grafo.add_nodes_from(courses.keys())

# Add edges (dependencies)
for course, prerequisites in courses.items():
    if prerequisites:
        for prerequisite in prerequisites:
            grafo.add_edge(prerequisite, course)

# ---

# Create a PyGraphviz graph from the NetworkX graph
A = nx.nx_agraph.to_agraph(grafo)

# Modify the graph's rank separation
A.graph_attr.update(ranksep="2")

# Write the graph to a .dot file
A.write('grafo_dependencias.dot')

# --- 

# Create layout for our nodes 
layout = graphviz_layout(grafo, prog='dot', args='-Granksep=42')

# Draw the graph using the layout
nx.draw(grafo, pos=layout, with_labels=True, arrows=True)

# Save it to a file
plt.savefig('grafo_dependencias.png', format='PNG')

