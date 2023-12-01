import sys
sys.path.append('../utils')  
from arg_parse_wrapper import only_filepath_argparse
from read_input import basic_read

valid_digits = {"zero":0, "one":1, "two":2, "three":3, "four":4,
                "five":5, "six":6, "seven":7, "eight":8, "nine":9}


#Takes:20*#InputLines*LengthInputLine Time ~ O(#InputLines*LengthInputLine) Time
def calibrate_values_no_written(input_data):
    calibrated_info = []
    for input_str in input_data:

        first_info = (None, None)
        last_info = (None, None)

        for num in valid_digits.values():
            try:
                first_ind = input_str.index(str(num))
                last_ind = input_str.rindex(str(num))

                if (first_info[0] is None) or (first_ind < first_info[0]):
                    first_info = (first_ind, num)

                if (last_info[0] is None) or (last_ind > last_info[0]):
                    last_info = (last_ind, num)

            except ValueError:
                pass
        
        calibrated_info.append([first_info, last_info])

    return calibrated_info

#Takes:40*#InputLines*LengthInputLine Time ~ O(#InputLines*LengthInputLine) Time
def calibrate_values_with_written(input_data):
    calibrated_info = []
    number_calibrated_vals = calibrate_values_no_written(input_data)
    for i,input_str in enumerate(input_data):
        first_info = number_calibrated_vals[i][0]
        last_info = number_calibrated_vals[i][1]

        for written_num in valid_digits.keys():
            try:
                first_ind = input_str.index(written_num)
                last_ind = input_str.rindex(written_num)

                if (first_info[0] is None) or (first_ind < first_info[0]):
                    first_info = (first_ind, valid_digits[written_num])

                if (last_info[0] is None) or (last_ind > last_info[0]):
                    last_info = (last_ind, valid_digits[written_num])

            except ValueError:
                pass
        
        calibrated_info.append([first_info, last_info])

    return calibrated_info

#Takes: O(#InputLines) Time
def sum_calibrated_infos(calibrated_info):
    running_sum = 0
    for info in calibrated_info:
        try:
            running_sum += info[0][1]*10 + info[1][1]
        except:
            #it couldn't anything in the string something
            running_sum += 0
    return running_sum


def main():
    file_path = only_filepath_argparse()
    input_data = basic_read(file_path)
    print(f"Calibrate no written words result:{sum_calibrated_infos(calibrate_values_no_written(input_data))}")
    print(f"Calibrate with written words result:{sum_calibrated_infos(calibrate_values_with_written(input_data))}")


if __name__ == "__main__":
    main()