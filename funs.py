def transpose(dict):
    result = {}
    for key in dict:
        if dict[key] not in result:
            result[dict[key]] = [key]
        else:
            result[dict[key]].append(key)
    return result


assert transpose({"Alice": 54981, "Bob": 75080, "Carol": 75080}) == {54981: ["Alice"], 75080: ["Bob", "Carol"]}
