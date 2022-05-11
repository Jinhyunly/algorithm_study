while True:
    tmp = input()
    if tmp == '.':
        break

    stack = []
    okFlg = True

    for t in tmp:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')':
            if not stack or stack[-1] == '[':
                okFlg = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif t == ']':
            if not stack or stack[-1] == '(':
                okFlg = False
                break
            elif stack[-1] == '[':
                stack.pop()
    
    if okFlg and not stack:
        print('yes')
    else:
        print('no')