import random

def text_to_numbers(text, bases):
    """
    Step 1: Converts text into a clean list of 3-digit lists.
    Handles values larger than 9 automatically.
    """
    encoded_message = []
    # Total combinations our mixed-radix system can support
    max_combinations = bases[0] * bases[1] * bases[2]
    
    for char in text.upper():
        if char.isalpha():
            # Standard map: A=1, B=2 ... Z=26. 
            # If your dictionary grows to full words, char_val can just be the word ID!
            char_val = ord(char) - 64 
            
            # Ensure the value actually fits in our custom number system
            char_val = char_val % max_combinations
            
            # Mixed-radix math conversion
            digit1 = (char_val // (bases[1] * bases[2])) % bases[0]
            digit2 = (char_val // bases[2]) % bases[1]
            digit3 = char_val % bases[2]
            
            encoded_message.append([digit1, digit2, digit3])
    return encoded_message

def inject_decoys_inline(clean_list, bases):
    """
    Step 2: Flattens the blocks into a single stream of integers, 
    randomly inserting decoys directly into the stream.
    """
    flat_stream = []
    
    for block in clean_list:
        # 30% chance to inject a decoy into this character block
        if random.random() < 0.30:
            # Choose which position (0, 1, or 2) to corrupt
            corrupt_position = random.randint(0, 2)
            
            for i in range(3):
                if i == corrupt_position:
                    # Generate an illegal value higher than the base allows
                    # This safely supports bases larger than 9!
                    invalid_value = bases[i] + random.randint(1, 5)
                    flat_stream.append(invalid_value)
                flat_stream.append(block[i])
        else:
            # No decoy, just add the 3 valid digits to the stream
            for digit in block:
                flat_stream.append(digit)
                
    return flat_stream

def add_date_padding(stream, skip_count, bases):
    """
    Step 3: Inserts random noise at the front of the stream based on the Date Key.
    The noise mimics the cipher rules so it blends in perfectly.
    """
    padding = []
    for _ in range(skip_count):
        # Generates a random number. Could be valid, could be an "illegal" decoy value.
        # This keeps the computer guessing.
        random_base_idx = random.randint(0, 2)
        max_val = bases[random_base_idx]
        
        # Give it a mix of normal and high numbers
        padding.append(random.randint(0, max_val + 5))
        
    return padding + stream
