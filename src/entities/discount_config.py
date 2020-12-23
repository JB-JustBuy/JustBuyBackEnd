config = {
    "蝦皮白卡": {
        'type': 'CreditCard',
        'belong': '玉山',
        'methods': [
            {"constraint": {"type": "單筆", "value": "500", 'platform': 'shoppe'},
             'feedback': {"type": "現金", "value": "5"}
             },
        ]
    },
    "蝦皮黃金卡": {
        'type': 'CreditCard',
        'belong': '玉山',
        'methods': [
            {"constraint": {"type": "單筆", "value": "500", 'platform': 'shoppe'},
             'feedback': {"type": "現金", "value": "50"}
             },
        ]
    },
    "PCHOME阿宅卡": {
        'type': 'CreditCard',
        'belong': '玉山',
        'methods': [
            {"constraint": {"type": "單筆", "value": "500", 'platform': 'pchome'},
             'feedback': {"type": "現金", "value": "100"}
             },

        ]
    },
    "PCHOME-Magic卡": {
        'type': 'CreditCard',
        'belong': '玉山',
        'methods': [
            {"constraint": {"type": "單筆", "value": "500", 'platform': 'pchome'},
             'feedback': {"type": "現金", "value": "200"}
             },

        ]
    },
    "花旗銀行": {
        'type': 'CreditCard',
        'belong': '花旗銀行',
        'methods': [
            {"constraint": {"type": "單筆", "value": "30000", 'platform': 'pchome'},
             'feedback': {"type": "現金", "value": "2400"}
             },
            {"constraint": {"type": "單筆", "value": "20000", 'platform': 'pchome'},
             'feedback': {"type": "現金", "value": "1400"}
             },
            {"constraint": {"type": "單筆", "value": "5000", 'platform': 'pchome'},
             'feedback': {"type": "現金", "value": "350"}
             },
        ]
    },
}