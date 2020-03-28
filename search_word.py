from urllib.request import urlopen
from bs4 import BeautifulSoup

def getHtml(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, 'html.parser')
    return bsObject

def getDefinition(word):
    url = 'https://dic.daum.net/search.do?q=' + word + '&dic=eng'

    # url = 'https://dic.daum.net/search.do?q=test&dic=eng'
    # url = 'https://dic.daum.net/search.do?q=hello&dic=eng'

    html = getHtml(url)

    temp = html.find_all(class_='list_search')
    definition_list = []

    if temp:
        temp = temp[0].find_all(class_='txt_search')
        for key_tag in temp:
            definition_list.append(key_tag.text)
    else:
        meta = html.head.find_all('meta')
        url = 'https://dic.daum.net' + meta[3].get('content').split('URL=')[1]
        html = getHtml(url)

        temp = html.find_all(class_='list_mean')[0].find_all(class_='txt_mean')
        for key_tag in temp:
            definition_list.append(key_tag.text)

    return definition_list


# if __name__ == '__main__':
#     definition_list = getDefinition('ambiguous')
#     print(definition_list)
