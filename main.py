
from utils import mask_card_num, prepare_message, transfer_amount, name_currency, get_date, mask_account


def final_message():
    print(f"{get_date()} {prepare_message(description_message='description')}")
    print(f"{mask_account(account_number='from')} - Счет {mask_card_num(card_num='to')}")
    print(f'{transfer_amount(amount_message1="amount")} {name_currency(name_code="name")}')
    return

