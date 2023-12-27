incom = open('text2.txt')
dict_urls = {}
list_urls = []
for line in incom:
    name_url = line[11:].strip()
    list_urls.append(name_url)

for name_url in list_urls:
    hm = list_urls.count(name_url)
    dict_urls[name_url] = hm

print(max(dict_urls, key=dict_urls.get), 'посещён:', max(dict_urls.values()), 'раз(а)')
