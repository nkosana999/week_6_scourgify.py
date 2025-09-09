import csv
import sys

def main():

    # These first conditionals test the mandotary requirements from user_input
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[0][-3:] != ".py" or sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
        sys.exit("Not a valid file type")


    # This last conditional attempts to open and manipulate the files or catch any FileNotFoundError
    else:
        try:
            #openning the csv files to read from onw and write into the new one.
            with open(sys.argv[1], "r") as before, open(sys.argv[2], "w", newline='') as after:
                before_file = csv.reader(before)
                after_file = csv.DictWriter(after, fieldnames = ["first", "last", "house"])
                after_file.writeheader()

                # This block of code  is for collecting the csv.reader() output so the data iin original csv can be manipulated.
                students = []
                for row in before_file:
                    students.append(row)

                # The rearranging the data in the original file and writing the formated output into the new file.
                for student in students[1:]:
                    combined = student[0]
                    last, first = combined.split(", ")
                    house = student[1]
                    after_file.writerow({"first" : first, "last" : last, "house" : house})

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
