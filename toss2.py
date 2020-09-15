# user_input = '[{"pk": 1,"value": "Toss Team","is_active": true,"parent": null},{"pk": 2,"value": "송금","is_active": true,"parent": 1},{"pk": 3,"value": "착오송금","is_active": true,"parent": 2},{"pk": 4,"value": "기타","is_active": true,"parent": 3}]/기타'

import json


def get_summary(data, target_value):

    data_dict = {}
    temp_key = -1
    for d in data:
        if d['is_active'] == False: continue
        data_dict[d['pk']] = d
        if d['value'] == target_value:
            temp_key = d['pk']

    result = []
    for i in range(3):
        if data_dict.get(temp_key) == None:
            break
        result.append(data_dict[temp_key]['value'])
        if data_dict[temp_key]['parent'] == 'null':
            break
        temp_key = data_dict[temp_key]['parent']

    answer = ''
    if len(result) > 0:
        for i in range(len(result) - 1, -1, -1):
            answer += result[i]
            answer += '>'
        answer = answer[:-1]
    else:
        answer = 'INACTIVE'

    return answer


user_input = input()
data, target_value = user_input.split('/')
data_list = json.loads(data)
print(get_summary(data_list, target_value))