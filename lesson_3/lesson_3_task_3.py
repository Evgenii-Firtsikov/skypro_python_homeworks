from address import Address
from mailing import Mailing

to_address = Address('999999', 'Москва', 'Ленина', '15', '5')
from_address = Address('888888', 'Санкт-Петербург', 'Пушкина', '20', '12')

mailing = Mailing(to_address, from_address, 250, 'TR_777_777')

print(mailing)
