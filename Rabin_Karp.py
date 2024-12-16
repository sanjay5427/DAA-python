def rabin_karp(text, pattern):
    # Define the base value for the rolling hash function
    base = 26
    # Define a prime number to minimize hash collisions
    prime = 101

    n = len(text)
    m = len(pattern)
    
    # Initial hash values for the pattern and the first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1

    # The value of h would be "base^(m-1) % prime"
    for i in range(m - 1):
        h = (h * base) % prime

    # Calculate the hash value of the pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # List to store the indices of pattern matches
    result = []

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of the current window of text and pattern
        if pattern_hash == text_hash:
            # If the hash values match, check the characters one by one
            if text[i:i + m] == pattern:
                result.append(i)

        # Calculate hash value for the next window of text
        # Remove leading character, add trailing character
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime

            # We might get a negative value of text_hash, convert it to positive
            if text_hash < 0:
                text_hash += prime

    return result

# Get 'text' and 'pattern' from user
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")
result = rabin_karp(text, pattern)
print("Pattern found at indices:", result)
