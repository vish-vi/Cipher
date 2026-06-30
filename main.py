from cipher import text_to_numbers, inject_decoys

def main():
    print("--- Textile Cipher Logic Engine ---")
    
    # 1. Get user input
    user_text = input("Enter your secret message: ")
    base_input = input("Enter 3-digit base max values (e.g., 4,5,6): ")
    
    # Convert string input "4,5,6" into a list of integers [4, 5, 6]
    bases = [int(x) for x in base_input.split(",")]
    
    # 2. Run Step 1: Exact translation
    clean_list = text_to_numbers(user_text, bases)
    print(\n"Step 1 (Clean List of Lists):", clean_list)
    
    # 3. Run Step 2: Decoy Injection
    final_scrambled = inject_decoys(clean_list, bases)
    print("Step 2 (Scrambled with 4-Digit Decoys):", final_scrambled)

if __name__ == "__main__":
    main()
