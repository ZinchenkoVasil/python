import json
import os
import datetime
def write_order_to_json(item, quantity, price, buyer, date):
    order = {}
    order['item'] = item
    order['quantity'] = quantity
    order['price'] = price
    order['buyer'] = buyer
    order['date'] = date
    dict_to_json['orders'].append(order)
    file_name = 'orders.json'
    full_name = os.path.join('output', file_name)
    with open(full_name, 'w') as f_n:
        json.dump(dict_to_json, f_n, indent=4)


if __name__ == "__main__":
    dict_to_json = {"orders": []}
    item = 'red rose'
    quantity = 1000000
    price = 100.0
    buyer = 'romantic man'
    date = datetime.datetime.today().date().isoformat()
    write_order_to_json(item, quantity, price, buyer, date)



