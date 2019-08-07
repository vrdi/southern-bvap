# Plans
## File Format
Each plans file contains a number of rows equal to the number of census blocks in that state. Each line contains two space separated integers; the first is the `geoid` of the block, and the second is a (zero-padded) district number. The order of the blocks in this file _should_ match the order of the nodes in the json dual graphs for the states, but no guarantees are made, so it's best to join on the `geoid`s.

## Real Life Plans
In the "real life" plans, the district numbers match the actual districts; ie, they are 1-indexed and the blocks labeled "01" actually belong to the 1st district for that state.

Each state contains (at least) these three "real life" plans:
* `xx_cd116.txt`: Congressional districts for the 116th Congress
* `xx_sldl.txt`: District lines for the state's lower legislative chamber, as of 2018.
* `xx_sldu.txt`: District lines for the state's upper legislative chamber, as of 2018.

The plans were generated from maup assignment (https://github.com/mggg/maup#assigning-precincts-to-districts), assigning blocks to relevant districts. All TIGER/line shapefiles provided by the Census. 2010 blocks were used, and most recent district shapefiles (116th congress and 2018 state districting plans).

One block in Arkansas, three blocks in South Carolina, and one block in Tennessee initially were assigned a "nan" value for indeterminant reason by maup. Possibly, these blocks did not align with any district according to the districting shapefiles. In any case, each of them unambiguously belong in a single district, because all of their neighbors belong to the same district. By contiguity rules, the unassigned block has a unique district to which it belongs. Each of the unassigned blocks also had zero total population. The plan files were manually edited to fix this mistake.

The file make_real_life_plans.py provides the script I used to automate the process.
