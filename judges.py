from calculators_and_converters import CalculatorsAndConverters
from decorators import Decorators

class Judges:

    def __init__(self):
        self = self
        self.cc = CalculatorsAndConverters()
        self.dec = Decorators()

    def wind_is_best_aligned_with(self, wind_direction_deg):
        ew_closeness_100 = abs(wind_direction_deg - 100)
        ew_closeness_280 = abs(wind_direction_deg - 280)
        ew_best_alignment = min(ew_closeness_100, ew_closeness_280)

        ns_closeness_10 = abs(wind_direction_deg - 10)
        ns_closeness_190 = abs(wind_direction_deg - 190)
        ns_best_alignment = min(ns_closeness_10, ns_closeness_190)

        best_alignment_ewns = min(ew_best_alignment, ns_best_alignment)

        if best_alignment_ewns == ew_best_alignment:
            return "east-west"
    
        elif best_alignment_ewns == ns_best_alignment:
            return "north-south"


    def generate_safe_datapoints_dict(self, observations_rows: list):
        """ Return `True` if a data row has crosswind between `5` and `8` knots and gusts at `12` knots.
        """
        WIND_SPEED, WIND_DIRECTION, PEAK_GUST = 3, 4, 5

        safe_dict = {

            'daylight_weather.csv': [],
            'current_runway_safe.csv': [],
            'proposed_runway_safe.csv': []

        }
        for r, row in enumerate(observations_rows):

            row += [""]

            wind_speed_mph = self.cc.convert_to_int( row[WIND_SPEED])
            wind_speed_knt = self.cc.convert_mph_to_Knots(wind_speed_mph)
            wind_direction_deg = self.cc.convert_to_int( row[WIND_DIRECTION] )

            crosswind_knt = self.cc.calculate_crosswind(wind_speed_knt, wind_direction_deg)
            
            peak_gust_mph = self.cc.convert_to_int( row[PEAK_GUST] )
            peak_gust_knt = self.cc.convert_mph_to_Knots( peak_gust_mph )

            best_wind_alignment = self.wind_is_best_aligned_with(wind_direction_deg)
            # print(best_wind_alignment)

            # ------------------------ CONDITION 0 -------------------------
            if wind_speed_mph <= 5: # We define “calm” as 5 mph wind or less

                if crosswind_knt == 0:
                    row[-1] = "either"

                    safe_dict['current_runway_safe.csv'].append(row)
                    safe_dict['proposed_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)

                else:
                    if best_wind_alignment == "east-west":
                        safe_dict['current_runway_safe.csv'].append(row)
                        safe_dict['daylight_weather.csv'].append(row)
                    
                    elif best_wind_alignment == "north-south":
                        safe_dict['proposed_runway_safe.csv'].append(row)
                        safe_dict['daylight_weather.csv'].append(row)

            # ------------------------ CONDITION I-------------------------
            elif 5 <= crosswind_knt <= 8 and peak_gust_knt <= 12:

                if best_wind_alignment == "east-west":
                    safe_dict['current_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)
                
                elif best_wind_alignment == "north-south":
                    safe_dict['proposed_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)

                                    
            # ---------------------- CONDITION II -------------------------
            elif 8 <= crosswind_knt <= 12 and peak_gust_knt <= 15:

                if best_wind_alignment == "east-west":
                    safe_dict['current_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)
                
                elif best_wind_alignment == "north-south":
                    safe_dict['proposed_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)

            # ---------------------- CONDITION III------------------------
            elif 12 <= crosswind_knt <= 15 and peak_gust_knt <= 15:

                if best_wind_alignment == "east-west":
                    safe_dict['current_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)
                
                elif best_wind_alignment == "north-south":
                    safe_dict['proposed_runway_safe.csv'].append(row)
                    safe_dict['daylight_weather.csv'].append(row)
                        
        return safe_dict
                

                    
            




    