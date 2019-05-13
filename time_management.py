"""
Logic for Calculating start times, total time,
assignment load, and scheduling
"""
from datetime import timedelta, datetime
import assignments
# Gets attributes so that we can sort by datetime later in module
from operator import attrgetter

def CalculateQuestionsTime(questions, rate, buffer=5):
    """
    Takes number of questions and Rate returns int
    Configurable Buffer, Default 5 Minutes, allows for Turn in
    :param questions:
    :param rate:
    :param buffer:
    :return:
    """
    questions = float(questions)
    rate = float(rate)
    # Rounding because Scheduling Seconds is not practical
    required_minutes = round(((questions) // (rate)) + buffer)
    return (required_minutes)


def CalculateStartTime(due_date, number_of_minutes):
    """
    Calculates Start Time Based on Due Date + Minutes
    :param due_date:
    :param number_of_minutes:
    :return:
    """
    start_time = due_date - timedelta(minutes=number_of_minutes)
    return (start_time)


def MultipleStartTimes(list_of_assignments, Student_object):
    """
    This will take a list of Assignments for a Student and Calculates the start dates
    and Update the Assignment With the Start time Takes a Student Object to determine their rates
    :param list_of_assignments:
    :param Student_object:
    :return:
    """
    date_total_dictionary={}
    sorted_list=sorted(list_of_assignments,key=getattr('due_date'))
    for assignment in sorted_list:
        if type(assignment) == assignments.SelfLearningAssignment:
            # Get number of questions and rate to figure out duration
            num_questions=assignment.questions
            questions_rate=Student_object.questions_per_min
            duration=CalculateQuestionsTime(num_questions,questions_rate)

        # If Due date isnt in the dictionary make it at 0
        if assignment.due_date.date() not in date_total_dictionary:
            date_total_dictionary[assignment.due_date.date()]=0
        due_date=assignment.due_date
        # Add Total Duration to get start time
        duration+=date_total_dictionary[assignment.due_date.date()]
        start_time=CalculateStartTime(due_date, duration)
        # Update Total Duration
        assignments.set_scheduled_start(start_time)
