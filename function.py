L = [[0]*5 for i in range(5)]
t = [[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
RC = [0x1,0x8082,0x800000000000808a,0x8000000080008000,0x808b,0x80000001,0x8000000080008081,0x8000000000008009,0x8a,0x88,0x80008009,0x8000000a,0x8000808b,0x800000000000008b,0x8000000000008089,0x8000000000008003,0x8000000000008002,0x8000000000000080,0x800a,0x800000008000000a,0x8000000080008081,0x8000000000008080,0x80000001,0x8000000080008008]
# 将64bits的x循环右移i位
def Rot(x,i):
  tmp = hex(x)
  i = i % 64
  tmp1 = (x<<i)
  t1 = hex(tmp1)
  tmp2 = (x>>(64-i)) 
  tmp3 = tmp1 | tmp2 
  tmp4 = tmp3 & 0xffffffffffffffff
  return tmp4

def Theta():
  global L
  C = [0,0,0,0,0]
  for i in range(5):
    for j in range(5):
      C[i] = C[i]^L[i][j]
  for j in range(5):
    for i in range(5):
      L[i][j] = L[i][j]^C[(i+4)%5]^Rot(C[(i+1)%5],1)

def Rho():
  global L
  for i in range(5):
    for j in range(5):
      L[i][j] = Rot(L[i][j],t[i][j])



def Pi():
  global L
  tmp = [[0]*5 for i in range(5)]
  for i in range(5):
    for j in range(5):
      tmp[j][(2*i+3*j) % 5] = L[i][j]
  L = tmp

def Chi():
  global L
  tmp = [[0]*5 for i in range(5)]

  for i in range(5):
    for j in range(5):
      tmp[i][j] = L[i][j] ^ (
          L[(i+1) % 5][j] ^ 0xffffffffffffffff) & (L[(i+2) % 5][j])
  L = tmp


def Iota(i):
  global L
  L[0][0] = L[0][0]^RC[i]
  # tmp1 = getS()
  # tmp1 = testL(int(tmp1, 16))
  # print()


def testL(s):
  global L
  s = str(hex(s))[2:]
  s = "0"*(400 - len(s))+s
  for j in range(5):
    for i in range(5):
      begin = (16*(5*j+i))
      last = (16*(5*j+i)+16)
      L[i][j] = testMini(s[begin:last])

# 使用小端方式转换
def testMini(s):
  tmp = ""
  for i in range(8):
    tmp = s[i*2:i*2+2] + tmp
  return tmp

# 使用小端方式转换
def mini(s):
  tmp = ""
  for i in range(8):
    tmp = s[i*2:i*2+2] + tmp
  return int(tmp,16)

# 输入str,len(s) = 100的16进制串
def setL(s):
  global L
  s = str(hex(s))[2:]
  s = "0"*(400 - len(s))+s
  for j in range(5):
    for i in range(5):
      begin = (16*(5*j+i))
      last = (16*(5*j+i)+16)
      L[i][j] = mini(s[begin:last])

def inverse_mini(s):
  tmp = ""
  for i in range(8):
    tmp =  s[i*2:i*2+2] + tmp
  return tmp

# 返回int
def getS():
  global L
  S = ""
  for j in range(5):
    for i in range(5):
      tmp = str(hex(L[i][j]))[2:]
      if len(tmp) < 16:
        tmp = "0"*(16-len(tmp))+tmp
      S = S + inverse_mini(tmp)
  return int(S,16)

def f(s, counts):
  setL(s)
  for i in range(counts):
    Theta()
    Rho()
    Pi()
    Chi()
    Iota(i)
  return getS()


if __name__ == "__main__":
    x = "06"+268*"0"+"80"+128*"0"
    print(f(int(x, 16), 24))

    # f(int(x,16),24)
    # print(getS())
    # print(len(RC))
