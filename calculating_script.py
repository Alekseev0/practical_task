def count_numbers():
    with open('number.txt', 'r') as number_file:
        lines = number_file.readlines()
        sum = 0
        for line in lines:
            line = line.strip()
            try:
                if line[0] != '#' and float(line):
                    sum += float(line)
            except ValueError:
                pass
        print(sum)


count_numbers()