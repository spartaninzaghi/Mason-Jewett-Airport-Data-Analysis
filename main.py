            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #~                                                                         ~#        
            #~                   FALL 2022 CSE 231 HONORS PROJECT                      ~#     
            #~    -- Data Analysis For Alternate Runway at Mason Jewett Airport --     ~#    
            #~                                                                         ~#   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~                                                                                                ~#
#~   --Algorithm--                                                                                ~#  
#~                                                                                                ~#
#~   import `Master` class from `master` module as `operateOn`                                    ~#
#~   declare program main()                                                                       ~#
#~                                                                                                ~#  
#~      generate clean `twilight_dict` by calling `data.rd.Twilight.create_dict()` object         ~#
#~      generate clean `observations_dict` which contains valid set of data points                ~#  
#~                                                                                                ~#  
#~      End of program:                                                                           ~#   
#~                                                                                                ~#  
#~      if __name__ is "__main__": call main()                                                    ~#   
#~                                                                                                ~#  
#~                                                                                                ~#  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#===================================================================================================

from master import Master as operateOn

# instantiating data object. All classes within the `master` module are operable on this object
data = operateOn("civil_twilight.txt", "TEW_2021_Observations.csv", "daylight_weather.csv", 
                 "current_runway_safe.csv", "proposed_runway_safe.csv")

def print_results_of_analysis(safe_dict: dict):
    """
    """
    safe_for_current = safe_dict['current_runway_safe.csv']
    safe_for_proposed = safe_dict['proposed_runway_safe.csv']
    safe_for_both = safe_for_current
    safe_for_all = safe_dict['daylight_weather.csv']

    n_current = len(safe_for_current)
    n_proposed = len(safe_for_proposed)
    n_both = len(safe_for_both)
    n_all = len(safe_for_all)

    print(f"Total feasible data points: {n_all}")
    print(f"Data points that are safe for the current runway: {n_current}")
    print(f"Data points that are safe for the proposed runway: {n_proposed}")
    print(f"Data points that are safe for both runways: {n_both}")

def main():
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~                                               STEP 1                                                  ~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # creating valid dictionary of valid all civil twilight times across all months
    twilight_dict = data.rd.Twilight.create_dict()
    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~                                               STEP 2                                                  ~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # generating clean observation data points stored as rows in list of lists of rows, `observations_rows`
    observations_rows = data.rd.Observations.read_file(twilight_dict)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~                                               STEP 3                                                  ~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # generating dictionary of safe data points for the daylight_weather.csv, current and proposed runway files
    safe_dict = data.jd.generate_safe_datapoints_dict(observations_rows)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~                                               STEP 4                                                  ~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # writing data to appropriate files
    data.wr.write_safe_runway_data(safe_dict)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~                                               STEP 5                                                  ~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # printing results to console
    print_results_of_analysis(safe_dict)
    

if __name__ == "__main__":
    main()
