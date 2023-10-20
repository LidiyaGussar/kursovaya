import json
from typing import Union
import re

file_path = "operation.json"
with open(file_path, 'r', encoding='utf - 8') as file:
    data = json.load(file)

"Создаем функцию сортировки дат для Совершенных операций и реверсивного вывода их на экран"


def filter_and_sorted(data):
    item = [item for item in data if item.get('state') == 'EXECUTED']
    item.sort(key=lambda x: x.get('date'), reverse=True)
    return item[:5]


def description_message(description):
    description_msg = 'description'
    for i in filter_and_sorted(data):
        if description_msg in i:
            description = i[description_msg]
    return description


def transfer_amount(amount_message1):
    amount_msg = "operationAmount"
    for i in filter_and_sorted(data):
        if amount_msg in i:
            amount_message = i[amount_msg]
            amount_message1 = amount_message['amount']
    return amount_message1


def name_currency(name_code):
    name_msg = 'operationAmount'
    for i in data:
        if name_msg in i:
            name_message = i[name_msg]
            name_message1 = name_message['currency']
            name_code = name_message1['name']
    return name_code


"выводим дату в формате ДД.ММ.ГГГГ при помощи срезов и индекса"


def get_date(data_operation):
    data_time = 'date'
    for i in data:
        if data_time in i:
            data_operat = i[data_time]
            data_operation = data_operat[0:4] + '-' + data_operat[5:9] + data_operat[9:10]
            return data_operation


def from_name(sender_name):
    from_name_sender = 'from'
    for i in data:
        if from_name_sender in i:
            sender_name = i[from_name_sender]

            print(sender_name[:-17])


"маскируем номер карты, так, чтобы выводились последнии четыре цифры, а остальное было под маской"


def mask_card_num(card_num):
    key = 'to'
    for i in data:
        if key in i:
            card_num = i[key]
    mask = "****"

    return f"{mask}{card_num[-4:]}"


"маскируем номер счета"

"извлекаем номер из списка словарей и выводим только цифры из полученной строки, с помощью регулярного выражения"


def mask_account(account_mask):
    mask = '******'
    number_from = 'from'
    for i in data:
        if number_from in i:
            account_mask = i[number_from]
    return f"{account_mask[:-10]} {mask} {account_mask[-4:]}"


print(f"{get_date(data_operation='date')} {description_message(description ='description')}")
print(f"{(mask_account(account_mask='from'))} --> Счет {mask_card_num(card_num='to')}")
print(f'{transfer_amount(amount_message1="amount")} {name_currency(name_code="name")}')



