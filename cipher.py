import random

def text_to_numbers(text, bases):
    """
    Step 1: Converts text into a list of lists based on the custom mixed-radix base.
    """
    # For now, we use a simple placeholder math map (A=1, B=2...) 
    # to get the list structure working.
    encoded_message = []
    
    for char in text.upper():
        if char.isalpha():
            char_val = ord(char) - 64 # A=1, B=2, etc.
            
            # This is where your custom mixed-radix math converts 'char_val' 
            # into 3 digits fitting your bases system
            digit1 = (char_val // (bases[1] * bases[2])) % bases[0]
            digit2 = (char_val // bases[2]) % bases[1]
            digit3 = char_val % bases[2]
            
            encoded_message.append([digit1, digit2, digit3])
            
    return encoded_message

def inject_decoys(clean_list, bases):
    """
    Step 2: Scrambles the data by turning ~30% of blocks into 4-digit decoys.
    """
    scrambled_output = []
    
    for block in clean_list:
        # Match the user's intent: ~30% chance to insert a decoy block
        if random.random() < 0.30:
            # Create a decoy block by adding an illegal 4th digit
            decoy_block = list(block)
            
            # Pick a random position to corrupt (0, 1, or 2)
            corrupt_position = random.randint(0, 2)
            # Make the value higher than the maximum allowed base for that position
            invalid_value = bases[corrupt_position] + random.randint(1, 5)
            
            decoy_block[corrupt_position] = invalid_value
            decoy_block.append(random.randint(0, 9)) # Add a 4th digit to flag it as a decoy
            
            scrambled_output.append(decoy_block)
            
        # Always keep the original valid block moving forward
        scrambled_output.append(block)
        
    return scrambled_output
