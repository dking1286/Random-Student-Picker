import random

def main():
    names = get_names_from_file('student_names.txt')
    print random.choice(names)

def get_names_from_file(filename):
    names = []
    with open(filename, 'r') as name_file:
        for line in name_file:
            name = line.split(',')
            name = tuple(map(lambda s: s.strip(), name))
            names.append(name)    
    return names
    
main()