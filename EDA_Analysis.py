from Datacoll_dataclean import a
import scipy.stats as stats
import pandas as pd


def eda(df11):
    #analysis for room and price
    price_private_room = df11[df11['room'] == 'Private room']['price']
    price_entire_home = df11[df11['room'] == 'Entire home/apt']['price']
    price_shared_room = df11[df11['room'] == 'Shared room']['price']

    statistic, p_value = stats.kruskal(price_private_room, price_entire_home, price_shared_room)

    #analysis for property and price
    price_by_property = {}
    for prop_category in df11['prop_type'].unique():
            key = prop_category
            price_by_property[key] = df11[(df11['prop_type'] == prop_category)]['price']
    
    statistic1,p_value1 = stats.kruskal(*price_by_property.values())

    #analysis for bed and price
    price_by_bed = {}
    for bed_category in df11['bed'].unique():
            key = bed_category
            price_by_bed[key] = df11[(df11['bed'] == bed_category)]['price']
    
    statistic2,p_value2 = stats.kruskal(*price_by_bed.values())

    #analysis for country and price
    price_by_country = {}
    for country_category in df11['country'].unique():
            key = country_category
            price_by_country[key] = df11[(df11['country'] == country_category)]['price']
    
    statistic3,p_value3 = stats.kruskal(*price_by_country.values())

    #analysis for price over room and country
    price_by_room_country = {}
    for room_category in df11['room'].unique():
        for country_category in df11['country'].unique():
            key = (room_category, country_category)
            price_by_room_country[key] = df11[(df11['room'] == room_category) & (df11['country'] == country_category)]['price']
    
    statistic4,p_value4 = stats.kruskal(*price_by_room_country.values())

    #analysis for rules over price
    price_by_rules = {}
    for rules_category in df11['rules'].unique():
            key = rules_category
            price_by_rules[key] = df11[(df11['rules'] == rules_category)]['price']
    
    statistic5,p_value5 = stats.kruskal(*price_by_rules.values())

    #analysis for cancellation policy over price
    price_by_cancel_pol = {}
    for can_policy_category in df11['cancel_pol'].unique():
            key = can_policy_category
            price_by_cancel_pol[key] = df11[(df11['cancel_pol'] == can_policy_category)]['price']
    
    statistic6,p_value6 = stats.kruskal(*price_by_cancel_pol.values())

    #analysis for bedrooms over price
    price_by_bedroom = {}
    for bedroom_category in df11['no_of_bedrooms'].unique():
            key = bedroom_category
            price_by_bedroom[key] = df11[(df11['no_of_bedrooms'] == bedroom_category)]['price']
    
    statistic7,p_value7 = stats.kruskal(*price_by_bedroom.values())

    #analysis of bathroom over price
    price_by_bathroom = {}
    for bathroom_category in df11['no_bathroom'].unique():
            key = bathroom_category
            price_by_bathroom[key] = df11[(df11['no_bathroom'] == bathroom_category)]['price']
    
    statistic8,p_value8 = stats.kruskal(*price_by_bathroom.values())

    #analysis of guest over price
    price_by_guest = {}
    for guest_category in df11['guest'].unique():
            key = guest_category
            price_by_guest[key] = df11[(df11['guest'] == guest_category)]['price']
    
    statistic9,p_value9 = stats.kruskal(*price_by_guest.values())

    #analysis of accomdates over price
    price_by_accomdates = {}
    for accomdates_category in df11['accomdates'].unique():
            key = accomdates_category
            price_by_accomdates[key] = df11[(df11['accomdates'] == accomdates_category)]['price']
    
    statistic10,p_value10 = stats.kruskal(*price_by_accomdates.values())


    return p_value,p_value1,p_value2,p_value3,p_value4,p_value5,p_value6,p_value7,p_value8,p_value9,p_value10


df1 = a[["price","room","prop_type","bed","country","rules","cancel_pol","no_of_bedrooms","no_bathroom","guest","accomdates"]]

p,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10 = eda(df1)
