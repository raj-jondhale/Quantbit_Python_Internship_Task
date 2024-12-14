# task 2 Read a file containing integers and calculate their sum
def calculate_sum(file_path):
    total=0
    with open(file_path,'r') as file:
        for line in file:
            total+=int(line.strip())
    return total        

file_path="numbers.txt"

print(calculate_sum(file_path)) #output 58