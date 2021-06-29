import sys

from utils.utils import *

with open(sys.argv[2]) as f:
    report = f.read()
    report = report.lower()
    #print(report)


if sys.argv[1] == "temperature":
    candidates = re.findall('\d{2,3}\.\d{1}', report)
    print(candidates)

    prefixes = ["temperature"]  # also covers:, "temperature is", "temperature was","temperature of", "temperature:"
    prefix_distance = 20
    suffixes = ["deg", "celsius", "fahrenheit"]  # also covers:"degree","degrees"
    suffix_distance = 15
    exception = ["down from", "gained", "increased", "decreased", "days ago", "week ago"]  # includes increased by, increased to
    exception_distance = 30

elif sys.argv[1] == "age":
    candidates = re.findall('\d{1,2}\-[a-z]{3,4}\-[o,l,d]{3}', report) + re.findall(
        '[e,x]{1,2}\-\d{2}\s[a-z]{3,5}', report)  # covers xx-year/week/day format and ex-XX weeks/week/day format

    prefixes = ["female", "male", "patient", "child",
                     "baby"]  # also covers:, "temperature is", "temperature was","temperature of", "temperature:"
    prefix_distance = 15
    suffixes = ["gentlemen", "women", "man", "male", "female"]  # also covers:"degree","degrees"
    suffix_distance = 15
    exception = ["father", "dad", "mother", "mom", "grandma", "grandpa", "sister", "brother", "uncle", "aunt",
                      "friend", "wife", "husband", "partner", "spouse"]
    exception_distance = 30


return_values = []

for candidate in candidates:

    cand_position = report.find(candidate)
    #print(cand_position)

    # check temperature prefix/suffix/exception
    prefix_state = prefix_check(report=report, cand_position=cand_position, prefixes=prefixes,
                                prefix_distance=prefix_distance)
    suffix_state = suffix_check(report, candidate=candidate,  cand_position=cand_position,  suffixes=suffixes,
                                suffix_distance=suffix_distance)
    exception_state = exception_check(report, candidate=candidate, cand_position=cand_position, exception=exception,
                                      exception_distance=exception_distance)

    if ((prefix_state == True) or (suffix_state == True)) & (exception_state == False) :
        #print(candidate)
        return_values.append(candidate)

if len(return_values) == 1 :
    print((sys.argv[1]).capitalize(),": ", return_values[0])

elif len(return_values) > 1 :
    print("Multiple values found: ", return_values)

elif len(return_values) == 0 :
    print("No value was found.")

