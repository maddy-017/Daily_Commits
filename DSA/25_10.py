def sumof_array(values : list[int]):
    ending = best  = values[0]
    for i in range(1,len(values)):
        value = values[i]
        ending= max(value,value+ending)
        best= max(best,ending)

    return best
print(sumof_array([2,-1,3]))
def maximum_subarray_with_indices(values: list[int]) -> tuple[int, int, int]:  # Return sum, start, and end.
    ending = values[0]  # Best sum of a section ending at the first value.
    best = values[0]  # Best sum found anywhere so far.
    current_start = 0  # Start index of the current section.
    best_start = 0  # Start index of the overall winning section.
    best_end = 0  # End index of the overall winning section.

    for i in range(1, len(values)):  # Visit each remaining index.
        value = values[i]  # Read the current value.

        if value > ending + value:  # Check whether starting fresh is better.
            ending = value  # Start a new section at this value.
            current_start = i  # Remember the new section's start.
        else:
            ending = ending + value  # Extend the current section.

        if ending > best:  # Check whether this section beats the overall best.
            best = ending  # Save the improved maximum sum.
            best_start = current_start  # Save its starting index.
            best_end = i  # Save its ending index.

    return best, best_start, best_end  # Return the answer and its boundaries.