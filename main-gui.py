## okay, this one is mine. it takes the input from an excel sheet and shoves it into dijixstras algorithm implementation in python, which i did NOT code. 
from tkinter import *
from tkinter.ttk import *
import dijix as a
import pandas as pd

# import sv_ttk

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
    window = Tk()
    input_text = Label(
        text="Input start station:",
    )

    output_text = Label(
        text="Input end station:",
    )

    combo_input = Combobox(
        values=nodes
    )

    combo_output = Combobox(
        values=nodes
    )
    combo_input.place(x=50, y=50)

    def getText():
        start = combo_input.get()
        end = combo_output.get()
        print(f"start: {start}")
        print(f"end: {end}")

        previous_nodes, shortest_path = a.dijkstra_algorithm(graph=graph, start_node=start)
        output = a.print_result(previous_nodes, shortest_path, start_node=start, target_node=end)

        the_route = output[0]
        the_interchanges = output[1]

        route.config(text=the_route)
        interchanges.config(text=the_interchanges)


    button1 = Button(
        text="Click here",
        command=getText
    )

    #main_text.place(x=0, y=0)
    input_text.pack()
    combo_input.pack()
    output_text.pack()
    combo_output.pack()
    button1.pack()

    route = Label(window, text="", wraplength=300)
    route.pack()
    

    interchanges = Label(window, text="", wraplength=300)
    interchanges.pack()

    disclaimer = "this program doesn't account for wait times or delays. Please factor in additional time when travelling."

    disclaimer = Label(window, text =disclaimer, wraplength=300)
    disclaimer.pack()

    # sv_ttk.set_theme("light")

    window.title("Python test")
    window.geometry("400x500")

    window.mainloop()

main()

