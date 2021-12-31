import json

class Pokemon:
    """ Struct to store pokemon info
    """
    def __init__(self, moves = [0, 0, 0, 0], items = [0], abilities = [0], types = [],
                 status = 0, hp = 1, base_stats = [199.88, 188.12, 188.12, 188.12, 179.72],
                 boosts = [0, 0, 0, 0, 0]):
        """ Constructor
            For unknown values, leave the unknown kwargs blank for default values.

        args:
        moves   --  List of move IDs.
                    For player pokemon, stores the pokemon's known moves (four moves)
                    For opponent pokemon, stores all possible moves      (any number of moves)
        items    -- List of possible item IDs (for known item this will be a one element list)
        abilities -- List of possible ability ID (for known ability this will be a one element list)
        types   -- List of type IDs
        status  -- status ID
        hp      -- Float ranging from [0, 1]
        base_stats -- List of floats ranging from [0, 1] (ordered [atk, def, spa, spd, spe])
        boosts  -- List of floats ranging from [-6, 6] (ordered [atk, def, spa, spd, spe])
        """
        self.moves = moves
        self.items = items
        self.abilities = abilities
        self.types = types
        self.status = status
        self.hp = hp
        self.base_stats = base_stats
        self.boosts = boosts


class FightState:
    """ Struct to store the state of a fight at a given turn
    """
    def __init__(self, pokemon, opp_pokemon):
        """ Constructor
            values need to be initialized manually for now
        """
        # Global fight state
        self.field_attrib = []          # List of field attribute IDs
        
        # Player state
        self.used_dynamax = False       # Boolean
        self.remaining_dynamax = 0      # Float element of {0, 0.33, 0.66, 1}
        self.side_attrib = []           # List of side attribute IDs
        self.pokemon = pokemon   # Array of pokemon objects
                                                        # (LEADING POKEMON AT IDX 0 and DO NOT CHANGE SIZE)

        # Opponent state
        self.opp_used_dynamax = False   # Boolean
        self.opp_remaining_dynamax = 0  # Float element of {0, 0.33, 0.66, 1}
        self.opp_side_attrib = []       # List of side attribute IDs
        self.opp_pokemon = opp_pokemon # Array of pokemon objects
                                                         # (LEADING POKEMON AT IDX 0 and DO NOT CHANGE SIZE)
    def from_json(self, path):
        """ Initializes a FightState object from a request.json file
        """
        with open(path, "r") as rf:
            state_data = json.load(rf)
        # TODO complete from_json()