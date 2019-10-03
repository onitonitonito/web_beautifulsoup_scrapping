"""
# functions_class.py - function & class definition
"""
# apply: multi_pop_tabs / stock_weekly_chart.ipynb
print(__doc__)

import random

def get_markdown_echo(code_stock, name, target, detail=True):
    url = "https://ssl.pstatic.net/imgfinance/chart/item/area/"
    sidecode=random.random()

    if detail:
        echo = f"""
## {name} ({code_stock[name]})
- URL = {url}
- target={target}
- png?sidedode = {sidecode}
![__CHART__]({url}/{target}/{code_stock[name]}.png?sidcode={sidecode})
"""
    else:
        echo = f"""
- target={target}
![__CHART__]({url}/{target}/{code_stock[name]}.png?sidcode={sidecode})
"""
    return echo


def get_pop_script(url_target):
    """타겟url을 오픈하는 script_string 을 반환한다"""
    return f"window.open('{url_target}', '_blank');"
