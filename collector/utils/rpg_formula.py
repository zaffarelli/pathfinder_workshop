import re
from collector.utils.pathfinder_tools import dice


class RpgFormula:
    def __init__(self, formula, degree=0):
        self.prefix = ''
        self.degree = degree
        for e in range(self.degree+1):
            self.prefix += '>'
        self.total = 0
        self.subs = []
        self.formula = formula.strip()
        self.params = []
        self.subformulas = []
        self.parse()
        self.compute()

    def display(self, str):
        print(f'{self.prefix} {str}')

    def parse(self):
        self.subs = re.findall(r'\((.*?)\)', self.formula)
        self.display(self.subs)
        for s in self.subs:
            f = RpgFormula(s, self.degree+1)
            self.subformulas.append(f)

    def compute(self):
        error = False
        self.params = self.formula.split("+")
        total = 0
        for pa in self.params:
            self.display(f"pa: [{pa}]")
            p = pa.strip()
            if p in self.subformulas:
                self.display(f"{p} --> subformula")
                for s in self.subformulas:
                    if s.formula == p:
                        total += s.total
            elif "(" in p:
                pass
            elif ")" in p:
                pass
            elif "d" in p:
                s = p.split('d')
                v = dice(int(s[0]), int(s[1]))
                self.display(f"{p} --> {v}")
                total += v
            elif '*' in p:
                s = p.split('*')
                v = int(s[0]) * int(s[1])
                self.display(f"{p} --> {v}")
                total += v
            elif p.isnumeric():
                self.display(f"{p} --> {p}")
                total += int(p)
            else:
                self.display(f"[{p}] as [{pa}] --> error")
                error = True
        if error:
            return -1
        else:
            return total

    def show(self):
        self.display(self.formula)
        self.display(self.total)
