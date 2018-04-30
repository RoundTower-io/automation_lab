letters = ['a', 'b', 'c']
print(letters[1]) #b
letters.extend(['d', 'e','f'])
print(letters[1]) #['a', 'b', 'c', 'd', 'e', 'f']

greek = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
print(greek['o']) #omega

greek = {'a': 'alpha', 'o': 'omega', 'g': 'gamma','e':{'epsilon':'zeta'}}
print(greek['e']['epsilon']) #zeta