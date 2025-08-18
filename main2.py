import csv
from BTrees.OOBTree import OOBTree
import timeit


# =========================
# 1. Завантаження даних
# =========================
def load_data(filename: str):
    items = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(
                {
                    "ID": int(row["ID"]),
                    "Name": row["Name"],
                    "Category": row["Category"],
                    "Price": float(row["Price"]),
                }
            )
    return items


# =========================
# 2. Структури даних
# =========================
tree = OOBTree()
dictionary = {}


# =========================
# 3. Додавання товарів
# =========================
def add_item_to_tree(item):
    # ключ = ID, значення = словник без ID (бо вже в ключі)
    tree[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


def add_item_to_dict(item):
    dictionary[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# =========================
# 4. Діапазонні запити
# =========================
def range_query_tree(min_price, max_price):
    # ефективно: перебираємо лише ID, а потім фільтруємо по Price
    return [
        (id_, data)
        for id_, data in tree.items()
        if min_price <= data["Price"] <= max_price
    ]


def range_query_dict(min_price, max_price):
    # доводиться перебирати всі елементи
    return [
        (id_, data)
        for id_, data in dictionary.items()
        if min_price <= data["Price"] <= max_price
    ]


# =========================
# 5. Тестування продуктивності
# =========================
def benchmark(min_price, max_price, number=100):
    tree_time = timeit.timeit(
        stmt=lambda: range_query_tree(min_price, max_price), number=number
    )
    dict_time = timeit.timeit(
        stmt=lambda: range_query_dict(min_price, max_price), number=number
    )

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict:    {dict_time:.6f} seconds")


# =========================
# 6. Запуск
# =========================
if __name__ == "__main__":
    data = load_data("../data/generated_items_data.csv")

    # заповнюємо структури
    for item in data:
        add_item_to_tree(item)
        add_item_to_dict(item)

    # приклад: шукаємо товари у діапазоні цін 100–500
    benchmark(100, 500, number=100)
