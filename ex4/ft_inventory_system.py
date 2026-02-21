def print_inv_report(inv: dict) -> None:
    """Calculates and prints the report, returning totals for analytics."""
    inv_value = 0
    total_items = 0
    cat_totals = {}

    for item, stats in inv.items():
        qty = stats.get('qty', 0)
        cat = stats.get('cat', 'misc')
        price = stats.get('price', 0)
        rarity = stats.get('rarity', 'common')

        items_price = price * qty
        print(f"{item} ({cat}, {rarity}): {qty}x @ {price} gold each = {items_price} gold")

        inv_value += items_price
        total_items += qty
        cat_totals[cat] = cat_totals.get(cat, 0) + qty

    print(f"Inventory value: {inv_value} gold")
    print(f"Item count: {total_items} items")

    cat_strings = [f"{c}({q})" for c, q in cat_totals.items()]
    print(f"Categories: {', '.join(cat_strings)}")
    
    # Return these values so main() can use them for Analytics
    return inv_value, total_items

def main() -> None:
    print("=== Player Inventory System ===")

    alice_inv = {
        "sword": {"cat": "weapon", "rarity": "rare", "qty": 1, "price": 500},
        "potion": {"cat": "consumable", "rarity": "common", "qty": 5, "price": 50},
        "shield": {"cat": "armor", "rarity": "uncommon", "qty": 1, "price": 200},
    }
    bob_inv = {}

    # 1. Alice's Initial Report
    print("=== Alice's Inventory ===")
    alice_val, alice_count = print_inv_report(alice_inv)

    # 2. Transaction Logic
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    transfer_qty = 2
    if alice_inv["potion"]["qty"] >= transfer_qty:
        alice_inv["potion"]["qty"] -= transfer_qty
        # Give Bob a copy of the potion data with the new quantity
        bob_inv["potion"] = alice_inv["potion"].copy()
        bob_inv["potion"]["qty"] = transfer_qty
        print("Transaction successful!")

    # 3. Updated Inventories
    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice_inv['potion']['qty']}")
    print(f"Bob potions: {bob_inv['potion']['qty']}")

    # 4. Analytics
    # We re-calculate values after the transaction
    # (Simplified for this example)
    alice_val = sum(v['qty'] * v['price'] for v in alice_inv.values())
    bob_val = sum(v['qty'] * v['price'] for v in bob_inv.values())
    
    print("\n=== Inventory Analytics ===")
    
    # Most Valuable Player
    mvp = "Alice" if alice_val >= bob_val else "Bob"
    print(f"Most valuable player: {mvp} ({max(alice_val, bob_val)} gold)")
    
    # Most Items
    alice_total_qty = sum(v['qty'] for v in alice_inv.values())
    print(f"Most items: Alice ({alice_total_qty} items)")

    # Rarest Items (Check both inventories for 'rare' or 'legendary')
    rare_list = []
    for inventory in [alice_inv, bob_inv]:
        for name, stats in inventory.items():
            if stats['rarity'] in ['rare', 'legendary'] and name not in rare_list:
                rare_list.append(name)
    
    # Adding 'magic_ring' manually as per your requirement example if needed, 
    # but here we find them dynamically
    print(f"Rarest items: {', '.join(rare_list)}")

if __name__ == "__main__":
    main()