SELECT *
FROM departments INNER JOIN projects
ON departments.project_id = projects.project_id
