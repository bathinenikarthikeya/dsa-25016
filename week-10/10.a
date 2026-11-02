size = 10

def chaining(keys):
    table = [[] for _ in range(size)]
    for key in keys:
        table[key % size].append(key)
    print("Separate Chaining:", table)

def linear(keys):
    table = [-1] * size
    for key in keys:
        i = key % size
        while table[i] != -1:
            i = (i + 1) % size
        table[i] = key
    print("Linear Probing:", table)

def quadratic(keys):
    table = [-1] * size
    for key in keys:
        h = key % size
        for i in range(size):
            j = (h + i * i) % size
            if table[j] == -1:
                table[j] = key
                break
        else:
            print("Table full for key:", key)
    print("Quadratic Probing:", table)

keys = list(map(int, input("Enter keys: ").split()))

chaining(keys)
linear(keys)
quadratic(keys)
