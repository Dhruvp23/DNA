import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:  # check for command line arguments
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as database:     # database file open
        reader = csv.DictReader(database)
        Db = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as dnaseq:  # sequence file open
        sequence = dnaseq.read()

    # TODO: Find longest found of each STR in DNA sequence
    colm = list(Db[0])      # csv database 1st column
    pattern = colm[1:]      # pattern to be matched
    strcount = {}  # counter for longest found in sequnce
    for d in pattern:
        strcount[d] = longest_match(sequence, d)  # longest found Called

    # TODO: Check database for matching profiles
    for guys in Db:
        found = 0
        for d in pattern:
            if int(guys[d]) == strcount[d]:
                found = found + 1     #counter for highest number of match
        if found == len(pattern):
            print(guys["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence found in a "substring" (a subset of characters) within sequence
        # If a found, move substring to next potential found in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a found in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no found in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
