import json
import os
from turtle import fillcolor
from fpdf import FPDF

# Find JSON file
CurrentDirectory = os.getcwd()
print(CurrentDirectory)
jsonFile = "%s/%s" % (CurrentDirectory, "personalDetails.json")
jsonData = {}

# Read JSON file and store in jsonData
with open(jsonFile) as data_file:
    jsonData = json.load(data_file)

# Set JSON Data # personal details
firstName = jsonData["first_name"]
middleName = jsonData["middle_name"]
lastName = jsonData["last_name"]

#Objective
objective1 = jsonData["objective1"]
objective2 = jsonData["objective2"]

#Public Information
mobileNumber = jsonData["mobile_number"]
gmail = jsonData["gmail"]
facebook = jsonData["facebook"]
instagram = jsonData["instagram"]
fullAddress1 = jsonData["address1"]
fullAddress2 = jsonData["address2"]

#Technical Skills
technicalSkills1 = jsonData["technical_skills1"]
technicalSkills2 = jsonData["technical_skills2"]
technicalSkills3 = jsonData["technical_skills3"]
technicalSkills4 = jsonData["technical_skills4"]
technicalSkills5 = jsonData["technical_skills5"]

# Education
university = jsonData["university_name1"]
universityDescription = jsonData["univ_description"]
seniorHighSchool = jsonData["school_name1"]
strandSHS = jsonData["strand_senior_high1"]
seniorHighSchoolDescription1 = jsonData["senior_high_description1"]
seniorHighSchoolAchievement1 = jsonData["senior_high_achievement1"]
seniorHighSchoolAchievement2 = jsonData["senior_high_achievement2"]

juniorHighSchool = jsonData["school_name2"]
juniorHighSchoolDescription1 = jsonData["junior_high_description1"]
juniorHighSchoolAchievement1 = jsonData["junior_high_achievement1"]
juniorHighSchoolAchievement2 = jsonData["junior_high_achievement2"]
juniorHighSchoolAchievement3 = jsonData["junior_high_achievement3"]

#Experience
experience1 = jsonData["experience1"]
experience2 = jsonData["experience2"]
experience3 = jsonData["experience3"]
experience4 = jsonData["experience4"]
experience5 = jsonData["experience5"]

# Create PDF
pdf = FPDF("P", "mm", "A4")
pdf.add_page()

# Header
pdf.set_font("times", "B", 20)
pdf.cell(0, 5, firstName + ' ' + middleName + ' '  + lastName, ln=1, align="C")
pdf.image('gmail.png', 72, 20, 0, 4)
pdf.image('insta.png', 89, 25, 0, 5)
pdf.image('facebook.png', 89, 32, 0, 4)
pdf.image('address.png', 69, 37, 0, 5)

pdf.set_font("times", "", 12)
pdf.cell(0, 4, "", ln=1, align="C")
pdf.cell(0, 6, '  ' + gmail, ln=1, align="C")
pdf.cell(0, 6, '  ' + instagram, ln=1, align="C")
pdf.cell(0, 6, '  ' + facebook, ln=1, align="C")
pdf.cell(0, 6, '  ' + fullAddress1, ln=1, align="C")
pdf.cell(0, 6, '  ' + fullAddress2, ln=1, align="C")

#Objective
pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(63, 63, 66)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, '  O B J E C T I V E', ln=1, align="L", fill = 1)

pdf.set_font("helvetica", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, objective1,ln=1, align="L")
pdf.cell(0, 6, objective2,ln=1, align="L")

#Technical Skills
pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(63, 63, 66)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, '  TECHNICAL SKILLS', ln=1, align="L", fill = 1)

pdf.set_font("helvetica", "", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, technicalSkills1,ln=1, align="L")
pdf.cell(0, 6, technicalSkills2,ln=1, align="L")
pdf.cell(0, 6, technicalSkills3,ln=1, align="L")
pdf.cell(0, 6, technicalSkills4,ln=1, align="L")
pdf.cell(0, 6, technicalSkills5,ln=1, align="L")

#Educational Attainment
pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(63, 63, 66)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, '  EDUCATIONAL ATTAINMENT', ln=1, align="L", fill = 1)

pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, university,ln=1, align="L")
pdf.set_font("helvetica", "", 12)
pdf.cell(0, 6, universityDescription,ln=1, align="L")

pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, juniorHighSchool,ln=1, align="L")
pdf.set_font("helvetica", "", 12)
pdf.cell(0, 6, strandSHS,ln=1, align="L")
pdf.cell(0, 6, seniorHighSchoolDescription1,ln=1, align="L")
pdf.cell(0, 6, seniorHighSchoolAchievement1,ln=1, align="L")
pdf.cell(0, 6, seniorHighSchoolAchievement2,ln=1, align="L")

pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, seniorHighSchool,ln=1, align="L")
pdf.set_font("helvetica", "", 12)
pdf.cell(0, 6, juniorHighSchoolDescription1,ln=1, align="L")
pdf.cell(0, 6, juniorHighSchoolAchievement1,ln=1, align="L")
pdf.cell(0, 6, juniorHighSchoolAchievement2,ln=1, align="L")


#Experience
pdf.set_font("helvetica", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(63, 63, 66)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, '  E X P E R I E N C E', ln=1, align="L", fill = 1)

pdf.set_font("helvetica", "B", 12)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, "", ln=1, align="C")
pdf.cell(0, 6, experience1,ln=1, align="L")
pdf.cell(0, 6, experience2,ln=1, align="L")
pdf.set_font("helvetica", "", 12)
pdf.cell(0, 6, experience3,ln=1, align="L")
pdf.cell(0, 6, experience4,ln=1, align="L")
pdf.cell(0, 6, experience5,ln=1, align="L")

# PDF output
pdf.output("LIM_SHIN_ITONG.pdf")