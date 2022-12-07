class RetailItem:

    def __init__(self, description, units, price):
        self.__item_description = description
        self.__units_in_inventory = units
        self.__price = price

    def set_item_description(self, description):
        self.__item_description = description

    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units

    def set_price(self, price):
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price


def main():
    inventory = make_list()
    print('Data entered:')
    display_list(inventory)


def make_list():
    item_list = []
    retail1 = RetailItem("Jacket", 12, 59.95)
    retail2 = RetailItem("Designer Jeans", 40, 34.95)
    retail3 = RetailItem("Shirt", 20, 24.95)

    item_list.append(retail1)
    item_list.append(retail2)
    item_list.append(retail3)

    return item_list


def display_list(item_list):
    for item in item_list:
        print(item.get_item_description())
        print(item.get_units_in_inventory())
        print(item.get_price())
        print()


if __name__ == "__main__":
    main()
