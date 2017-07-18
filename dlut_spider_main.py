import url_manager, html_parser, html_download, html_output,csv_output
import csv

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        #self.output = html_output.HtmlOutput()
        self.output = csv_output.CsvOutput()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)#初始添加一条
        new_data = []
        try:
                print("craw:%s"%root_url)
                html_cont = self.download.download(root_url)
                new_data = self.parser.parse(root_url, html_cont)
                #print(new_data)
                #self.output.output_html(new_data)
                self.output.output_csv(new_data)
        except Exception as e:
                print(e)




if __name__=="__main__":
    root_url = "http://zhjw.dlut.edu.cn/menu/s_main.jsp"
    root_url_grade = "http://zhjw.dlut.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=6747"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url_grade)