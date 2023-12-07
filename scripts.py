def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return False
    return stack == []


def remove_duplicates(sequence):
    result = []
    seen = set()
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result



def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency