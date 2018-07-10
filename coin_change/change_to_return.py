from curr_constants import CURR_NAMES, CURR_VALUES

def get_inputs() -> int:
    try:
        payment = input('How much money did the customer give you (in $)?   ')
        payment = int(float(payment) * 100)
        price = input("What was the customer's total bill (in $)?   ")
        price = int(float(price) * 100)
    except ValueError:
        print('Must enter $ values as numbers, please try again:')
        price, payment = get_inputs()
    if payment < price:
        print('Payment must be greater than the price, please eneter again:')
        price, payment = get_inputs()
    return price, payment


def calculate_change(price: int, payment: int) -> int:
    change = payment - price
    return change


def calc_change_items_to_return(price: int, payment: int) -> list:
    change = calculate_change(price, payment)
    change_desc = []
    counter = 0
    while change != 0:
        if change >= CURR_VALUES[counter]:
            floor = change // CURR_VALUES[counter]
            change = change % CURR_VALUES[counter]
            if floor == 1:
                change_desc.append((CURR_NAMES[counter], floor))
            else:
                change_desc.append((CURR_NAMES[counter] + 's', floor))
        counter += 1
    return change_desc


def main() -> None:
    price, payment = get_inputs()
    change_list = calc_change_items_to_return(price, payment)
    for change_item in change_list:
        print('{0} {1}'.format(change_item[1], change_item[0]))


if __name__ == "__main__":
    main()


