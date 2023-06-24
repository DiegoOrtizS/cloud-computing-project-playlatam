from attrs import define


@define
class Pokemon:
    """
    Pokemon model for MongoDB.

    Attributes:
        name (str): Pokemon name.
        tera_type (str): Pokemon tera type.
        ability (str): Pokemon ability.
        item (str): Pokemon item.
        move1 (str): Pokemon move 1.
        move2 (str): Pokemon move 2.
        move3 (str): Pokemon move 3.
        move4 (str): Pokemon move 4.
    """

    name: str
    tera_type: str
    ability: str
    item: str
    move1: str
    move2: str
    move3: str
    move4: str
