def product_of_others(elements):
    left = []
    right = []

    for el in elements:
        if not left:
            left.append(el)
        else:
            left.append(left[-1]*el)

    for el in elements[::-1]:
        if not right:
            right.append(el)
        else:
            right.append(el*right[-1])
    right=right[::-1]

    res =[]
    for i in range(len(elements)):
        if i==0:
            res.append(left[-1])
        elif i==len(elements)-1:
            res.append(left[i-1])
        else:
            res.append(left[i-1]*right[i+1])
    
    return res

if __name__=="__main__":
    elements = [1, 2, 3, 4, 5]
    assert product_of_others(elements) == [120, 60, 40, 30, 24]
    


