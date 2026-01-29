import os
import json
import pandas as pd
import numpy as np


def data_collection():
    path = r"Please enter the path here"
    files = os.listdir(path)

    for i in files:
        path1 = "{0}/{1}".format(path,i)
        data = open(path1,"r")
        data = json.load(data)

    df = {
        "id": [],
        "name": [],
        "host_id": [],
        "host_name": [],
        "image": [],
        "rules": [],
        "prop_type": [],
        "room": [],
        "bed": [],
        "min_night": [],
        "max_night": [],
        "cancel_pol": [],
        "accomdates": [],
        "no_of_bedrooms": [],
        "no_bathroom": [],
        "tot_review": [],
        "amenities": [],
        "price": [],
        "sec_dep": [],
        "guest": [],
        "address": [],
        "country": [],
        "coordinates": [],
        "availability_365": [],
        "rev_acc": [],
        "rev_clean": [],
        "rev_checkin": [],
        "rev_comm": [],
        "rev_loc": [],
        "rev_val": [],
        "overall_rev": [],
    }

    for i in range(len(data)):
        df["id"].append(data[i]["_id"])
        df["name"].append(data[i]["name"])
        df["host_id"].append(data[i]["host"]["host_id"])
        df["host_name"].append(data[i]["host"]["host_name"])
        if data[i]["house_rules"] == '':
            df["rules"].append("No rules")
        else:
            df["rules"].append(data[i]["house_rules"])
        df["image"].append(data[i]["images"]["picture_url"])
        df["prop_type"].append(data[i]["property_type"])
        df["room"].append(data[i]["room_type"])
        df["bed"].append(data[i]["bed_type"])
        df["min_night"].append(data[i]["minimum_nights"])
        df["max_night"].append(data[i]["maximum_nights"])
        df["cancel_pol"].append(data[i]["cancellation_policy"])
        df["accomdates"].append(data[i]["accommodates"])
        df["no_of_bedrooms"].append(data[i].get("bedrooms",None))
        df["no_bathroom"].append(data[i].get("bathrooms",None))
        df["tot_review"].append(data[i]["number_of_reviews"])
        df["amenities"].append(data[i]["amenities"])
        df["price"].append(data[i]["price"])
        df["sec_dep"].append(data[i].get("security_deposit", 0))
        df["guest"].append(data[i]["guests_included"])
        address = "{0} {1} {2}".format(data[i]["address"]["street"],data[i]["address"]["suburb"],data[i]["address"]["market"])
        df["address"].append(address)
        df["country"].append(data[i]["address"]["country"])
        df["coordinates"].append(data[i]['address']["location"]["coordinates"])
        df["availability_365"].append(data[i]["availability"]["availability_365"])
        review_scores = data[i].get("review_scores", {})
        df["rev_acc"].append(review_scores.get("review_scores_accuracy", 0))
        df["rev_clean"].append(review_scores.get("review_scores_cleanliness", 0))
        df["rev_checkin"].append(review_scores.get("review_scores_checkin", 0))
        df["rev_comm"].append(review_scores.get("review_scores_communication", 0))
        df["rev_loc"].append(review_scores.get("review_scores_location", 0))
        df["rev_val"].append(review_scores.get("review_scores_value", 0))
        df["overall_rev"].append(review_scores.get("review_scores_rating", 0) / 10)

    df1 = pd.DataFrame(df)

    return df1
    

def data_cleaning(df1): 
    #excluding the null value for bathroom and bedroom
    bedroom_changed = np.where(df1['no_of_bedrooms'].isna() == True, 0, 1)
    df1['bedroom_changed'] = bedroom_changed
    bathroom_changed = np.where(df1['no_bathroom'].isna() == True, 0, 1)
    df1['bathroom_changed'] = bathroom_changed
    df1 = df1.fillna({'no_bathroom':1,'no_of_bedrooms':1,})
    df1['bathroom_changed'] = np.where(df1['no_bathroom'] == 0, 0, df1['bathroom_changed'])
    df1['no_bathroom'] = np.where(df1['no_bathroom'] == 0, 1, df1['no_bathroom'])
    df1['bedroom_changed'] = np.where(df1['no_of_bedrooms'] == 0, 0, df1['bedroom_changed'])
    df1['no_of_bedrooms'] = np.where(df1['no_of_bedrooms'] == 0, 1, df1['no_of_bedrooms'])
    df1['no_bathroom'] = df1['no_bathroom'].astype('int')
    df1['no_of_bedrooms'] = df1['no_of_bedrooms'].astype('int')

    #converting the data type
    df1['min_night'] = df1['min_night'].astype('int')
    df1['max_night'] = df1['max_night'].astype('int')


    df1['coordinates'] = df1['coordinates'].astype(str)
    df1['coordinates'] = df1['coordinates'].str.replace("[","")
    df1['coordinates'] = df1['coordinates'].str.replace("]","")
    lat_long = df1['coordinates'].str.split(",", expand = True)
    df1['latitude'] = lat_long[0]
    df1['longitude'] = lat_long[1]
    df1['latitude'] = df1['latitude'].astype('float')
    df1['longitude'] = df1['longitude'].astype('float')
    df1.drop('coordinates', axis = 1, inplace = True)

    df1['amenities'] = df1['amenities'].astype(str)
    df1['amenities'] = df1['amenities'].str.replace("[","")
    df1['amenities'] = df1['amenities'].str.replace("]","")

    return df1


a = data_collection()    
a = data_cleaning(a)
