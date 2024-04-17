import datetime, heapq
import time
class Product:

    def __init__(self, name, owner, add_timestamp, expiration_date):
        self.name = name
        self.owner = owner
        self.add_timestamp = add_timestamp
        self.expiration_date = expiration_date


def print_tree(heap):

    max_depth = 0
    node_to_depth = {}
    for i in range(len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(heap):
            node_to_depth[left] = node_to_depth.get(i, 0) + 1
            max_depth = max(max_depth, node_to_depth[left])
        if right < len(heap):
            node_to_depth[right] = node_to_depth.get(i, 0) + 1
            max_depth = max(max_depth, node_to_depth[right])
        node_to_depth[i] = node_to_depth.get(i, 0)

    for depth in range(max_depth + 1):
        nodes = [i for i in node_to_depth if node_to_depth[i] == depth]
        nodes.sort()
        spaces = 2 ** (max_depth - depth + 1) - 1
        line = ""
        for i in nodes:
            line += " " * spaces + str(heap[i])
            spaces = 2 * spaces + 1
        print(line + '\n')

lista = [9, 8, 6, 5, 2, 1]

def add_new_element(users, storage, product_to_add):
    nowy_man = product_to_add.owner
    if nowy_man not in users:
        users[product_to_add.owner] = []
    product_to_add.add_timestamp = int(time.time())
    product_id = str(len(storage) + 1)
    expiration_date = product_to_add.add_timestamp + (product_to_add.expiration_date * 24 * 60 * 60)
    heapq.heappush(users[product_to_add.owner], (expiration_date, product_to_add.name))
    storage[product_id] = product_to_add.name
    pass


def no_spoilled_food(users, outdated_and_free, now):

    day = 24 * 60 * 60
    for i in users:
        user_value = users[i]
        while user_value > now:
            terminate_product = heapq.heappop(user_value)
            heapq.heappush(outdated_and_free, terminate_product)

    while outdated_and_free >=now * day:
        heapq.heappop(outdated_and_free)
    pass
