from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import urllib.request
LOGIN_INFO = {
    'user_id': 'haya0206',
    'password': 'rladudgk12'
}
with requests.Session() as s:
    cnt=0
    login_req = s.post('http://codeup.kr/JudgeOnline/login.php', data=LOGIN_INFO)
    l_url = ""
    soup = ""
    while(1):
        print(cnt)
        if(cnt==0):
            url = "http://codeup.kr/JudgeOnline/status.php?user_id=haya0206&jresult=4"
            html = s.get(url)
            soup = BeautifulSoup(html.text, "html.parser")
            table = soup.find(id="result-tab")
        else:
            lll = l_url.find('ul', 'pager')
            ll = lll.find_all('a')
            ll = ll[2]['href']
            sss = ll.split('&')
            first = 0
            end = 0
            for i in sss:
                if(i.find('prevtop')!=-1):
                    end = int(i[i.find('prevtop')+8:])
                elif(i.find('top')!=-1):
                    first = int(i[i.find('top')+4:])
            if(first==end):
                break
            print(ll)
            url = "http://codeup.kr/JudgeOnline/"+ll
            html = s.get(url)
            soup = BeautifulSoup(html.text, "html.parser")
            table = soup.find(id="result-tab")
        for i in table.tbody.find_all("tr"):
            A = []
            for link in i.find_all("td"):
                A.append(link)
            idd = A[0].get_text(" ", strip=True)
            num = A[2].div.find_all("a")
            numm = num[0].get_text(" ", strip=True)
            fileName = "C:/Users/user/Desktop/aaaaaaaaaaaa/"+numm+".cpp"
            url = "http://codeup.kr/JudgeOnline/downsource.php?id="+idd
            req = s.get(url)
            file = open(fileName, 'wb')
            for chunk in req.iter_content(100000):
                file.write(chunk)
            file.close()
        cnt+=1
        l_url=soup
