#Note, use user-agent. Because without it, the website will refuse get request.
#https://www.reddit.com/r/learnpython/comments/4eaz7v/error_503_when_trying_to_get_info_off_amazon/
#!python 3.9.2
#requests == 2.5.1 ,beautifulsoup4 == 4.9.3,openpyxl version==2.6.2
#Description: scrape stock price of FOCUSP and RHB market from klsescreener and write the data into an excel file

import webbrowser,requests,bs4,openpyxl
from datetime import date
print('Searching...')
headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
res1 = requests.get("https://www.klsescreener.com/v2/stocks/view/0157/focus-point-holdings-berhad", headers=headers)
res2 = requests.get("https://www.klsescreener.com/v2/stocks/view/1066/rhb-bank-berhad", headers=headers)

res1.raise_for_status()
res2.raise_for_status()

soup1 = bs4.BeautifulSoup(res1.text,'html.parser')
soup2 = bs4.BeautifulSoup(res2.text,'html.parser')

fcsp = soup1.select('#price')
rhb = soup2.select('#price')

def getPrice(quote):
    return quote[0].getText()

print("Price of focusp is",getPrice(fcsp))
print("Price of rhb is",getPrice(rhb))

today = date.today()
ftoday = today.strftime('%d/%m/%Y')
try:
    wb = openpyxl.load_workbook('stockprice.xlsx')
    sheet= wb['Sheet']
    maxrow = sheet.max_row+1
    sheet.cell(row=maxrow,column=1).value = ftoday
    sheet.cell(row=maxrow,column=2).value = getPrice(fcsp)
    sheet.cell(row=maxrow,column=4).value = ftoday
    sheet.cell(row=maxrow,column=5).value = getPrice(rhb)
    wb.save('stockprice.xlsx')
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'FOCUSP'
    sheet['D1'] = 'RHB'
    print('file created')
    print("Quit this program and run it again please")
    wb.save('stockprice.xlsx')

