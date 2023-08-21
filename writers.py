import csv
from decorators import Decorators

HEADER_1 = "JEWETT FLD AP (MI),54822,,Lat: 42.5658,Lon: -84.4331,Elev: 922 ft,,,".split(",")
HEADER_2 = "Date,Hr,Min,Temp (F),Wind Spd (mph),Wind Direction (deg),Peak Wind Gust(mph),Low Cloud Ht (ft),Visibility (mi)".split(",")

class Writers:

    def __init__(self, daylight_csv_fn, current_csv_fn, proposed_csv_fn):
            self.daylight_csv_fn = daylight_csv_fn
            self.current_csv_fn = current_csv_fn
            self.proposed_csv_fn = proposed_csv_fn

            self.dec = Decorators()

    def write_safe_runway_data(self, safe_dict: dict):

        with open(f"{self.daylight_csv_fn}", "w") as d, open(f"{self.current_csv_fn}", "w") as c, open(f"{self.proposed_csv_fn}", "w") as p, open("seer.txt", "w") as see:

            d_wr = csv.writer(d)
            c_wr = csv.writer(c)
            p_wr = csv.writer(p)

            d_wr.writerow(HEADER_1)
            d_wr.writerow(HEADER_2)

            c_wr.writerow(HEADER_1)
            c_wr.writerow(HEADER_2)

            p_wr.writerow(HEADER_1)
            p_wr.writerow(HEADER_2)            

            #SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
            print("TEST VIEW OF `daylight_weather.csv` OUTPUT [`writers` | 18w, 34, 37 ]\n", file=see)
            print(self.dec.decorate_test_header(HEADER_2), file=see)
            for row in safe_dict[self.daylight_csv_fn]:
                d_wr.writerow(self.dec.decorate_row_output(row))
                print(self.dec.decorate_test_row(row), file=see)

            for row in safe_dict[self.current_csv_fn]:
                c_wr.writerow(self.dec.decorate_row_output(row))

            for row in safe_dict[self.proposed_csv_fn]:
                p_wr.writerow(self.dec.decorate_row_output(row))


            




        