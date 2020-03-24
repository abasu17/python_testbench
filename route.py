from app import *
from flask import render_template, session, send_from_directory
from controllers.controller import *


@app.route('/', methods=['GET', 'POST'])
def index():
    obj_login = LoginController()
    obj_registration = RegistrationController()

    msg_idx = 0
    session['auth'] = False

    if request.method == 'POST':
        if request.form['form'] == 'loginForm':
            check = obj_login.check_login(dict(request.form))
            if check == None:
                msg_idx = 1
            else:
                new_data = eval(str(check))
                session['auth'] = True
                session['u_name'] = new_data["u_name"]
                session['u_id'] = new_data["u_id"]
                return render_template('sys_dashboard/sys_dashboard.html',
                                       curr_user=str(new_data["f_name"] + " " + new_data["l_name"]))
        else:
            msg_idx = obj_registration.process_registration(request.form)

    return render_template('index/index.html', err_chk=msg_idx)


@app.route('/home')
def home():
    return render_template('index/nav-menu/index-home.html')


@app.route('/about')
def about():
    return render_template('index/nav-menu/index-about.html')


@app.route('/contact')
def contact():
    return render_template('index/nav-menu/index-contact.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    obj_projectController = ProjectController(session['u_id'])
    check_stat = -1
    event_flag = None

    if request.method == 'POST':

        event_flag = request.form['event']
        if request.form['event'] == 'create':
            check_stat, session['workspace_path'] = obj_projectController.create(request.form)
        elif request.form['event'] == 'update':
            check_stat = obj_projectController.update(request.form)
        elif request.form['event'] == 'delete':
            check_stat = obj_projectController.delete(request.form)

    all_projects = obj_projectController.fetch_all()

    return render_template('sys_dashboard/project-console/sys_dashboard-create-project.html',
                           check_stat=check_stat,
                           projects=all_projects,
                           event_flag=event_flag)


@app.route('/package/<project_alias>', methods=['GET', 'POST'])
def package(project_alias):
    obj_projectController = ProjectController(session['u_id'])
    check_stat = None
    event_flag = None

    project_path = obj_projectController.fetch_path(project_alias)

    if request.method == 'POST':
        event_flag = request.form['event']
        if event_flag == 'create':
            check_stat = obj_projectController.create_package(request.form)
            project_path = obj_projectController.fetch_path(project_alias)
        elif event_flag == 'delete':
            check_stat = obj_projectController.delete_package(request.form)
            project_path = obj_projectController.fetch_path(project_alias)
        elif event_flag == 'edit':
            session['package-path'] = request.form['package-path']
            return redirect(url_for('source_edit'))

    return render_template('sys_dashboard/project-console/sys_dashboard-create-package.html', project_path=project_path,
                           check_stat=check_stat, event_flag=event_flag)


@app.route('/source_edit', methods=['GET', 'POST'])
def source_edit():
    package_path = session['package-path']
    return render_template('sys_dashboard/project-console/sys_dashboard-source-code.html', package_path=package_path)


@app.route('/logout')
def logout():
    return redirect('/')
