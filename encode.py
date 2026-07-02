import random
from cipher import Cipher, parse_file
from main import CHAR_SHEET


# Define custom character sheet
# CHAR_SHEET = "1234567890 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,?!-"

def encode_message(message, bases):
    clean_list = []
    for char in message:
        if char not in CHAR_SHEET:
            print(f"Warning: Character '{char}' is not in the character sheet. It will be skipped.")
        else:
            # Get the exact numeric position from our sheet (Space=0, A=1, etc.)
            char_val = CHAR_SHEET.index(char)
            
            # Mixed-radix math conversion
            digit1 = (char_val // (bases[1] * bases[2])) % bases[0]
            digit2 = (char_val // bases[2]) % bases[1]
            digit3 = char_val % bases[2]
            
            clean_list.append([digit1, digit2, digit3])
    return clean_list
            


def inject_decoys_inline(clean_list, bases, n):
    # Inserting decoy numbers 
    flat_stream = []
    for block in clean_list:
        if random.random() < n:
            corrupt_position = random.randint(0, 2)
            for i in range(3):
                if i == corrupt_position:
                    invalid_value = bases[i] + random.randint(1, 5)
                    flat_stream.append(invalid_value)
                flat_stream.append(block[i])
        else:
            for digit in block:
                flat_stream.append(digit)
    return flat_stream

def add_date_padding(stream, skip_count, bases):
    """
    Inserts random noise at the front of the stream based on the Date Key.
    """
    padding = []
    for _ in range(skip_count):
        random_base_idx = random.randint(0, 2)
        max_val = bases[random_base_idx]
        padding.append(random.randint(0, max_val + 5))
    return padding + stream

def decode_stream(full_stream, skip_count, bases):
    """
    Decodes the stream, handles the date skip, filters decoys,
    and maps values back to the custom character sheet.
    """
    actual_data_stream = full_stream[skip_count:]
    decoded_characters = []
    current_block = []
    position = 0 
    
    for digit in actual_data_stream:
        if digit < bases[position]:
            current_block.append(digit)
            position += 1
            
            if position == 3:
                # Reconstruct the exact character value
                char_val = (current_block[0] * bases[1] * bases[2]) + (current_block[1] * bases[2]) + current_block[2]
                
                # Pull the character safely from our sheet
                if char_val < len(CHAR_SHEET):
                    decoded_characters.append(CHAR_SHEET[char_val])
                else:
                    decoded_characters.append("?") # Fallback for math overflows
                
                current_block = []
                position = 0
        else:
            # Decoy bypassed smoothly by the eye/code
            pass
            
    return "".join(decoded_characters)
