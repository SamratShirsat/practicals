def rabin_karp_search_all_occurrences(text, pattern):
 pattern_length = len(pattern)
 text_length = len(text)
 
 def simple_hash(s):
    return sum(ord(c) for c in s)
 pattern_hash = simple_hash(pattern)
 
 print(f"\nPattern: '{pattern}'")
 print(f"Pattern Length: {pattern_length}")
 print(f"Pattern Hash (sum of ASCII values): {pattern_hash}\n")
 found_indices = []
 for start_index in range(text_length - pattern_length + 1):
    current_substring = text[start_index:start_index + pattern_length]
    current_hash = simple_hash(current_substring)
    print(f"Checking substring '{current_substring}' starting at index {start_index}:")
    print(f" Substring Hash: {current_hash}")
    if current_hash == pattern_hash:
        print(" Hash matches pattern hash. Verifying substring characters...")
    if current_substring == pattern:
        print(f" Pattern found at index {start_index}!\n")
        found_indices.append(start_index)
    else:
        print(" Hash collision! Substring does not match pattern.\n")
 else:
    print(" Hash does not match. Moving to next substring.\n")
 if found_indices:
    print(f"Pattern found at indices: {found_indices}\n")
 else:
    print("Pattern not found in the text.\n")
    return found_indices
input_text = input("Enter the text: ")
input_pattern = input("Enter the pattern to search: ")
rabin_karp_search_all_occurrences(input_text, input_pattern)

# KMP

def boyer_moore_search_all(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    match_indices = []

    bad_character_table = {}
    for i in range(pattern_length):
        bad_character_table[pattern[i]] = i
    print("Bad character table:", bad_character_table)

    shift_in_text = 0
    while shift_in_text <= text_length - pattern_length:
        index_in_pattern = pattern_length - 1
        print(f"\nAttempting pattern alignment at text index:{shift_in_text}")

    while index_in_pattern >= 0 and pattern[index_in_pattern] == text[shift_in_text + index_in_pattern]:
        print(f"Matched pattern[{index_in_pattern}] ='{pattern[index_in_pattern]}' with text[{shift_in_text +
        index_in_pattern}] = '{text[shift_in_text + index_in_pattern]}'")
        index_in_pattern -= 1

    if index_in_pattern < 0:
        print(f"Pattern found at index {shift_in_text} in text.")
        match_indices.append(shift_in_text)

        next_index = shift_in_text + pattern_length
        if next_index < text_length:
            next_char = text[next_index]
            shift_amount = pattern_length - bad_character_table.get(next_char, -1)
        else:
            shift_amount = 1
            shift_in_text += shift_amount
    else:
        mismatched_char = text[shift_in_text + index_in_pattern]
        last_occurrence_index = bad_character_table.get(mismatched_char, -1)
        shift_amount = max(1, index_in_pattern - last_occurrence_index)
        print(f"Mismatch at pattern[{index_in_pattern}] ='{pattern[index_in_pattern]}' and "f"text[{shift_in_text + index_in_pattern}] = '{mismatched_char}'")
        print(f"Shifting pattern to the right by {shift_amount} positions")
    shift_in_text += shift_amount

    if not match_indices:
        print("Pattern not found in text.")
        return match_indices
input_text = input("Enter the text: ")
input_pattern = input("Enter the pattern to search for: ")
matches = boyer_moore_search_all(input_text, input_pattern)
if matches:
 print(f"\nPattern found at indices: {matches}")
else:
 print("\nPattern not found.")