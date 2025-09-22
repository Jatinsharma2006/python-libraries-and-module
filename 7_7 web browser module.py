url="http://python.org/"
url2="https://www.w3schools.com/"
url3="https://www.site24x7.com/"


import webbrowser
webbrowser.open(url)
webbrowser.open_new(url2)


c=webbrowser.get('FireFox')
c.open_new_tab(url3)
