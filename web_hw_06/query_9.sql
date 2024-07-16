SELECT DISTINCT s.name AS subject_name
FROM grades g
JOIN subjects s ON s.id = g.subject_id
WHERE g.student_id = ?;