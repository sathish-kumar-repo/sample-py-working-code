import requests


r = requests.get("https://www.python.org")
print(r)
print(r.status_code)  # 200

print(r.text)
# open('toWriteSampleFileUsingRequestModule.html','w',encoding="utf-8").write(r.text)

# to download img from website
r1 = requests.get(
    "https://banner2.cleanpng.com/20180412/kye/kisspng-python-programming-language-computer-programming-language-5acfdc3636bac7.8891188615235717662242.jpg"
)
if r1.status_code == 200:
    print('Respond')
    with open("sample.jpg", "wb") as f:
        f.write(r1.content)
else:
    print('Not Respond')
