import random

def text_to_numbers(text, bases):
    """
    Step 1: Converts text into a clean list of 3-digit lists.
    """
    encoded_message = []
    for char in text.upper():
        if char.isalpha():
            char_val = ord(char) - 64 # A=1, B=2
            
            # Mixed-radix math placeholder
            digit1 = (char_val // (bases[1] * bases[2])) % bases[0]
            digit2 = (char_val // bases[2]) % bases[1]
            digit3 = char_val % bases[2]
            
            encoded_message.append([digit1, digit2, digit3])
    return encoded_message

def inject_decoys_inline(clean_list, bases):
    """
    Step 2: Loops through blocks. ~30% of the time, injects an illegal 
    decoy digit directly into the block, making it 4 digits long.
    """
    scrambled_output = []
    
    for block in clean_list:
        # 30% chance to inject a decoy inside this specific block
        if random.random() < 0.30:
            modified_block = list(block)
            
            # Pick which position to mess up (0, 1, or 2)
            corrupt_position = random.randint(0, 2)
            
            # Generate a false value higher than the base max for that position
            invalid_value = bases[corrupt_position] + random.randint(1, 3)
            
            # Insert the decoy directly into that position, shifting the rest right
            modified_block.insert(corrupt_position, invalid_value)
            scrambled_output.append(modified_block)
        else:
            # Keep it a normal 3-digit block
            scrambled_output.append(block)
            
    return scrambled_output

def flatten_to_string(list_of_lists):
    """
    Step 3: Flattens the blocks into one long, confusing string of numbers.
    """
    flat_list = []
    for block in list_of_lists:
        for digit in block:
            flat_list.append(str(digit))
            
    return "".join(flat_list)
