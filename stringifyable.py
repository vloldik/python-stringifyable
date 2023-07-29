from abc import ABC


class Stringifyable(ABC):
    def __str__(self):
        d = self.__dict__
        s = f'{self.__class__.__name__}('
        s += ', '.join([f'{a}={d.get(a)}' for a in d.keys() if not isinstance(d.get(a), list)])
        s += ', ' if not s.endswith('(') else ''
        s += ', '.join([f'{a}=[{", ".join([str(e) for e in d.get(a)])}]' for a in d.keys() if isinstance(d.get(a), list)])
        s = s[:-2] if s.endswith(', ') else s
        s += ')'
        return s

    def __repr__(self):
        return str(self)
