import networkx as nx
import matplotlib.pyplot as plt
from src.edmonds_karp import edmonds_karp


def test_edmonds_karp():

    TERMAINAL = "Термінал"
    SHOP = "Магазин"

    # Створюємо граф
    G = nx.DiGraph()

    # Ребра з пропускною здатністю
    edges = [
        ("Термінал 1", "Склад 1", 25),
        ("Термінал 1", "Склад 2", 20),
        ("Термінал 1", "Склад 3", 15),
        ("Термінал 2", "Склад 3", 15),
        ("Термінал 2", "Склад 4", 30),
        ("Термінал 2", "Склад 2", 10),
        ("Склад 1", "Магазин 1", 15),
        ("Склад 1", "Магазин 2", 10),
        ("Склад 1", "Магазин 3", 20),
        ("Склад 2", "Магазин 4", 15),
        ("Склад 2", "Магазин 5", 10),
        ("Склад 2", "Магазин 6", 25),
        ("Склад 3", "Магазин 7", 20),
        ("Склад 3", "Магазин 8", 15),
        ("Склад 3", "Магазин 9", 10),
        ("Склад 4", "Магазин 10", 20),
        ("Склад 4", "Магазин 11", 10),
        ("Склад 4", "Магазин 12", 15),
        ("Склад 4", "Магазин 13", 5),
        ("Склад 4", "Магазин 14", 10),
    ]

    # Додаємо всі ребра до графа
    G.add_weighted_edges_from(edges)

    # Вершини графа
    pos = {
        "Термінал 1": (2, 6),
        "Термінал 2": (10, 6),
        "Склад 1": (4, 9),
        "Склад 2": (8, 9),
        "Склад 3": (4, 3),
        "Склад 4": (8, 3),
        "Магазин 1": (0, 12),
        "Магазин 2": (2, 12),
        "Магазин 3": (4, 12),
        "Магазин 4": (6, 12),
        "Магазин 5": (8, 12),
        "Магазин 6": (10, 12),
        "Магазин 7": (0, 0),
        "Магазин 8": (2, 0),
        "Магазин 9": (4, 0),
        "Магазин 10": (6, 0),
        "Магазин 11": (8, 0),
        "Магазин 12": (10, 0),
        "Магазин 13": (12, 0),
        "Магазин 14": (14, 0),
    }

    vertexs = [key for key in pos]

    capacity_matrix = []

    for row_vertex in vertexs:
        row = []
        for col_vertex in vertexs:
            capacity = 0
            for edge in edges:
                if row_vertex == edge[0] and col_vertex == edge[1]:
                    capacity = edge[2]
                    break
            row.append(capacity)
        capacity_matrix.append(row)

        row = []

    result_table = []

    for source_idx, source in enumerate(vertexs):
        for sink_idx, sink in enumerate(vertexs):
            if source.find(TERMAINAL) != -1 and sink.find(SHOP) != -1:
                result_table.append(
                    {
                        "source": source,
                        "sink": sink,
                        "flow": edmonds_karp(capacity_matrix, source_idx, sink_idx),
                    }
                )

    print("{:<10} | {:<15} | {:<10}".format("Source", "Sink", "Flow"))
    for e in result_table:
        source, sink, flow = e.values()
        print("{:<10} | {:<15} | {:<10}".format(source, sink, flow))

    # Малюємо граф
    plt.figure(figsize=(10, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="skyblue",
        font_size=12,
        font_weight="bold",
        arrows=True,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Відображаємо граф
    plt.show()


if __name__ == "__main__":

    test_edmonds_karp()
