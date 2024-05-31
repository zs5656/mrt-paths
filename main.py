## okay, this one is mine. it takes the input from an excel sheet and shoves it into dijixstras algorithm implementation in python, which i did NOT code. 

import dijix as a
import pandas as pd

df = pd.read_excel(r'MRT.xlsx')

station_start = list(df["station_start"])
station_end = list(df["station_end"])
cost = list(df["cost"])
node_list = list(df["node_list"])

nodes = [x for x in node_list if x == x]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

for i in range(len(cost)):
    init_graph[str(station_start[i])][str(station_end[i])] = int(cost[i])


graph = a.Graph(nodes, init_graph)

def main():
    start = input("Starting station? ")
    end = input("Ending station? ")
    previous_nodes, shortest_path = a.dijkstra_algorithm(graph=graph, start_node=start)
    a.print_result(previous_nodes, shortest_path, start_node=start, target_node=end)

    main()

main()

