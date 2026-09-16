# Jordan Fitzgerald
# Travel Weather Planner
# 2/18/26

distance_mi = 5
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if distance_mi > 6:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")
elif distance_mi <= 6 and distance_mi > 1:
    if has_bike and is_raining == False:
        print("True")
    else:
        print("False")
elif distance_mi <= 1:
    if is_raining == False:
        print("True")
    else: 
        print("False")


