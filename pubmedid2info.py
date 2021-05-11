import requests
from bs4 import BeautifulSoup
from openpyxl import workbook

def pubmedid2info(list):
    url = 'https://pubmed.ncbi.nlm.nih.gov/'
    """创建空白列表"""
    DOI = []
    JU = []
    DES = []
    TITLE = []
    SITE = []
    AUTHOR = []
    """开始分析"""
    for id in list:
        website = url + id
        r = requests.post(website)
        soup = BeautifulSoup(r.content, 'html5lib')
        doi = soup.find("span",class_="citation-doi")
        DOI.append(doi.text.replace(' ',''))
        ju = soup.find("button",{"ref":"linksrc=journal_actions_btn"})
        JU.append(ju.text.replace(' ',''))
        des = soup.find("div",{"class":"abstract-content selected"})
        DES.append(des.p.text.replace(' ',''))
        title = soup.find("meta",{"name":"twitter:title"})
        TITLE.append(title["content"].replace(' ',''))
        site = soup.find("meta",{"name":"twitter:url"})
        SITE.append(site["content"].replace(' ',''))
        author = soup.find("meta",{"name":"citation_authors"})
        AUTHOR.append(author["content"].replace(' ',''))        
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['DOI号','摘要','期刊','标题','网址','作者'])
    for i in range(len(JU)):
        ws.append([DOI[i],DES[i],JU[i],TITLE[i],SITE[i],AUTHOR[i]])
    wb.save("test.xlsx")

"""测试输入"""
pubmedid = ["26735580","25581428"]

def main():
    pubmedid2info(pubmedid)

if __name__ == "__main__":
    main()
