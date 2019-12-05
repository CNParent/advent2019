import urllib.request

def get(day, year, session):
    req = urllib.request.Request(f'https://adventofcode.com/{year}/day/{day}/input')
    req.add_header('cookie', f'session={session}')
    return urllib.request.urlopen(req).read().decode('utf-8').split()