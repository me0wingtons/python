import random

class Item:
    def __init__(self, name):
        self.name = name
        self.trainer = None

    def owned(self, trainer):
        self.trainer = trainer

    def get_owner(self):
        return self.trainer.name

class Ball(Item):
    def __init__(self, name, R1):
        super().__init__(name)
        self.pokemon = None

    def caught(self, trainer, pokemon):
        self.pokemon = pokemon
        self.name = self.name + ' - ' + pokemon.name
        pokemon.trainer = self.trainer
        trainer.pokemon.append(pokemon)
        return 'All right! ' + pokemon.name + ' was caught!'
        

    def throw(self, trainer, pokemon):
        """ ELABORATE CATCH MECHANICS CALCULATIONS """
        return self.caught(trainer, pokemon)

class Move:
    def __init__(self, name, type, power, pp, *HM):
        self.name = name
        self.type = type
        self.power = power
        self.pp = pp
        if HM:
            self.hm = True
        else:
            self.hm = False

class Pokemon:
    def __init__(self, name, type, lvl, hp, p_atk, p_def):
        self.name = name
        self.type = type
        self.lvl = lvl
        self.hp = hp
        self.p_atk = p_atk
        self.p_def = p_def
        self.faint = False
        self.trainer = None
        self.moves = []

    def get_moves(self):
        res = []
        for move in self.moves:
            res.append(move.name)
        return res

    def damage(self, damage):
        pass

    def fainted(self):
        self.faint = True
        return self.name + ' fainted!'
    
    def learn(self, move):
        if move in self.moves:
            return self.name + ' already knows ' + move.name
        elif len(self.moves) == 4:
            print(self.name + ' is trying to learn ' + move.name + '!')
            print('But, ' + self.name + ' can\'t learn more than 4 moves!')
            print('Delete an older move to make room for ' + move.name + '?')
            ans = input('yes/no : ')
            if ans == 'yes':
                print('Which move should be forgotten?')
                print(self.get_moves())
                forgot = input('> ')
                for m in self.moves:
                    if m.name.lower() == forgot.lower():
                        if m.hm:
                            print('HM techniques can\'t be deleted!')
                            return self.learn(move)
                        else:
                            self.moves.remove(m)
                            self.moves.append(move)
                            print('1, 2 and...')
                            print('Poof!')
                            print(self.name + ' forgot ' + forgot.upper() + ' and...')
                            return self.name + ' learned ' + move.name + '!'
                print('Invalid option!')
                return self.learn(move)
            elif ans == 'no':
                print('Abandon learning ' + move.name + '?')
                ans2 = input('yes/no : ')
                if ans2 == 'no':
                    return self.learn(move)
                elif ans2 == 'yes':
                    return self.name + ' did not learn ' + move.name + '!'      
        else:
            self.moves.append(move)
            return self.name + ' learned ' + move.name + '!'

    def attack(self, move, other):
        if self.faint:
            return self.name + ' has already fainted!'
        elif other is self:
            return self.name + ' cannot attack itself!'
        elif other.faint:
            return other.name + ' has already fainted!'
        print(self.name + ' used ' + move.name)
        initial = weakness_chart[move.type][other.type]
        if initial == 0:
            return 'It doesn\'t affect ' + other.name + '!'
        elif initial == 2:
            print('It\'s super effective!')
        elif initial == 0.5:
            print('It\'s not very effective...')
        DAMAGE = int(((2*self.lvl/5)+2) * move.power * (self.p_atk/other.p_def)/50)
        crit_roll = random.randint(1, 100)
        if crit_roll >= 90:
            crit = 1.5
            print('Critical hit!')
        else:
            crit = 1
        if self.type == move.type:
            stab = 1.5
        else:
            stab = 1
        r = random.randint(0, 4)
        MODIFIER = crit * stab * (0.85 + (r*0.5)) * weakness_chart[move.type][other.type]
        deal = int(DAMAGE * MODIFIER)
        before = other.hp
        other.hp -= deal
        if other.hp <= 0:
            other.hp = 0
        if other.hp == 0:
            print((other.name + '\'s HP went from ' + str(before) + ' to ' + str(other.hp)))
            return other.fainted()
        else:
            return other.name + '\'s HP went from ' + str(before) + ' to ' + str(other.hp)
        

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.bag = []
        self.pokedex = {}

    def get_pokemon(self):
        if self.pokemon:
            res = []
            for pokemon in self.pokemon:
                res.append(pokemon.name)
            return res
        else:
            return self.name + ' has no Pokemon!'

    def get_items(self):
        if self.bag:
            res = []
            for item in self.bag:
                res.append(item.name)
            return res
        else:
            return self.name + '\'s inventory is empty!'

    def take(self, item):
        if item.trainer == None:
            self.bag.append(item)
            item.trainer = self
            return self.name + ' received ' + item.name + '!'
        else:
            return item.name + ' belongs to someone!'

    def catch(self, ball, pokemon):
        if ball in self.bag and ball.pokemon == None:
            return ball.throw(self, pokemon)
        else:
            return ball.name + ' not in bag or ' + ball.name + ' already contains a Pokemon!'

        
            
        
# WEAKNESS CHART # [ATTACKER][DEFENDER] #
weakness_chart = {'bug':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':0.5,\
                             'flying':0.5,'ghost':1,'grass':2,'ground':1,'ice':1,\
                             'normal':1,'poison':2,'psychic':2,'rock':0.5,'water':1},\
                   'dragon':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':1,'ghost':1,'grass':1,'ground':1,'ice':1,\
                             'normal':1,'poison':1,'psychic':1,'rock':1,'water':1},\
                    'electric':{'bug':1,'dragon':1,'electric':0.5,'fighting':1,'fire':1,\
                             'flying':2,'ghost':1,'grass':0.5,'ground':0,'ice':1,\
                             'normal':1,'poison':1,'psychic':1,'rock':1,'water':2},\
                     'fighting':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':0.5,'ghost':0,'grass':1,'ground':1,'ice':2,\
                             'normal':2,'poison':1,'psychic':0.5,'rock':2,'water':1},\
                      'fire':{'bug':2,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':1,'ghost':1,'grass':2,'ground':1,'ice':2,\
                             'normal':1,'poison':1,'psychic':1,'rock':0.5,'water':0.5},\
                       'flying':{'bug':2,'dragon':1,'electric':0.5,'fighting':2,'fire':1,\
                             'flying':1,'ghost':1,'grass':2,'ground':1,'ice':1,\
                             'normal':1,'poison':1,'psychic':1,'rock':0.5,'water':1},\
                        'ghost':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':1,'ghost':1,'grass':1,'ground':1,'ice':1,\
                             'normal':0,'poison':1,'psychic':0,'rock':1,'water':1},\
                         'grass':{'bug':0.5,'dragon':1,'electric':1,'fighting':1,'fire':0.5,\
                             'flying':0.5,'ghost':1,'grass':0.5,'ground':2,'ice':1,\
                             'normal':1,'poison':0.5,'psychic':1,'rock':2,'water':2},\
                          'ground':{'bug':1,'dragon':1,'electric':2,'fighting':1,'fire':2,\
                             'flying':0,'ghost':1,'grass':0.5,'ground':2,'ice':1,\
                             'normal':1,'poison':0.5,'psychic':2,'rock':2,'water':1},\
                           'ice':{'bug':1,'dragon':2,'electric':1,'fighting':1,'fire':1,\
                             'flying':2,'ghost':1,'grass':2,'ground':2,'ice':0.5,\
                             'normal':1,'poison':1,'psychic':1,'rock':1,'water':1},\
                            'normal':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':1,'ghost':0,'grass':1,'ground':1,'ice':1,\
                             'normal':1,'poison':1,'psychic':1,'rock':1,'water':1},\
                             'poison':{'bug':2,'dragon':1,'electric':1,'fighting':1,'fire':1,\
                             'flying':1,'ghost':1,'grass':2,'ground':0.5,'ice':1,\
                             'normal':1,'poison':0.5,'psychic':1,'rock':0.5,'water':1},\
                              'psychic':{'bug':1,'dragon':1,'electric':1,'fighting':2,'fire':1,\
                             'flying':1,'ghost':1,'grass':1,'ground':1,'ice':1,\
                             'normal':1,'poison':2,'psychic':0.5,'rock':1,'water':1},\
                               'rock':{'bug':2,'dragon':1,'electric':1,'fighting':0.5,'fire':2,\
                             'flying':2,'ghost':1,'grass':1,'ground':1,'ice':2,\
                             'normal':1,'poison':1,'psychic':1,'rock':0.5,'water':1},\
                                'water':{'bug':1,'dragon':1,'electric':1,'fighting':1,'fire':2,\
                             'flying':1,'ghost':1,'grass':0.5,'ground':2,'ice':0.5,\
                             'normal':1,'poison':1,'psychic':1,'rock':2,'water':1}}

#############################
#        TEST CASES         #
#############################

# ADMIN MOVES #
delete = Move('I AM ADMIN', 'normal', 1000000000, 10)

# NORMAL MOVES #
tackle = Move('TACKLE', 'normal', 40, 35)
smokescreen = Move('SMOKESCREEN', 'normal', 0, 20)
growl = Move('GROWL', 'normal', 0, 20)
scratch = Move('SCRATCH', 'normal', 40, 35)
strength = Move('STRENGTH', 'normal', 80, 15, 'HM')
hyperbeam = Move('HYPER BEAM', 'normal', 150, 5)

# FIRE MOVES #
fireblast = Move('FIRE BLAST', 'fire', 110, 5)
ember = Move('EMBER', 'fire', 40, 25)

# WATER MOVES #
watergun = Move('WATER GUN', 'water', 40, 25)
surf = Move('SURF', 'water', 90, 15, 'HM')
hydropump = Move('HYDRO PUMP', 'water', 110, 5)

# GRASS MOVES #
vinewhip = Move('VINE WHIP', 'grass', 45, 25)
solarbeam = Move('SOLAR BEAM', 'grass', 120, 10)

# PSYCHIC MOVES #
psychic = Move('PSYCHIC', 'psychic', 90, 10)


### POKEMON ###
charmander = Pokemon('CHARMANDER', 'fire', 5, 23, 14, 13)
squirtle = Pokemon('SQUIRTLE', 'water', 5, 24, 14, 16)
bulbasaur = Pokemon('BULBASAUR', 'grass', 5, 24, 14, 14)
mewtwo = Pokemon('MEWTWO', 'psychic', 100, 150, 255, 90)


### ITEMS ###
pokeball = Ball('POKEBALL', 255)
potion = Item('POTION')
nugget = Item('NUGGET')

### TRAINER ###
andy = Trainer('ANDY')

def test_learn():
    charmander = Pokemon('CHARMANDER', 'fire', 5, 23, 14, 13)
    squirtle = Pokemon('SQUIRTLE', 'water', 5, 24, 14, 16)
    bulbasaur = Pokemon('BULBASAUR', 'grass', 5, 24, 14, 14)
    mewtwo = Pokemon('MEWTWO', 'psychic', 100, 150, 255, 90)
    print(charmander.learn(ember))
    print(charmander.learn(ember))
    print(charmander.learn(tackle))
    print(charmander.learn(strength))
    print(charmander.learn(smokescreen))
    print(charmander.get_moves())
    print(charmander.learn(fireblast))

def test_battle():
    charmander = Pokemon('CHARMANDER', 'fire', 5, 23, 14, 13)
    squirtle = Pokemon('SQUIRTLE', 'water', 5, 24, 14, 16)
    bulbasaur = Pokemon('BULBASAUR', 'grass', 5, 24, 14, 14)
    mewtwo = Pokemon('MEWTWO', 'psychic', 100, 150, 255, 90)
    print(charmander.attack(scratch, squirtle))
    print(squirtle.attack(tackle, charmander))
    print(charmander.attack(ember, squirtle))
    print(squirtle.attack(watergun, charmander))
    print(charmander.attack(fireblast, squirtle))
    print(bulbasaur.attack(delete, squirtle))
    print(bulbasaur.attack(delete, charmander))

def boss_battle():
    charmander = Pokemon('CHARMANDER', 'fire', 5, 23, 14, 13)
    squirtle = Pokemon('SQUIRTLE', 'water', 5, 24, 14, 16)
    bulbasaur = Pokemon('BULBASAUR', 'grass', 5, 24, 14, 14)
    mewtwo = Pokemon('MEWTWO', 'psychic', 100, 150, 255, 90)
    print(charmander.attack(scratch, mewtwo))
    print(squirtle.attack(tackle, mewtwo))
    print(charmander.attack(fireblast, mewtwo))
    print(squirtle.attack(hydropump, mewtwo))
    print(bulbasaur.attack(solarbeam, mewtwo))
    print(mewtwo.attack(psychic, squirtle))
    print(mewtwo.attack(hyperbeam, charmander))
    print(bulbasaur.attack(delete, mewtwo))
