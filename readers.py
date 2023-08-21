import csv
import variables as v
from filters import Filters
from calculators_and_converters import CalculatorsAndConverters


class Readers:

    def __init__(self, filename_txt, filename_csv):
        self.filename_txt = filename_txt
        self.filename_csv = filename_csv

    class Observations:

        def __init__(self, filename_csv):
            self.filename_csv = filename_csv

            self.cc = CalculatorsAndConverters()
            self.fl = Filters()
            self.fl.Observations = self.fl.Observations()

        def read_file(self, twilight_dict):
            """
            Read the csv file containing the relevant data.
            """
            with open(f"{self.filename_csv}", "r") as observations:
        
                START_OF_ACTUAL_DATA = 13 - 1
                reader = list( csv.reader(observations) )
                reader = reader[ START_OF_ACTUAL_DATA: ] # beginning at start of actual data

            observations_rows = self.fl.Observations.full_filter_by_emptiness_and_VFR(reader, twilight_dict)

            with open("out.txt", "w") as out:
                for row in observations_rows:
                    print(row, file=out)
            return observations_rows


        def create_dict(self):
            """
            -- STRUCTURE --

            observations_dict = {month number: {month day: [ [time, temp, wind_speed, wind_direction, wind_peak, low_cloud_Ht, visibility] ] }}
            
            Date,Hr,Min,Temp (F),Wind Spd (mph),Wind Direction (deg),Peak Wind Gust(mph),Low Cloud Ht (ft),Visibility (mi)
            """
            observations_rows = self.read_file()

            observations_dict = {
                row[v.DATE_mm_dd][ v.MM ]: 
                {row[v.DATE_mm_dd][ v.DD ]: [  row[1:] for row[v.DATE_mm_dd] in observations_rows ] }
                for row in observations_rows
            }
            return observations_dict


    class Twilight:

        def __init__(self, filename_txt):
            self.filename_txt = filename_txt

            self.cc = CalculatorsAndConverters()
            self.fl = Filters()
            self.fl.Twilight = self.fl.Twilight()
            self.fl.Observations = self.fl.Observations()

        def read_file(self):
            """ Read `civil_twilight.txt` into list of rows of day + time tuple data.
            """
            
            with open(f"{self.filename_txt}", "r") as twilight:
                twilight = twilight.readlines()
                

            # slicing only needful time & date data (starts at index 9 and ends at index 39 in `twilight`)
            twilight = twilight[ 9 : 40 ]

            # reading each `non-empty` (number_containing) row element into `twilight_rows`
            twilight_rows = [ 
                
                [self.cc.convert_to_int(time_data) for time_data in row.strip().split()]
                for row in twilight
            ]
            
            # updating `twilight_rows` to have format [day (int), start_and_end_time_tuple (ints), ... ]
            twilight_rows = [
                [day] + list( zip( row[1::2], row[2::2] ) ) 
                for day, row in enumerate (twilight_rows, 1)
            ]
            
            # filling appropriate days in February, April, June, September, and November with `none` tuples
            for day, row in enumerate(twilight_rows[28:], 29):
                for month, _ in enumerate(row):
                    
                    if ( month == v.FEB and day in [29, 30, 31]  or
                        month in v.MONTHS_WITH_ONLY_30_DAYS and day == 31
                    ):
                        row.insert(month, v.tuple_of_2nones)
            return twilight_rows

        
    
        def create_dict(self):
            """
            STRUCTURE --> twilight_dict = {month number: day: {Start: <start time>, End: <end time>}  }
            """
            twilight_rows = self.read_file()        
            DAY, START, END = 0, 0, 1

            twilight_dict = {
                    month_number: {
                        row[DAY]: {"sunrise": row[month_number][START], "sunset": row[month_number][END]}
                        for row in twilight_rows
                        if row[month_number] != v.tuple_of_2nones
                    }
                    for month_number in v.MONTH_NUMBERS                        
                }
            return twilight_dict

    
    def __str__(self):
        return f"{self}"

    def __repr__(self):
        return self.__str__()
        
