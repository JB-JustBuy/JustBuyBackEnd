import re


class PriceParser:
    @staticmethod
    def price_parser(price):
        if isinstance(price, int):
            return price
        elif isinstance(price, str):
            # remove the symbols
            price = price.replace(',', '')
            no_symbols = re.sub(r'[^\w]', ' ', price)
            tokens = no_symbols.split(' ')
            for token in tokens:
                if len(token.replace(' ', '')) > 0:
                    return int(token)
            return None
        else:
            return None