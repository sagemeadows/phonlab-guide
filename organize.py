# !user/bin/python
#
# organize.py -- organize 'aggregated_data.csv' file(s)
#
# usage:
#     organize.py [aggregated_data.csv] ([aggregated_data.csv...]) (export (output_directory/))
#

import sys
import pandas as pd

#read data
data = pd.read_csv(sys.argv[1])

if len(sys.argv) >= 3:
    count = 1
    for x in sys.argv[2:]:
        if ".csv" in x:
            tmp = pd.read_csv(x)
            data = data.append(tmp, ignore_index=True)
            count = count + 1
    print("\nOrganizing {num} data files...\n".format(num=count))
else:
    print("\nOrganizing 1 data file...\n")

#clean up
##split 'file' column
data.insert(1, 'sound', '')
data[['file', 'sound']] = data['file'].str.split('_',expand=True)
##delete unnecessary columns
del data['group']
del data['color']
del data['number']
del data['cutoff']

#get average formants
data['f1_mean'] = round(data[['f12', 'f13', 'f14']].mean(axis=1), 0)
data['f2_mean'] = round(data[['f22', 'f23', 'f24']].mean(axis=1), 0)
data['f3_mean'] = round(data[['f32', 'f33', 'f34']].mean(axis=1), 0)
data['f4_mean'] = round(data[['f42', 'f43', 'f44']].mean(axis=1), 0)

#get vocal tract lengths
##equations
def vt_formant(n, l, c=35000):
    return (((2 * n) - 1) * c) / (4 * l)

def vt_length(n, f, c=35000):
    return (((2 * n) - 1) * c) / (4 * f)

##get formant lengths
data['length_f1'] = vt_length(1, data['f1_mean'])
data['length_f2'] = vt_length(2, data['f2_mean'])
data['length_f3'] = vt_length(3, data['f3_mean'])
data['length_f4'] = vt_length(4, data['f4_mean'])
##get average formant length
data['length_mean'] = data[['length_f1', 'length_f2', 'length_f3', 'length_f4']].mean(axis=1)
##delete unnecessary length columns
del data['length_f1']
del data['length_f2']
del data['length_f3']
##round lengths
data['length_f4'] = round(data['length_f4'], 2)
data['length_mean'] = round(data['length_mean'], 2)

#wrap up
print(data)

message_export_true_here = "\nFinished!\nFile 'organized_data.csv' has been created in current directory.\n"
message_export_true_there = "\nFinished!\nFile 'organized_data.csv' has been created in {output_directory}\n"
message_export_false = "\nFinished!\nOrganized data was not saved. To save and export data, repeat command (up-arrow key) and add 'export'.\n"

##compute option
if "export" in sys.argv:
    if sys.argv[-1] != "export":
        output = sys.argv[-1] + 'organized_data.csv'
        data.to_csv(path_or_buf=output)
        print(message_export_true_there.format(output_directory=sys.argv[-1]))
    else:
        data.to_csv(path_or_buf='organized_data.csv')
        print(message_export_true_here)
else:
    print(message_export_false)

#end
