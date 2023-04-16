# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()[0]

    if input_type == 'F':
        input_file = "06"
        input_file = "tests/" + input_file
        with open(input_file) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    elif input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    else:
        return None
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(*occurrences)

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    q = len(pattern)
    w = len(text)
    p = 10**9 + 7
    x = 263
    h = pow(x, q-1, p)
    pattern_hash = sum(ord(pattern[i])* pow(x, i, p) for i in range(q)) % p
    text_hash = sum(ord(text[i]) * pow(x, i, p) for i in range(q)) % p
    occurrences = []

    for i in range(w-q+1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+q]:
                occurrences.append(i)
        if i < w-q:
            text_hash = (text_hash - ord(text[i]) * h) % p
            text_hash = (text_hash * x + ord(text[i+q])) % p

    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    input_data = read_input()
    if input_data:
        pattern, text = input_data
        occurrences = get_occurrences(pattern, text)
        print_occurrences(occurrences)

