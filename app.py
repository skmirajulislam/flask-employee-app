from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://db1_owner:OzX4nQUMLV6v@ep-floral-leaf-a182z0z7.ap-southeast-1.aws.neon.tech/db1?sslmode=require"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"Employee {self.name}, {self.designation}, {self.salary}"


@app.route('/', methods=['GET', 'POST'])
def insert_user():
    all_details = Employees.query.all()
    if request.method == 'POST':
        name = request.form.get('name')
        designation = request.form.get('designation')
        salary = request.form.get('salary')

        if salary and salary.strip():
            salary = float(salary)
        else:
            return "Error: Salary cannot be empty", 400
        
        new_employee = Employees(
            name=name, designation=designation, salary=float(salary) # type: ignore
        ) 
        db.session.add(new_employee)
        db.session.commit()
        return redirect('/')

    return render_template('insert.html', all_details=all_details)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    details = Employees.query.filter_by(id=id).first()

    if request.method == 'POST':
        name = request.form.get('name')
        designation = request.form.get('designation')
        salary = request.form.get('salary')
        details.name = name  # type: ignore
        details.designation = designation  # type: ignore
        details.salary = salary  # type: ignore
        db.session.add(details)
        db.session.commit()
        return redirect('/')

    return render_template('update.html', details=details)


@app.route('/delete/<int:id>')
def delete_user(id):
    details = Employees.query.filter_by(id=id).first()
    print(f'{details} is deleted from record!')
    db.session.delete(details)
    db.session.commit()
    return redirect('/')

# jesonify is also valid Flask method

@app.route('/show')
def details():
    all_details = Employees.query.all()
    if len(all_details) > 0:
        employees_list = [
            {'name': emp.name, 'designation': emp.designation, 'salary': emp.salary}
            for emp in all_details
        ]
        return render_template('response.html', data=employees_list)
    else:
        return render_template('response.html', data={'message': 'No employees found'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

