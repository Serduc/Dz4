def isPowerOfFour(n):

    if (n == 0):
       return False

    while (n != 1):

            if (n % 4 != 0):
                return False
            n = n // 4
   
    return True

test_no = 15

if(isPowerOfFour(15)):

    print(test_no, 'is a power of 4')

else:

    print(test_no, 'is not a power of 4')