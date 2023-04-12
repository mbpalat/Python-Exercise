
alpabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sentence = "The quick brown fox jumps over the lazy dog"
isexistcheck = 0

def checkPanagram(val):
    for ch in sentence:
        if ch.lower() == val:
            exist = True
            break
        else:
            exist = False
    return exist

for i in alpabetList:
    exist = checkPanagram(i)
    if exist == False:
        isexistcheck = isexistcheck+1

if isexistcheck > 0:
    print('Not Panagram')
else:
    print('Panagram')



