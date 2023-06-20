from attrs import define

@define
class Pokemon:
    name: str
    tera_type: str
    ability: str
    item: str
    move1: str
    move2: str
    move3: str
    move4: str
