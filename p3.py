list=[2,1,3,-4,7,-1,0,-7,9,6,2,66,5,-6,10]
def even_odd(l):
    length=len(l)
    even_list=[]
    odd_list=[]
    for i in l:
        if length>1:
            if i%2==0:
                even_list.append(i)
            elif i%2!=0:
                odd_list.append(i)
            else:
                print("List is enmpty or Containing only one element")
    print(f"Even numbers are: {even_list}")
    print(f"\nOdd numbers are: {odd_list}")
even_odd(list)
def positive_negative(l):
    length=len(l)
    positive_list=[]
    negative_list=[]
    for i in l:
        if length>1:
            if i>=0:
               positive_list.append(i)
            else:
               negative_list.append(i)
        else:
            print("List is enmpty or Containing only one element")
    print(f"Positive Numbers are: {positive_list}\n")
    print(f"Negative Numbers are: {negative_list}")
positive_negative(list)
def sum_digits(l):
    length=len(l)
    total_sum=0
    for i in l:
        if length>1:
           total_sum+=i
        else:
            print("List is enmpty or Containing only one element")
    print(f"\nSum of digits is: {total_sum}")
sum_digits(list)
def largest_smallest(l):
    length=len(l)
    if length>1:
       largest=max(l)
       smallest=min(l)
       print(f"\nLargest number is: {largest}")
       print(f"\nSmallest number is: {smallest}")
    else:
        print("List is enmpty or Containing only one element")
largest_smallest(list)
def duplicates_remove(l):
    length=len(l)
    unique_list=[]
    if length>1:
       list=set(l)
       unique_list.append(list)
       print(f"\nAfter duplicates removed: {unique_list}")
    else:
        print("List is enmpty or Containing only one element")
duplicates_remove(list)
def second_largest(l):
    length=len(l)
    largest=0
    second_largest=0
    for i in l:
        if length>1:
            if i>=largest:
               largest=i
            elif i<largest and i>second_largest:
                   second_largest=i
        else:
            print("List is enmpty or Containing only one element")
    print(f"\nSecond Largest element is:{second_largest} ")
second_largest(list)
    
