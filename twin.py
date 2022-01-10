from math import isnan


class twin(object):
    # inside [a-,a+] external[A-,A+]
    def __init__(self ,a1,a2):
        self.inside = a1
        if (isnan(float(a1.a)) or isnan(float(a1.b))) and a2.a == a2.b:
            self.inside = a2

        self.external = a2

    def inside_width(self):
        if isnan(self.inside.a):
            return -1
        return self.inside.wid

    def external_width(self):
        return self.external.wid

    def Print_result(self):
        print("[ ", self.inside, ", ", self.external, " ]")

