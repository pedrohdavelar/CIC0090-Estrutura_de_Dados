def print_compressed(string):
    if len(string) > 0:
        #print(f'string: {string}, length: {len(string)}')
        char = string[0]
        #print(f'char: {char}')
        numbers = []
        for digit in string[1:]:
            if digit.isdigit():
                #print(f'digit: {digit}')
                numbers.append(int(digit))
            else:
                break
        #print(f'numbers: {numbers}')    
        #print(f'string: {string}, length: {len(string)}')
        n = 0
        removeQt = 1
        multiplier = 1   
        while len(numbers) > 0:
            n += numbers.pop() * multiplier
            multiplier *= 10
            removeQt += 1
        #print(f'n: {n}, removeQt: {removeQt}')
        while (n > 0):
            print(char, end="")
            n -= 1
        newString = string[removeQt:]
        print_compressed(newString)
        #print(f'string: {string}, length: {len(string)}')
        #print(f'new string: {newString}, new length: {len(newString)}')
    else:
        print()




for _ in range(int(input())):
    string = input()
    print_compressed(string)