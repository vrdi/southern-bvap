# southern-bvap
Home for data, code, &amp; sundry for the Southern BVAP paper.

## At a Glance
State | FIPS | Congressional Seats | Lower Chamber Seats | Upper Chamber Seats | Blocks | Block Groups | Population | BPOP* % | BVAP* %
----- | ---- | ------------------- | ------------------- | ------------------- | ------ | ------------ | ---------- | ----- | -----
Alabama | `01` | 7 | 105 | 35 | 252266 | 3437 | 4779736 | 26.04% | 24.74%
Arkansas | `05` | 4 | 100 | 35 | 186211 | 2147 | 2915918 | 15.33% | 14.24%
Georgia | `13` | 14 | 180 | 56 | 291086 | 5529 | 9687653 | 30.05% | 28.81%
Louisiana | `22` | 6 | 105 | 39 | 204447 | 3461 | 4533372 | 31.82% | 29.85%
Mississippi | `28` | 4 | 122 | 52 | 171778 | 2161 | 2967297 | 36.85% | 34.55%
South Carolina | `45` | 7 | 124 | 46 | 181908 | 3054 | 4625364 | 27.67% | 26.32%
Tennessee | `47` | 9  | 99 | 33 | 240116 | 4125| 6346105 | 16.54% | 15.48%

\* counts only Black alone populations

## Data
State dual graphs (block level) are too large to host on github; [they can be downloaded here](http://groups.csail.mit.edu/gdpgroup/redistricting/states.zip).

## State Laws
Comprehensive writeup for each state's redistricting rules [can be found here](https://docs.google.com/document/d/1aJmJ_u3CV50kMVMtmDcI9op_Zsq1k4dLLo6pYbaa1uw/edit).

### [Alabama](http://www.legislature.state.al.us/aliswww/reapportionment/Reapportionment%20Guidelines%20for%20Redistricting.pdf)
* Congressional district populations must be "as nearly equal in population as practicable."
* State legislative districts must not deviate by more than 2%.
* Must prioritize "race-neutral criteria" over "consideriations that stereotype voters on the basis of race, color, or membership in a language-minority group."
* Must be "contiguous and reasonably compact".
* Each district composed of "as few counties as practicable."
* Contiguity by water is allowed.
* Communities of interest must be respected.

### [Arkansas](http://www.arkansasredistricting.org/article-8)
* Congressional district populations must deviate by no more than 1%; state legislative districts by 10%.
* State legislative districts must follow county lines except where otherwise legally impossible. (No such requirement for Congressional districts.)
* Must minimize political subdivisions.
* Must maintain communities of interest.
* Squares and circles preferable; deviation from these shapes increases chance that the district will be thrown out.

### [Georgia](https://www.dropbox.com/s/2egd5vpo0djzqt5/GeorgiaHouseCommitteeGuidelines2011-12.pdf)
* Congressional districts must deviate by no more than one person.
* State legislative districts should "achieve a total population that is substantially equal as pacticable..."
* Single-point (queen) contiguity not allowed.

### [Louisiana](http://house.louisiana.gov/h_redistricting2011/2011_H&GA_REAPP%20RULES_ADOPTED.pdf)
* Congressional districts must have "a population as nearly equal to the ideal district population as practicable."
* All redistricting plans must contain "whole election precincts."

### [Mississippi](https://www.dropbox.com/s/z36sc17c3m1cewv/MississippiLegislativeAndCongressionalRedistrictingCommitteeMinutes2012-04-05.pdf)
* No rules other than federally mandated rules and laws.

### [South Carolina](http://redistricting.schouse.gov/6334-1500-2011-Redistricting-Guidelines-(A0404871).pdf)
* Congressional district ideal population is 660,766; plans must "produce the lowest overall range of deviation possible when taking into consideration geographic limitations."
* State House ideal population is 37,301. No deviation more than 5% (federal standard).
* Communities of interest must be respected.

### [Tennessee](https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=52a2d157-6b41-4f61-8774-bb258bac8500&nodeid=AADAABAABAAC&nodepath=%2fROOT%2fAAD%2fAADAAB%2fAADAABAAB%2fAADAABAABAAC&title=3-1-102.+Composition+of+state+senatorial+districts.&config=025054JABlOTJjNmIyNi0wYjI0LTRjZGEtYWE5ZC0zNGFhOWNhMjFlNDgKAFBvZENhdGFsb2cDFQ14bX2GfyBTaI9WcPX5&pddocfullpath=%2fshared%2fdocument%2fstatutes-legislation%2furn%3acontentItem%3a4X8J-6SH0-R03N-6340-00008-00&ecomp=g37_kkk&prid=fb0c9dd9-aeb8-45d1-be46-126cc5b507d9)
* Contiguity by water is sufficient.

