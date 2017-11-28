import requests
from bs4 import BeautifulSoup

def crawler(max_pages):
    final_d = []
    start = []
    list = []
    page = 1
    while page <= max_pages:
        url = 'http://www.wikicfp.com/cfp/call?conference=data%20mining&page=' + str(page)
        source_code = requests.get(url)
        all_text = source_code.text
        soup = BeautifulSoup(all_text, "html.parser")
        final_d = []
        start = []
        table5 = soup.findAll("table")[5]
        for record in table5.findAll(["tr"]):
            if record.attrs['bgcolor' or 'valign'] != '#bbbbbb':
                for data in record.findAll("td"):
                    if record.findAll("td"):
                        #print(data.string)
                        start.append(data.string)
                        if len(start) == 6:
                            indexes = [2, 3, 5]
                            for index in sorted(indexes, reverse=True):
                                del start[index]
                            final_d.append(start)
                            start = []
        return final_d

    
mine = crawler(1)
print(mine)