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
        other_stuff.append(td_tags[0].text)
        content.append(td_tags[1].text)
    contents_lower = []
    for val in content:
        if val == None:
            contents_lower.append("")
        else:
            contents_lower.append(val.lower())
    words_to_remove = ['Occurred', 'Reported', 'Posted', 
                       'Location', 'Shape', 'Duration']
    features_dic = {'Occurred': [],'Location': [],
                    'Shape': [], 'Duration': []}
    
    for i in range(len(other_stuff)):
        removekeys = other_stuff[i]
        for val in words_to_remove:
            removekeys = removekeys.replace(val,"")
        lst = removekeys.split(':')
        try:
            features_dic['Occurred'].append(lst[1])
        except:
            features_dic['Occurred'].append(None)
        try:
            features_dic['Location'].append(lst[10])
        except:
            features_dic['Location'].append(None)
        try:
            features_dic['Shape'].append(lst[11])
        except:
            features_dic['Shape'].append(None)
        try:
            features_dic['Duration'].append(lst[12])
        except:
            features_dic['Duration'].append(None)
    return features_dic, contents_lower

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
    # records = import_records(file)
    
    # id_lst, url_lst, soup_lst, time_lst = separate_json(file)
    # print(len(id_lst), len(url_lst), len(soup_lst), len(time_lst))
    dic, content = pipeline(file)
    print(dic['Duration'])
    # print(features_dic)
    # features_dic = {'Occurred': [], 'Reported': [], 'Posted': [], 'Location': [],
    #                 'Shape': [], 'Duration': []}
    # words_to_remove = list(features_dic.keys())
    # print(words_to_remove)
    # print(other_stuff[0])
    # removekeys = other_stuff[10]
    # for val in words_to_remove:
    #     removekeys = removekeys.replace(val,"")
    # print('\n',removekeys)

    # lst = removekeys.split(':')
    # print(lst)
    # for idx, val in enumerate(lst):
    #     print(f'{idx}: {val}')

    # actual_dic = {'Occurred': [lst[1]],'Location': [lst[10]],
    #                 'Shape': [lst[11]], 'Duration': [lst[12]]}
    
    # lenLst = []
    # for i in range(len(other_stuff)):
    #     removekeys = other_stuff[i]
    #     for val in words_to_remove:
    #         removekeys = removekeys.replace(val,"")
    #     lst = removekeys.split(':')
    #     lenLst.append(len(lst))
    # print(lenLst)


