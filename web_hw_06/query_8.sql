SELECT AVG(g.grade) AS avg_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = ?;
