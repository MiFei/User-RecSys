import random
import numpy as np
import csv

# Generate preferences for HIT


#1.ATTRIBUTES
accomodation_type = ['holiday home',  'villa', 'hostel',
                     'hotel'] #9

activity = ['play tennis', 'go skiing', 'play in casino', 'do horse riding', 'go cycling', 'go hiking',
            'play table tennis'] #7
outside_facility = ['balcony', 'terrace', 'patio', 'garden', 'beach nearby'] #7
view = ['mountain view', 'lake view'] #3
relax_facility = ['massage center', 'hot tub', 'sauna', 'hammam', 'swimming pool', 'fitness center', 'library',
                 'fireplace', 'TV with cable channels', 'DVD player'] #13
hotel_facility = ['restaurant', 'laundry', 'ski school', 'lift', '24-hour reception', 'business center', 'bar',
                  'safety deposit box', 'shuttle service', 'room services', 'parking spot', 'children’s playground',
                  'breakfast', 'pets are allowed'] #13
room_facility = ['sofa', 'coffee machine', 'kitchen', 'desk', 'washing machine', 'minibar',
                 'refrigerator', 'microwave', 'hairdryer', 'air conditioning',
                 'WiFi', 'TV'] #15


hm_features = {'accomodation_type': accomodation_type, 'activity': activity, 'outside_facility': outside_facility, 'view': view, 'relax_facility': relax_facility, 'hotel_facility': hotel_facility, 'room_facility': room_facility}


with open('hit_preference_one.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['category', 'preference'])

    # random shuffle
    # for i in range(5000):
    #     category, preferences = random.choice(list(hm_features.items()))
    #     preference = random.choice(preferences)
    #     writer.writerow([category, preference])

    # feature enumeration
    for category, preferences in hm_features.items():
        for preference in preferences:
            writer.writerow([category, preference])





