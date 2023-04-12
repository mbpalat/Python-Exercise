
farray = [1,[2,3,'null',4],['null'],5]
#farray = ([1,[2,3,4,4],[3],5])

strfarray = type(farray)
outarray = []

for i in farray:
    if(i != 'null' and i != 'nil'):
        str = type(i)
        if str == strfarray:
            for j in i:
                if(j != 'null' and j != 'nil'):
                    print(j)
                    outarray.insert(len(outarray),j)
        else:
            outarray.insert(len(outarray),i)
            print(i,type(i))

print(outarray)