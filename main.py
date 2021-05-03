from pincode import PinCode


def main():
    pin_slot = PinCode()
    # pin_slot.week(pin=686575, search_date="03-05-2021")
    print(pin_slot.day(pin=744302, search_date="03-05-2021"))


if __name__ == "__main__":
    main()
