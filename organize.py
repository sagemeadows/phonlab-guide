# !user/bin/python
#
# organize.py -- organize 'aggregated_data.csv' file(s)
#
# usage:
#     organize.py [aggregated_data.csv] ([aggregated_data.csv...]) (-l) (-s (-e [output_directory]/))
#

import sys
import optparse
import pandas as pd

# parse the options
parser = optparse.OptionParser()
parser.add_option("-s", "--save", action="store_true", dest="save_data", default=False,
                  help="choose to save organized data file")
parser.add_option("-e", "--elsewhere", dest="save_location",
                  help="save organized data file in specific location: path_to_output_directory/",
                  metavar="output_directory/")
parser.add_option("-l", "--lite", action="store_true", dest="data_format", default=False,
                  help="delete time-spaced formant values after mean formants are calculated")
(options, args) = parser.parse_args()

# read data
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

# clean up
## split 'file' column
data.insert(1, 'sound', '')
data[['file', 'sound']] = data['file'].str.split('_',expand=True)
## delete unnecessary columns
del data['group']
del data['color']
del data['number']
del data['cutoff']

# get average formants
data['f1_mean'] = round(data[['f12', 'f13', 'f14']].mean(axis=1), 0)
data['f2_mean'] = round(data[['f22', 'f23', 'f24']].mean(axis=1), 0)
data['f3_mean'] = round(data[['f32', 'f33', 'f34']].mean(axis=1), 0)
data['f4_mean'] = round(data[['f42', 'f43', 'f44']].mean(axis=1), 0)

# lite option
if options.data_format == True:
    del data['f11']
    del data['f21']
    del data['f31']
    del data['f41']
    del data['f12']
    del data['f22']
    del data['f32']
    del data['f42']
    del data['f13']
    del data['f23']
    del data['f33']
    del data['f43']
    del data['f14']
    del data['f24']
    del data['f34']
    del data['f44']
    del data['f15']
    del data['f25']
    del data['f35']
    del data['f45']


# get vocal tract lengths
## vocal tract length formula
def vt_length(n, f, c=35000):
    return (((2 * n) - 1) * c) / (4 * f)

## get formant lengths
data['length_f1'] = vt_length(1, data['f1_mean'])
data['length_f2'] = vt_length(2, data['f2_mean'])
data['length_f3'] = vt_length(3, data['f3_mean'])
data['length_f4'] = vt_length(4, data['f4_mean'])
## get average formant length
data['length_mean'] = data[['length_f1', 'length_f2', 'length_f3', 'length_f4']].mean(axis=1)
## delete unnecessary length columns
del data['length_f1']
del data['length_f2']
del data['length_f3']
## round lengths
data['length_f4'] = round(data['length_f4'], 2)
data['length_mean'] = round(data['length_mean'], 2)

# wrap up
print(data)

message_export_true = "\nFinished!\nCreated 'organized_data.csv' in current directory.\n"
message_export_elsewhere = "\nFinished!\nCreated 'organized_data.csv' in {}\n"
message_export_false = "\nFinished!\nOrganized data was not saved.\n To save data, repeat command (up-arrow key) and add `-s`\
                        To save data in different directory, add `-s -e [path_to_output_directory]/`"

## export option
if options.save_data == True:
    if options.save_location:
        location = options.save_location
        output = location + 'organized_data.csv'
        data.to_csv(path_or_buf=output)
        print(message_export_elsewhere.format(location))
    else:
        data.to_csv(path_or_buf='organized_data.csv')
        print(message_export_true)
else:
    print(message_export_false)

# end
