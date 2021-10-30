# sets up how the website flows
from flask import render_template, flash, redirect, request, url_for, session, send_file
from app import app
import os, sys
from question_generation import q_getter, q_setup


# home page stuff
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if  request.method == 'POST':
        # getting selected topics and redirecting to the setup page
        topics = request.form.getlist('topics')
        if topics == []:
            return redirect(url_for('index'))
        session['topics'] = [topic.replace("_", " ") for topic in topics]
        return redirect(url_for('question_setup'))

    # initalizing all the vars for the page
    session['topic'] = 'topics'
    question_type = 'checkbox'


    # getting the avaliable topics
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path = path + '/topics/'
    topics = os.listdir(path)
    topics = [topic.replace('.txt', '').replace(' ', '_') for topic in topics]
    topics.remove('submitted_questions')

    # setting up vars that will start on the left
    if 'question_num' not in session.keys():
        session['question_num'] = 1
        session['correct'] = 0
        session['incorrect'] = 0
        session['streak'] = 0
        session['accuracy'] = 'None wrong so far, good job!'

    
    # renders the given template and then defines vars
    return render_template('index.html', title='Home', topics=topics, question_type=question_type)

@app.route('/question/setup')
def question_setup():
    topics = []
    topics = session['topics']
    session['questions'] = {}
    for topic in topics:
        topic = topic.replace('_', ' ')
        session['questions'].update(q_setup(topic))
    return redirect(url_for('testing'))



@app.route('/testing', methods = ['GET', 'POST'])
def testing():
    from timeit import default_timer as timer
    if  request.method == 'POST':
        session['question']['time'] =  round(timer() - session.pop('time'))
        session['question_num']+=1
        answer = request.form['answer'].replace('_', ' ')
        question = session.pop('question')
        
        # making number answers actual numbers
        if answer.replace('.', '').replace('-', '').isnumeric():
            answer = float(answer)
        question['your_answer'] = answer

        # giving the corresponding stats for correct and incorrrect answers
        if answer == question['answer']:
            session['last_result'] = "Correct, good job!"
            session['correct']+= 1
            session['streak']+= 1
        else:
            session['last_result'] = "Incorrect, try again next time."
            session['incorrect']+=1
            session['streak'] = 0
        
        
        # generating some stats
        session['accuracy'] = session['correct'] / session['question_num']
        
        session['last_answered'] = True
        session['last_question'] = question
        return redirect(url_for('testing'))
    
    # getting info
    session['question'] = q_getter(session['questions'])
    session['time'] = timer()
    return render_template('testing.html', title='Trainer')

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        path = path + "/topics/submitted_questions.txt"
        f = open(path, 'a')        

        # adding all the different vars to the new question file
        f.write('\nsubject: "{}"\n'.format(request.form['subject']))
        f.write('title: "{}"\n'.format(request.form['title']))
        f.write('question: "{}"\n'.format(request.form['question']))
        f.write('type: "{}"\n'.format(request.form['type']))
        f.write('variables: {}\n'.format(request.form['variables']))
        f.write('equation_vars: {}\n'.format(request.form['equation_vars']))
        f.write('round: {}\n'.format(request.form['round']))
        f.write('hint: "{}"\n'.format(request.form['hint']))
        f.write('reasoning: "{}"\n'.format(request.form['reasoning']))
        f.close()
        return redirect(url_for('submit'))
    return render_template('submit.html', title='Submit')

@app.route('/submit_download')
def download():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path = path + "/submitted_questions.txt"
    return send_file(path, as_attachment=True)

@app.route('/new_session')
def new_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

@app.route('/UIL_tests', methods = ['GET', 'POST'])
def UIL_index():
    # session.clear()
    # initalizating
    session['topic'] = 'UIL test'
    question_type = 'radio'


    # getting the tests
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path = path + '/tests/'
    tests = os.listdir(path)
    tests = [test.replace('.txt', '').replace(' ', '_') for test in tests]
    tests = [test.rstrip().replace(" ", "test") for test in tests]

    if  request.method == 'POST':
        test = request.form['options']
        if test == []:
            return redirect(url_for('UIL_index'))
        session['test_name'] = test
        return redirect(url_for('test_setup'))
    return render_template('test_index.html', title='UIL Tests', tests=tests, question_type=question_type)


@app.route('/test_setup')
def test_setup():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    path = path + "/tests/{}.txt".format(session['test_name'])
    f = open(path, 'r')
    test_questions = list(f.readlines())
    f.close()


    # removes all the empty strings in the list
    test_questions = [question for question in test_questions if question.rstrip('\n') != '']
    session['correct_value'] = int(test_questions.pop(0).split(':')[1].replace(' ', ''))
    session['incorrect_value'] = int(test_questions.pop(0).split(':')[1].replace(' ', ''))
    session['unanswered_value'] = int(test_questions.pop(0).split(':')[1].replace(' ', ''))


    question_num = 0
    session['test'] = []
    test = []
    for topics in test_questions:
        question_num+=1 
        topics_list = topics.split(',')
        questions = {}


        for subject in topics_list:
            questions.update(q_setup(subject.rstrip()))


        question = q_getter(questions)
        question['number'] = question_num
        test.append(question)


    session['test'] = test
    return redirect(url_for('UIL_tester'))

@app.route('/UIL_tester', methods = ['GET', 'POST'])
def UIL_tester():
    from timeit import default_timer as timer
    if request.method == 'POST':
        session['time'] =  int(timer() - session.pop('time'))
        session['correct'] = session['questions'] = session['incorrect'] = session['unanswered']= 0
        answerlist = request.form.getlist('answers')
        

        for question in session['test']:
            # getting each corresponding answer and running it through some tests and formatting things
            answer = answerlist.pop(0)
            if type(answer) == str:
                answer = answer.replace('_', ' ')
            if answer.replace(' ', '') == '':
                session['unanswered']+=1
                continue
            if answer.replace('.', '').replace('-', '').isnumeric():
                answer = float(answer)
            session['questions']+=1


            if question['answer'] == answer:
                question['result'] = 'Correct'
                session['correct']+=1
            else:
                question['result'] = 'Incorrect'
                session['incorrect']+=1
            question['your_answer'] = answer


        # dealing with not answering any questions and other possiblities
        if session['questions'] != 0:
            session['accuracy'] = session['correct'] / session['questions']
            if session['accuracy'] == 1:
                session['accuracy'] = "WOW!! You didn't get any questions wrong!!"
            session['avg_time'] = session['time'] // session['questions']
        else:
            session['accuracy'] = "WOW!! You didn't get any questions wrong!!"
            session['avg_time'] = "∞,-∞, or 0"
        
        return redirect(url_for('UIL_results'))


    session['time'] = timer()
    return render_template('test.html', title='Trainer')

@app.route('/UIL_results', methods = ['GET', 'POST'])
def UIL_results():
    session['points'] = int(session['correct']) * session['correct_value'] - int(session['incorrect']) * session['incorrect_value'] - int(session['unanswered']) * session['unanswered_value']
    return render_template('test_results.html')
