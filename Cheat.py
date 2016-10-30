import requests

payload = {'scores': [{'pos': 1, 'score': 2500, 'name': "Soroosh Zamani", 'current': True}], 'new': True}
headers = {'Host': 'tbot.xyz',
           'Connection': 'keep-alive',
           'Content-Length': '213',
           'Origin': 'https://tbot.xyz',
           # 'User-Agent:': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
           'Content-Type': 'text/plain;charset=UTF-8',
           'Accept': '*/*',
           'Referer': 'https://tbot.xyz/math/',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'en-US,en;q=0.8,fa;q=0.6,fr;q=0.4',
           }

r = requests.post("https://tbot.xyz/api/setScore",
                  data='data=eyJ1Ijo2NjA4MzY1OSwibiI6IlNvcm9vc2ggWmFtYW5pIiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6IjIyMTYzNzQxMjI0MjU2ODk3ODIiLCJpIjoiQkFBQUFPOFBFQUJKRW5jRTlidHlMSnNPRGdvIn0wOWMwMjc3NWFiZWQ2OWQwMWQ3YjAzMGZkMTY1MDE4Nw%3D&score=2500',
                  json=payload,
                  headers=headers)
# You should replace the data argument, name, Origin, Content-Length with the appropriate amounts