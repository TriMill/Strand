import random

def main():
    print('Strand (C) 2019 CC BY-SA 4.0')
    print('https://github.com/TriMill/Strand')
    inp = input('> ')
    while inp != '':
        print(parse(inp))
        inp = input('> ')

def parse(s):
    if '[' not in s:
        if ']' in s:
            raise ValueError('String "%s" contains an unmatched closing bracket' % s)
        return s
    if ']' not in s:
        raise ValueError('String "%s" contains an unmatched opening bracket' % s)
    result = ''
    nextChoice = ''
    depth = 0
    for char in s:
        if char == '[' and depth == 0: # If depth is 0, skip adding the char...
            depth += 1
        elif char == ']' and depth == 1:
            depth -= 1
            result += choose(nextChoice)
            nextChoice = ''
        else:
            if char == '[': depth += 1 # ...otherwise add it but still increase depth
            elif char == ']': depth -= 1
            if depth == 0: result += char
            else: nextChoice += char
    return result

def choose(s):
    choices = ['']
    depth = 0
    for char in s:
        if char == '|' and depth == 0:
            choices.append('')
            continue
        elif char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        choices[-1] += char
    return parse(random.choice(choices))

if __name__ == '__main__':
    main()
