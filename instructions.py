# -------------------- CREDITS TO ORIGINAL AUTHOR OF HONORS PROJECT DOC ---------------------

# Analysis of whether to fly and on which runway
"""
________________________________________________________________________________________________
| 1 Safe runway based on a crosswind component of 5 knots to 8 knots with gusts to 12 knots    |
|___ __________________________________________________________________________________________|
| 2 Safe runway based on a crosswind component of 8 knots to 12 knots with gusts to 15         |
| knots                                                                                        |
|______________________________________________________________________________________________|
| 3 Safe runway based on crosswind component of 12 to 15 knots with gusts to 20 kts            |
|______________________________________________________________________________________________|
| 4 1-3 above – where the conditions remain within the limits between sunrise and sunset.      |
| Need to note whether the landing runway would differ from the take-off runway in the         |
| PM. (east/west vs north/south)                                                               |
|______________________________________________________________________________________________|
| 5 Based on the above, Days and number of Hours that favor current or proposed runway.        |
|______________________________________________________________________________________________|
| 6 Days and number of hours that would be out of limits for the east/west runway that would   |
| be within limits for a north/south runway                                                    |
|______________________________________________________________________________________________|
| 7 For purposes of this analysis, safety is binary – it is ether within limits or not. In low |
| wind conditions, either runway may be safe and should be thus represented. Unless the        |
| wind is zero, only one runway direction would be preferred, and that should be indicated.    |
| (Note: the choice of runway is up to the pilot – many may choose the hard surface            |
| runway as long as it is safe. This would also be true in reverse for those who prefer a      |
| grass strip.)                                                                                |
|______________________________________________________________________________________________|
| 8 Note restrictions below.                                                                   |
|______________________________________________________________________________________________|
"""

# Restrictions: only these times are to be considered
"""
_______________________________________________________________________________________________
1 All take offs and landings would be restricted to modified VFR conditions (less than
2000 foot MSL cloud ceiling and 5 miles or more of visibility). Also, only in daylight
(we provide a file of civil twilight times civil_twilight.txt – did you know there
are three different twilights?). Lucky you, both data files provided use the same time
standard (Local Standard Time) so Daylight Savings Time adjustments are not needed.
We use the “Low Cloud Ht” field for the MSL cloud ceiling.
_______________________________________________________________________________________________
2 March through November
_______________________________________________________________________________________________
3 Temperature is 35 degrees F or greater.
_______________________________________________________________________________________________
"""