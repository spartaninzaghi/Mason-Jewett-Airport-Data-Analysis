from readers import Readers as rd
from writers import Writers as wr
from filters import Filters as fl
from judges  import Judges  as jd
from decorators import Decorators as dc
from calculators_and_converters import CalculatorsAndConverters as cc

class Master:

    def __init__(self, filename_txt, filename_csv, daylight_csv_fn, current_csv_fn, proposed_csv_fn):
        
        # constructing file name variables 
        self.filename_txt = filename_txt
        self.filename_csv = filename_csv
        self.daylight_csv_fn = daylight_csv_fn
        self.current_csv_fn = current_csv_fn
        self.proposed_csv_fn = proposed_csv_fn
        
        # constructing class suite, assigning variables where necessary

        # 1 Readers
        self.rd = rd(self.filename_txt, self.filename_csv)
        self.rd.Twilight = self.rd.Twilight(self.filename_txt)
        self.rd.Observations = self.rd.Observations(self.filename_csv)

        # 2 Writers
        self.wr = wr(self.daylight_csv_fn, self.current_csv_fn, self. proposed_csv_fn)

        # 3 Filters 
        self.fl = fl()
        self.fl.Twilight = self.fl.Twilight()
        self.fl.Observations = self.fl.Observations()

        # 4 Judges
        self.jd = jd()

        # 5 Decorators
        self.dc = dc()

        # 6 CalculatorsAndConverters
        self.cc = cc()

        
        

        

        


        
        