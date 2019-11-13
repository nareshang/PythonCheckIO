def getdepthelem(orgarray, deparray, depth, pos):
    for elem02 in deparray:
        if isinstance(elem02, list):            
            if depth == 10:
                return None, None
            depth = depth + 1
            orgarray, pos = getdepthelem(orgarray,elem02,depth,pos)
        else:
            orgarray.insert(pos, elem02)
            pos = pos + 1
    return orgarray, pos
    
def flat_list(givenarray):    
    len1 = len(givenarray)    
    for index in range(0, len1):
        elem = givenarray[index]        
        if isinstance(elem, list):
            givenarray.remove(elem)
            givenarray, subindex = getdepthelem(givenarray,elem,0,index)                
    
    return givenarray

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')