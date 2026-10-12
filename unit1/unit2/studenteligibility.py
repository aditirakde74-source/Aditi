marks=65
attendence=80
marks_ok =marks>=65
attendence_ok=attendence>=80
eligible=marks_ok and attendence_ok
one_condition=marks_ok or attendence_ok
not_eligible=not eligible
print("and=",eligible)
print("or=",one_condition)
print("not=",not_eligible)