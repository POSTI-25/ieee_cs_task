'''Design a stack that supports the following operations in O(1) time and O(n) space:
push(x): Pushes element x onto the stack.
pop(): Removes the top element of the stack.
top(): Returns the top element without removing it.
getMin(): Returns the smallest element in the stack.
getMax(): Returns the largest element in the stack.
'''

# list1 = []  
# list_min = []  
# list_max = []  

# def push(x):
#     list1.append(x)
    
#     if len(list_min) == 0 or x <= list_min[-1]:
#         list_min.append(x)  
    
#     if len(list_max) == 0 or x >= list_max[-1]:
#         list_max.append(x)  

# def pop():
#     popped_value = list1.pop()
    
#     if popped_value == list_min[-1]:
#         list_min.pop()
    
#     if popped_value == list_max[-1]:
#         list_max.pop()
    
#     return list1
    
# def top():
#     return list1[-1]

# def get_min():
#     return list_min[-1]

# def get_max():
#     return list_max[-1]

# def main():
#     choice = 0
#     while choice < 7:   
#         choice = int(input('Enter the Choice:'))
#         if choice == 1:
#             x = int(input("enter element to be added: "))
#             push(x)
#         elif choice == 2:
#             if len(list1) == 0:
#                 print("stack is empty, cant pop.")
#             else:
#                 pop()
#                 print("the top element has been removed.")
#         elif choice == 3:
#             print("top element: ",top())
#         elif choice == 4:
#             print(get_min())
#         elif choice == 5:
#             print(get_max())
#         elif choice == 6:
#             if len(list1) == 0:
#                 print("stack is empty.")
#             else:
#                 print("stack: ",list1)
#         else:
#             print("invalid choice")
#         # break
#     # choice += 1  

# print("1) add element to stack")
# print("2) remove top element ")
# print("3) view the top element ")
# print("4) view minimum value in the stack ")
# print("5) view maximum value in the stack ")
# print("6) view stack ")

# main()


'''Interval Merger: Maintain a set of non-overlapping intervals and efficiently merge them when new intervals are added.

Operations:

addInterval(start, end): Adds a new interval [start, end]. If it overlaps with existing intervals, merge them into one. Ensures the set of intervals remains non-overlapping and sorted.

getIntervals(): Returns the current set of non-overlapping, merged intervals in ascending order.
'''

l1 = []
new1 = []
merge = []

def add(a, b):
    l = [a, b]
    l1.append(l)

def get_interval(l1):
    
    l1.sort()
    for i in range(len(l1)):
        if not merge or merge[-1][1] < l1[i][0]:
            merge.append(l1[i])
        else:
            merge[-1][1] = max(merge[-1][1], l1[i][1])

    new1 = merge

    print("Merged intervals:", new1)

add(1, 2)
add(3, 5)
add(4, 6)
add(7, 8)

get_interval(l1)