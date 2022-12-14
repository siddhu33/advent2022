import ast
import copy
from functools import cmp_to_key

def compare(list1: list, list2: list, level=0):
    l1c = copy.deepcopy(list1)
    l2c = copy.deepcopy(list2)
    while l1c and l2c:
        n1 = l1c.pop(0)
        n2 = l2c.pop(0)
        if isinstance(n1, int) and isinstance(n2,int):
            if n1 != n2:
                return 1 if n1 < n2 else -1
            
        elif isinstance(n1, list) and isinstance(n2, list):
            c1 = compare(n1,n2,level+1)
            if c1 != 0:
                return c1
        else:
            if isinstance(n1, int):
                c1 = compare([n1], n2, level=level+1)
            elif isinstance(n2, int):
                c1 = compare(n1, [n2], level=level+1)
            
            if c1 != 0:
                return c1
    
    if len(l1c) < len(l2c):
        return 1
    elif len(l1c) > len(l2c):
        return -1
    else:
        return 0
        
 
def main():
    true_pair_sum = 0
    packets = []
    for idx, group in enumerate(open("day13/day13.txt", "r").read().split("\n\n")):
        list1, list2 = [ ast.literal_eval(l) for l in group.split("\n") ]
        packets.extend([list1, list2])
        
        if compare(list1, list2) == 1:
            true_pair_sum += (idx+1)
            
    print(true_pair_sum)
    packets.extend([[[2]],[[6]]])
    packets.sort(key=cmp_to_key(compare), reverse=True)
    print((packets.index([[2]])+1)*(packets.index([[6]])+1))
    
    

if __name__ == "__main__":
    main()
    