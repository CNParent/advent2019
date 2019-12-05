import urllib.request
req = urllib.request.Request('https://adventofcode.com/2018/day/2/input')
req.add_header('cookie', 'session=53616c7465645f5f3b11f98d4ad0d173b5924fafd79b0c5e9be05963d42e40e6c4d7f30f10a77eab04467ce7d4f99424')
response = urllib.request.urlopen(req).read().decode('utf-8')
values = response.split()

def differBy(a, b):
    return sum(map(lambda x, y: x != y, a, b))

box1 = {}
box2 = {}
for a in values:
    for b in values:
        if(differBy(a, b) == 1):
            box1 = a
            box2 = b

print(f'{box1} and {box2}')
print(''.join(map(lambda a, b: a if a == b else '', box1, box2)))