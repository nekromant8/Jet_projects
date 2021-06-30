class University:

    def __init__(self):
        self.departments = {"Biotech": [], "Chemistry": [], "Engineering": [], "Mathematics": [], "Physics": []}
        self.test = {"Biotech": 2, "Chemistry": 3, "Engineering": 4, "Mathematics": 5, "Physics": 6}  # position of the test results
        self.students = []
        self.places = int(input())
        self.applicants = self.load_applicants()

    def load_applicants(self):
        file = open("applicant_list_5.txt", 'r')
        file_list = [applicant.strip('\n').split() for applicant in file]
        file.close()
        return self.mean_calculation(file_list)

    def mean_calculation(self, file_list):  # defining applicants list with combined scores
        applicants = []
        for applicant in file_list:
            applicants.append([applicant[0], applicant[1], str((int(applicant[2]) + int(applicant[3])) / 2), applicant[3],
                               str((int(applicant[4]) + int(applicant[5])) / 2), applicant[4],
                               str((int(applicant[2]) + int(applicant[4])) / 2), applicant[6], applicant[7], applicant[8], applicant[9]])
        return applicants

    def assign_applicants(self):  # launching logic per priority
        for i in range(6, 11):  # updated indexes to fit new list
            self.priority_lists(i)

    def priority_lists(self, priority):  # updated logic to accept applicants based on respective test scores
        for department in self.departments.keys():
            self.applicants.sort(key=lambda x: (-max(float(x[self.test[department]]), float(x[7])),  x[0] + x[1]))# sort by corresponding test
            for applicant in self.applicants:
                if applicant[priority] == department and len(self.departments.get(department)) < self.places  \
                        and applicant not in self.students:
                    self.departments[department].append([applicant[0], applicant[1], applicant[self.test[department]], applicant[7], department])
                    self.students.append(applicant)



    def publish_results(self):
        for key in self.departments.keys():
            self.departments[key].sort(key=lambda x: (-max(float(x[2]), float(x[3])), x[0] + x[1]))
            self.print_department_students(key)
            print(key)
            for student in self.departments[key]:
                print(" ".join(student[0:2]), max(float(student[2]), float(student[3])))
            print("")

    def print_department_students(self, department):
        new_file = open(f"{department}.txt", "w", encoding='utf-8')
        for student in self.departments[department]:
            new_file.write(" ".join(student[0:2]) + ' ' + str(max(float(student[2]),float(student[3]))) + "\n")
        new_file.close()


mit = University()
mit.assign_applicants()
mit.publish_results()
