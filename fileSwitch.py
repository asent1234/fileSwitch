def fileSwitch(path1, path2):
    file1 = open(r(path1), "w+")
    file2 = open(r(path2), "w+")
    contents1 = file1.readlines()
    contents2 = file2.readlines()
    file1.writelines(contents1)
    file2.writelines(contents2)
    file1.close()
    file2.close()

fileSwitch("C:\Users\aakas\Downloads\path1.text", "C:\Users\aakas\Downloads\path2.txt")
