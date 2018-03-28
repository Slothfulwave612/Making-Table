x = 'Dehradun,,,India'
print(x)
for i in x:
    if(i == ','):
        x = x.replace(',', '-')
print(x)
