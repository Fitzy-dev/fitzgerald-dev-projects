# Jordan Fitzgerald
# 3/17/26
# Pin Extractor

def pin_extractor(poems):
  # Making a list of secret codes 
    secret_codes = []
    # Iterating over each poem called in the argument
    for poem in poems:
        secret_code = ''
        # Spliting Each line of a poem it its own 
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            # If a word length is greater than the index its extracts the pin
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        # Appends the secret code to the list
        secret_codes.append(secret_code)
    # Returns the list of each pin of each peom
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'
print(pin_extractor([poem, poem2, poem3]))
