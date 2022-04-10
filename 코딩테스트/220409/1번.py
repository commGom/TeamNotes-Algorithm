
def check_cycle(check_dict, key):
    result = False
    original_val = key
    while check_dict.get(key):
        key = check_dict.get(key)
        if original_val == key:
            result = True
            break
    return result


def solution(tstring, variables):
    answer = ''
    variable_dict = {}
    for variable in variables:
        key = "{"+variable[0]+"}"
        val = variable[1]
        variable_dict[key] = val
    tstring_arr = tstring.split(" ")
    changed_idx = []

    for i in range(len(tstring_arr)):
        if variable_dict.get(tstring_arr[i]):
            if not check_cycle(variable_dict, tstring_arr[i]):
                changed_idx.append(i)
                tstring_arr[i] = variable_dict.get(tstring_arr[i])

    while changed_idx:
        new_idx_arr = []
        for i in changed_idx:
            if variable_dict.get(tstring_arr[i]):
                tstring_arr[i] = variable_dict.get(tstring_arr[i])
                new_idx_arr.append(i)
        changed_idx = new_idx_arr

    answer = " ".join(tstring_arr)

    return answer
