from urllib.request import urlopen
from bs4 import BeautifulSoup

# Need to change reg_week_year value by dates
# HarenKei did not talked me to change reg_week_year value by date
# So I hard-coded this value with 46 that shows when I wrote this code
url303 = "http://www.daelim.ac.kr/hme/stu_service/prg/stu_cafeteria.do?reg_week_year=46&cafe_cd=139"

html = urlopen(url303).read()
soup = BeautifulSoup(html, "html.parser")

table_meal = soup.find("table", class_="table_col mt_30 ml_22")
tr_corner = table_meal.find_all("tr")

for i in range(5):
    # Show Day
    th_day = table_meal.find("thead")
    str_day = th_day.find_all("th")[i + 2]
    print("/*", str_day.text, "*/")
    # Get Menu data by Day, List with Corner Names
    for j in range(9):
        content = tr_corner[j + 1].find_all("td")
        # HTML has a little bit special structure with Corner1 so separated just Corner1
        if j == 0:
            currentCorner = content[1]
            td_meal = content[i + 2]

            corner1_meal=currentCorner.text + ':' + td_meal.text.strip()
            cnr1_db=open('/Users/harenkei/PycharmProjects/DUC_bot/cnr1_meal','w')
            cnr1_db.write(corner1_meal)
        else:
            currentCorner = content[0]
            td_meal = content[i + 1]


        print(currentCorner.text, ":", td_meal.text.strip())
    meal = currentCorner.text + ":" + td_meal.text.strip()


    # Make a Line-Breking when a day is ended
    print("")



    str_meal = currentCorner.text + ":" + td_meal.text.strip()
    meal_data = open('/Users/harenkei/PycharmProjects/DUC_bot/meal_db', 'w')
    meal_data.write(str_meal)
