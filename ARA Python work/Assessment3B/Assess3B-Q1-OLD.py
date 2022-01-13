# Assessment 3B Question 1
# Timothy Williams, tsw0050@arastudent.ac.nz

def get_demerit_points(driving_speed, speed_limit, light_trailer = False, school_zone = False, holiday_period = False):
    '''
    Function works out the demerit point penalty for a driving speed in a particular speed zone
    

    driving_speed int or float can be assumed +ve
    speed_limit is a +ve int
    
    The function returns the results as a tuple.  The tuple is in the format of (Mandatory penalty, penalty points)

    Mandatory is true when:
    driving_speed > speed_limit + 10
    driving_speed > speed_limit + 5 & light_trailer = True
    driving_speed > speed_limit + 4 & school_zone = True
    driving_speed > speed_limit + 4 & holiday_period = True
    lowest possible discretion applies

    if over the speed limit it will be minimum 10 penalty points

    Penalty Points:
    if driving_speed <= speed_limit, PP = 0 MP = False
    if speed_limit < driving_speed <= speed_limit + 10 & all args false             PP = 10 MP = False
    if speed_limit < driving_speed <= speed_limit + 10 & any args true              PP = 10 MP = (as above)
    if speed_limit + 10 < driving_speed <= speed_limit + 20                         PP = 20 MP = True
    if speed_limit + 20 < driving_speed <= speed_limit + 30                         PP = 35 MP = True
    if speed_limit + 30 < driving_speed <= speed_limit + 35                         PP = 40 MP = True
    if speed_limit + 35 < driving_speed                                             PP = 50 MP = True

    '''
    # all speeds in km/h any additons to speed_limit (e.g. speed_limit + 20) are additional speed categories
    TRAILER_LENIENCY = 5
    SCHOOL_ZONE_LENIENCY = 4
    HOLIDAY_LENIENCY = 4
    DEFAULT_LENIANCY_SPEED = 10

    # No mandatory penalty unless driver breaks the rules past leniency criteria
    mandatory_penalty = False

    # test for each speed category and if speed >= 10 over the limit then check leniency rules
    if speed_limit < driving_speed <= speed_limit + DEFAULT_LENIANCY_SPEED and not any([light_trailer, school_zone, holiday_period]):
        penalty_points = 10

    elif speed_limit < driving_speed <= speed_limit + DEFAULT_LENIANCY_SPEED and any([light_trailer, school_zone, holiday_period]):
        penalty_points = 10
        
        #Check if any leniency rules are broken and set mandatory penalty
        if driving_speed > speed_limit + TRAILER_LENIENCY and light_trailer:
            mandatory_penalty = True
        if driving_speed > speed_limit + SCHOOL_ZONE_LENIENCY and school_zone:
            mandatory_penalty = True
        if driving_speed > speed_limit + HOLIDAY_LENIENCY and holiday_period:
            mandatory_penalty = True

    #check rest of speed categories
    elif speed_limit + DEFAULT_LENIANCY_SPEED < driving_speed <= speed_limit + 20:
        penalty_points = 20
        mandatory_penalty = True
    elif speed_limit + 20 < driving_speed <= speed_limit + 30:
        penalty_points = 35
        mandatory_penalty = True
    elif speed_limit + 30 < driving_speed <= speed_limit + 35:
        penalty_points = 40
        mandatory_penalty = True
    elif speed_limit + 35 < driving_speed:
        penalty_points = 50
        mandatory_penalty = True
    else:
        penalty_points = 0

    return (mandatory_penalty, penalty_points)