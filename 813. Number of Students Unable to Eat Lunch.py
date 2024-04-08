

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = 0
        square_student_count = 0
        for student in students:
            if student == 1:
                square_student_count += 1
            else:
                circle_student_count += 1
        for sandwich in sandwiches:
            if sandwich == 1:
                if square_student_count > 0:
                    square_student_count -= 1
                else:
                    break
            if sandwich == 0:
                if circle_student_count > 0:
                    circle_student_count -= 1
                else:
                    break
        return square_student_count + circle_student_count
