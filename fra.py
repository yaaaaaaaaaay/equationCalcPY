

def reader(s, b):
    
    d = bool(False)
    c = bool(False)
    r = ""

    for i in range(len(s)):

        print (s)

        if (s[i].isnumeric() == True and c == False):

            r = r + s[i]

        else:
            c = True


        if ((s[i] == "," or s[i] == ".") and d == False):

            r = r + "."
            d = True


    return float(r)

#---------------------------#


def hah(&gogo):

    print (gogo)

    gogo = gogo + 55

    print (gogo) 

    return (gogo)


#a = str(input())


a = 2

hah(*a)

print (a)


#print (reader(a, 0))
