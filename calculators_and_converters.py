from math import sin as Sine
from decorators import Decorators
import variables as v

class CalculatorsAndConverters:

    def __init__(self):
        self.dec = Decorators()     

    def calculate_crosswind(self, wind_speed: float, wind_direction: float) -> float:
        """ Return crosswind componend of `wind_speed`.
        """
        crosswind = wind_speed * Sine(wind_direction)
        
        return crosswind

    
    def convert_mph_to_Knots(self, mph: int) -> float:
        """ Convert a speed value in `mph` to `knots` (nautical mph).
        """
        speed_in_Knots = self.convert_to_flt(mph) * v.KNOTS_IN_1MPH

        return speed_in_Knots

    
    def convert_to_flt(self, value) -> float:
        """ Convert numeric value to a floating point number.
        """
        if type(value) == float or type(value) == int: flt = float(value)
        elif type(value) == str:
            value_as_num = "".join([n for n in value if n.isnumeric()])           
            flt = float(value_as_num)
        else: print("Error: Unconvertible type for this function")

        return flt


    def convert_to_int(self, value) -> int:
        """ Convert a string to an integer. Non-numeric values get returned as `-1`.
        """
        i = int( self.convert_to_flt(value) )

        return i

    def daylight_time(self, t_twilight: int) -> int:
        """ Convert a civil twilight time value to daylight time. 
        eg. `15:00` (represented as `1500`) becomes `1600` after adding `1 hour` as `100`
        """
        t_daylight = t_twilight + 100

        return t_daylight

    def fill_in_missing_data_with_valid_predecessor(self, super_list: list):
        """ Fill cells with invalid values (`m` or `M`) with immediately, previously recorded value for
        that column. This algorithm assumes that the 1st row in `super_list` has valid values throughout
        """
        for r, row in enumerate(super_list):
            for c, col in enumerate(row):
                if self.is_missing(col):

                    previous_row = r - 1
                    previous_col = c
                    previous_data = super_list[previous_row][previous_col]

                    if not self.is_missing(previous_data):
                        super_list[r][c] = self.dec.sprinkle_trailing_asterisk(previous_data)

    def is_missing(self, value) -> bool:
        """ Returns `True` if a data cell is missing a valid value (i.e.contains string `m` or `M`)
        """
        if type(value) == str and value in "mM": return True
        else: return False

    def make_m_d_list(self, forwardslash_sep_mm_dd_yy: str) -> list:
        """ Return a 2-length integer list: [month, day]. eg. "3/31/2021" becomes `[3, 31]`
        """
        m_d_list = forwardslash_sep_mm_dd_yy.split("/")
        m_d_list = [self.convert_to_int(s) for s in m_d_list[:2]]

        return m_d_list

    def generate_date_str(self,m_d_list: list) -> str:
        """ Create a date string from a [month, day] list. eg. `[3, 31]` becomes "03/31/2021"
        """
        m = m_d_list[v.MM]
        d = m_d_list[v.DD]

        mm = self.dec.sprinkle_leading_zeroes(m, 2)
        dd = self.dec.sprinkle_leading_zeroes(d, 2)
        yyyy = str(2021)

        date_str = f"{mm}/{dd}/{yyyy}"

        return date_str
    
    def merge_time_hm(self, colon_sep_time_h_m: str) -> int:
        """ Merge time string into a single integer. eg. "15:30" becomes `1530` of type (int).
        """
        merged_time_hm = colon_sep_time_h_m.strip().split(":")
        merged_time_hm = "".join(merged_time_hm)
        merged_time_hm = self.convert_to_int(merged_time_hm)

        return merged_time_hm

    def unmerge_time_hh_mm(self, merged_time_int: int) -> list:
        """ Unmerges time from a single integer into a 2-length list of the hour and minute
        components of the time: `[hh_string, mm_string]`
        """
        merged_time_str = str(merged_time_int)
        merged_time_str = self.dec.sprinkle_leading_zeroes(merged_time_str, 4)
        unmerged_time_str_lst = [merged_time_str[:2], merged_time_str[2:]]

        return unmerged_time_str_lst
        

    def months_dict(self):
        """ Create a dictionary of all month numbers as keys and month names as values.
        """
        months_dict = dict(   zip(v.MONTH_NUMBERS, v.month_names)  )

        return months_dict

    def month_name_from_number(self, month_number: int) -> str:
        """ Retrieve the name of a particular month by passing its number as argument.
        """
        months_dict = self.months_dict()

        month_name = months_dict[month_number]
        return month_name

    def month_number_from_name(self, month_name: str) -> int:
        """ Retrieve the number of a particular month by passing its name as argument.
        """
        months_dict = self.months_dict()

        for m_name, m_num in months_dict.items():
            if m_name == month_name: month_number = m_num
                
        return month_number
        

    def __str__(self):
        return f"{self}"

    def __repr__(self):
        return self.__str__()
    