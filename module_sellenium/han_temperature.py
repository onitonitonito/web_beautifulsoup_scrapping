"""
# 실시간 수질정보 : http://www.koreawqi.go.kr/index_web.jsp
"""

DATE_FROM, DATE_TO = ('20200115', '20200116')
URL = {
        "http://www.koreawqi.go.kr/wQDDRealTotalDataList_D.wq?",
        "item_id"           : "M69",
        "action_type"       : "L",
        "action_type_seq"   : 1,
        "auto_flag"         : "",
        "auto_site_id"      : "S01007",
        "search_data_type"  : 1,
        "search_flag2"      : 1,
        "river_id"          : "R01",
        "site_id"           : "%27S01004%27",
        "site_name"         : "%B1%B8%B8%AE",
        "search_interval"   : "HOUR",
        "order_type_1"      : "MSR_DATE",
        "order_type_2"      : "ASC",
        "search_date_from"  : "${}".format(DATE_FROM),
        "search_date_to"    : "${}".format(DATE_FROM),
    }

print("&".join(URL))
