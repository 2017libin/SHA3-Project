from function import *
s=0

def pad(s, r):
    # 只需要填充一个字节
    if (len(s)*4 % r) == (r - 8):
        return s+"86"
    # 需要填充多个字节
    else:
        # 实际这里应该是16进制数个数
        pad_len = int((r - (len(s)*4 % r))/4)
        return s+"6"+(pad_len-2)*"0"+"1"



def SHA3(filename, r, l):
    fo = open(filename, "rb")
    Bytes = fo.read()
    fo.close()

    p = str(bytearray(Bytes).hex())
    #p = "06"+268*"0"+"80"+128*"0"
    if (len(p)*4) % r != 0:
        p = pad(p, r)

    s = 0
    c = 1600-r
    n = int((4*len(p))/r)
    for i in range(n):
      # 以r bits为一个分组
      num = int(r/4)
      # 第i个明文块
      pi = p[i*num:i*num+num]
      # 填充后的第i个明文块
      pad_pi = pi +"0"*int(c/4)

      s = s ^ int(pad_pi,16)      
      s = f(s,24)
        
    # 取前l个bits
    return str(hex(s))[(2+0):int(2+l/4)]
    # return int(str(hex(s))[(2+0):int(2+l/4)],16)



if __name__ == "__main__":
    length = 0
    tmp = SHA3("test.txt",1088,256)
    print(tmp)
