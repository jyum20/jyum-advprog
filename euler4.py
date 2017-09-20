x=0
a = []
def pallindrome1(x):
    strx = str(x)
    for j in range (len(strx)/2):
        if strx[j] != strx[-(j+1)]:
            return False
    return True

def main():
    for b in range (100,999):
        for c in range (100, 999):
            x = b*c
            if pallindrome1 (x):
                a.append(x)
    a.sort()
    a.reverse()
    print a[0]
main()

#x=0
#def pallindrome2(x):
 # strx = str(x)
  #lx = len(x)
    #for i in range
        #string = strx
        #    string[0:lx:-1]
