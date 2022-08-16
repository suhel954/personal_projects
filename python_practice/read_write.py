#conver to .pynb
example1 = 'Example1.txt'
with open('filename.json', "r") as file1:
    #run methods on the file here like
    FileContent = file1.read()

    #'with automatically closes the file so no need to do
    # file.closed()'

    #for reading one line, use, add a number 
    # inside readline to see the next 'n' chars:
    print('first line: ' + file1.readline()) 

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1


with open(example1, "r") as file1:
    FileasList = file1.readlines()

FileasList[0]

