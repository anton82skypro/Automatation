from smartphone import Smartphone

catalog = [] # Создаётся пустой список
# Создаются 5 разных экземпляров класса Smartphone
phone1 = Smartphone("Honor", "8X", "+79872055863")
phone2 = Smartphone("Samsung", "A21", "+79174590559")
phone3 = Smartphone("Айфон", "14", "+79625986325")
phone4 = Smartphone("Xiaomi", "MIUI 12", "+79080000000")
phone5 = Smartphone("RealMe", "c55", "+79011114455")
# Каждый экземпляр добавляется в список catalog
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'<{phone.marka}> - <{phone.model}>. <{phone.number}>')