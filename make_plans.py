import geopandas
from gerrychain import Graph
import maup

state = 'tennessee'
fips = '47'
abbr = 'tn'

blocksfile = 'tl_2018_%s_tabblock10.shp'
types = ['cd116', 'sldl', 'sldu']
types_col = ['CD116FP', 'SLDLST', 'SLDUST']
shapefiles = ['%s_cd116.shp', 'tl_2018_%s_sldl.shp', 'tl_2018_%s_sldu.shp']

def isnan(x):
    return x != x

blocks = geopandas.read_file('/tmp/' + abbr + '/' + (blocksfile % fips))
for i in range(3):
    districts = geopandas.read_file('/tmp/' + abbr + '/' + (shapefiles[i] % fips))
    assignment = maup.assign(blocks, districts)
    blocks[types[i]] = assignment
    f = open('plans/' + state + '/' + abbr + '_' + types[i] + '.txt', 'w')
    for j in range(blocks.shape[0]):
        dis = 'nan' if isnan(assignment[j]) else districts[types_col[i]][assignment[j]]
        if dis == 'nan':
            print('WARNING: nan found, ' + types[i])
        f.write('%s %s\n' % (str(blocks['GEOID10'][j]), dis))
    f.close()

