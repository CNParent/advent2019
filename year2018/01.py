import urllib.request
req = urllib.request.Request('https://adventofcode.com/2018/day/1/input')
req.add_header('cookie', 'session=53616c7465645f5f3b11f98d4ad0d173b5924fafd79b0c5e9be05963d42e40e6c4d7f30f10a77eab04467ce7d4f99424')
response = urllib.request.urlopen(req).read().decode('utf-8')
results = []

total = 0
found = False
while not found:
    print(total)
    for value in response.split():
        total += int(value)
        if total in results:
            found = True
            print(total)
            break

        results.append(total)