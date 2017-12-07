import csv
class CsvOutput(object):
    def output_csv(self, datas):
        if(datas!=None):
            fout = open('grade.csv', 'w', newline='')
            headers = ['number', 'smallNumber', 'name', 'EnglishName','credit','attributes','score']
            writer = csv.writer(fout)
            writer.writerow(headers)
            for i in range(len(datas)):
                cont = []
                cont.append(datas[i].get('number'))
                cont.append(datas[i].get('smallNumber'))
                cont.append(datas[i].get('name'))
                cont.append(datas[i].get('EnglishName'))
                cont.append(datas[i].get('credit'))
                cont.append(datas[i].get('attributes'))
                cont.append(datas[i].get('score'))
                print(cont)
                writer.writerow(cont)
            fout.close()