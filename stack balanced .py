def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}': 
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

expr1 = "(a+b)*[c/d}"
expr2 = "(a+b)*[c/d"

print("Expression 1:", "Balanced" if is_balanced(expr1) else "Not Balanced")
print("Expression 2:", "Balanced" if is_balanced(expr2) else "Not Balanced")
