import math
"""
https://adventofcode.com/2022/day/4
Usage:
    cat day4_input.txt | python3 day4.py
        > The contents of the expense report:

    ou
    python3 day4.py
        input moves and ctrl-d (EOF) to end inputs
         > The contents of the expense report:
"""

class File:

# instance attributes
    def __init__(self, name, parent, size=None, type="dir"):
        self.name = name
        self.parent = parent
        self.type = type
        self.size = size
        if size:
            self.type = "file"

    # instance method
    def filePath(self):     
        return self.parent
    
    def __str__(self) -> str:
        return F"""
name: {self.name}
parent: {self.parent}
type: {self.type}
size: {self.size}
        """






def readFileSystem():
    line = input()
    files = []
    current_dir = []
    new_directory=False
    current_parent=""
    
    while line:
        print(line)
        
        if "cd " in line:
            new_directory = True
            current_parent = line.split()[1]
        elif "$ ls" in line:
            print(line)
        else:
            size, name = line.split()
            temp = File(name,current_parent,size=size)
            print(temp)
            



        # if line[0] == '$':
        #     if "cd" in line: 

        
        try:
            line = input()
        except EOFError:
            break



def main():
    fileStructure = readFileSystem()
    # print(F"Part 1: {process_packet(datastream_buffer,4)} ")
    # print(F"Part 2: {process_packet(datastream_buffer,14)} ")


if __name__ == '__main__':
    main()
