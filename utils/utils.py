import re

def prefix_check(report, cand_position, prefixes, prefix_distance) :
    prefix_state = False
    for prefix in prefixes :
        if report[cand_position - prefix_distance :cand_position].find(prefix) != -1 :
            prefix_state = True
    return prefix_state


def suffix_check(report, candidate, cand_position, suffixes, suffix_distance) :
    suffix_state = False
    for suffix in suffixes :
        if report[cand_position :cand_position + len(candidate) + suffix_distance].find(suffix) != -1 :
            suffix_state = True
    return suffix_state


def exception_check(report,candidate, cand_position, exception, exception_distance) :
    exception_state = False
    for ex in exception :
        if report[cand_position - exception_distance :cand_position + len(candidate) + exception_distance].find(
                ex) != -1 :
            exception_state = True
    return exception_state


def get_value(data_request, report) :

    report = report.lower()

    if data_request == "temperature" :
        candidates = re.findall('\d{2,3}\.\d{1}', report)
        print(candidates)

        prefixes = ["temperature"]  # also covers:, "temperature is", "temperature was","temperature of", "temperature:"
        prefix_distance = 20
        suffixes = ["deg", "celsius", "fahrenheit"]  # also covers:"degree","degrees"
        suffix_distance = 15
        exception = ["down from", "gained", "increased", "decreased", "days ago",
                     "week ago"]  # includes increased by, increased to
        exception_distance = 30

    elif data_request == "age" :
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

    for candidate in candidates :

        cand_position = report.find(candidate)
        # print(cand_position)

        # check temperature prefix/suffix/exception
        prefix_state = prefix_check(report=report, cand_position=cand_position, prefixes=prefixes,
                                    prefix_distance=prefix_distance)
        suffix_state = suffix_check(report, candidate=candidate, cand_position=cand_position, suffixes=suffixes,
                                    suffix_distance=suffix_distance)
        exception_state = exception_check(report, candidate=candidate, cand_position=cand_position, exception=exception,
                                          exception_distance=exception_distance)

        if ((prefix_state == True) or (suffix_state == True)) & (exception_state == False) :
            # print(candidate)
            return_values.append(candidate)

    if len(return_values) == 1 :

        print((data_request).capitalize(), ": ", return_values[0])
        return report,return_values

    elif len(return_values) > 1 :
        print("Multiple values found: ", return_values)
        return report, return_values

    elif len(return_values) == 0 :
        return_values = ["nan"]
        print(return_values)
        return report,return_values
        print("No value was found.")
