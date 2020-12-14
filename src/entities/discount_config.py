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
}