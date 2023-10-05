
def main():
    bits = random_gen(8)
    print(bits)
    stuff(bits)
    print(bits)
    
def stuff(bits: list) -> list:
    count = 0 
    for index in range(len(bits)):
        
        if bits[index] == True:
            count += 1
        else:
            count = 0
        
        if count == 5:
            bits.insert(index + 1, False)
            count = 0
    return bits
    
def unstuff(bits: list) -> list:
    ...
    
    
def random_gen(len, weight=4) -> list:
    import random
    op = [True, False]
    for _ in range(weight):
        op.append(True)
    lis = []
    for _ in range(len):
        lis.append(random.choice(op))
    return lis

if __name__ == '__main__':
    main()