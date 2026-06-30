from cipher import text_to_numbers, inject_decoys_inline, flatten_to_string, decode_string

def main():
    print("--- Textile Cipher: Full Cycle Test ---")
    
    # cipher customization
    user_text = input("Enter text to be encoded (letters only): ")
    base_input = input("Enter 3-digit base max values (e.g., 5,7,6): ")
    bases = [int(x) for x in base_input.split(",")]
    
    # encryption
    clean_list = text_to_numbers(user_text, bases)
    scrambled_blocks = inject_decoys_inline(clean_list, bases)
    final_stream = flatten_to_string(scrambled_blocks)
    
    print("\n--- OUTPUT ---")
    print(f"Final Pattern: {final_stream}")
    
    # decoded text (to check if decoding is successful)
    decrypted_text = decode_string(final_stream, bases)
    
    print("\n--- DECODED RESULT ---")
    print(f"Decoded Message: {decrypted_text}")
    print("-----------------------")

if __name__ == "__main__":
    main()
