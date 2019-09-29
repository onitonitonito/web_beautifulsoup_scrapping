"""
# functions_class.py - function/class definition
"""
# apply: multi_pop_tabs / stock_weekly_chart.ipynb
print(__doc__)

import random

def get_echo(code_dict, name, target, detail=True):
    url = "https://ssl.pstatic.net/imgfinance/chart/item/area/"
    sidecode=random.random()

    if detail:
        echo = f"""
## {name} ({code_dict[name]})
- URL = {url}
- target={target}
- png?sidedode = {sidecode}
![__CHART__]({url}/{target}/{code_dict[name]}.png?sidcode={sidecode})
"""
    else:
        echo = f"""
- target={target}
![__CHART__]({url}/{target}/{code_dict[name]}.png?sidcode={sidecode})
"""
    return echo



def get_finance_site(site_finances, code_stock, code_name):
    mixed_string = site_finances + code_stock[code_name]
    return mixed_string


def get_window_open_script(site_finances, code_stock, code_name):
    mixed_string = f"window.open('{site_finances + code_stock[code_name]}','_blank');"
    return mixed_string
