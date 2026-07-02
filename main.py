
CHAR_SHEET = "1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!-"

def main():
    print("Encode Text")
    print("Please edit textForm.txt to change the text to be encoded.")
    file_path = input("Write file path: ")







"""
from cipher import text_to_numbers, inject_decoys_inline, flatten_to_string, decode_string

def main():
    print("--- Textile Cipher: Full Cycle Test ---")
    
    # cipher customization
    user_text = get_message()
    base_input = input("Enter 3-digit base max values (e.g., 5,7,6): ")
    bases = [int(x) for x in base_input.split(",")]
    n = input("Enter percent of decoy numbers (e.g. 0.3, 0.5): ") 
    
    # encryption
    clean_list = text_to_numbers(user_text, bases)
    scrambled_blocks = inject_decoys_inline(clean_list, bases, n)
    final_stream = flatten_to_string(scrambled_blocks)
    
    print("\n--- OUTPUT ---")
    print(f"Final Pattern: {final_stream}")
    
    # decoded text (to check if decoding is successful)
    decrypted_text = decode_string(final_stream, bases)
    
    print("\n--- DECODED RESULT ---")
    print(f"Decoded Message: {decrypted_text}")
    print("-----------------------")

def get_message():
    method = input("Select method of input, text or file (t/f): ")
    if method.lower() == "t":
        return input("Enter text to be encoded (letters only): ")
    elif method.lower() == "f":
        file_path = input("Enter the path to the text file: ")
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            return get_message()
    else:
        print("Invalid selection. Please choose 't' for text or 'f' for file.")
        return get_message()

if __name__ == "__main__":
    main()
"""