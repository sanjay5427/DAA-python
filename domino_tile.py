def demo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return demo(n-1) + demo(n-2)
a=int(input())
print(f"Number of ways to tile a 2x{a} board: {demo(a)}")