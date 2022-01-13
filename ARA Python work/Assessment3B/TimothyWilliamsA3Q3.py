# Assessment 3B Question 3
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

def result_display(demerit_result,drive_speed,speed_limit):
    '''
    Function tells calculate_points function what result to display handling the demerit_result arg
    Aim is to tidy up calculate points function and stop doubling up
    '''
    if demerit_result[1] != 0:
        if demerit_result[0]:
            printable = f"The mandatory penalty for driving at {drive_speed}km/h in a {speed_limit}km/h zone is {demerit_result[1]} points."
        else:
            printable = f"The discretional penalty for driving at {drive_speed}km/h in a {speed_limit}km/h zone is {demerit_result[1]} points."
    else:
        printable = f"{drive_speed}km/h in a {speed_limit}km/h is not speeding."
    return printable

def calculate_points():
    '''
    Function runs the demerit points calculation from Q1 taking inputs from the GUI
    '''
    ds = request.form.get("driving-speed")
    sl = request.form.get("speed-limit")
    to = request.form.get("towing-trailer")
    so = request.form.get("school-zone")
    ho = request.form.get("holiday-period")

    if ds.isdigit() and sl.isdigit():
        ds = int(ds)
        sl = int(sl)
        demerit_result = get_demerit_points(ds, sl, to, so, ho)
        field_text = result_display(demerit_result,ds,sl)
    elif ds.count(".") == 1 and ds.replace(".", "").isdigit() and sl.isdigit():
        ds = float(ds)
        sl = int(sl)
        demerit_result = get_demerit_points(ds, sl, to, so, ho)
        field_text = result_display(demerit_result,ds,sl)
    elif sl.count(".") == 1 and sl.replace(".", "").isdigit() and ds.isdigit():
        sl = float(sl)
        ds = int(ds)
        demerit_result = get_demerit_points(ds, sl, to, so, ho)
        field_text = result_display(demerit_result,ds,sl)
    else:
        demerit_result = (False, 'No Value')
        field_text = "Both speeds must be numeric values."

    return (demerit_result[1], field_text)

from flask import Flask, render_template, request
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cool-and-groovy'
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def home():

    reset_check = ""
    demerit_check = ""
    response = ""

    if request.method == 'POST':
        button_select = request.form.getlist("action")[0]
        if button_select == "Reset":
            reset_check = "True"
        if button_select == "Calculate points":
            response = calculate_points()[1]
            demerit_check = calculate_points()[0]
            print(demerit_check)

    return render_template('index.html', title='Demerit points calculator', highlighted = reset_check, demerit_value = demerit_check, response_text = response)

@app.errorhandler(404)
def page_not_found(e):
    '''
    If page entered incorrectly send back to main page
    '''
    return render_template('404.html'), 404

app.run()
