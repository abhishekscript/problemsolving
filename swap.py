def swap(  a, b ):
    print( "Before Swap",a,b )
    backup = a
    a = b
    b = backup
     
    
    print("Post Swap",a,b)

def directSwap( a, b ):
    print("Before Swap",a,b)
    a,b=b,a
    print("Post Swap", a,b)



swap(10,20)
directSwap(10,20)
    