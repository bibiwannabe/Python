import html_parser, csv_output, loginDownload
import csv

import input_window


class SpiderMain(object):
    def __init__(self):
        self.getinfo = input_window.window()
        self.download = loginDownload.Download()
        self.parser = html_parser.HtmlParser()
        self.output = csv_output.CsvOutput()

    def craw(self):
        new_data = []
        try:
                fuck_data = self.getinfo.input_information()
                number = fuck_data['number']
                password = fuck_data['password']
                html_cont = self.download.fuck_login(number,password)
                new_data = self.parser.parse(html_cont)
                print(new_data)
                self.output.output_csv(new_data)
        except Exception as e:
                print(e)


if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.craw()