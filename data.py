import random


class Url:

    url_home_page = "https://qa-scooter.praktikum-services.ru/"
    url_order_page = "https://qa-scooter.praktikum-services.ru/order"
    url_dzen = "https://dzen.ru/?yredirect=true"


class Answers:

    answers = [
                'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
                ]


class Order1:

    @staticmethod
    def generate_order_data(name=None, surname=None):
        result = ''
        if name or surname:
            result = random.choice(list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'))
            for i in range(5):
                result += random.choice(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))

        return result

    name = generate_order_data(name='name')
    surname = generate_order_data(surname='surname')
    address = 'г. Москва, ' + random.choice(
        ['ул. Тверская, 44, кв. 100', 'ул. Арбат, 100, кв. 44', 'ул. Варварка, 200, кв. 144'])
    station = random.choice(['Лужники', 'Митино', 'ВДНХ', 'Лихоборы', 'Театральная'])
    telephone = int('89' + ''.join([random.choice(list('1234567890')) for num in range(9)]))
    date = random.choice(range(7))
    rental_period = random.choice(
        ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])
    color = random.choice(['black', 'grey'])
    comment = random.choice(['Код домофона: 123', 'Домофон не работает', 'Просьба доставить после 18:00'])


class Order2:

    @staticmethod
    def generate_order_data(name=None, surname=None):
        result = ''
        if name or surname:
            result = random.choice(list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ'))
            for i in range(5):
                result += random.choice(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'))

        return result

    name = generate_order_data(name='name')
    surname = generate_order_data(surname='surname')
    address = 'г. Москва, ' + random.choice(
        ['ул. Тверская, 44, кв. 100', 'ул. Арбат, 100, кв. 44', 'ул. Варварка, 200, кв. 144'])
    station = random.choice(['Лужники', 'Митино', 'ВДНХ', 'Лихоборы', 'Театральная'])
    telephone = int('89' + ''.join([random.choice(list('1234567890')) for num in range(9)]))
    date = random.choice(range(7))
    rental_period = random.choice(
        ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])
    color = random.choice(['black', 'grey'])
    comment = random.choice(['Код домофона: 123', 'Домофон не работает', 'Просьба доставить после 18:00'])
