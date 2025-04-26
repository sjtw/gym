# ensure s

def valid_parentheses(s: str) -> bool:
    opens = []
    bracket_pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    for char in s:
        if char in bracket_pairs.values():
            opens.append(char)
        elif char in bracket_pairs:
            if not opens or opens[-1] != bracket_pairs[char]:
                return False
            opens.pop()
    return not opens
