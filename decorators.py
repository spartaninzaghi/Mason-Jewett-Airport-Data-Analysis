import variables as v

class Decorators:

    def __init__(self):
        self = self

    def sprinkle_leading_zeroes(self, num: int, width: int) -> str:
        """ Pad number with leading zeroes of specified width, from right to left
        """
        decorated_num = str(num)
        decorated_num = decorated_num.zfill(width)

        return decorated_num

    def sprinkle_trailing_asterisk(self, num) -> str:
        """ Append an asterisk to the end of a numeric string. eg. 7 or '7' becomes "7*"
        """
        num_str = str(num)
        num_str = num.strip("*")
        decorated_num = f"{num_str}*"
        
        return decorated_num

    def colon_pierce_time(self, time_hh_mm: list) -> str:
        """ Returns time as colon separated string. eg. ['15', '30'] becomes "15:30"
        """
        colon_pierced_time = ":".join(time_hh_mm)

        return colon_pierced_time

    def slash_date(self,m_d_list: list) -> str:
        """ Create a date string from a [month, day] list. eg. `[3, 31]` becomes "03/31/2021"
        """
        m = m_d_list[v.MM]
        d = m_d_list[v.DD]

        mm = self.sprinkle_leading_zeroes(m, 2)
        dd = self.sprinkle_leading_zeroes(d, 2)
        yyyy = str(2021)

        slashed_date = f"{mm}/{dd}/{yyyy}"
        return slashed_date

    def decorate_row_output(self, row: list):
        """ Make an observation row match the required output format.
        """
        DT, TM, TP, SP, DR, PK, CL, VS, EI = 0, 1, 2, 3, 4, 5, 6, 7, 8
        HR, MN = 0, 1

        date = row[DT]       
        time = row[TM]   
        temp = row[TP]              
        wspd = row[SP] 
        wdir = row[DR]
        pkwg = row[PK]
        ceil = row[CL] 
        vsbl = row[VS]
        ethr = row[EI]
        
        hrs = time[HR]
        mns = time[MN]

        decorated_row = [date, hrs, mns, temp, wspd, wdir, pkwg, ceil, vsbl, ethr]
        
        return decorated_row

    def decorate_test_row(self, row: list):

        test_row = self.decorate_row_output(row)
        test_row = [f"{data:^20s}" for data in test_row]
        decorated_row = "|".join(test_row)

        return decorated_row

    def decorate_test_header(self, header: list):
        header = [f"{data:^20s}" for data in header]
        decorated_header = "|".join(header)

        return decorated_header

    def __str__(self):
        return f"{self}"

    def __repr__(self):
        return self.__str__()