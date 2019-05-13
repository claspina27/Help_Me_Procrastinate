"""
Defines Assignment Class and properties
"""
from dateutil.parser import parse
from datetime import datetime, timedelta

class BaseAssignment(object):
    """
    Base Assignment all Assignments require these fields (scheduled start optional)
    """
    def __init__(self, name, due_date, professor,scheduled_start=""):
        self.name = name
        self.due_date = parse(due_date)
        self.professor = professor
        if scheduled_start == '':
            #self.scheduled_start=scheduled_start
            self.scheduled_start = datetime.now() + timedelta(minutes=9600)
        else:
            #self.scheduled_start = parse(scheduled_start)
            self.scheduled_start = datetime.now()

    def set_scheduled_start(self,scheduled_start):
        self.scheduled_start=scheduled_start

class SelfLearningAssignment(BaseAssignment):
    """
    Inherits BaseAssignment, Adds required Fields for Test Review
    """
    def __init__(self, name,due_date,professor,questions,scheduled_start=""):
        BaseAssignment.__init__(self,name,due_date,professor,scheduled_start)
        self.questions = questions

class ReadingAssignment(BaseAssignment):
    """
    Inherits BaseAssignment, Adds Required Fields for Reading
    """
    def __init__(self, name, due_date, professor, pages):
        BaseAssignment.__init__(self, name, due_date, professor)
        self.pages = pages

class WritingAssignment(BaseAssignment):
    """
    Inherits BaseAssignment, Adds required Fields for Writing 
    """
    def __init__(self, name,due_date,professor,word_amount, research):
        BaseAssignment.__init__(self,name,due_date,professor)
        self.word_amount = word_amount
        self.research = research

class OtherAssignment(BaseAssignment):
    """
    Inherits BaseAssignment, Adds required Fields for Other 
    """
    def __init__(self, name,due_date,professor,required_hours):
        BaseAssignment.__init__(self,name,due_date,professor)
        self.required_hours = required_hours






































