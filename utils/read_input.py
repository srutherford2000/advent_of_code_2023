import re

def basic_read(file_path, data_type):
    try:
        input_file = open(file_path)
    except OSError:
        print(f"could not open {input_file}")
        exit(-1)

    ret_val = None

    try:
        ret_val = [data_type(line.strip()) for line in input_file]
    except ValueError:
        print("not all correct type try again")
        input_file.close()
        exit()
    
    input_file.close()
    return ret_val

def read_and_split(file_path, delimeter, data_type):
    try:
        input_file = open(file_path)
    except OSError:
        print(f"could not open {input_file}")
        exit(-1)

    ret_val = []

    try:
        for line in input_file:
            ret_val.append([data_type(val) for val in line.strip().split(delimeter)])
    except ValueError:
        print("not all correct type try again")
        input_file.close()
        exit()
    
    input_file.close()
    return ret_val
    
def read_from_regex(file_path, regex_pattern, data_types):
    try:
        input_file = open(file_path)
    except OSError:
        print(f"could not open {input_file}")
        exit(-1)

    num_fields = len(data_types)
    regex = re.compile(regex_pattern)
    result_list = []

    for line in input_file:
        match = regex.match(line.strip())
                
        try:
            if match:
                all_fields = []
                if data_types is not None:
                    for i in range(num_fields):
                        all_fields.append(data_types[i](match.group(i+1)))
                else:                    
                    for i in range(num_fields):
                        all_fields.append(match.group(i+1))


                result_list.append(all_fields)
            else:
                raise ValueError
        except ValueError:
            print(f"Line:{line.strip()} didnt match the regex pattern or data type is wrong")
            input_file.close()
            exit()
    
    input_file.close()
    return result_list

def read_separated_multiline_input(file_path, delimiter, data_type):
    try:
        input_file = open(file_path)
    except OSError:
        print(f"could not open {input_file}")
        exit(-1)
    
    ret_val = []
    current_val = []

    for line in input_file:
        line = line.strip()
        if line == "":
            ret_val.append(current_val)
            current_val = []
        else:
            try:
                current_val += [data_type(i) for i in line.split(delimiter)]
            except ValueError:
                print(f"line:{line} had bad data type")
                input_file.close()
                exit()

    ret_val.append(current_val)

    input_file.close()
    return ret_val