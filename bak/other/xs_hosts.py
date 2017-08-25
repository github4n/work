input = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'r')
lines = input.readlines()
print(lines)
input.close()
liness = []
output = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'w')
for line in lines:
    if line[0] != '#':
        line = '#' + line
    liness.append(line)
output.writelines(liness)
output.close()
