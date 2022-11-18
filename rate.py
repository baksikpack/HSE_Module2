import requests


class Rate:
    """
    Класс, выгружающий и обрабатывающий курсы и параметры различных валют с внешнего ресурса
    """

    def __init__(self, format_='Value', diff='False'):
        self.format = format_
        self.diff = diff

    def exchange_rates(self):
        """
        Возвращает словарь словарей всех валют от внешнего сервиса в формате:
         "USD":   {
                "ID": "R01235",
                "NumCode": "840",
                "CharCode": "USD",
                "Nominal": 1,
                "Name": "Доллар США",
                "Value": 61.1629,
                "Previous": 61.1958
            }
        """
        self.req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.req.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух возможных форматах:

        1) Полный (инициализация экземпляра класса с параметром 'Full'):
        {
            "ID": "R01235",
            "NumCode": "840",
            "CharCode": "USD",
            "Nominal": 1,
            "Name": "Доллар США",
            "Value": 61.1629,
            "Previous": 61.1958
        }

        2) Сокращенный (по умолчанию):
        61.1629
        """
        response = self.exchange_rates()
        difference = float(response[currency]['Value']) - float(response[currency]['Previous'])

        if currency in response:
            if self.format == 'Full':
                return response[currency]

            if self.format == 'Value':

                if self.diff == 'True':
                    return difference

                if self.diff == 'False':
                    return response[currency]['Value']

        return 'Error'

    def usd(self):
        """Возвращает текущий курс доллара США"""
        return self.make_format('USD')

    def eur(self):
        """Возвращает текущий курс евро"""
        return self.make_format('EUR')

    def kzt(self):
        """Возвращает текущий курс тенге"""
        return self.make_format('KZT')

    def try_(self):
        """
        Возвращает текущий курс турецкой лиры.
        ВНИМАНИЕ на наименование метода!
        """
        return self.make_format('TRY')

    # Задание 1 оформляю не функцией как сформулировано в задании, а методом класса, как было сказано на вебинаре от 08.10 (2:24:45)
    def max_rate(self):
        """Возвращает наименование валюты с максимальным значение курса к российскому рублю"""
        max_rate_currency = []
        temp_max_rate_currency = 0
        response = self.exchange_rates()

        for k, v in response.items():
            if v['Value'] > temp_max_rate_currency:
                temp_max_rate_currency = v['Value']
                max_rate_currency = v['Name']

        return max_rate_currency

# Задание 2