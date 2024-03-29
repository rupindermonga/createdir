

import os
for tmpdir in ('/tmp',r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print("No temp directory available")
    tmpdir = ""

if tmpdir:
    cwd = os.getcwd()
    print("*** current temporary directory")
    print(cwd)
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print("*** current temporary directory")
    print(cwd)

    print("creating example directory...")
    os.mkdir("example")
    os.chdir("example")
    cwd = os.getcwd()
    print("*** new working directory: ")
    print(cwd)
    print("*** original directory listing: ")
    print(os.listdir(cwd))

    print("*** creating test file...")
    f = open("test","w")
    f.writelines(["foo\n", "bar\n"])
    f.close()
    print("*** updated directory listing: ")
    print(os.listdir(cwd))

    print("*** renaming 'test' to 'filetest.txt'")
    os.rename('test','filetest.txt')
    print("*** updated directory listing: ")
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print("*** full file pathname")
    print(path)

    print("*** (pathname, basename) == ")
    print(os.path.split(path))
    print("*** (filename, extension) ==")
    print(os.path.splitext(os.path.basename(path)))

    print("*** displaying file contents: ")
    f = open(path)
    for eachLine in f:
        print(eachLine)
    f.close

    print("*** deleting test file")
    os.remove(path)
    print("*** updated directory listing: ")
    print(os.listdir(cwd))
    os.chdir(os.pardir)
    print("*** deleting test directory")
    os.rmdir("example")
    print("*** done")