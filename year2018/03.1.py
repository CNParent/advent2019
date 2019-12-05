import urllib.request
req = urllib.request.Request('https://adventofcode.com/2018/day/3/input')
req.add_header('cookie', 'session=53616c7465645f5f3b11f98d4ad0d173b5924fafd79b0c5e9be05963d42e40e6c4d7f30f10a77eab04467ce7d4f99424')
values = urllib.request.urlopen(req).read().decode('utf-8').split('\n')

class Claim:
    identifier
    left
    top
    width
    height

def parse(x):
    properties = x.split()
    print(properties)
    postition = properties[2].split(',')
    size = properties[3].split('x')
    return Claim {  
        identifier: properties[0].replace('#', ''),
        left: int(postition[0]),
        top: int(postition[1].trim(':')),
        width: int(size[0]),
        height: int(size[1]) 
    }

claims = list(map(parse, values))
print(claims)