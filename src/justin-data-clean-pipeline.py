from bs4 import BeautifulSoup as bs
import json

def import_records(json_file):
    records = []
    with open(json_file) as f:
        for i in f:
            records.append(json.loads(i))
    return records

def separate_json(json_file):
    records = import_records(json_file)
    id_lst = []
    url_lst = []
    soup_lst = []
    time_lst = []
    for i in range(len(records)):
        id_lst.append(records[i]['_id'])
        url_lst.append(records[i]['url'])
        soup_lst.append(bs(records[i]['html'], 'lxml'))
        time_lst.append(records[i]['time'])
    return id_lst, url_lst, soup_lst, time_lst

def pipeline(json_file):
    id_lst, url_lst, soup_lst, time_lst = separate_json(json_file)
    content = []
    other_stuff = []
    for i in range(len(soup_lst)):
        td_tags = soup_lst[i].find_all('td')
        other_stuff.append(td_tags[0])
        content.append(td_tags[1])
    return other_stuff, content

if __name__ == "__main__":
    
    # records = []
    # with open('../data/ufo_first100records.json') as f:
    #     for i in f:
    #         records.append(json.loads(i))
    # # print(len(records))
    # # print(records[0]['_id'])
    
    
    # id_lst = []
    # url_lst = []
    # soup_lst = []
    # time_lst = []
    # for i in range(len(records)):
    #     id_lst.append(records[i]['_id'])
    #     url_lst.append(records[i]['url'])
    #     soup_lst.append(bs(records[i]['html'], 'lxml'))
    #     time_lst.append(records[i]['time'])

    # # print(len(id_lst), len(url_lst), len(soup_lst), len(time_lst))
    # # print(soup_lst[0].prettify())
    
    # td_tags = soup_lst[0].find_all('td')
    
    # other = td_tags[0].text
    # description = td_tags[1].text
    # # print(other)
    # # print(description)
    
    # other_lst = other.split(":")
    # print(other_lst)
    # print(time_lst[0])
    file = '../data/ufo_first100records.json'
    records = import_records(file)
    
    # id_lst, url_lst, soup_lst, time_lst = separate_json(file)
    # print(len(id_lst), len(url_lst), len(soup_lst), len(time_lst))
    other_stuff, content = pipeline(file)
    print(len(other_stuff), len(content))
