inventory = {

}

def add_item(item_id, name, quantity):
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
    return

add_item(131, "Jeans", 5)
add_item(437, "T-Shirt", 16)
add_item(35, "Shorts", 3)
add_item(993, "Dress Shirt", 1)
add_item(1, "Polo", 12)

def check_stock(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Requested Item: {item}")
    else:
        print(f"Item with ID {item_id} cannot be found within the inventory")
    return

def update_stock(item_id, delta):
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item {item_id} updated")
    else:
        print(f"The item with the requested id: {item_id} cannot be found. Update failed")
    return

