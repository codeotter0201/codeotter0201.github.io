import urllib.request
import json
import csv

def get_data() -> list[dict]:
    url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    htmlfile = urllib.request.urlopen(url)
    ret = htmlfile.read().decode('utf-8')
    return json.loads(ret)['result']['results']

def get_attraction_row(data:dict) -> list:
    url = data['file'] = 'https://' + data['file'].split('https://')[1]
    area = data['address'].split('  ')[-1][:3]
    return [data['stitle'], area, data['longitude'], data['latitude'], url]

def get_mrt_row(data:dict) -> list:
    if data['MRT'] is None:
        data['MRT'] = '沒有捷運站'
    return [data['MRT'], data['stitle']]

def extract_mrt(mrts:dict) -> list:
    return [[k] + v for k, v in mrts.items()]

def create_files(data:list[dict]) -> None:
    attractions, mrts = [], {}
    for spot in data:
        attractions.append(get_attraction_row(spot))
        mrt_row = get_mrt_row(spot)
        mrts[mrt_row[0]] = mrts.get(mrt_row[0], [])
        mrts[mrt_row[0]].append(mrt_row[1])
    mrts = extract_mrt(mrts)

    with open('mrt.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for r in mrts:
            writer.writerow(r)

    with open('attraction.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        for r in attractions:
            writer.writerow(r)


if __name__ == '__main__':
    data = get_data()
    create_files(data)