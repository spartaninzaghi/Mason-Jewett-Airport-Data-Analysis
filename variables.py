
# 0 ----------------------------------- MONTH VARIABLES ----------------------------------
JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
MONTHS_WITH_ONLY_30_DAYS = [APR, JUN, SEP, NOV]
month_names = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]      
MONTH_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ALLOWED_MONTHS = [MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV]

# 1 ------- ORIGINAL DATA INDEXES IN `TEW_2021_Observations.csv` file HEADER ------------

DATE_mm_dd_yy = 0
TIME_hh_mm = 1
TEMP_F = 2 
RH_percent = 3
DEWPT_F = 4
WIND_SPEED_mph = 5
WIND_DIRECTION_deg = 6
PEAK_WIND_GUST_mph = 7
LOW_CLOUD_HT_ft = 8
MED_CLOUD_HT_ft = 9 
HIGHT_CLOUD_HT_ft = 10
VISIBILITY_mi = 11
ATMOSPHERIC_PRESSURE_hPa = 12
SEA_LEVEL_PRESSURE_hPa = 13
ALTIMETER_hPa = 14
PRECIP_in = 15
WIND_CHILL_F = 16
HEAT_INDEX_F = 17

# 2 ------------------------------ CONVERSION CONSTANTS ---------------------------------
KNOTS_IN_1MPH = 0.868976


# 3 -------------------------- NEW DATA INDICES FOR FILE WRITING ------------------------
MM, DD = 0, 1 
DATE_mm_dd = 0
TIME_hhmm = 1
TEMP_F_flt = 2
WIND_SPEED_mph_flt = 3
WIND_DIRECTION_deg_flt = 4
PEAK_WIND_GUST_mph_flt = 5
LOW_CLOUD_HT_ft_flt = 6
VISIBILITY_mi_flt = 7

# 4 ------------------------ OTHER USEFUL VARIABLE ASSIGNMENTS -------------------------
tuple_of_2nones = (None, None)

