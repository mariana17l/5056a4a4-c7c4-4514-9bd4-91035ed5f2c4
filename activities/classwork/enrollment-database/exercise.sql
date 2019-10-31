/*
 SECTION: Group exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */


-- A) Get all the unique department names.

-- B) Get the top 10 female students (first_name, last_name, age, gpa) with the best GPA scores and order by age (asc).

-- C) Count the number of male/female students that are at least 25 years old.

-- D) Get the number of male/female students that were accepted

-- E) Get the min, average, and max GPA of the accepted male students that are less than 20 years old.

-- F) Get the number of enrollments to courses that take longer than 2 years to finalize.

-- G) Get the number of male/female student that will take a course from the 'Statistics' department.


/*
 SECTION: Individual exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */

-- A) Count the number of courses per department
SELECT
    department,
    count(department)
FROM
    course
GROUP BY department
;


-- B) How many male/female students were accepted?
SELECT
	s.gender AS "Student Gender",
	count(s.gender)
FROM
	student s INNER JOIN enrollment e ON s.id = e.student_id
WHERE
	e.approved = 1
GROUP BY
	s.gender
;

-- C) How many students were accepted per course?
SELECT
    name,
    count(name)
FROM
    course INNER JOIN  enrollment ON enrollment.course_id = course_id
WHERE
    enrollment.approved = 1
GROUP BY
    name
;

-- D) What's the average age and gpa per course?
SELECT
    name,
    avg(gpa),
    avg(age)
FROM
    student INNER JOIN enrollment  on student.id = enrollment.student_id
    INNER JOIN course on course.id = enrollment.course_id
GROUP BY
    course.name
;

-- E) Get the average number of years the enrolled (approved) female student will study.
SELECT
    gender,
    AVG(years)
FROM
    student INNER JOIN enrollment ON student.id = enrollment.student_id
    INNER JOIN course ON course.id = enrollment.course_id
WHERE
    enrollment.approved = 1 AND gender = 'female'
GROUP BY
    student.gender
;

