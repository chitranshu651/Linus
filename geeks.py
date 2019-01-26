from googlesearch import search
import firefox
search_string= input() + " geeksforgeeks"
d = search(search_string, num=10, lang= 'en', stop=1, pause =2.0)
for i in range(3):
    parameter['url']= i
    open_url(parameter)
