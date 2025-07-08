nano climate_analysis.pynano climate_analysis.pynano climate_analysis.pynano climate_analysis.py# TODO: Add NONO data transformation logic for North Pacific Gyre analysis# TODO: Add NONO data transformation logic for North Pacific Gyre analysisimport sys
import temp_conversion
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, f"{script}: requires a data filename"

filename = sys.argv[1]
climate_data = open(filename, 'r')

for line in climate_data:
    data = line.strip().split(',')

    if data[0].startswith('#'):
        # skip comment lines
        pass
    else:
        try:
            fahr = float(data[3])
            if fahr != -9999:
                celsius = temp_conversion.fahr_to_celsius(fahr)
                kelvin = temp_conversion.fahr_to_kelvin(fahr)
                print(f"{celsius}, {kelvin}")
        except (IndexError, ValueError):
            continue
import sys
import temp_conversion
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, f"{script}: requires a data filename"

filename = sys.argv[1]
climate_data = open(filename, 'r')

for line in climate_data:
    data = line.strip().split(',')

    if data[0].startswith('#'):
        # skip comment lines
        pass
    else:
        try:
            fahr = float(data[3])
            if fahr != -9999:
                celsius = temp_conversion.fahr_to_celsius(fahr)
                kelvin = temp_conversion.fahr_to_kelvin(fahr)
                print(f"{celsius}, {kelvin}")
        except (IndexError, ValueError):
            continue
import sys
import temp_conversion
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, f"{script}: requires a data filename"

filename = sys.argv[1]
climate_data = open(filename, 'r')

for line in climate_data:
    data = line.strip().split(',')

    if data[0].startswith('#'):
        # skip comment lines
        pass
    else:
        try:
            fahr = float(data[3])
            if fahr != -9999:
                celsius = temp_conversion.fahr_to_celsius(fahr)
                kelvin = temp_conversion.fahr_to_kelvin(fahr)
                print(f"{celsius}, {kelvin}")
        except (IndexError, ValueError):
            continue
import sys
import temp_conversion
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, script + ": requires filename"
filename = sys.argv[1]

climate_data = open(filename, 'r')

for line in climate_data:
    data = line.split(',')

    if data[0][0] == '#':
        # don't want to process comment lines, which start with '#'
        pass
    else:
        # extract our max temperature in Fahrenheit - 4th column
        fahr = float(data[3])

        # don't process invalid temperature readings of -9999
        if fahr != -9999:
            celsius = temp_conversion.fahr_to_celsius(fahr)
            kelvin = temp_conversion.fahr_to_kelvin(fahr)

            print(str(celsius)+", "+str(kelvin))
import sys
import temp_conversion
import signal

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, f"{script}: requires a data filename"

filename = sys.argv[1]
climate_data = open(filename, 'r')

for line in climate_data:
    data = line.strip().split(',')

    if data[0].startswith('#'):
        # skip comment lines
        pass
    else:
        try:
            fahr = float(data[3])
            if fahr != -9999:
                celsius = temp_conversion.fahr_to_celsius(fahr)
                kelvin = temp_conversion.fahr_to_kelvin(fahr)
                print(f"{celsius}, {kelvin}")
        except (IndexError, ValueError):
            continue
# TODO: Add NONO data transformation logic for North Pacific Gyre analysis# TODO: Add NONO data transformation logic for North Pacific Gyre analysis
git add climate_analysis.py
git commit -m "Added NONO data processing placeholder"


