def ctrl_z(s):
    stack= []
    for i in s.split(' ' ):
        try:
            stack.append(int(i))
        except:
            stack.pop()
    return sum(stack)