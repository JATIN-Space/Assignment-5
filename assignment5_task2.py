
original_list=[1,2,3,4,5,6,7,8,9,10]
extracted_list=[]
i=0
while i<5:
    extracted_list.append(original_list[i])
    reversed_list=extracted_list[::-1]
    i=i+1
print("original list:",original_list)
print("extracted list:",extracted_list)
print("reversed list:",reversed_list)
