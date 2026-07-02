# Cipher
A visual cryptography engine that hides encrypted messages inside procedurally generated textile designs using custom mixed-radix number systems.
Not based off of standard encryption systems.
Each level of obstufication is customizable by the user. 
Input is first converted to numbers with each letter being assigned a number
The number is then converted to a number with a custom, three digit, mixed radix base
This is stored as a list of numbers and depending on the base at position, decoy numbers are added to the the digit. The amount of decoy numbers can be customized by the user.
The output is a string of numbers.
This string of numbers is then used to create a design.

## Current Progress 
Converts input message to string of numbers. Converts numbers to custom mixed radix number.
