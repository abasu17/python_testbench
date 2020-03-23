from models.model import *


# Create database model
class IndexModel(db.Model):
    __tablename__ = 'sys_users'
    u_id = db.Column(db.String(32), primary_key=True)
    f_name = db.Column(db.String(25))
    l_name = db.Column(db.String(25))
    u_name = db.Column(db.String(25))
    password = db.Column(db.String(64))
    del_flag = db.Column(db.Boolean)
    status = db.Column(db.Boolean)

    def __init__(self, u_id, f_name, l_name, u_name, password):
        self.u_id = u_id
        self.f_name = f_name
        self.l_name = l_name
        self.u_name = u_name
        self.password = password
        self.del_flag = False
        self.status = True

    def __repr__(self):
        return '{"f_name":"' + str(self.f_name) + \
               '", "l_name":"' + str(self.l_name) + \
               '", "u_name":"' + str(self.u_name) + \
               '", "u_id":"' + str(self.u_id) + \
               '"}'
