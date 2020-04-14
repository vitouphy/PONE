with open('src-train.txt') as f:
    length = 0
    for line in f.readlines():
        length = max(length, len(line.split()))
    print(length)
