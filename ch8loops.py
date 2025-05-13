def meditate(mana, max_mana, num_potions):    
    
    while num_potions > 0:
        print(f"BEFORE num_potions: {num_potions}")
        print(f"BEFORE mana {mana}")
        if mana <= max_mana:
            mana += 1
            #potion_+=counter += 1
            num_potions -= 1
            #return mana, num_potions
        print(f"AFTER num_potions: {num_potions}")
        print(f"AFTER mana {mana}")            
         
    print(f"While Loop exited mana={mana} and num_potions={num_potions}")
    return mana, num_potions
       
