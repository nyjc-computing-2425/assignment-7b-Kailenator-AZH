# Built-in imports
import math

def read_testscores(filename: str) -> list:
  """
  Reads the specified file and returns the student row data in the form of a dictionary in a list

  Parameter
  -----------
  filename: str
    The name of the file to be read

  Returns
  ------------
  list
    The list of student row data as dictionaries
  """
  data = []
  with open(filename,'r') as f:
    f.readline()
    for i in f:
      row_dict = {}
      overall = 0
      i = i.strip("\n").split(',')
      overall = math.ceil((int(i[2])/30 * 15) + (int(i[3])/40 * 30) + (int(i[4])/80 * 35) + (int(i[5])/30 * 20))
      row_dict["class"] = i[0]
      row_dict["name"] = i[1]
      row_dict["overall"] = overall
      row_dict["grade"] = GRADE[overall]
      data.append(row_dict)
  return data


def analyze_grades(student_data: list) -> dict:
  analysis = {}
  """
  Analyzes the students data and returns a dictionary of the number of grades in each class

  Parameter
  ----------
  student_data: list
    The list of student data to be analyzed

  Returns
  ----------
  dict
    A dictionary with the number of grades in each class
  """
  GRADINGS = ['A','B','C','D','E','S','U']
  for i in range(18):
    class_grade = [0]*7
    for m in student_data:
      if m["class"] == f"Class{i+1}":
        class_grade[GRADINGS.index(m["grade"])] += 1
        #print(m)
    #print(class_grade)
    analysis[f"Class{i+1}"] = {}
    for m in range(7):
      analysis[f"Class{i+1}"][GRADINGS[m]] = class_grade[m]
  return analysis

# Your code below
# GRADE = {}
# for i in range(1,101):
#   if i >= 70:
#     GRADE[i] = "A"
#   elif i >= 60:
#     GRADE[i] = "B"
#   elif i >= 55:
#     GRADE[i] = "C"
#   elif i >= 50:
#     GRADE[i] = "D"
#   elif i >= 45:
#     GRADE[i] = "E"
#   elif i >= 40:
#     GRADE[i] = "S"
#   else:
#     GRADE[i] = "U"

GRADE = {1: 'U', 2: 'U', 3: 'U', 4: 'U', 5: 'U', 6: 'U', 7: 'U', 8: 'U', 9: 'U', 10: 'U', 11: 'U', 12: 'U', 13: 'U', 14: 'U', 15: 'U', 16: 'U', 17: 'U', 18: 'U', 19: 'U', 20: 'U', 21: 'U', 22: 'U', 23: 'U', 24: 'U', 25: 'U', 26: 'U', 27: 'U', 28: 'U', 29: 'U', 30: 'U', 31: 'U', 32: 'U', 33: 'U', 34: 'U', 35: 'U', 36: 'U', 37: 'U', 38: 'U', 39: 'U', 40: 'S', 41: 'S', 42: 'S', 43: 'S', 44: 'S', 45: 'E', 46: 'E', 47: 'E', 48: 'E', 49: 'E', 50: 'D', 51: 'D', 52: 'D', 53: 'D', 54: 'D', 55: 'C', 56: 'C', 57: 'C', 58: 'C', 59: 'C', 60: 'B', 61: 'B', 62: 'B', 63: 'B', 64: 'B', 65: 'B', 66: 'B', 67: 'B', 68: 'B', 69: 'B', 70: 'A', 71: 'A', 72: 'A', 73: 'A', 74: 'A', 75: 'A', 76: 'A', 77: 'A', 78: 'A', 79: 'A', 80: 'A', 81: 'A', 82: 'A', 83: 'A', 84: 'A', 85: 'A', 86: 'A', 87: 'A', 88: 'A', 89: 'A', 90: 'A', 91: 'A', 92: 'A', 93: 'A', 94: 'A', 95: 'A', 96: 'A', 97: 'A', 98: 'A', 99: 'A', 100: 'A'}
#student_data = read_testscores("testscores.csv")
#print(student_data)
#analyze = analyze_grades(student_data)
#print(analyze["Class18"]['U'])