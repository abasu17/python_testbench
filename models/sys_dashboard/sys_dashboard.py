from models.model import *


# Create database model
class ProjectModel(db.Model):

    __tablename__ = 'sys_projects'
    id = db.Column(db.String(32), primary_key=True)
    project_title = db.Column(db.String(100))
    project_alias = db.Column(db.String(100))
    project_description = db.Column(db.String(500))
    project_path = db.Column(db.String(200))
    project_owner = db.Column(db.String(32))
    del_flag = db.Column(db.Boolean)
    status = db.Column(db.Boolean)

    def __init__(self, id, project_title, project_alias, project_description, project_path, project_owner):
        self.id = id
        self.project_title = project_title
        self.project_alias = project_alias
        self.project_description = project_description
        self.project_path = project_path
        self.project_owner = project_owner
        self.del_flag = False
        self.status = True

    def __repr__(self):
        return '{"project_id":"' + str(self.id) + \
               '", "project_title":"' + str(self.project_title) + \
               '", "project_alias":"' + str(self.project_alias) + \
               '", "project_description":"' + str(self.project_description) + \
               '", "project_path":"' + str(self.project_path) + \
               '", "project_owner":"' + str(self.project_owner) + \
               '"}'
