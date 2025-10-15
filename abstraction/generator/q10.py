def read_file_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

 

