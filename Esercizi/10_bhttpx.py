import httpx
p = httpx.post("http://127.0.0.1:5000/insertincomes", json={"description":"lottery","amount":80})
r = httpx.get('http://127.0.0.1:5000/incomes')

print(p.status_code)

print(r.json())

