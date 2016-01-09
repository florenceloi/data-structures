

# file_data = open('cohort_data.txt')

# for line in file_data:
#     data = line.rstrip()
#     data = data.split("|")
#     first_name = data[0]
#     last_name = data[1]
    
  #  advisor = data[3]
   # cohort = data[4]

#return first_name, last_name, 

def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    file_data = open('cohort_data.txt')

    houses = set([])
    for line in file_data:
        data = line.rstrip()
        data = data.split("|")
        house = data[2]
        if house != '':
            houses.add(house)
    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    file_data = open('cohort_data.txt')

    for line in file_data:
        data = line.rstrip()
        data = data.split('|')
        if data[4] == "Winter 2015":
            winter_name = data[0] + " " + data[1]
            winter_15.append(winter_name)# Code goes here

        elif data[4] == "Spring 2015":
            spring_name = data[0] + " " + data[1]
            spring_15.append(spring_name)

        elif data[4] == "Summer 2015":
            summer_name = data[0] + " " + data[1]
            summer_15.append(summer_name)

        elif data[4] == "TA":
            ta_name = data[0] + " " + data[1]
            tas.append(ta_name)

    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()

    all_students.append(winter_15)
    all_students.append(spring_15)
    all_students.append(summer_15)
    all_students.append(tas)

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # Code goes here
    file_data = open('cohort_data.txt')

    for line in file_data:
        data = line.rstrip()
        data = data.split('|')
        if data[2] == "Gryffindor":
            last_name = data[1]
            gryffindor.append(last_name)# Code goes here

        elif data[2] == "Hufflepuff":
            last_name = data[1]
            hufflepuff.append(last_name)

        elif data[2] == "Slytherin":
            last_name = data[1]
            slytherin.append(last_name)

        elif data[2] == "Dumbledores_army":
            last_name = data[1]
            dumbledores_army.append(last_name)

        elif data[2] == "Order of the Phoenix":
            last_name = data[1]
            order_of_the_phoenix.append(last_name)

        elif data[2] == "Ravenclaw":
            last_name = data[1]
            ravenclaw.append(last_name)

        elif data[4] == "TA":
            last_name = data[1]
            tas.append(last_name)

        elif data[4] == "I":
            last_name = data[1]
            instructors.append(last_name)

    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    ravenclaw.sort()
    tas.sort()
    instructors.sort()

    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(dumbledores_army)
    all_students.append(order_of_the_phoenix)
    all_students.append(ravenclaw)
    all_students.append(tas)
    all_students.append(instructors)

    return all_students

  




def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
