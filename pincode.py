from datetime import datetime
from requests import get
from const import API_WEEK_PIN, API_DAY_PIN
from parser import find_by


class PinCode:

    @staticmethod
    def __get_api_call(api, pin, search_date):
        """
        Function to perform the api get call
        :param api: API for performing the get call
        :param pin: PinCode of the location
        :param search_date: date from which slots are to be searched
        :return: Get call response
        """
        search_date = search_date if search_date else datetime.today().strftime('%d-%m-%Y')
        get_call = api + "?pincode=" + str(pin) + "&date=" + str(search_date)
        try:
            response = get(get_call)
            response = response.json() if response.status_code == 200 else None
        except Exception as e:
            print("Error while API call!! Please check your internet connection and try again after some time...")
            response = None
        finally:
            return response

    def day(self, pin, search_date):
        """
        Function to get slots available on a given date

        :param pin: Pin Code of the location
        :param search_date: date from which slots are to be searched
        :return: Dictionary with centres mapped to available slots
        """
        search_date = search_date if search_date else datetime.today().strftime('%d-%m-%Y')
        response = self.__get_api_call(api=API_DAY_PIN, pin=pin, search_date=search_date)
        if response:
            response = find_by(response=response.get("sessions", []), age_limit=45)
        return response

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
