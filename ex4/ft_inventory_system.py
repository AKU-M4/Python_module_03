def print_inv_report(inv: dict) -> None:

    """ function that automates the printing of any inventory """
    inv_value = 0
    total_items = 0
    cat_totals = {}

    for item in inv:
        curr_item = inv.get(item)
        qty = curr_item.get('qty')
        cat = curr_item.get('cat')
        price = curr_item.get('price')
        rarity = curr_item.get('rarity')

        items_price = price * qty
        print(f"{item} ({cat}, {rarity}):{qty}x @ {price}"
              f" gold each = {items_price} gold")

        inv_value += items_price
        total_items += qty
        cat_totals[cat] = cat_totals.get(cat, 0) + qty

    print(f"\nInventory value: {inv_value} gold")
    print(f"Item count: {total_items} items")

    cat_strings = []
    for c_name, c_qty in cat_totals.items():
        cat_strings.append(f"{c_name}({c_qty})")

    print(f"Cartegories: {', '.join(cat_strings)}")
    

def main() -> None:
    print("=== Player Inventory System ===")

    alice_inv = {
        "sword": {"cat": "weapon", "rarity": "rare", "qty": 1, "price": 500},
        "potion": {"cat": "consumable", "rarity": "common", "qty": 5, "price": 50},
        "shield": {"cat": "armor", "rarity": "uncommon", "qty": 1, "price": 200},
        "forbiden ring" : {"cat": "armor", "rarity": "legendary", "qty": 2, "price": 700}
    }
    
    print("=== Alice's Inventory ===")
    print_inv_report(alice_inv)

    print("=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successfull!")

    print("=== Updated Inventories ===")

if __name__ == "__main__":
    main()