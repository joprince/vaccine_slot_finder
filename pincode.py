from datetime import datetime
from requests import get
from const import API_WEEK_PIN, API_DAY_PIN


class PinCode:

    @staticmethod
    def __get_api_call(api, pin, search_date):
        """
        Function to perform the api get call
        :param api:
        :param pin:
        :param search_date:
        :return: Get call response
        """
        search_date = search_date if search_date else datetime.today().strftime('%d-%m-%Y')
        get_call = api + "?pincode=" + str(pin) + "&date=" + str(search_date)
        response = get(get_call)
        return response

    def day(self, pin, search_date):
        """
        Function to get slots available on a given date

        :param pin:
        :param search_date:
        :return:
        """
        search_date = search_date if search_date else datetime.today().strftime('%d-%m-%Y')
        response = self.__get_api_call(api=API_DAY_PIN, pin=pin, search_date=search_date)
        print(response)

    def week(self, pin, search_date):
        """
        Function to get slots available for 7 days from a given date
        :param pin:
        :param search_date:
        :return:
        """
        search_date = search_date if search_date else datetime.today().strftime('%d-%m-%Y')
        response = self.__get_api_call(api=API_WEEK_PIN, pin=pin, search_date=search_date)
        print(response)
