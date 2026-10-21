
# string for nums from 0 to 19
nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
    "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# string for multiples of ten
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


# num --> words
def number_to_words(number):
    if number == 100:
        return "one hundred"
    if number < 20:
        return nums[number]
    if number % 10 == 0:
        return tens[number // 10]
    return tens[number // 10] + "-" + nums[number % 10]


# open txt file
with open("checks.txt", "r", encoding="utf-8") as file:
   for line in file:    # read line by line
        parts = line.strip().split(maxsplit=1)  # separate amount and description by removing extra spaces + nl and splitting at 1st whitespace
        if len(parts) != 2: # check for amt and description parts
            print("invalid line:", line.strip())
            continue    # skip loop and go to next line
        amount, description = parts # store as separate variables
        try:
            dollar_text, cent_text = amount.split(".")
            if not (dollar_text.isdigit()   # check format
                    and len(cent_text) == 2
                    and cent_text.isdigit()):
                raise ValueError
            dollars = int(dollar_text)
            cents = int(cent_text)

            if dollars > 100 or (dollars == 100 and cents > 0): # check limit
                raise ValueError
        except ValueError:
            print(amount, "-> invalid amount")
            continue

        dollar_unit = "dollar" if dollars == 1 else "dollars"   # more text formatting plural/singular
        cent_unit = "cent" if cents == 1 else "cents"

        expected = (    # text response
            "only " + number_to_words(dollars) + " " + dollar_unit
            + " and " + number_to_words(cents) + " " + cent_unit
        )

        if description.lower().strip() == expected: # compare actual vs expected
            print(amount, "-> correct")
        else:
            print(amount, "-> incorrect")
            print("  expected:", expected)
