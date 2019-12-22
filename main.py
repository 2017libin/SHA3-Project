import pyperclip
import sys
import SHA3
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-help":
            print("可选选项:\n", "1. 对file1进行hash并将hash值输入file2: -input file1 file2\n",
                  "2. 对file进行hash并将hash值拷贝到粘贴板: -copy file")
        elif sys.argv[1] == "-input":
            value = SHA3.SHA3(sys.argv[2], 1088, 256)
            fi = open(sys.argv[3], "w+")
            fi.write(value)
            fi.close()
            print("hash值以保存到文件！")
        elif sys.argv[1] == "-copy":
            value = SHA3.SHA3(sys.argv[2], 1088, 256)
            pyperclip.copy(value)
            print("hash值已拷贝！")
        else:
            print("输入有误！")
    else:
        print("使用选项--help查看帮助")
