
class UrlParser:
    @staticmethod
    def recognize_platform(url):
        print('url:', url, 'is belong', end='')
        if 'shopee' in url:
            print('shopee')
            return 'shopee'
        elif 'pchome' in url:
            print('pchome')
            return 'pchome'
        else:
            raise ValueError('url is not acceptable.')