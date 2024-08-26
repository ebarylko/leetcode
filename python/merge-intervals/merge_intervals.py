from toolz import thread_last, first, juxt, iterate, last, drop, count
from itertools import takewhile


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
        cpy_1 = list(iter(current_unmerged_intervals))
        if count(cpy_1) == 0 or ffirst(cpy_1) not in range(*merged_interval):
            return None
        else:
            return update_interval(merged_interval, first(cpy_1)), drop(1, cpy_1)

    return iterate(largest_overlapping_interval, (current_merged_interval, unmerged_intervals))


def find_overlapping_interval(overlapping_intervals, remaining_intervals):
    """
    :param overlapping_intervals: a collection of intervals I such that each I_i represents an interval
    which encompasses one or more intervals in the original collection
    :param remaining_intervals: a subset of the intervals in the original collection which have not been merged
    :return: an updated set of the overlapping intervals with the remaining intervals which did not overlap
    """
    def interval_can_be_merged(interval):
        return interval is not None

    return thread_last(overlapping_interval(first(remaining_intervals), drop(1, remaining_intervals)),
                       (takewhile, interval_can_be_merged),
                       list,
                       last)


def merge_intervals(intervals):
    """
    :param intervals: a collection of pairs, each containing a minimum and maximum element of the range
    they represent
    :return: the merged intervals
    """
    def sort_by_lower_bound(intervls):
        return sorted(intervls, key=first)

    def gen_range(interval):
        return set(range(interval[0], interval[1] + 1))

    return thread_last(intervals,
                       sort_by_lower_bound,

                       )

