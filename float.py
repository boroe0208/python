#get a string of numbers from the user and convert it to a list of those numbers in the order it was writen in  # noqa: E501

num_list =input('what is your list of numbers you want to sort? ')
num_list = 


#sort the list of numbers from least to greatest
def insetion_sort(num_list):
  
  for i in range(1,len(num_list)):
    j =i
    while num_list[j-1]> num_list[j] and j>0:
      num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
      j-=1
      
      
    
    
insetion_sort(num_list)

  





print(num_list)