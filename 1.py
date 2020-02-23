import string
vowels = "aeyuioAEYUIOαειοωυηΑΕΙΟΩΥΗίώόάύέ"
f = open("python.txt", "r")
my_list=[]

words = f.read().split()

for word in words:
    
    for ch in vowels:
            word = word.replace(ch, '') 
    my_list.append(word[::-1]) 
    my_list.sort(key=len)  
    my_list.reverse() 



my_list = [''.join(c for c in s if c not in string.punctuation) for s in my_list]

print(my_list[0:5]) 