def split_and_reverse(word):
    #start
    # split 
    temp =word.split(" ")
    # print(temp)
    final = ""
    for i in range(0,len(temp),+1):
        #reverse word in i
        final = final + " "+ reverse(temp[i])
    print(final)
    #stop

def reverse(x):
    #start
    result = ""
    for i in x:
        result = i + result
    return result
    #stop

split_and_reverse("Abc def")