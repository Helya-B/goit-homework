SELECT g.*
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.group_id = ? AND g.subject_id = ?
LIMIT 10 OFFSET 0;