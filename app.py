from flask import Flask, render_template, jsonify, request
app = Flask(__name__, template_folder='templates')
students = [
    {'id': 1, 'name': 'Vasu', 'age': '14', 'gradYear': '2026'},
    {'id': 2, 'name': 'Josh', 'age': '14', 'gradYear': '2026'},
    {'id': 3, 'name': 'Sam', 'age': '14', 'gradYear': '2026'},
]


@app.route('/displayHello')
def hello():
    return 'Hello World!'


@app.route('/schoolDisp')
def school():
    return 'Edgemont Jr/Sr High'


@app.route('/dispHTML')
def showHTML():
    return render_template('index.html', index_variable='HELLO')


@app.route('/addStudent', methods=['POST'])
def addStudent():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Insufficient Information to Add Student'
        })
    s = {
        'id': students[-1]['id']+1,
        'name': request.json['name'],
        'age': request.json['age'],
        'gradYear': request.json['gradYear'],
    }
    students.append(s)
    return jsonify({
        'status': 'success',
        'message': 'Student Successfully Added to Database'
    })


@app.route('/showStudents')
def showStudents():
    return jsonify({
        'data': students,
    })


app.run(debug=True)
