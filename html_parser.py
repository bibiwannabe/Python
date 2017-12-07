import re
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup
class HtmlParser(object):

    def parse(self, html_cont):
        datas = []
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='GBK')
        count = 0
        data_node = soup.find_all('td', align="center")
        # print(data_node)
        res_data = {}
        for data in data_node:
            counter = count

            if counter % 7 == 0 and count != 0:
                res_data = {}
                datas.append(res_data)
                # print(datas)

            if counter % 7 == 0:
                res_data['number'] = "".join(data.get_text().split())
                count = count + 1
            if counter % 7 == 1:
                res_data['smallNumber'] = "".join(data.get_text().split())
                count = count + 1

            if counter % 7 == 2:
                res_data['name'] = "".join(data.get_text().split())
                count = count + 1

            if counter % 7 == 3:
                res_data['EnglishName'] = "".join(data.get_text().split())
                count = count + 1

            if counter % 7 == 4:
                res_data['credit'] = "".join(data.get_text().split())
                count = count + 1

            if counter % 7 == 5:
                res_data['attributes'] = "".join(data.get_text().split())
                count = count + 1

            if counter % 7 == 6:
                res_data['score'] = "".join(data.get_text().split())
                count = count + 1

        return datas







