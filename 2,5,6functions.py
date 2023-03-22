"""def separator(list1):
    c='"'
    for i in range(len(list1)):
        if i!=len(list1)-1:
            c=c+list1[i]+","
        else:
         c=c+list1[i]+'"'
    print(c)
list1=list(map(str, input().split(",")))
separator(list1)"""

"""def funr(list1):
    c=''
    for i in range(len(list1)):
     if i!=len(list1)-1:
        c=c+list1[i]+separator
    else:
        c=c+list1[i]
    print(c)
list1=list(map(str, input().split(",")))
separator=input("enter the separator")
funr(list1)"""
"""def function(l,d_small,d_caps):
 string=input("enter the string")                    #get the input string from the user
 for i in range(0,26):                               #this loop iterate and update the keys and values of lowercase alphabets & ascii values in d_small
    a=chr(97+i)
    b=97+i
    d_small.update({a:b})
 for i in range(0,26):                               #this loop iterate and update the keys and values of uppercase alphabets & ascii values in d_caps
    a1=chr(65+i)
    b1=65+i
    d_caps.update({a1:b1})
 print("list of ascii codes:")                      # print the list of ascii codes                                              # create an empty list to store the ascii values for the given string
 for i in range(len(string)):                       #this loop access the elements  in a string
    if string[i] >= "a" and string[i] <= "z":      # check the condition
        l.append(d_small[string[i]])               #if the above condition is true add the ascii values of that  lowercase alphabet in l
    else:
        l.append(d_caps[string[i]])                #otherwise append the ascii vales of uppercase in l
 print(l)
d_small={}                                          #create an empty dict to store the lowercase alphabets and ascii values  in form of keys value pair
d_caps={}                                           #create an empty dict to store the uppercase alphabets and ascii values  in form of keys value pair
l=[]
function(l,d_small,d_caps)"""
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m <list[0] else list[0]

list=[100,22,3,4,4,4]
print(Max(list))





p