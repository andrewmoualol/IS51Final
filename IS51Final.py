"""
Open Final.txt, read Final.txt. Find the number of grades (print "24"), 
find the average grades (print "83.25") by total score / number of students ("24")
Numbers of students grade above (83.25) (print "13" students out of (24) = 54.17%) 
by number of students grade higher than (83.25) / total students.


"""
"""
import file

    num1 = input(total_numbers_of_students)
    num2 = input(total_scores)
    num3 = input(class_average)
    num4 = input(number_of_students_score_above_class_average)
    num5 = input(percentage_of_grades_above_average)

    num3 = num1 / num 2
    num5 = num4 / 1

"""
import fileinput

def calculate_average():

    text = open(r'Final.txt').read()
    num_list = []

    with open('Final.txt', 'r') as f:
        for line in f:
            num = line.strip()
            num_list += [num]
            return (num_list)


main()
