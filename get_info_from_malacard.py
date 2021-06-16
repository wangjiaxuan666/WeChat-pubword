from bs4 import BeautifulSoup
import pandas as pd

def read_file(file):
    htmlfile = open(file, 'r', encoding='utf-8')
    #读取html的句柄内容
    htmlhandle = htmlfile.read()
    #使用Beautifulsoup解析
    soup = BeautifulSoup(htmlhandle, features='lxml')
    return(soup)

def get_info(soup,id):
    info = soup.find("table",id=id)
    info_data = pd.read_html(str(info))
    info_data[0].to_excel(id+'.xlsx',index=False)



def main():
    soup = read_file('need.html')
    id = ["RelatedDiseases-table",
          "MaladiesUnifiedCompounds-table",
          "ClinicalTrial-table",
          "Publications-table",
          "RelatedGenes-table",
          "ClinVarVariations-table",
          "CnvdVariations-table",
          "de_genes-table",
          "Pathway-table",
          "go_proc-table"
          ]
    for id in id:
        get_info(soup,id)

if __name__ == "__main__":
    main()