# Python code to remove duplicate elements from a list
def Remove(props):
    final_list = []
    for num in props:
        if num not in final_list:
            final_list.append(num)
    
    return final_list    


# Driver Code
numbers = [1,2,2,3,4,5,6,4,3,5,2,5]
print(Remove(numbers))
