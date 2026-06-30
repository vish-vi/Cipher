from cipher import text_to_numbers, inject_decoys_inline, flatten_to_string

def main():
    print("--- Textile Cipher Logic Engine V2 ---")
    
    user_text = input("Enter message: ")              # Example: HI
    base_input = input("Enter bases (e.g., 5,7,6): ") # Example: 5,7,6
    bases = [int(x) for x in base_input.split(",")]
    
    # 1. Clean Translation
    clean_list = text_to_numbers(user_text, bases)
    
    # 2. Inject Decoys Inline (e.g., [4, 6, 3] becomes [4, 8, 6, 3])
    scrambled_blocks = inject_decoys_inline(clean_list, bases)
    
    # 3. Flatten into a single massive string
    final_stream = flatten_to_string(scrambled_blocks)
    
    print("\n--- OUTPUT STREAM ---")
    print(f"Continuous Code String: {final_stream}")
    print("----------------------")

if __name__ == "__main__":
    main()
