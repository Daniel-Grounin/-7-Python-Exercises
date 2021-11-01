"""
Daniel Grounin
Dori Fourer
"""
#-----------Mission 1-------------#
def geometric_progression(a, q, n):
    """
    Mission 1:
    Function prints geometric sequence,
    start with 'a' in range of 'n' with jumps of 'q'.
    """
    if ((a or n) == 0):
       return 0
    else:
        for i in range(n):
            print(a*q**i)


#-----------Mission 2-------------#
def reverse(x):
    """
    Mission 2:
    Function reverse a number
    """
    rev=0
    if(x==0):
       return 0
    else:
       while x>0:
           remider=x%10
           rev=(rev*10)+remider
           '''Floor division'''
           x=x//10
    return (rev)


#-----------Mission 3-------------#
def removeDigit(Number,n):
    """
    Mission 3:
    Function that removes the 'n' digit from the 'Number' var
    """
    newNumber,count,rev=0,0,0
    if (Number or n)< 0:
        return 0
    else:
        while (Number>0):
            lastdigit = Number % 10
            if (lastdigit==n):
                Number=Number//10
            else:
                rev=(rev*10)+lastdigit
                Number=Number//10
                newNumber=newNumber+(lastdigit*10**count)
                count=count+1
        return newNumber



#-----------Mission 4-------------#
def figure(n):
    """
    Mission 4:
    Function that prints reverse triangle contains from numbers
    """
    i = 1
    j = n*2-2
    for i in range(0,n):
        print(' '*j, end=" ")
        j = j - 2
        for k in range(i+1):
                print(k+1, end=" ")
                k = k + 1
        i = i + 1
        print(" ")


#-----------Mission 5-------------#
def printEvenDigits(Number):
        """
        Mission 5:
        Recursive func prints only even digits
        """
        newNumber, count, rev = 0, 0, 0
        while (Number>0):
            lastdigit = Number % 10
            if (lastdigit %2 ==0):
                rev = (rev * 10) + lastdigit
                newNumber = newNumber + (lastdigit * 10 ** count)
                count = count + 1
                print(newNumber % 10, end='')
            return printEvenDigits(Number//10)


#-----------Mission 6-------------#
def mulPrimeNumbers(Number):
        """
        Mission 6:
        Function identify prime numbers and return sum of them.
        """
        sum = 1
        while (Number>0):
            lastdigit = Number % 10
            if (lastdigit ==2 or lastdigit ==3 or lastdigit == 5 or lastdigit == 7 ):
                sum=sum*lastdigit
                Number=Number//10
            else:
                Number=Number//10

        return sum


#-----------Mission 7-------------#
def luckyNumber(num):
    """
    Mission 7:
    boolean function that defines lucky numbers , we used two for loops
    to and compare two different sums.
    """
    sum1,sum2=0,1
    if (num <0):
        return 0
    else:
        for i in range(3):
            lastdigit=num%10
            sum1=sum1+lastdigit
            num=num//10
        for j in range(3):
            lastdigit2=num%10
            sum2=sum2*lastdigit2
            num=num//10
        if(sum1==sum2):
            return True
        return False

