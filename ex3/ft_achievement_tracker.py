def return_rare(all_achievements, rare_achiev, alice, bob, charlie) -> None:
    """ return all the rare achievements """
    for achiev in all_achievements:
        count = 0
        if achiev in bob:
            count += 1
        if achiev in alice:
            count += 1
        if achiev in charlie:
            count += 1
        if count == 1:
            rare_achiev.add(achiev)
        

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player bob achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_achievements = alice.union(bob,charlie)
    print(f"all unique achievments: {all_achievements}")

    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_achiev = alice.intersection(bob, charlie)
    print(f"Common to all players:{common_achiev}")

    rare_achiev = set()
    return_rare(all_achievements, rare_achiev, alice, bob, charlie)
    print(f"Rare achievemtns (1 player): {rare_achiev}\n")

    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    common_bob_alice = alice.intersection(bob)

    print(f"Alice vs Bob common: {common_bob_alice}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")




if __name__ == "__main__":
    main()