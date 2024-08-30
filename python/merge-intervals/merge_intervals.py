from toolz import thread_last, first, juxt, iterate, last, count
from itertools import takewhile, dropwhile
from functools import partial


def overlapping_interval(current_merged_interval, unmerged_intervals):
    """
    :param current_merged_interval: the largest merged interval so far
    :param unmerged_intervals: the intervals remaining to merge
    :return: a collection containing the results of updating the largest overlapping interval found so far
    """
    def update_interval(interval_1, interval_2):
        joined_intervals = interval_1 + interval_2
        return juxt(min, max)(joined_intervals)

    def ffirst(coll):
        return first(first(coll))

    def largest_overlapping_interval(merged_and_unmerged_intervals):
        """
        :param merged_and_unmerged_intervals: the largest merged interval so far and the intervals remaining to merge
        :return: a pair consisting of the updated largest interval and the intervals left to merge if the interval
        could be expanded, None otherwise
        """
        merged_interval, current_unmerged_intervals = merged_and_unmerged_intervals
        if count(current_unmerged_intervals) == 0 or ffirst(current_unmerged_intervals) not in range(merged_interval[0], merged_interval[1] + 1):
            return None
        else:
            return update_interval(merged_interval, current_unmerged_intervals[0]), current_unmerged_intervals[1:]

    return iterate(largest_overlapping_interval, (current_merged_interval, unmerged_intervals))


def find_overlapping_interval(overlapping_and_remaining_intervals):
    """
    :param overlapping_intervals: a collection of intervals I such that each I_i represents an interval
    which encompasses one or more intervals in the original collection
    :param remaining_intervals: a subset of the intervals in the original collection which have not been merged
    :return: an updated set of the overlapping intervals with the remaining intervals which did not overlap
    """
    def interval_can_be_merged(interval):
        return interval is not None

    def update_merged_intervals(current_merged_intervals, merged_interval_and_remaining_unmerged_intervals):
        merged_interval, _ = merged_interval_and_remaining_unmerged_intervals
        return current_merged_intervals + [merged_interval]

    def remaining_intervals_to_merge(merged_interval_and_remaining_unmerged_intervals):
        return list(last(merged_interval_and_remaining_unmerged_intervals))

    overlapping_intervals, remaining_intervals = overlapping_and_remaining_intervals
    return thread_last(overlapping_interval(remaining_intervals[0], remaining_intervals[1:]),
                       (takewhile, interval_can_be_merged),
                       list,
                       last,
                       juxt(partial(update_merged_intervals, overlapping_intervals), remaining_intervals_to_merge))


def merge_intervals(intervals):
    """
    :param intervals: a collection of pairs, each containing a minimum and maximum element of the range
    they represent
    :return: the merged intervals
    """
    def sort_by_lower_bound(intervls):
        return sorted(intervls, key=first)

    def still_merging_intervals(merged_and_unmerged_intervals):
        _, unmerged_intervals = merged_and_unmerged_intervals
        return count(unmerged_intervals) != 0

    def prepare_initial_data(unmerged_intervals):
        return [[], unmerged_intervals]

    return thread_last(intervals,
                       sort_by_lower_bound,
                       prepare_initial_data,
                       (iterate, find_overlapping_interval),
                       (dropwhile, still_merging_intervals),
                       next,
                       first,
                       (map, list),
                       list
                       )


def overlapping_interval_2(merged_and_unmerged_intervals):
    """
    :param merged_and_unmerged_intervals: the largest merged interval so far and the intervals remaining to merge
    :return: a collection containing the updated largest overlapping interval and the remaining intervals which did not overlap if
    the interval could be expanded, None otherwise
    """
    def update_interval(interval_1, interval_2):
        joined_intervals = interval_1 + interval_2
        return [min(joined_intervals), max(joined_intervals)]

    def ffirst(coll):
        return coll[0][0]

    merged_interval, current_unmerged_intervals = merged_and_unmerged_intervals
    if len(current_unmerged_intervals) == 0 or ffirst(current_unmerged_intervals) not in range(merged_interval[0], merged_interval[1] + 1):
        return None
    else:
        return update_interval(merged_interval, current_unmerged_intervals[0]), current_unmerged_intervals[1:]


def iterate_until(func, pred, initial_val):
    curr_val, prev = initial_val, initial_val
    while pred(curr_val):
        prev = curr_val
        curr_val = func(curr_val)

    return prev


def find_overlapping_interval_2(overlapping_and_remaining_intervals):
    """
    :param overlapping_and_remaining_intervals: a tuple of merged intervals and the intervals remaining to merge
    :return: an expanded set of the overlapping intervals with the remaining intervals which did not overlap
    """
    def interval_can_be_merged(interval):
        return interval is not None

    def update_merged_intervals(current_merged_intervals, merged_interval):
        return current_merged_intervals + [merged_interval]

    overlapping_intervals, remaining_intervals = overlapping_and_remaining_intervals
    intervals_to_merge = (remaining_intervals[0], remaining_intervals[1:])
    new_merged_interval, remaining_intervals = iterate_until(overlapping_interval_2,
                                                             interval_can_be_merged,
                                                             intervals_to_merge)

    return update_merged_intervals(overlapping_intervals, new_merged_interval), remaining_intervals


def merge_intervals_2(intervals):
    """
    :param intervals: a collection of pairs, each containing a minimum and maximum element of the interval
    they represent
    :return: joins all the intervals sharing a common element and returns the resulting disjoint intervals
    """
    def sort_by_lower_bound(intervls):
        return sorted(intervls, key=first)

    def still_merging_intervals(merged_and_unmerged_intervals):
        _, unmerged_intervals = merged_and_unmerged_intervals
        return count(unmerged_intervals) != 0

    def prepare_initial_data(unmerged_intervals):
        return [[], unmerged_intervals]

    def first_elem_not_satisfying_pred(coll, pred):
        """
        :param coll: a collection of data
        :param pred: a predicate which can be applied on each element in coll
        :return: the first element in coll not satisfying pred
        """
        return next(dropwhile(pred, coll))

    def iterate_using_f(func, x):
        while True:
            yield x
            x = func(x)

    initial_data = prepare_initial_data(sort_by_lower_bound(intervals))
    merged_intervals, _ = first_elem_not_satisfying_pred(iterate_using_f(find_overlapping_interval_2, initial_data),
                                                         still_merging_intervals)
    return merged_intervals


