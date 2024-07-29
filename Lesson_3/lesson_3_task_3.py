from address import Address
from mailing import Mailing

to_address = Address("423457", "Альметьевск", "Нефтяников", "27", "10")
from_address = Address("423450", "Альметьевск", "Шевченко", "70", "12")
mailing = Mailing(to_address, from_address, 250, 304945478)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")