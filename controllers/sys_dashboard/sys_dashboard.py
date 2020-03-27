from controllers.controller import *


class ProjectController:
    PROJECT_OWNER = None
    PROJECT_PATH = None
    TESTING_PATH = None

    def __init__(self, project_owner):
        self.PROJECT_OWNER = project_owner

    def create(self, req):

        project_id = uuid()
        project_title = req['project-title']
        project_alias = req['alias-name']
        project_description = req['project-description']

        if not db.session.query(ProjectModel).filter(ProjectModel.project_alias == project_alias,
                                                     ProjectModel.project_owner == self.PROJECT_OWNER).count():
            workspace_path = create_workspace(project_id)
            if workspace_path is not None:
                insert_qry = ProjectModel(project_id, project_title, project_alias, project_description, workspace_path,
                                          self.PROJECT_OWNER)
                db.session.add(insert_qry)
                db.session.commit()
            else:
                return 0, None

        else:
            if db.session.query(ProjectModel).filter(ProjectModel.project_alias == project_alias,
                                                     ProjectModel.project_owner == self.PROJECT_OWNER,
                                                     ProjectModel.del_flag == True,
                                                     ProjectModel.status == False
                                                     ).count():
                update_obj = db.session.query(ProjectModel).filter_by(project_alias=project_alias,
                                                                      del_flag=True,
                                                                      status=False).first()
                update_obj.del_flag = False
                update_obj.status = True
                workspace_path = create_workspace(update_obj.id)
                db.session.commit()
            else:
                return 0, None

        return 1, workspace_path

    def update(self, req):

        project_title = req['project-title']
        project_alias = req['alias-name']
        project_description = req['project-description']

        update_obj = db.session.query(ProjectModel).filter_by(project_alias=project_alias,
                                                              project_owner=self.PROJECT_OWNER,
                                                              del_flag=False,
                                                              status=True).first()
        if update_obj is not None:
            update_obj.project_title = project_title
            update_obj.project_description = project_description
            db.session.commit()
            return 1

        return 0

    def delete(self, req):

        project_alias = req['project-alias']

        update_obj = db.session.query(ProjectModel).filter_by(project_alias=project_alias,
                                                              project_owner=self.PROJECT_OWNER,
                                                              del_flag=False,
                                                              status=True).first()
        workspace_path = update_obj.project_path
        if 'remove-all' in req.keys():
            remove_workspace(workspace_path)

        if update_obj is not None:
            update_obj.del_flag = True
            update_obj.status = False
            db.session.commit()
            return 1

        return 0

    def fetch_all(self):

        all_projects = db.session.query(ProjectModel).filter(ProjectModel.project_owner == self.PROJECT_OWNER,
                                                             ProjectModel.del_flag == False,
                                                             ProjectModel.status == True).all()

        return all_projects

    def fetch_path(self, project_alias):

        project_path = db.session.query(ProjectModel).filter(ProjectModel.project_owner == self.PROJECT_OWNER,
                                                             ProjectModel.project_alias == project_alias,
                                                             ProjectModel.del_flag == False,
                                                             ProjectModel.status == True).first()
        self.PROJECT_PATH = project_path.project_path + "/src"
        self.TESTING_PATH = project_path.project_path + "/testcase"
        list_dir = get_dir(self.PROJECT_PATH)
        return list_dir

    def create_package(self, req):

        if req['folder-name'] == '':
            if create_pkg(self.PROJECT_PATH + "/" + req['package-name']):
                if create_pkg(self.TESTING_PATH + "/" + req['package-name'], "test"):
                    return 1
        else:
            new_path = create_folder(self.PROJECT_PATH + "/" + req['folder-name'])
            if new_path:
                if create_pkg(new_path + "/" + req['package-name']):
                    if create_pkg(self.TESTING_PATH + "/" + req['package-name'], "test"):
                        return 1
        return 0

    def delete_package(self, req):

        if delete_pkg(req['package-path']):
            if delete_pkg(req['package-path'].replace('/src/', '/testcase/')):
                return 1

        return 0


    def read_package(self, path):
        package_content = read_file(path)
        test_content = read_file(path.replace("/src/", '/testcase/'))

        return {"package_content": package_content, "test_content": test_content}


    def source_code_process(self, req, path):
        if req['event'] == "generate":
            if write_file(path, req['source_code']):
                if write_file(path.replace('/src/', '/testcase/'), process_analyze(path)):
                    return True
        elif req['event'] == "save":
            if write_file(path, req["source_code"]):
                if write_file(path.replace('/src/', '/testcase/'), req["test_case"]):
                    return True
        return False

    def testcase_execute(self, path):
        return exe_testcase(path.replace('/src/', '/testcase/'))