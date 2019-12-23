from function import *
s = 0


def pad(s, r):
    # 只需要填充一个字节
    if (len(s)*4 % r) == (r - 8):
        return s+"86"
    # 需要填充多个字节
    else:
        # 实际这里应该是16进制数个数
        lens = len(s)
        tmp = (len(s)*4 % r)
        pad_len = int((r - (len(s)*4 % r))/4)
        return s+"6"+(pad_len-2)*"0"+"1"


def inverse_p(s):
    len_p = len(s)
    tmp = ""
    for i in range(int(len(s)/2)):
        bits = bin(int(s[i*2:i*2+2], 16))
        inverse_bits = str(bits)[2:]
        inverse_bits = ("0"*(8-len(inverse_bits))+inverse_bits)[::-1]
        tmp = tmp + inverse_bits
    tmp2 = str(hex(int(tmp, 2)))[2:]
    return (len_p-len(tmp2))*"0" + tmp2


def SHA3(filename, r, l):
    fo = open(filename, "rb")
    Bytes = fo.read()
    fo.close()

    p = str(bytearray(Bytes).hex())
    #p = "06"+268*"0"+"80"+128*"0"
    if ((len(p)*4) % r != 0) or len(p) == 0:
        p = pad(p, r)
    p = inverse_p(p)
    s = 0
    c = 1600-r
    lenp = len(p)
    n = int((4*len(p))/r)
    for i in range(n):
        # 以r bits为一个分组
        num = int(r/4)
        # 第i个明文块
        pi = p[i*num:i*num+num]
        # 填充后的第i个明文块
        pad_pi = pi + "0"*int(c/4)

        s = s ^ int(pad_pi, 16)
        s = f(s, 24)

    # 取前l个bits
    return str(hex(s))[(2+0):int(2+l/4)]
    # return int(str(hex(s))[(2+0):int(2+l/4)],16)


if __name__ == "__main__":
    length = 0
    tmp = SHA3("test.txt", 1088, 256)
    print(tmp)
    # x = "06"+268*"0"+"80"+128*"0"
    # print(inverse_p(x))
