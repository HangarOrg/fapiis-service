from bs4 import BeautifulSoup
import requests
import json

site = requests.get("https://fapiis.gov/fapiis/fapiisrecords_all.action").text
doc = BeautifulSoup(site, "html.parser")


def get_data_from_row(row):
    fields = row.find_all("td")
    cage = fields[0].get_text().strip()
    duns = fields[1].get_text().strip()
    url = "https://fapiis.gov%s" % (row.find("a").attrs["href"])
    name = fields[2].get_text().strip()
    record_type = fields[3].get_text().strip()
    record_date = fields[4].get_text().strip()
    award_number = fields[5].get_text().strip()
    ref_number = fields[6].get_text().strip()
    agency = fields[7].get_text().strip()
    sol_number = fields[8].get_text().strip()
    sub_cage = fields[9].get_text().strip()
    sub_duns = fields[10].get_text().strip()
    sub_name = fields[11].get_text().strip()
    violation_against = fields[12].get_text().strip()

    return {
        "cage": cage,
        "duns": duns,
        "url": url,
        "name": name,
        "record_type": record_type,
        "record_date": record_date,
        "award_number": award_number,
        "ref_number": ref_number,
        "agency": agency,
        "sol_number": sol_number,
        "sub_cage": sub_cage,
        "sub_duns": sub_duns,
        "sub_name": sub_name,
        "violation_against": violation_against,
    }


res = [get_data_from_row(record) for record in doc.select(".dt-body-nowrap")]

with open("fapiis.json", "w") as outfile:
    json.dump(res, outfile)
