import urllib.request
req = urllib.request.Request('https://adventofcode.com/2018/day/2/input')
req.add_header('cookie', 'session=53616c7465645f5f3b11f98d4ad0d173b5924fafd79b0c5e9be05963d42e40e6c4d7f30f10a77eab04467ce7d4f99424')
response = urllib.request.urlopen(req).read().decode('utf-8')
twos = 0
threes = 0

for value in response.split():
    plustwo = False
    plusthree = False
    while len(value) != 0:
        c = value[0]
        n = value.count(c)
        plustwo = plustwo or n == 2
        plusthree = plusthree or n == 3
        value = value.replace(c, '')
    
    if(plustwo): 
        twos += 1
    if(plusthree): 
        threes += 1

print(f'twos: {twos}, threes: {threes}, total: {twos * threes}')