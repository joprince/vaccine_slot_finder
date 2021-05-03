# Functions used to parse the api responses

def find_by(response, age_limit):
    """
    Function to parse the response to a dict mapping each centre to available slots
    :param response: API response
    :param age_limit: Desired age limit
    :return: dictionary with centres mapped against available slots
    """
    available = list(filter(lambda each_one:
                            each_one.get("available_capacity", 0) > 0 and
                            each_one.get("min_age_limit", 999) <= age_limit,
                            response))
    available_dict = {}
    for each in available:
        available_dict[each["name"]] = available_dict.get(each["name"], 0) + each["available_capacity"]
    return available_dict


def calender(response, age_limit):
    """
    Function to parser the response which has data for 7 days
    :param response: response of the api
    :param age_limit: age limit of the slot looking for
    :return: list containing the centers along with number of slots on each date
    """
    available_dict = [{each["name"]: {session["date"]: session["available_capacity"]
                                      for session in each["sessions"]
                                      if session.get("available_capacity", 0) > 0 and
                                      session.get("min_age_limit", 999) <= age_limit}}
                      for each in response]
    available_dict = [each for each in available_dict if list(each.values())[0] != {}]
    return available_dict
