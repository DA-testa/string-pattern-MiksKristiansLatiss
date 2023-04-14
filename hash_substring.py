# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip()

    if input_type == 'F':
        with open('input.txt') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1], t_hash, text[i])
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

