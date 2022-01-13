# Assessment 3B Question 1
# Timothy Williams, tsw0050@arastudent.ac.nz

def get_demerit_points(driving_speed, speed_limit, light_trailer = False, school_zone = False, holiday_period = False):
    '''
    Function works out the demerit point penalty for a driving speed in a particular speed zone
    '''
    # all speeds in km/h any additons to speed_limit (e.g. speed_limit + 20) are additional speed categories
    TRAILER_LENIENCY = 5
    SCHOOL_ZONE_LENIENCY = 4
    HOLIDAY_LENIENCY = 4
    DEFAULT_LENIANCY_SPEED = speed_limit + 10

    # No mandatory penalty unless driver breaks the rules past leniency criteria
    mandatory_penalty = False

    # test for each speed category and if speed >= 10 over the limit then check leniency rules
    if speed_limit < driving_speed:
        penalty_points = 10

        if driving_speed <= DEFAULT_LENIANCY_SPEED:
            if any([light_trailer, school_zone, holiday_period]):

                #Check if any leniency rules are broken and set mandatory penalty
                if driving_speed > speed_limit + TRAILER_LENIENCY and light_trailer: mandatory_penalty = True
                if driving_speed > speed_limit + SCHOOL_ZONE_LENIENCY and school_zone: mandatory_penalty = True
                if driving_speed > speed_limit + HOLIDAY_LENIENCY and holiday_period: mandatory_penalty = True
        else:
            penalty_points += 10
            mandatory_penalty = True

            #check rest of speed categories 21-30 // 31-35 // 36+ and add demerits for each tier
            if driving_speed > speed_limit + 20:
                penalty_points += 15
            if driving_speed > speed_limit + 30:
                penalty_points += 5
            if driving_speed > speed_limit + 35:
                penalty_points += 10
    else:
        penalty_points = 0

    return (mandatory_penalty, penalty_points)