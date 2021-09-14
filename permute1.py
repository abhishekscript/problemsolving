

def permute( data, left, right , pm ):
    
    if left==right:
        pm.append( list(map(int, data) ))
    
    else:
        for i in range(left, right):
            data[left], data[i] = data[i], data[left]
            permute( data, left+1, right,pm )
            data[left], data[i] = data[i], data[left]
pm=[]
nums = [1,2,3]
permute( list(map(str, nums)), 0 , len(nums) ,pm )
print(pm)

