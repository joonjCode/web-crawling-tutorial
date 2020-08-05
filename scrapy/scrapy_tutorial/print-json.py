import pprint

# Older version
'''
file = open('posts.json')
data = file.read()
print(data)

file.close()
'''


with open('posts.json', 'r') as f:
    print(f.read())