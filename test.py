import csv

# Import Selenium WebDriver
from selenium import webdriver

# Import Select to access data on DropDowns
from selenium.webdriver.support.ui import Select

## Path Of ChromeDriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

## Creating Web Driver
driver = webdriver.Chrome(PATH)


## Create CSV File
csv_file = open('courses.csv', 'w')

## Create A Writer Object to write to file
csv_writer = csv.writer(csv_file)

## Create Table Headings
csv_writer.writerow(["Course Code", "Course Name", "Units"])

## Link of Site
driver.get("https://reg.run.edu.ng")

## Find First Link with ''Click To View''
link = driver.find_element_by_link_text("Click to view")

## Click Link
link.click()

## Find The Dropdown with Name 
program = driver.find_element_by_name("lstProgrammes")

# Creating A Select Object
select_element = Select(program)

# Select Value of CMP in Dropdown
select_element.select_by_value("CMP")

level = driver.find_element_by_name("lstLevels")
select_element = Select(level)
select_element.select_by_value("300")

#Find Element tha has a Value ''Show Curriculum''
button = driver.find_element_by_xpath("//input[@value='Show Curriculum']")
button.click()

# Get All the Tables with Class Name with "Course Reg"
for table in driver.find_elements_by_class_name("course_reg")[1:3]:

	# GEt All the rows of Each Table
	rows = table.find_elements_by_class_name("tn")

	# For Single row in every row
	for row in rows:
		## Get Each Cell
		cell = row.find_elements_by_tag_name("td")

		## Get Course Code
		code = cell[1]
		code = code.text
		print(code)

		## GEt Course Name
		course = cell[2]
		course = course.text
		print(course)

		## Get Unit
		unit = cell[3]
		unit = unit.text
		print(unit)

		print("----")

		## Add To CSV File
		csv_writer.writerow([code, course, unit])
csv_file.close()


driver.quit()
