from bs4 import BeautifulSoup
from datetime import datetime


if __name__ == "__main__":
    f = open('data.txt', 'w')
    f.write("id \t date \t amount-paid \t views \t city \t state \t \
        department \t transaction \n")
    # f.close()
    # f = open('data.txt', 'a')

    #370 not working
    for num in range(0, 1001, 10):
        if num == 370:
            continue
        print(num)
        
        # read html
        doc = "webdocs/bribe" + str(num) + ".html"
        html_doc = open(doc, 'r')
        soup = BeautifulSoup(html_doc, 'html.parser')

        #get information from html
        unid = soup.find_all("span", {"class": "unique-reference"})
        date = soup.find_all('span', {'class': 'date'})
        amountpaid = soup.find_all('li', {'class': 'paid-amount'})
        views = soup.find_all('li', {"class": "views"})
        city = soup.find_all('a', {"class": "location"})

        department = soup.find_all('li', {"class": "name"})
        transaction = soup.find_all('li', {"class": "transaction"})
        

        #read all entries
        data_len = len(date)
        for i in range(data_len):
            #id
            w = unid[i].get_text()

            #date
            x = date[i].get_text()
            x = x.replace(",", "")
            x = x.split()
            x[0] = x[0][:3]
            x = x[0] + " " + x[1] + " " + x[2]
            x = str(datetime.strptime(x, "%b %d %Y")).split()[0]

            #amount-paid
            y = amountpaid[i].get_text().split()[-1]
            y = y.replace(',', '') # clean data
            z = views[i].get_text().split()[0]

            #city/state
            c = city[i].get_text().replace("\n", "")
            c = c.replace(" ", "").split(sep=",")
            s = c[-1]
            c = c[0]

            #department
            d = department[i].get_text()
            d = d.replace("\n", "")
            d = d.replace(" ", "-")
            if d == "":
                d = "null"

            #transaction
            t = transaction[i].get_text()
            t = t.replace("\n", "")
            t = t.replace(" ", "-")
            if t == "":
                t = "null"

            #write to text file (id date amount-paid views city state)
            row = w + "\t" + x + "\t" + y + "\t" + z + "\t" + c + "\t" \
                + s + "\t" + d + "\t" + t + '\n'

            #write to file
            f.write(row)
        
    #close file
    f.close()