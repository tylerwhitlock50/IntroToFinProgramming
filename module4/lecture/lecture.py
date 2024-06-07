

#def create a file that contains dummy data
file_name = 'external_files/initial_file.txt'
lines = ['Hello World\n', 'This is a test file\n', 'Goodbye World\n']

with open(file_name, 'w') as file: #using a context manager to open the file
    file.write('Hello World\n')
    file.write('This is a test file\n')
    file.write('Goodbye World\n')
    file.write('Cup\n')
    file.write('Table\n')
    file.writelines(lines)

#def read the file and print the contents
with open(file_name, 'r') as file:
    for line in file:
        print(line, end='')


with open(file_name, 'r') as file:
    text = file.read()
with open(file_name, 'r') as file:
    lines = file.readlines()

print('Text:')
print(text)  # prints the entire file

print("Lines:")
print(lines) # prints an empty list

print('\n'*2)
print('x'*30)
#print the lines that have less than 5 characters
[print(line.strip()) for line in lines if len(line.strip()) <= 5]

print('x'*30)
print('\n'*2)


# Create our funner file to work with
data_file = 'external_files/data.csv'
#def create a datafrane that contains dummy data
import pandas as pd
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'location': ['New York', 'Paris', 'Berlin', 'London'],
    'age': [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
data_pandas.to_csv(data_file, index=False, sep=';')
loaded_data = pd.read_csv(data_file, sep=';')
print(loaded_data)

# print the lines of the file


csv_array = []
with open(data_file, 'r') as file:
    for line in file:
        print(line.strip().split(';'), end='')
        csv_array.append(line.strip().split(';'))


print('\n'*2)
print('x'*30)
[print(line) for line in csv_array]

new_csv = 'csv_array.csv'

with open(new_csv, 'w') as file:
    for line in csv_array:
        file.write(','.join(line) + '\n')