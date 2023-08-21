import variables as v
from calculators_and_converters import CalculatorsAndConverters
from decorators import Decorators

class Filters:

    def __init__(self):
        self = self

    class Observations:
         
        def __init__(self):
            self.cc = CalculatorsAndConverters()
            self.dec = Decorators()
        
        def filter_out_empty_rows_and_fill_in_missing_data(self, reader: list, twilight_dict: dict) -> list:
            """ Return reader list with empty rows excluded and missing data filled in.
            """
            
            reader = [

                [
                    self.cc.make_m_d_list( row[v.DATE_mm_dd_yy] ), # row [0]
                    self.cc.merge_time_hm( row[v.TIME_hh_mm]    ), # row [1]
                    row[v.TEMP_F],                                 # row [2]
                    row[v.WIND_SPEED_mph],                         # row [3]
                    row[v.WIND_DIRECTION_deg],                     # row [4]
                    row[v.PEAK_WIND_GUST_mph],                     # row [5]
                    row[v.LOW_CLOUD_HT_ft],                        # row [6]
                    row[v.VISIBILITY_mi]                           # row [7]
                ]
                for row in reader 

                # skipping empty rows
                if  row and '' not in row                              
            ]

            self.cc.fill_in_missing_data_with_valid_predecessor(reader)

            return reader

        def full_filter_by_emptiness_and_VFR(self, reader: list, twilight_dict: dict) -> list:
            """ Return list of observations' rows with all unallowed data excluded.
            """

            reader = self.filter_out_empty_rows_and_fill_in_missing_data(reader, twilight_dict)
            
            observations_rows = []

            for row in reader:

                date = row[0]       
                time = row[1]   
                temp = self.cc.convert_to_int( row[2] )             
                wspd = self.cc.convert_to_int( row[3] )   
                wdir = self.cc.convert_to_int( row[4] )
                pkwg = self.cc.convert_to_int( row[5] )
                ceil = self.cc.convert_to_int( row[6] )  
                vsbl = self.cc.convert_to_int( row[7] )   

                month = date[v.MM]
                day = date[v.DD]

                sunrise = twilight_dict[month][day]['sunrise']
                sunset  = twilight_dict[month][day]['sunset']

                if ceil < 2000 or temp < 35 or vsbl < 5 or pkwg > 20 or month not in v.ALLOWED_MONTHS: 
                    continue

                elif time < sunrise or time > sunset:
                    continue
                    
                else:
                    row[0] = self.dec.slash_date(date)
                    row[1] = self.cc.unmerge_time_hh_mm(time)
                    
                    observations_rows.append(row)
            
            return observations_rows

            
    class Twilight:

        def __init__(self):
            self = self
            
        def full_filter_by_month(self, twilight_dict: dict) -> dict:
            
            twilight_dict = {

                month_number: value_list
                for month_number, value_list in twilight_dict.items()
                if month_number in v.ALLOWED_MONTHS
            }

            return twilight_dict

    def __str__(self):
        return f"{self}"

    def __repr__(self):
        return self.__str__()

            
    
        