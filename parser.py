# Functions used to parse the api responses

def find_by(response, age_limit):
    """
    Function to parse the response to a dict mapping each centre to available slots
    :param response: API response
    :param age_limit: Desired age limit
    :return: dictionary with centres mapped against available slots
    """
    available = list(filter(lambda each_one:
                            each_one.get("available_capacity") > 0 and each_one.get("min_age_limit") <= age_limit,
                            response))
    available_dict = {}
    for each in available:
        available_dict[each["name"]] = available_dict.get(each["name"], 0)+each["available_capacity"]
    return available_dict
