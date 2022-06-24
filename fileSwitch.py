def fileSwitch(path1, path2):
    file1 = open(path1, "r")
    file2 = open(path2, "r")
    contents1 = file1.readlines()
    contents2 = file2.readlines()
    file1.close()
    file2.close()
    file1 = open(path1, "w")
    file2 = open(path2, "w")
    print(contents1)
    print(contents2)
    file1.writelines(contents2)
    file2.writelines(contents1)
    file1.close()
    file2.close()

fileSwitch(r"C:\Users\aakas\Downloads\path1.txt", r"C:\Users\aakas\Downloads\path2.txt")
 