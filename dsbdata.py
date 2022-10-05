import requests
from bs4 import BeautifulSoup


class dsbdata:
    def getData(url, klasse):
        data = []
        
        html = requests.get(url).text
        soup = BeautifulSoup(html,'html.parser')
            
        ## Find Table
        
        html_table_list = soup.find_all("table")
        
        html_table = ""
        listelement = -1
        
        for i in html_table_list:
            listelement = listelement + 1
            if "Vertretungs-Text" in i.text and f"{klasse}" in i.text:
                break
        
        html_table = html_table_list[listelement]
        
        # Find Date
        
        html_data = soup.find("body").find_all(["table","center"])
        
        date_index = html_data.index(html_table)-2
        
        global date
        
        date = html_data[date_index].text.split(",")[0]

        
        # for getting the header from
        # the HTML file
        list_header = []
        header = html_table.find("tr")
        
        for items in header:
            try:
                list_header.append(items.get_text())
            except:
                continue
        
        # for getting the data 
        HTML_table_data = html_table.find_all("tr")[1:]
        
        for element in HTML_table_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text())
                except:
                    continue
            data.append(sub_data)
        
        return data


    def getFach(fach):
        fachList = {
            "D": "Deutsch",
            "M": "Mathe",
            "B": "Biologie",
            "Ku": "Kunst",
            "C": "Chemie",
            "D": "Deutsch",
            "E": "Englisch",
            "Ev": "Evangelischer Religionsunterricht",
            "K": "Katholischer Religionsunterricht",
            "Eth": "Ethik",
            "F": "Französisch",
            "G": "Geschichte",
            "Inf": "Informatik",
            "L": "Latein",
            "M": "Mathe",
            "Mu": "Musik",
            "Ph": "Physik",
            "Sm": "Sport M",
            "Sw": "Sport W"
        }
        
        if fach in fachList:
            return fachList.get(fach)
        else:
            return fach

    def getVertretungen(data, klasse):
        vertretungen_count = 0
        
        Vertretungen = [[],""]
        
        Vertretungen[1] = date
        
        for i in data:
            if klasse in i[0]:
                vertretungen_count = vertretungen_count + 1
                if i[5] == "Ausfall":
                    if i[0] == klasse:
                        Vertretungen[0].append(f"{i[3]} fällt in der {i[1]}ten Stunde aus.")
                    else:
                        Vertretungen[0].append(f"{i[3]} fällt in der {i[1]}ten Stunde für {i[0]} aus.")
                elif i[5] == "Veranstaltung":
                    if i[0] == klasse:
                        Vertretungen[0].append(f"Veranstaltung in der {i[1]}ten Stunde im Raum {i[4]} für {i[0]}.")
                    else:
                        Vertretungen[0].append(f"Veranstaltung in der {i[1]}ten Stunde im Raum {i[4]} für {i[0]}.")
                else:
                    if i[0] == klasse:
                        if i[2] == i[3]:
                            Vertretungen[0].append(f"{dsbdata.getFach(i[2])} {i[5]} in der {i[1]}ten Stunde im Raum {i[4]}.")
                        else:
                            Vertretungen[0].append(f"{dsbdata.getFach(i[2])} statt {dsbdata.getFach(i[3])} in der {i[1]}ten Stunde im Raum {i[4]}. ({i[5]})")
                    else:
                        if i[2] == i[3] or i[3] == "":
                            Vertretungen[0].append(f"{dsbdata.getFach(i[2])} {i[5]} in der {i[1]}ten Stunde im Raum {i[4]} für {i[0]}.")
                        else:
                            Vertretungen[0].append(f"{dsbdata.getFach(i[2])} statt {dsbdata.getFach(i[3])} in der {i[1]}ten Stunde im Raum {i[4]} für {i[0]}. ({i[5]})")
                    
        if vertretungen_count == 0:
            Vertretungen[0].append("\nKeine Vertretungen.")
        #else :
            #Vertretungen[0].append(f"\nDas sind {vertretungen_count} Änderungen.")
        
        return Vertretungen
