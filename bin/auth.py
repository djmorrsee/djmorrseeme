from flask.ext.basicauth import BasicAuth

class dj_auth(BasicAuth):
    def check_credentials(self, username, password):
        return True