insert_status = """
    INSERT INTO status (name)
    VALUES (?);
"""

insert_user = """
    INSERT INTO users (fullname, email)
    VALUES (?, ?);
"""

insert_task = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (?, ?, ?, ?);
"""

select_tasks_by_user = """
    SELECT * FROM tasks
    WHERE user_id = ?;
"""

select_tasks_by_status = """
    SELECT * FROM tasks
    WHERE status_id = (
        SELECT id FROM status
        WHERE name = ?
    );
"""

update_task_status = """
    UPDATE tasks
    SET status_id = (
        SELECT id FROM status
        WHERE name = ?
    )
    WHERE id = ?;
"""

select_users_without_tasks = """
    SELECT * FROM users
    WHERE id NOT IN (
        SELECT user_id FROM tasks
    );
"""

select_tasks_with_status_except = """
    SELECT * FROM tasks
    WHERE status_id <> (
        SELECT id FROM status
        WHERE name = ?
    );
"""

delele_task_by_id = """
    DELETE FROM tasks
    WHERE id = ?;
"""

select_users_by_email_like = """
    SELECT * FROM users
    WHERE email LIKE ?;
"""

update_user_name = """
    UPDATE users
    SET fullname = ?
    WHERE id = ?;
"""

count_of_tasks_by_status = """
    SELECT COUNT(status_id) as total_tasks, status_id
    FROM tasks
    GROUP BY status_id;
"""

select_tasks_by_user_email_domain = """
    SELECT t.title, t.description, u.fullname, u.email FROM tasks AS t
    JOIN users AS u ON u.id = t.user_id
    WHERE u.email LIKE ?;
"""

select_tasks_without_desc = """
    SELECT * FROM tasks
    WHERE description IS NULL;
"""

select_tasks_and_users_by_status = """
    SELECT t.title, t.status_id, u.fullname FROM tasks AS t
    JOIN users AS u ON u.id = t.user_id
    WHERE t.status_id = (
        SELECT id FROM status
        WHERE name = ?
    );
"""

count_of_user_tasks = """
    SELECT COUNT(t.id) as total_tasks, u.fullname as user_name
    FROM users as u
    LEFT JOIN tasks AS t ON u.id = t.user_id
    GROUP BY u.id 
"""
