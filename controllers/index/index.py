from controllers.controller import *


class LoginController:

    def check_login(self, req):
        u_name = req['inputUserID']
        password = encrypt_string(req['inputPassword'])

        check_registered_user = db.session.query(IndexModel).filter(IndexModel.u_name == u_name,
                                                                    IndexModel.password == password,
                                                                    IndexModel.del_flag == False).first()
        return check_registered_user


class RegistrationController:

    def process_registration(self, req):

        if req['inputPassword'] == req['inputConfPassword']:
            u_id = uuid()
            f_name = req['inputFname']
            l_name = req['inputLname']
            u_name = req['inputUserName']
            password = encrypt_string(req['inputPassword'])

            if not db.session.query(IndexModel).filter(IndexModel.u_name == u_name).count():
                reg = IndexModel(u_id, f_name, l_name, u_name, password)
                db.session.add(reg)
                db.session.commit()
            else:
                return 3
        else:
            return 4

        return 2
