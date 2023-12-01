def basic_read(file_path):
    try:
        input_file = open(file_path)
    except OSError:
        print(f"could not open {input_file}")
        exit(-1)

    return [line.strip() for line in input_file]