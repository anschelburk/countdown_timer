from datetime import timedelta
import math

def next_occurrence(target_minute, current_datetime):
    """
    Returns the next datetime where the minute equals target_minute.

    Args:
        target_minute (int): The target minute after the hour that the timer should count down to.
        current_datetime (datetime): The current date and time.

    Returns:
        next_occurrence (datetime): The next datetime where the minute equals target_minute.
    """
    # If the target minute has not yet passed for the current hour:
    if current_datetime.minute < target_minute:
        next_occurrence = current_datetime.replace(minute=target_minute, second=0, microsecond=0)
    
    # If the target minute has already passed for the current hour:
    else:
        next_hour = current_datetime + timedelta(hours=1)
        next_occurrence = next_hour.replace(minute=target_minute, second=0, microsecond=0)
    
    return next_occurrence

def progress_bar(remaining_time_in_seconds):
    """
    Generates a visual progress bar representing the remaining time until the next hour.

    Args:
        remaining_time_in_seconds (int): An integer which represents the total remaining time in seconds
            until the current timer finishes counting down.

    Returns:
        progress_bar_text (str):
            A visual progress bar composed of '#' and '.' characters showing the remaining
            amount of time until the current timer finishes counting down.

            Each '#' represents about 2 minutes of remaining time. (Every 2 minutes, the '#' character furthest
            to the right is replaced by a '.' character.) The '.' characters represent elapsed time. The
            number of minutes is rounded up if any seconds are left beyond a full minute to ensure a more
            intuitive countdown.

            The bar is 32 characters wide: 30 total '#' and '.' characters, enclosed in a left and right bracket.

            Examples:

            - 16 minutes, 00 seconds → 16 minutes → 8 filled ('#') characters and 22 empty ('.') characters, shown below.
                [########......................]
            
            - 16 minutes, 01 second  → 17 minutes → 9 filled ('#') characters and 21 empty ('.') characters, shown below.
                [#########.....................]
    """

    remaining_minutes_rounded = math.ceil(remaining_time_in_seconds / 60)
    progress_bar_full = '#' * round(remaining_minutes_rounded / 2)
    progress_bar_empty = '.' * (30 - round(remaining_minutes_rounded / 2))
    progress_bar_text = f'[{progress_bar_full}{progress_bar_empty}]'
    return progress_bar_text

def total_remaining_seconds(end_of_current_timer_loop, current_datetime):
    """
    Calculates the total number of whole seconds remaining until the next timer event.

    This function computes the time difference between the current moment and the
    specified end time, and returns the total number of seconds as an integer.

    Args:
        end_of_current_timer_loop (datetime): The target end time of the current timer cycle.
        current_datetime (datetime): The current time and date.

    Returns:
        total_remaining_time_in_seconds (int): The total number of seconds remaining until the timer reaches its end.
    """
    remaining_time = end_of_current_timer_loop - current_datetime
    total_remaining_time_in_seconds = int(remaining_time.total_seconds())
    return total_remaining_time_in_seconds