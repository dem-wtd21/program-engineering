lines = ['one','two','three']
with open('rd.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run' +line)
    print('Done!')    