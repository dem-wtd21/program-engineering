with open('rd.txt','a+') as f:
    f.write('\nIm additional line')

with open('rd.txt', 'r') as f:
    result =f.readlines()
    print(result)