
print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
# omniparser/gradebook_parser.py

import pandas

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath)

    breakpoint()

    return 90.64 #"OOPS"


if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    calculate_average_grade_from_csv(gradebook_filepath)