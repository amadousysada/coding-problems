def is_add_up(elements, k):
    seen = []
    for i in elements:
        if k-i in seen:
            return True
        seen.append(i)
    return False

if __name__=="__main__":
    elements = [7, 15, 3, 10]
    assert is_add_up(elements, 17) == True
    assert is_add_up(elements, 147) == False
