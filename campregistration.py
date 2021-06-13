from tkinter import *
import tkinter.messagebox as tk



#MAIN

def listFormat(aList):
    s = ""
    for i in range (0, len(aList)):
        s += f"{i+1}. {aList[i]}\n"
    return s

def displayInfo(index,aList,bList,cList,dList, eList, fList, gList, hList, iList, jList, kList, lList, mList, nList, oList, pList, qList, rList,sList):
    s = ""
    i = index
    name = f"Name: {aList[i]}, {bList[i]}\n"
    age = f"Age: {cList[i]}\n"
    gender = f"Gender: {dList[i]}\n"
    childFullAddress = f"Address: {eList[i]}, {fList[i]}, {gList[i]}\n"
    parent = f"Parent: {hList[i]}, {iList[i]}\n"
    parentPhone = f"Parent Phone Number: {jList[i]}\n"
    parentFullAddress = f"Address: {kList[i]}, {lList[i]}, {mList[i]}\n"
    childHealthCard = f"Child Healthcard Number: {nList[i]}\n"
    childAllergies = f"Child Allergies: {oList[i]}\n"
    childEmergencyContact = f"Child Emergency Contact: {pList[i]}\n"
    signature = f"Signature: {qList[i]}\n"
    campSelection = f"Camps: {rList[i]}\n"
    cost = f"Total Cost: ${sList[i]}"
    s = name + age + gender + childFullAddress+ parent + parentPhone + parentFullAddress +  childHealthCard + childAllergies+ childEmergencyContact+ signature+ campSelection+cost
    return s
    
def updateMedical(event):
    name = parentFNameEntryVar.get()
    emergencyParentRadio.config(text = name)

#Signature======================================
def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            cv.create_line(xold,yold,event.x,event.y,smooth=TRUE)
                          
        xold = event.x
        yold = event.y
def b1down(event):
    global b1
    b1 = "down"
    
def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           
    yold = None
#==============================================

#Save Function, connected to saveButton========
def save():
    if childFNameEntryVar.get() not in childFNames:
        cfirstName = childFNameEntryVar.get()
        clastName = childLNameEntryVar.get()
        childFNames.append(cfirstName)
        childLNames.append(clastName)

        childAge.append(childAgeVar.get())

        if childGenderVar.get() == "Other":
            childGender.append(childOtherGenderVar.get())
        else:
            childGender.append(childGenderVar.get())

        childAddress.append(childAddressVar.get())

        childCityTown.append(childCityVar.get())

        childProvince.append(childProvinceVar.get())

        pfirstName = parentFNameEntryVar.get()
        plastName = parentLNameEntryVar.get()
        parentFName.append(pfirstName)
        parentLName.append(plastName)

        parentPhone.append(parentPhoneVar.get())
        if parentAddressVar.get() == "Yes":
            parentAddress.append(childAddressVar.get())
            parentCityTown.append(childCityVar.get())
            parentProvince.append(childProvinceVar.get())
        elif parentAddressVar.get() == "No":
            parentAddress.append(parentAddressEntryVar.get())
            parentCityTown.append(parentCityVar.get())
            parentProvince.append(parentProvinceVar.get())
        else:
            parentAddress.append(" ")
            parentCityTown.append(" ")
            parentProvince.append(" ")

        childHealthCard.append(healthcardVar.get())

        if allergyVar.get() == "Yes":
            childAllergies.append(allergySpecVar.get())
        elif allergyVar.get() == "No":
            childAllergies.append(" ")
        else:
            childAllergies.append(" ")

        if emergencyRadioVar.get() == "Parent":
            childEmergencyContact.append(f"{parentPhoneVar.get()}, {parentFNameEntryVar.get()} {parentLNameEntryVar.get()}")
        elif emergencyRadioVar.get() == "Other":
            childEmergencyContact.append(emergencyOtherVar.get())
        else:
            childEmergencyContact.append(" ")

        if cv.find_all() == ():
            signature.append("No")
        else:
            signature.append("Yes")


    #camps======================================
        camp = []
        totalcost = 0
        if camp1Var.get() == "Session CK101: Introduction to Camp":
            camp.append(camp1Var.get())
            camp1.append(f'{cfirstName} {clastName}')
            camp1PplVar.set(f'{updateNum(camp1)}/10')
            if int(updateNum(camp1)) > 10:
                camp1PplLabel.config(fg = "red")
            totalcost += 113
            
        if camp2Var.get() == "Junior Canoe Trip":
            camp.append(camp2Var.get())
            camp2.append(f'{cfirstName} {clastName}')
            camp2PplVar.set(f'{updateNum(camp2)}/10')
            if int(updateNum(camp2)) > 10:
                camp2PplLabel.config(fg = "red")
            totalcost += 432
            
        if camp3Var.get() == "Algonquin Canoe Adventure":
            camp.append(camp3Var.get())
            camp3.append(f'{cfirstName} {clastName}')
            camp3PplVar.set(f'{updateNum(camp3)}/10')
            if int(updateNum(camp3)) > 10:
                camp3PplLabel.config(fg = "red")
            totalcost += 867
            
        if camp4Var.get() == "Challenge & Adventure":
            camp.append(camp4Var.get())
            camp4.append(f'{cfirstName} {clastName}')
            camp4PplVar.set(f'{updateNum(camp4)}/10')
            if int(updateNum(camp4)) > 10:
                camp4PplLabel.config(fg = "red")
            totalcost += 543
            
        if camp5Var.get() == "Pre-Leadership Camp":
            camp.append(camp5Var.get())
            camp5.append(f'{cfirstName} {clastName}')
            camp5PplVar.set(f'{updateNum(camp5)}/10')
            if int(updateNum(camp5)) > 10:
                camp5PplLabel.config(fg = "red")
            totalcost += 632
            
        if camp6Var.get() == "Hackathon Camp":
            camp.append(camp6Var.get())
            camp6.append(f'{cfirstName} {clastName}')
            camp6PplVar.set(f'{updateNum(camp6)}/10')
            if int(updateNum(camp6)) > 10:
                camp6PplLabel.config(fg = "red")
            totalcost += 543
            
        if camp7Var.get() == "Artist Design":
            camp.append(camp7Var.get())
            camp7.append(f'{cfirstName} {clastName}')
            camp7PplVar.set(f'{updateNum(camp7)}/10')
            if int(updateNum(camp7)) > 10:
                camp7PplLabel.config(fg = "red")
            totalcost += 134
            
        if camp8Var.get() == "Mathamatics Camp":
            camp.append(camp8Var.get())
            camp8.append(f'{cfirstName} {clastName}')
            camp8PplVar.set(f'{updateNum(camp8)}/10')
            if int(updateNum(camp8)) > 10:
                camp8PplLabel.config(fg = "red")
            totalcost += 321
            
        if camp9Var.get() == "Swim and Explore Program":
            camp.append(camp9Var.get())
            camp9.append(f'{cfirstName} {clastName}')
            camp9PplVar.set(f'{updateNum(camp9)}/10')
            if int(updateNum(camp9)) > 10:
                camp9PplLabel.config(fg = "red")
            totalcost += 532
            
        camps.append(camp)
        cost.append(str(totalcost))
    #===========================================

    #Check for empty slots====================== 
        for i in range(0, len(childFNames)):
            if childFNames[i] == "" or childLNames[i] == "" or childAge[i] == "" or childGender[i] == " " or childAddress[i] == "" or childCityTown[i] == "" or childProvince[i] == "" or parentFName[i] == "" or parentLName[i] == "" or parentPhone[i] == "" or parentAddress[i] == "" or parentCityTown[i] == "" or parentProvince[i] == "" or childHealthCard[i] == "" or childAllergies[i] == "" or childEmergencyContact[i] == "" or signature[i] == "" or camps[i] == "":
                childFNames.pop(i)
                childLNames.pop(i)
                childAge.pop(i)
                childGender.pop(i)
                childAddress.pop(i)
                childCityTown.pop(i)
                childProvince.pop(i)
                parentFName.pop(i)
                parentLName.pop(i)
                parentPhone.pop(i)
                parentAddress.pop(i)
                parentCityTown.pop(i)
                parentProvince.pop(i)
                childHealthCard.pop(i)
                childAllergies.pop(i)
                childEmergencyContact.pop(i)
                signature.pop(i)
                camps.pop(i)
                tk.showerror("Error", "Please completely fill the registration")
            else:
                tk.showinfo("Saved", "Your information has been saved")
                #clear the information
                childFNameEntryVar.set("")
                childLNameEntryVar.set("")
                childAgeVar.set("6")
                childGenderVar.set(" ")
                childAddressVar.set("")
                childCityVar.set("")
                childProvinceVar.set("Select")
                healthcardVar.set("")
                parentFNameEntryVar.set("")
                parentLNameEntryVar.set("")
                parentAddressVar.set(" ")
                parentAddressEntryVar.set("")
                parentCityVar.set("")   
                parentProvinceVar.set("Select")
                parentPhoneVar.set("")
                allergyVar.set(" ")
                allergySpecVar.set("")
                emergencyParentRadio.config(text = "Parent")
                emergencyRadioVar.set(" ")
                emergencyOtherVar.set("")
                signatureTest = ""
                camp1Var.set("")
                camp2Var.set("")
                camp3Var.set("")
                camp4Var.set("")
                camp5Var.set("")
                camp6Var.set("")
                camp7Var.set("")
                camp8Var.set("")
                camp9Var.set("")
                cv.delete("all")
        
    else:
        tk.showerror("Error", "This child is already registered")

    
         
def updateNum(camp):
    num = 0
    for item in camp:
        if item != " ":
            num +=1
    return str(num)

def displayCamp1Names(event):
    if len(camp1) < 1:
        tk.showinfo("Junior Canoe Trip", "There are currently no campers in this camp.")
    else:
        tk.showinfo("Junior Canoe Trip", listFormat(camp1))
        
def displayCamp2Names(event):
    if len(camp2) < 1:
        tk.showinfo("Junior Canoe Trip", "There are currently no campers in this camp.")
    else:
        tk.showinfo("Junior Canoe Trip", listFormat(camp2))

def displayCamp3Names(event):
    if len(camp3) < 1:
        tk.showinfo("Algonquin Canoe Adventure","There are currently no campers in this camp.")
    else:
        tk.showinfo("Algonquin Canoe Adventure",listFormat(camp3))
    

def displayCamp4Names(event):
    if len(camp4) < 1:
        tk.showinfo("Challenge & Adventure","There are currently no campers in this camp.")
    else:
        tk.showinfo("Challenge & Adventure",listFormat(camp4))

def displayCamp5Names(event):
    if len(camp5) < 1:
        tk.showinfo("Pre-Leadership Camp","There are currently no campers in this camp.")
    else:
        tk.showinfo("Pre-Leadership Camp",listFormat(camp5))

def displayCamp6Names(event):
    if len(camp6) < 1:
        tk.showinfo("Hackathon Camp","There are currently no campers in this camp.")
    else:
        tk.showinfo("Hackathon Camp",listFormat(camp6))

def displayCamp7Names(event):
    if len(camp7) < 1:
        tk.showinfo("Artist Design","There are currently no campers in this camp.")
    else:
        tk.showinfo("Artist Design",listFormat(camp7))


def displayCamp8Names(event):
    if len(camp8) < 1:
        tk.showinfo("Mathamatics Camp","There are currently no campers in this camp.")
    else:
        tk.showinfo("Mathamatics Camp",listFormat(camp8))

def displayCamp9Names(event):
    if len(camp9) < 1:
        tk.showinfo("Swim and Explore Program","There are currently no campers in this camp.")
    else:
        tk.showinfo("Swim and Explore Program",listFormat(camp9))

def search():
    userInput = searchChildFNameVar.get()
    if userInput in childFNames:
        index = childFNames.index(userInput)
        tk.showinfo("Search",displayInfo(index,childFNames,childLNames,childAge,childGender,childAddress,childCityTown,childProvince,parentFName,parentLName,parentPhone,parentAddress,parentCityTown,parentProvince,childHealthCard,childAllergies,childEmergencyContact,signature,camps, cost))
    else:
        tk.showerror("Error","This child is currently not registered in the system.")
            
    
def changeFont(event):
    size = fontVar.get()
    customFont = f"Arial {size}"

    childFNameLabel.config(font = customFont)
    childLNameLabel.config(font = customFont)
    childAgeLabel.config(font = customFont)
    childGenderLabel.config(font = customFont)
    maleRadio.config(font = customFont)
    femaleRadio.config(font = customFont)
    otherRadio.config(font = customFont)
    childAddressLabel.config(font = customFont)
    childCityLabel.config(font = customFont)
    childProvinceLabel.config(font = customFont)
    childProvinceOptionMenu.config(font = customFont)
    parentFNameLabel.config(font = customFont)
    parentLNameLabel.config(font = customFont)
    parentPhoneLabel.config(font = customFont)
    parentAddressLabel.config(font = customFont)
    parentAddressLabel1.config(font = customFont)
    parentAddressLabel2.config(font = customFont)
    parentSameAddressRadio.config(font = customFont)
    parentNotSameAddressRadio.config(font = customFont)
    parentCityLabel.config(font = customFont)
    parentProvinceLabel.config(font = customFont)
    parentProvinceOptionMenu.config(font = customFont)
    healthcardLabel.config(font = customFont)
    allergyLabel.config(font = customFont)
    allergyYesRadio.config(font = customFont)
    allergySpecVarLabel.config(font = customFont)
    allergyNoRadio.config(font = customFont)
    emergencyLabel.config(font = customFont)
    emergencyParentRadio.config(font = customFont)
    emergencyOtherRadio.config(font = customFont)

    campNameLabel.config(font = customFont)
    numPplLabel.config(font = customFont)
    campCostLabel.config(font = customFont)
    campDateLabel.config(font = customFont)
    campAgeLabel.config(font = customFont)

    camp1check.config(font = customFont)
    camp1PplLabel.config(font = customFont)
    camp1CostLabel.config(font = customFont)
    camp1DateLabel.config(font = customFont)
    camp1AgeLabel.config(font = customFont)
    
    camp2check.config(font = customFont)
    camp2PplLabel.config(font = customFont)
    camp2CostLabel.config(font = customFont)
    camp2DateLabel.config(font = customFont)
    camp2AgeLabel.config(font = customFont)
  
    camp3check.config(font = customFont)
    camp3PplLabel.config(font = customFont)
    camp3CostLabel.config(font = customFont)
    camp3DateLabel.config(font = customFont)
    camp3AgeLabel.config(font = customFont)
  
    camp4check.config(font = customFont)
    camp4PplLabel.config(font = customFont)
    camp4CostLabel.config(font = customFont)
    camp4DateLabel.config(font = customFont)
    camp4AgeLabel.config(font = customFont)
  
    camp5check.config(font = customFont)
    camp5PplLabel.config(font = customFont)
    camp5CostLabel.config(font = customFont)
    camp5DateLabel.config(font = customFont)
    camp5AgeLabel.config(font = customFont)
  
    camp6check.config(font = customFont)
    camp6PplLabel.config(font = customFont)
    camp6CostLabel.config(font = customFont)
    camp6DateLabel.config(font = customFont)
    camp6AgeLabel.config(font = customFont)
  
    camp7check.config(font = customFont)
    camp7PplLabel.config(font = customFont)
    camp7CostLabel.config(font = customFont)
    camp7DateLabel.config(font = customFont)
    camp7AgeLabel.config(font = customFont)
    
    camp8check.config(font = customFont)
    camp8PplLabel.config(font = customFont)
    camp8CostLabel.config(font = customFont)
    camp8DateLabel.config(font = customFont)
    camp8AgeLabel.config(font = customFont)
    
    camp9check.config(font = customFont)
    camp9PplLabel.config(font = customFont)
    camp9CostLabel.config(font = customFont)
    camp9DateLabel.config(font = customFont)
    camp9AgeLabel.config(font = customFont)
  
    photoLabel.config(font = customFont)
    printLabel.config(font = customFont)
    saveButton.config(font = customFont)
    
    searchLabel.config(font = customFont)
    searchButton.config(font = customFont)
    childNameLabel.config(font = customFont)
 

root = Tk()
mainframe = Frame(root)

global childFNames, childLNames, childAge, childGender, childAddress, childCityTown, childProvince, parentFName, parentLName, parentPhone, parentAddress, parentCityTown, parentProvince, childHealthCard, childAllergies, childEmergencyContact, signature, camps
b1 = "up"
xold, yold = None, None
global customFont

customFont = "Arial 10"

childFNames = []
childLNames= []
childAge= []
childGender= []
childAddress= []
childCityTown= []
childProvince= []
parentFName= []
parentLName= []
parentPhone= []
parentAddress= []
parentCityTown= []
parentProvince= []
childHealthCard= []
childAllergies= []
childEmergencyContact= []
signature= []
camps= []
cost = []

camp1 = []
camp2 = []
camp3 = []
camp4 = []
camp5 = []
camp6 = []
camp7 = []
camp8 = []
camp9 = []




#CREATE WIDGETS
mainframe.grid(padx=30, pady=30)

fontVar = IntVar()
fontVar.set(10)
fontSize= Scale(mainframe, variable = fontVar, from_=5, to= 13, label = "Font Size", font = "Arial 10", width = 20, length = 100, orient= VERTICAL)
fontSize.bind("<ButtonRelease-1>", changeFont)
campNameLabel1 = Label(mainframe, font=("Arial 20"), text="Camp Registration Form")

childFrame = LabelFrame(mainframe, text = "Child Information", font = "Arial 15")
childFNameLabel = Label(childFrame, font= "Arial 10", text="First Name:")


childFNameEntryVar = StringVar()
childFNameEntry = Entry(childFrame, textvariable = childFNameEntryVar)


childLNameLabel = Label(childFrame, font=("Arial 10"), text="Last Name:")

childLNameEntryVar = StringVar()
childLNameEntry = Entry(childFrame, textvariable = childLNameEntryVar)


childAgeLabel = Label(childFrame, font=("Arial 10"), text="Age:")

childAgeVar = StringVar()
childAgeOption = Spinbox(childFrame, from_=6, to=17, textvariable=childAgeVar)

childGenderLabel = Label(childFrame, font=("Arial 10"), text="Gender:")

childGenderVar = StringVar()
childGenderVar.set(" ")
maleRadio = Radiobutton(childFrame, text="Male", variable=childGenderVar, value="Male")
femaleRadio = Radiobutton(childFrame, text="Female", variable=childGenderVar, value="Female")
childOtherGenderVar = StringVar()
childOtherGenderVar.set("Other")
childOtherGenderEntry = Entry(childFrame, textvariable = childOtherGenderVar)
childOtherGenderVar.set(" ")
otherRadio = Radiobutton(childFrame, text = "Other", variable = childGenderVar, value= "Other")

childAddressLabel = Label(childFrame, text="Address:",font=("Arial 10"))
childAddressVar = StringVar()
childAddressEntry = Entry(childFrame, textvariable = childAddressVar)

childCityLabel = Label(childFrame, text="City/Town:",font=("Arial 10"))
childCityVar = StringVar()
childCityEntry = Entry(childFrame, textvariable = childCityVar)

childProvinceLabel = Label(childFrame, text="Province:",font=("Arial 10"))
childProvinces = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island', 'Quebec','Saskatchewan','Northwest Territories', 'Nunavut','Yukon']
childProvinceVar = StringVar()
childProvinceVar.set("Select")
childProvinceOptionMenu = OptionMenu(childFrame, childProvinceVar, *childProvinces)


parentFrame = LabelFrame(mainframe, text = "Parent Information", font = "Arial 15")

parentFNameLabel = Label(parentFrame, font=("Arial 10"), text="First Name:")

parentFNameEntryVar = StringVar()
parentFNameEntry = Entry(parentFrame, textvariable = parentFNameEntryVar, width = 50)
parentFNameEntry.bind("<Key>", updateMedical)


parentLNameLabel = Label(parentFrame, font=("Arial 10"), text="Last Name:")

parentLNameEntryVar = StringVar()
parentLNameEntry = Entry(parentFrame, textvariable = parentLNameEntryVar)


parentPhoneLabel = Label(parentFrame, font=("Arial 10"), text="Phone #:")

parentPhoneVar = StringVar()
parentPhoneEntry = Entry(parentFrame, textvariable = parentPhoneVar)

parentAddressLabel = Label(parentFrame, font=("Arial 10"), text="Address:")
parentAddressLabel1 = Label(parentFrame, font=("Arial 10"), text="Same as child?")

parentAddressVar= StringVar()
parentAddressVar.set(" ")
parentSameAddressRadio = Radiobutton(parentFrame, text = "Yes", variable = parentAddressVar, value = "Yes")

parentAddressLabel2 = Label(parentFrame, font=("Arial 10"), text="If no? Enter Address:")
parentAddressEntryVar = StringVar()
parentAddressEntryVar.set(" ")
parentAddressEntry = Entry(parentFrame, textvariable = parentAddressEntryVar)

parentNotSameAddressRadio = Radiobutton(parentFrame, text = "No", variable = parentAddressVar, value = "No")

parentCityLabel = Label(parentFrame, text="City/Town:",font=("Arial 10"))
parentCityVar = StringVar()
parentCityEntry = Entry(parentFrame, textvariable = parentCityVar)

parentProvinceLabel = Label(parentFrame, text="Province:",font=("Arial 10"))
parentProvinces = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island', 'Quebec','Saskatchewan','Northwest Territories', 'Nunavut','Yukon']
parentProvinceVar = StringVar()
parentProvinceVar.set("Select")
parentProvinceOptionMenu = OptionMenu(parentFrame, parentProvinceVar, *parentProvinces)

medicalFrame = LabelFrame(mainframe, text = "Child Medical Information", font = "Arial 15")

healthcardLabel = Label(medicalFrame, text="Healthcard Number:",font=("Arial 10"))
healthcardVar = StringVar()
healthcardEntry = Entry(medicalFrame, textvariable = healthcardVar, width=50)

allergyLabel = Label(medicalFrame, text = "Allergies:",font=("Arial 10"))
allergyVar = StringVar()
allergyVar.set(" ")
allergyYesRadio = Radiobutton(medicalFrame, text = "Yes", value = "Yes", variable = allergyVar)
allergySpecVarLabel = Label(medicalFrame, font=("Arial 10"), text="If yes, please specify:")
allergySpecVar = StringVar()
allergySpecVar.set(" ")
allergySpecEntry = Entry(medicalFrame, textvariable = allergySpecVar)
allergyNoRadio = Radiobutton(medicalFrame, text = "No", value = allergySpecVar, variable = allergyVar)


emergencyLabel = Label(medicalFrame, font=("Arial 10"), text="Emergency Contact:")
emergencyRadioVar= StringVar()
emergencyRadioVar.set(" ")
emergencyParentRadio = Radiobutton(medicalFrame, variable = emergencyRadioVar, text = "Parent", value = "Parent")
emergencyOtherLabel = Label(medicalFrame, font=("Arial 10"), text="If other, please specify:")
emergencyOtherVar = StringVar()
emergencyOtherEntry = Entry(medicalFrame, textvariable = emergencyOtherVar)
emergencyOtherRadio = Radiobutton(medicalFrame, variable = emergencyRadioVar, text = "Other", value = "Other")

campSelectionFrame = LabelFrame(mainframe, text = "Camp Selection", font = "Arial 15")

campNameLabel = Label(campSelectionFrame, font=("Arial 12"), text="Camp Name", bg = "#FFFFFF")
numPplLabel = Label(campSelectionFrame, font=("Arial 12"), text="#/#", bg = "#F5F5F5")
campCostLabel = Label(campSelectionFrame, font=("Arial 12"), text="Cost ($)", bg = "#FFFFFF")
campDateLabel = Label(campSelectionFrame, font=("Arial 12"), text="Camp Dates", bg = "#F5F5F5")
campAgeLabel = Label(campSelectionFrame, font=("Arial 12"), text="Ages", bg = "#FFFFFF")

camp1Var = StringVar()
camp1check = Checkbutton(campSelectionFrame, text='Session CK101: Introduction to Camp', onvalue = "Session CK101: Introduction to Camp", offvalue="", variable = camp1Var)
camp1PplVar = StringVar()
camp1PplVar.set("0/10")
camp1PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp1PplVar, fg = "blue")
camp1CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "113")
camp1DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Jan 3 - Feb 17")
camp1AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp1PplLabel.bind("<Button-1>", displayCamp1Names)

camp2Var = StringVar()
camp2check = Checkbutton(campSelectionFrame, text = 'Junior Canoe Trip', onvalue= "Junior Canoe Trip", offvalue="", variable=camp2Var)
camp2PplVar = StringVar()
camp2PplVar.set("0/10")
camp2PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp2PplVar, fg = "blue")
camp2CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "432")
camp2DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "May 1 - Aug 1")
camp2AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp2PplLabel.bind("<Button-1>", displayCamp2Names)

camp3Var = StringVar()
camp3check = Checkbutton(campSelectionFrame, text = 'Algonquin Canoe Adventure', onvalue= "Algonquin Canoe Adventure", offvalue="", variable=camp3Var)
camp3PplVar = StringVar()
camp3PplVar.set("0/10")
camp3PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp3PplVar, fg = "blue")
camp3CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "867")
camp3DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "May 12 - Jun 11")
camp3AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp3PplLabel.bind("<Button-1>", displayCamp3Names)

camp4Var = StringVar()
camp4check =Checkbutton(campSelectionFrame, text = 'Challenge & Adventure ', onvalue="Challenge & Adventure", offvalue="", variable=camp4Var)
camp4PplVar = StringVar()
camp4PplVar.set("0/10")
camp4PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp4PplVar, fg = "blue")
camp4CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "543")
camp4DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Dec 22 - Jan 1")
camp4AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp4PplLabel.bind("<Button-1>", displayCamp4Names)

camp5Var = StringVar()
camp5check =Checkbutton(campSelectionFrame, text = 'Pre-Leadership Camp ', onvalue="Pre-Leadership Camp", offvalue="", variable=camp5Var)
camp5PplVar = StringVar()
camp5PplVar.set("0/10")
camp5PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp5PplVar, fg = "blue")
camp5CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "632")
camp5DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Jul 1 - Aug 1")
camp5AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp5PplLabel.bind("<Button-1>", displayCamp5Names)

camp6Var= StringVar()
camp6check =Checkbutton(campSelectionFrame, text = 'Hackathon Camp', onvalue='Hackathon Camp', offvalue="", variable=camp6Var)
camp6PplVar = StringVar()
camp6PplVar.set("0/10")
camp6PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp6PplVar, fg = "blue")
camp6CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "543")
camp6DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Jul 20 - Aug 15")
camp6AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp6PplLabel.bind("<Button-1>", displayCamp6Names)

camp7Var = StringVar()
camp7check =Checkbutton(campSelectionFrame, text = 'Artist Design', onvalue='Artist Design', offvalue="", variable=camp7Var)
camp7PplVar = StringVar()
camp7PplVar.set("0/10")
camp7PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp7PplVar, fg = "blue")
camp7CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "134")
camp7DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Mar 6 - Apr 10")
camp7AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp7PplLabel.bind("<Button-1>", displayCamp7Names)

camp8Var = StringVar()
camp8check =Checkbutton(campSelectionFrame, text = 'Mathamatics Camp', onvalue='Mathamatics Camp', offvalue="", variable=camp8Var)
camp8PplVar = StringVar()
camp8PplVar.set("0/10")
camp8PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp8PplVar, fg = "blue")
camp8CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "321")
camp8DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Oct 4 - Nov 22")
camp8AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp8PplLabel.bind("<Button-1>", displayCamp8Names)

camp9Var = StringVar()
camp9check =Checkbutton(campSelectionFrame, text = 'Swim and Explore Program', onvalue='Swim and Explore Program', offvalue="", variable=camp9Var)
camp9PplVar = StringVar()
camp9PplVar.set("0/10")
camp9PplLabel = Label(campSelectionFrame, font=("Arial 10"), textvariable =camp9PplVar, fg = "blue")
camp9CostLabel =Label(campSelectionFrame, font=("Arial 10"), text = "532")
camp9DateLabel =Label(campSelectionFrame, font=("Arial 10"), text = "Jul 4 - Aug 30")
camp9AgeLabel = Label(campSelectionFrame, font=("Arial 10"), text = "6-18")
camp9PplLabel.bind("<Button-1>", displayCamp9Names)

saveFrame = LabelFrame(mainframe, text = "Signatures & Save", font = "Arial 15")
photoLabel = Label(saveFrame, font=("Arial 10"), text = "Allow Camp Iroquios Ridge to use photos of your child for promotion and other camp related services.")
printLabel = Label(saveFrame, font = ("Arial 10"), text = "Signature X")
cv = Canvas(saveFrame, width=500, height=60, bg="#FFFFFF")
cv.bind("<Motion>", motion)
cv.bind("<ButtonPress-1>", b1down)
cv.bind("<ButtonRelease-1>", b1up)

saveButtonVar = StringVar()
saveButtonVar.set("Save")
saveButton = Button(saveFrame, textvariable = saveButtonVar, font= "Arial 10", command = save, activebackground = "white", fg = "black", bg = "#77dd77",activeforeground = "#77dd77")


searchFrame = LabelFrame(mainframe, text = "Search Engine", font = "Arial 15")

searchLabel = Label(searchFrame, text= "Search for a registered child.",font = "Arial 15")
childNameLabel = Label(searchFrame, text= "Child First Name:",font = "Arial 12")
searchChildFNameVar = StringVar()
searchChildFNameEntry = Entry(searchFrame, textvariable = searchChildFNameVar, width = 60)

searchButtonVar = StringVar()
searchButtonVar.set("Search")
searchButton = Button(searchFrame, textvariable = searchButtonVar, font = "Arial 10", command = search, activebackground = "white", fg = "black", bg = "#779ecb",activeforeground = "#779ecb")
                         
#GRID widgets
mainframe.grid(padx=30, pady=30)

campNameLabel1.grid(row=0, column=1, columnspan=2, sticky=W+E)

fontSize.grid(row=2,column=3)

childFrame.grid(row=2, column=1, sticky=W+E+N)

childFNameLabel.grid(row=1, column =1, sticky=E)
childFNameEntry.grid(row=1, column =2, sticky =W+E, columnspan=4)

childLNameLabel.grid(row=2, column =1, sticky=E)
childLNameEntry.grid(row=2, column =2, sticky =W+E, columnspan=4)

childAgeLabel.grid(row=3, column =1, sticky=E)
childAgeOption.grid(row=3, column = 2, sticky =W)

childGenderLabel.grid(row=4, column =1, sticky=E)
maleRadio.grid(row=4, column=2, sticky=W)
femaleRadio.grid(row=4, column=3, sticky=W )
otherRadio.grid(row=4, column=4, sticky=W)
childOtherGenderEntry.grid(row=4, column=5, sticky=W,columnspan=1)

childAddressLabel.grid(row=5,column=1,sticky=E)
childAddressEntry.grid(row=5,column=2, sticky=W+E, columnspan=4)

childCityLabel.grid(row=6,column=1,sticky=E)
childCityEntry.grid(row=6, column=2, sticky=W)

childProvinceLabel.grid(row=6,column=3,sticky=E)
childProvinceOptionMenu.grid(row=6,column=4,sticky=W+E, columnspan=2)

parentFrame.grid(row=3,column=1, sticky=W+E+N+S,ipadx=20,)
parentFNameLabel.grid(row=1, column =1, sticky=E)
parentFNameEntry.grid(row=1, column =2, sticky =W+E, columnspan=4)

parentLNameLabel.grid(row=2, column =1, sticky=E)
parentLNameEntry.grid(row=2, column =2, sticky =W+E, columnspan=4)

parentPhoneLabel.grid(row=3, column =1, sticky=E)
parentPhoneEntry.grid(row=3, column =2, sticky =W+E, columnspan=4)

parentAddressLabel.grid(row=4, column=1, sticky=E)
parentAddressLabel1.grid(row=4, column=2, sticky=E)
parentSameAddressRadio.grid(row=4, column=3)
parentNotSameAddressRadio.grid(row=4,column=4)
parentAddressLabel2.grid(row=5,column=1,sticky=E)
parentAddressEntry.grid(row=5, column=2, columnspan=4, sticky=W+E)

parentCityLabel.grid(row=7,column=1,sticky=E)
parentCityEntry.grid(row=7, column=2, sticky=W)

parentProvinceLabel.grid(row=7,column=3,sticky=E)
parentProvinceOptionMenu.grid(row=7,column=4,sticky=W+E, columnspan=2)

medicalFrame.grid(row=4, column=1, sticky=W+E)
healthcardLabel.grid(row=1,column=1,sticky=E)
healthcardEntry.grid(row=1,column=2,sticky=W+E, columnspan=2)

allergyLabel.grid(row=2,column=1,sticky=E)
allergyYesRadio.grid(row=2, column=2, sticky=W)
allergyNoRadio.grid(row=2,column=3, sticky=W)

allergySpecVarLabel.grid(row=3, column=1, sticky=E)
allergySpecEntry.grid(row=3,column=2, sticky=W+E, columnspan=2)

emergencyLabel.grid(row=4,column=1,sticky=E)
emergencyParentRadio.grid(row=4, column=2,columnspan=2, sticky=W)
emergencyOtherRadio.grid(row=4, column=3, sticky=W)

emergencyOtherLabel.grid(row=5,column=1)
emergencyOtherEntry.grid(row=5,column=2, columnspan=2, sticky=W+E)

#grid the camps
campSelectionFrame.grid(row=2,column=2, ipadx=20, sticky=W+E+S+N, rowspan=2)
campNameLabel.grid(row=1,column=1, sticky=W+E)
numPplLabel.grid(row=1, column=2, sticky=W+E)
campCostLabel.grid(row=1,column=3, sticky=W+E)
campDateLabel.grid(row=1, column=4, sticky=W+E)
campAgeLabel.grid(row=1, column=5, sticky=W+E)

camp1check.grid(row = 2, column=1, sticky = W, pady = 3)
camp1PplLabel.grid(row=2,column=2,sticky=W)
camp1CostLabel.grid(row=2, column=3,sticky=W+E)
camp1DateLabel.grid(row=2, column=4, sticky=E)
camp1AgeLabel.grid (row=2,column=5,sticky=W+E)

camp2check.grid(row = 3,column=1, sticky = W, pady = 3)
camp2PplLabel.grid(row=3,column=2,sticky=W)
camp2CostLabel.grid(row=3, column=3,sticky=W+E)
camp2DateLabel.grid(row=3, column=4, sticky=E)
camp2AgeLabel.grid (row=3,column=5,sticky=W+E)

camp3check.grid(row = 4,column=1, sticky = W, pady = 3)
camp3PplLabel.grid(row=4,column=2,sticky=W)
camp3CostLabel.grid(row=4, column=3,sticky=W+E)
camp3DateLabel.grid(row=4, column=4, sticky=E)
camp3AgeLabel.grid (row=4,column=5,sticky=W+E)

camp4check.grid(row = 5,column=1, sticky = W, pady = 3)
camp4PplLabel.grid(row=5,column=2,sticky=W)
camp4CostLabel.grid(row=5, column=3,sticky=W+E)
camp4DateLabel.grid(row=5, column=4, sticky=E)
camp4AgeLabel.grid (row=5,column=5,sticky=W+E)

camp5check.grid(row = 6,column=1, sticky = W, pady = 3)
camp5PplLabel.grid(row=6,column=2,sticky=W)
camp5CostLabel.grid(row=6, column=3,sticky=W+E)
camp5DateLabel.grid(row=6, column=4, sticky=E)
camp5AgeLabel.grid (row=6,column=5,sticky=W+E)

camp6check.grid(row = 7,column=1, sticky = W, pady = 3)
camp6PplLabel.grid(row=7,column=2,sticky=W)
camp6CostLabel.grid(row=7, column=3,sticky=W+E)
camp6DateLabel.grid(row=7, column=4, sticky=E)
camp6AgeLabel.grid (row=7,column=5,sticky=W+E)

camp7check.grid(row = 8,column=1, sticky = W, pady = 3)
camp7PplLabel.grid(row=8,column=2,sticky=W)
camp7CostLabel.grid(row=8, column=3,sticky=W+E)
camp7DateLabel.grid(row=8, column=4, sticky=E)
camp7AgeLabel.grid (row=8,column=5,sticky=W+E)

camp8check.grid(row = 9,column=1, sticky = W, pady = 3)
camp8PplLabel.grid(row=9,column=2,sticky=W)
camp8CostLabel.grid(row=9, column=3,sticky=W+E)
camp8DateLabel.grid(row=9, column=4, sticky=E)
camp8AgeLabel.grid (row=9,column=5,sticky=W+E)

camp9check.grid(row = 10,column=1, sticky = W, pady = 3)
camp9PplLabel.grid(row=10,column=2,sticky=W)
camp9CostLabel.grid(row=10, column=3,sticky=W+E)
camp9DateLabel.grid(row=10, column=4, sticky=E)
camp9AgeLabel.grid (row=10,column=5,sticky=W+E)

saveFrame.grid(row=4,column=2,sticky=W+E)
photoLabel.grid(row=1, column=1, columnspan=4)
printLabel.grid(row=2,column=1, sticky=W)
cv.grid(row=2,column=2,columnspan=2)

saveButton.grid(row=4, column=2, sticky = W+E, columnspan=2, pady = 10)

searchFrame.grid(row=5,column=1,sticky=W+E, columnspan=2)
searchLabel.grid(row=1,column=1,sticky=E+W)
childNameLabel.grid(row=1, column=2,sticky=E)
searchChildFNameEntry.grid(row=1, column=3, sticky=W+E, pady = 10)
searchButton.grid(row=1, column=4, ipadx = 50, pady = 10, padx=30)

