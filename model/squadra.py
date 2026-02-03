from dataclasses import dataclass
@dataclass
class Squadra:
    name: str
    team_code: str

    def __str__(self):
        return self.name
    def __hash__(self):
        return hash(self.team_code)



