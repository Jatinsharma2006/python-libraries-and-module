url="http://python.org/"


import urllib.request
with urllib.request.urlopen(url) as response:
    html=response.read()
    print(html)
    


import webbrowser
webbrowser.open_new_tab(url)
