from breezypythongui import EasyFrame
import assignments
import student
import time_management

def assignment_properties(input_line):
    line=line.split(';')
    assignment_type=line[0]
    assignment_dict={}
    for part in line[1].split('|'):
        key,value=part.split('^')
        assignment_dict[key]=value
    return(assignment_type,assignment_dict)

class Scheduler(EasyFrame):
    def __init__(self):
        self.assignments_list=[]
        try:
            open("assignments.txt", 'x')
        except:
            test = 1
        # self.loadassignments_list(self.assignments_list)
        EasyFrame.__init__(self, title="Help Me Procrastinate")
        self.setBackground("#BF0261")
        self.addLabel(text="Assignment Name: ",
                      row=0, column=0)
        self.assignmentnameField = self.addTextField(text="",
                                                row = 0,
                                                column = 1)
        self.addLabel(text="Due Date: ",
                      row=1, column=0)
        self.due_dateField = self.addTextField(text="",
                                                row=1,
                                                column=1)
        self.addLabel(text="Professor Name: ",
                      row=2, column=0)
        self.profField = self.addTextField(text="",
                                            row=2,
                                            column=1)

        self.addLabel(text="Pages: ",
                      row=0, column=2)
        self.pagesField = self.addFloatField(value=0, row=0, column=3,
                                                columnspan = 1, rowspan = 1,
                                                width = 10)
        self.addLabel(text="Citations: ",
                      row=1, column=2)
        self.researchField = self.addTextField(text="",
                                                row=1,
                                                column=3)
        self.addLabel(text="Words: ",
                      row=2, column=2)
        self.wordsField = self.addTextField(text="",
                                            row=2,
                                            column=3)
        self.addLabel(text="Questions: ",
                      row=3, column=2)
        self.questionsField = self.addFloatField(value=0, row=3, column=3,
                                             columnspan=1, rowspan=1,
                                             width=10)
        self.addLabel(text="Above Fields Required",
                      row=3, column=0)

        self.group = self.addRadiobuttonGroup(row=4, column=2,
                                              columnspan=4)
        defaultRB = self.group.addRadiobutton("Self Learning")
        self.group.addRadiobutton("Reading")
        self.group.addRadiobutton("Writing")
        self.group.addRadiobutton("Other")
        self.group.setSelectedButton(defaultRB)
        self.addButton(text = "Add", row = 5, column = 0,
                       command = self.addAssignment)
        self.addButton(text = "Edit", row = 5, column = 1,
                       command = self.editAssignment)
        self.addButton(text = "Delete", row = 5, column = 2,
                       command = self.deleteAssignment)
        self.addButton(text = "View", row = 5, column = 3,
                       command = self.viewAssignment)
        self.contactEntry = self.addTextArea("", row = 6, column = 0,
                                             columnspan = 6,
                                             width = 75, height = 10)
        self.addButton(text = "Save", row = 7, column = 0,
                      command = self.saveAssignment)
        self.addButton(text = "Exit", row = 7, column = 3,
                       command = self.exitAssignment)

def exitScheduler(self):
        exit()
def main():
    Scheduler().mainloop()
if __name__ == "__main__":
    main()