from breezypythongui import EasyFrame
import assignments
import student
import time_management

class Scheduler(EasyFrame): 
    def __init__(self):
        self.listoPeople = []
        try: 
            open("family.txt", 'x')
        except:
            test = 1
        try: 
            open("friend.txt", 'x')
        except:
            test = 1
        self.loadpersonContacts(self.listoPeople)
        self.loadotherContacts(self.listoPeople)
        EasyFrame.__init__(self, title = "Contact List")
        self.setBackground("#d0ae9b")
        self.addLabel(text = "First Name: ",
                      row = 0, column =0)
        self.firstnameField = self.addTextField(text = "",
                                           row = 0,
                                           column = 1)
        self.addLabel(text = "Last Name: ",
                      row = 1, column = 0)
        self.lastnameField = self.addTextField(text = "",
                                               row = 1,
                                               column = 1)
        self.addLabel(text = "Phone Number: ",
                      row = 2, column = 0)
        self.phoneField = self.addTextField(text = "",
                                            row = 2,
                                            column = 1)

        self.addLabel(text = "Date Met: ",
                                        row = 3, column = 0)
        self.optionField = self.addTextField(text = "",
                                             row = 3, 
                                             column = 1)
        self.group = self.addRadiobuttonGroup(row = 4, column = 0,
                                              columnspan = 2)       
        defaultRB = self.group.addRadiobutton("Family")
        self.group.addRadiobutton("Friend")
        self.group.setSelectedButton(defaultRB)       
        self.addButton(text = "Add", row = 5, column = 0,
                       command = self.addContacts)
        self.addButton(text = "Edit", row = 5, column = 1,
                       command = self.editContact)
        self.addButton(text = "Delete", row = 5, column = 2,
                       command = self.deleteContact)
        self.addButton(text = "View", row = 5, column = 3,
                       command = self.viewContact)
        self.contactEntry = self.addTextArea("", row = 6, column = 0,
                                             columnspan = 6,
                                             width = 75, height = 10)
        self.addButton(text = "Save", row = 7, column = 0,
                      command = self.saveContact)
        self.addButton(text = "Exit", row = 7, column = 3,
                       command = self.exitContact)
    def clearField(self):
        self.firstnameField.setText("")
        self.lastnameField.setText("")
        self.phoneField.setText("")
        self.optionField.setText("")
    def loadpersonContacts(self, listoPeople):
        contactInfo = []
        personFile = open("family.txt", 'r')
        for line in personFile:
            contactInfo = line.split()
            name = contactInfo[0]
            Lname = contactInfo[1]
            phoneNum = contactInfo[2]
            relationship = contactInfo[3]
            newContact = family(name, Lname, phoneNum, relationship)
            listoPeople.append(newContact)
        personFile.close()
    def loadotherContacts(self, listoPeople):
        otherFile = open("friend.txt", 'r')
        for line in otherFile:
            contactInfo = line.split()
            name = contactInfo[0]
            Lname = contactInfo[1]
            phoneNum = contactInfo[2]
            dateMet = contactInfo[3]
            newContact = person(name, Lname, phoneNum, dateMet)
            listoPeople.append(newContact)
        otherFile.close()
    def addContacts(self):
        personbutton = self.group.getSelectedButton()["text"]
        if personbutton == "Family":
            name = self.firstnameField.getText()
            Lname = self.lastnameField.getText()
            phoneNum = self.phoneField.getText()
            relationship = self.optionField.getText()
            newContact = family(name, Lname, phoneNum, relationship)
        else:
            name = self.firstnameField.getText()
            Lname = self.lastnameField.getText()
            phoneNum = self.phoneField.getText()
            met = self.optionField.getText()
            newContact = person(name, Lname, phoneNum, met)
        self.listoPeople.append(newContact)
        self.clearField()
    def viewContact(self):
        count = 0
        oField = "Contact List\n"
        oField += "%-20s%-20s%-20s%-20s\n" % ("First Name", "Last Name", "Phone Number", "Date Met")
        while(count < len(self.listoPeople)):
            if isinstance(self.listoPeople[count], family):
                name = self.listoPeople[count].returnName()
                lastName = self.listoPeople[count].returnLname()
                phoneNumber = self.listoPeople[count].returnphoneNum()
                otherOption = self.listoPeople[count].returnrelationship()
            else:
                name = self.listoPeople[count].returnName()
                lastName = self.listoPeople[count].returnLname()
                phoneNumber = self.listoPeople[count].returnphoneNum()
                otherOption = self.listoPeople[count].returndateMet() 
            oField += "%-20s%-20s%-20s%-20s\n" % \
                    (name, lastName, phoneNumber, otherOption)
            count += 1
        self.contactEntry.setText(oField)        
    def saveContact(self):
        personFile = open("family.txt", 'w')
        otherFile = open("friend.txt", 'w')
        for Person in self.listoPeople:
            sect = Person.returnName() + " "
            sect += Person.returnLname() + " "
            sect += Person.returnphoneNum() + " "
            if isinstance(Person, family):
                sect += Person.returnrelationship() + "\n"
                personFile.write(sect)
            else:
                sect += Person.returndateMet() + "\n"
                otherFile.write(sect)
        personFile.close()
        otherFile.close()
    def editContact(self):
        count = 0
        name = self.firstnameField.getText()
        while(count < len(self.listoPeople)):
            contact_name = self.listoPeople[count].returnName()
            if(contact_name == name):
                phoneNum = self.phoneField.getText()
                self.listoPeople[count].setphoneNum(phoneNum)
                self.clearField()
                break
            count += 1
        self.clearField()
    def deleteContact(self):
        count = 0
        name = self.firstnameField.getText()
        while(count < len(self.listoPeople)):
            contact_name = self.listoPeople[count].returnName()
            if(contact_name == name):
                self.listoPeople.pop(count)
                self.clearField()
                break
            count += 1
        self.clearField()
    def exitContact(self):
        exit()






