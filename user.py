#user class to store information about the user
class User:
    def __init__(self, name, experience, availability, project, now):
        self._name = name #name of user
        self._experience = experience #years of experience as an int
        self._availability = availability #availaibility as string ie MW or MTuTh etc
        self._project = project #project they are working on / department ie, we will match people in the same places
        self._now = now #true if they need a match now, false if they want to wait for matches in pool

    # getters
    def get_name(self):
        return self._name

    def get_experience(self):
        return self._experience

    def get_availability(self):
        return self._availability

    def get_project(self):
        return self._project

    def get_now(self):
        return self._now

    # setters
    def set_name(self, name):
        self._name = name

    def set_experience(self, experience):
        self._experience = experience

    def set_availability(self, availability):
        self._availability = availability

    def set_project(self, project):
        self._project = project

    def set_now(self, now):
        self._now = now