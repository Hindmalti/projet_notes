from bs4 import BeautifulSoup, SoupStrainer

all_notes = {}

with open("./res.html") as html_file:

    parse_only = SoupStrainer(id=["main"])

    soup = BeautifulSoup(html_file, 'html.parser', parse_only=parse_only)

    divs = soup.findAll("table", {"class": "table table-bordered table-splited table-hover"})  
    for div in divs:
        tbodies = div.findAll('tbody')
        for tbody in tbodies:
            trs = tbody.findAll('tr')
            for tr in trs:
                td = tr.findAll('td')
                matiere = td[0].text
                note = td[1].text
                all_notes[matiere] = note
    print(all_notes)
            