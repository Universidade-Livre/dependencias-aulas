import networkx as nx
import pygraphviz as pgv
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

# Course data with prerequisites
courses = {
    "Circuitos Digitais": [],
    "Matemática Discreta": [],
    "Linguagens de Programação": [],
    "Introdução à Ciência da Computação com Python I": [],
    "Geometria Analítica": [],
    "Cálculo I": ["Geometria Analítica"],
    "Álgebra Linear I": ["Geometria Analítica"],
    "Estruturas de Dados": ["Matemática Discreta", "Introdução à Ciência da Computação com Python I"],
    "Introdução à Ciência da Computação com Python II": ["Introdução à Ciência da Computação com Python I"],
    "Laboratório de Programação Orientada a Objetos I": ["Introdução à Ciência da Computação com Python I"],
    "Algoritmos em Grafos": ["Estruturas de Dados"],
    "Arquitetura de Computadores I": ["Circuitos Digitais"],
    "Probabilidade e Estatística": ["Cálculo I"],
    "Cálculo II": ["Cálculo I"],
    "Programação Funcional em Haskell": [],
    "Análise de Algoritmos": ["Algoritmos em Grafos"],
    "Métodos Numéricos I": ["Introdução à Ciência da Computação com Python I", "Cálculo I"],
    "Banco de Dados": [],
    "Arquitetura de Computadores II": ["Introdução à Ciência da Computação com Python II", "Arquitetura de Computadores I"],
    "Programação Lógica": [],
    "Redes de Computadores": [],
    "Introdução à Engenharia de Software": ["Introdução à Ciência da Computação com Python II"],
    "Sistemas Operacionais": ["Arquitetura de Computadores II"],
    "Programação Matemática": ["Álgebra Linear I"],
    "Fundamentos de Computação Gráfica": ["Geometria Analítica"],
    "Linguagens Formais e Autômatos": ["Matemática Discreta"],
    "Inteligência Artificial": ["Estruturas de Dados", "Probabilidade e Estatística"],
    "Sistemas Distribuídos": ["Redes de Computadores"],
    "Teoria dos Grafos": ["Matemática Discreta"],
    "Cálculo III": ["Cálculo II"],
    "Teoria da Computação": ["Linguagens Formais e Autômatos"],
    "Deep Learning": ["Inteligência Artificial"],
    "Compiladores": ["Estruturas de Dados", "Teoria dos Grafos"],
    "Computação Quantica": ["Cálculo III", "Arquitetura de Computadores II"],
    "Metodologia da Pesquisa": []
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

