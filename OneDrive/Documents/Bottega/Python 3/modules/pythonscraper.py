# from requests import get

# #set headers

# url = 'http://www.dailysmarty.com/topics/python'
# response = get(url)
# print(response.text[:500])

# http://www.dailysmarty.com/posts/installing-anaconda-python-data-science-platform
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/topics/anaconda-python
# http://www.dailysmarty.com/topics/machine-learning
# http://www.dailysmarty.com/posts/python-libraries-to-import-for-data-science-programs
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/topics/data-science
# http://www.dailysmarty.com/topics/machine-learning
# https://dailysmarty-production.s3.amazonaws.com/uploads/post/img/76/post_thumb_Snip20170713_12.png
# http://www.dailysmarty.com/posts/shortcut-for-opening-the-object-inspector-in-python-spyder
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/topics/anaconda-python
# http://www.dailysmarty.com/topics/spyder-python
# http://www.dailysmarty.com/topics/machine-learning
# http://www.dailysmarty.com/posts/python-script-for-replacing-missing-data-in-a-machine-learning-algorithm
# http://www.dailysmarty.com/topics/machine-learning
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/posts/python-script-for-pulling-in-the-same-column-from-an-array-of-arrays
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/posts/how-to-implement-fizzbuzz-in-python
# http://www.dailysmarty.com/topics/fizzbuzz
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/posts/how-to-think-like-a-computer-scientist
# http://www.dailysmarty.com/topics/computer-science
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/topics/programming
# http://www.dailysmarty.com/posts/base-case-example-for-how-to-test-a-python-class
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/topics/tdd
# http://www.dailysmarty.com/posts/installing-and-working-with-pipenv
# http://www.dailysmarty.com/topics/pipenv
# http://www.dailysmarty.com/topics/python
# http://www.dailysmarty.com/posts/steps-for-building-a-flask-api-application-with-python-3
# http://www.dailysmarty.com/topics/flask
# http://www.dailysmarty.com/topics/tutorial
# http://www.dailysmarty.com/topics/python






# #import libs
# #geturl



import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if "post" in url:
             url = url.split('/')[-1]
             url = url.replace('-', ' ')
             url = titleize(url)
             titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        post_formatter(link.get('href'))
    return titles



r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)