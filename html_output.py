class HtmlOutput(object):
    def output_html(self,datas):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<meta charset=\'utf-8\'>')
        fout.write('<body>')
        fout.write('<table>')

        for data in datas:
               # count = 0
                fout.write('<tr>')
                fout.write('<td>%s</td>' %data['number'])
                fout.write('<td>%s</td>' %data['smallNumber'])
                fout.write('<td>%s</td>' %data['name'])
                fout.write('<td>%s</td>' %data['EnglishName'])
                fout.write('<td>%s</td>' %data['credit'])
                fout.write('<td>%s</td>' %data['attributes'])
                fout.write('<td>%s</td>' %data['score'])
                fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()