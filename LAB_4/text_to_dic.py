from collections import defaultdict
text_list = list(input("Input some text:"))

print(text_list)
dict = defaultdict(int)
for i in text_list:
    dict[i] += 1
    
  
print(dict)
