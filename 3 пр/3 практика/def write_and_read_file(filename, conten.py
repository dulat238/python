def write_and_read_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        
    with open(filename, 'r') as file:
        return file.read()
        
result = write_and_read_file('example.txt' , 'hello')
print (result)