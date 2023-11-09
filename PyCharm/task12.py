def proverka():
    n = int(input())
    s = n
    while n != 0:
        n = int(input())
        s += n
    print(s)

if __name__ == '__main__':
    proverka()