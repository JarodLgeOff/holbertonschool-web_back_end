function updateStudentGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students) || !Array.isArray(newGrades)) {
        return [];
    }

    return students
        .filter((student) => student.location === city)
        .map((student) => {
            const grade = newGrades.find((item) => item.studentId === student.id);
            return {
                ...student,
                grade: grade ? grade.grade : 'N/A',
            };
        });
}

export default updateStudentGradeByCity;
