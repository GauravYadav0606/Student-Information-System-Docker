
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul Sharma", "course": "B.Tech CSE", "email": "rahul@gmail.com"},
    {"id": 2, "name": "Priya Verma", "course": "B.Tech DS", "email": "priya@gmail.com"},
    {"id": 3, "name": "Aman Singh", "course": "B.Tech IT", "email": "aman@gmail.com"}
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Information System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f5fa;
            margin: 0;
            padding: 30px;
        }
        .container {
            max-width: 950px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 3px 12px #00000015;
        }
        h1 {
            color: #234a80;
            text-align: center;
        }
        p {
            text-align: center;
            color: #666;
        }
        form {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin: 25px 0;
        }
        input {
            flex: 1;
            min-width: 150px;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            background: #234a80;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 14px;
            border-bottom: 1px solid #ddd;
            text-align: left;
        }
        th {
            background: #234a80;
            color: white;
        }
        .count {
            text-align: right;
            color: #234a80;
            font-weight: bold;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Information System</h1>
    <p>Manage and view student records</p>

    <form method="POST" action="/add">
        <input name="name" placeholder="Student Name" required>
        <input name="course" placeholder="Course" required>
        <input name="email" type="email" placeholder="Email" required>
        <button type="submit">Add Student</button>
    </form>

    <div class="count">Total Students: {{ students|length }}</div>

    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Course</th>
            <th>Email</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.course }}</td>
            <td>{{ student.email }}</td>
        </tr>
        {% endfor %}
    </table>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, students=students)

@app.route("/add", methods=["POST"])
def add_student():
    student = {
        "id": len(students) + 1,
        "name": request.form["name"],
        "course": request.form["course"],
        "email": request.form["email"]
    }
    students.append(student)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
