import requests
from bs4 import BeautifulSoup
from config import studentScheduleLink
from datetime import datetime
import re

headers = {"accept-language": "ru-RU", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                                                     "KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
curDate = str(datetime.now().date())
day = None
userFaculty = "ARTS"
userGroup = "332874"


def removeWhitespace(str):
    return re.sub("""[\s+]""", " ", str)


def studentSchedule():
    global day
    result = ""
    url = studentScheduleLink.format(userFaculty, userGroup, curDate)
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    # print(" ".join(soup.text.split()))
    for panel in soup.findAll("div", class_="panel panel-default"):
        if panel.find(class_="panel-title") and re.search("\d+", panel.find(class_="panel-title").text).group() == \
                curDate[8:10]:
            day = panel
            break
    if day is not None:
        result += day.find("h4").text.strip() + "\n"
        for li in day.findAll("li"):
            spans = [span for span in li.findAll("span")]
            for span in spans:
                result += " ".join(span.text.split()) + "\n"
        return result
    else:
        return "седня пар нет"
