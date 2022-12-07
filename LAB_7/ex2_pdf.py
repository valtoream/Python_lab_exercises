def read_file(filename):
    filename = input("Enter file name: ")
    try:
        f = open(f"./{filename}","r")
        
    except FileNotFoundError as ex:
        print("Couldnt open file")
        print(str(ex))
    except OSError:
        print(f'Could not read/open file{filename}')
    else:
        lines = f.readlines()
        print(lines)
        f.close()
    
    
    
read_file('')