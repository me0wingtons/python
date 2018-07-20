def make_atom(name, atomic, mass):
    return ([name], atomic, mass)

def get_name(atom):
    return atom[0]

def get_atomic(atom):
    return atom[1]

def get_mass(atom):
    return atom[2]

def make_molecule(molecule, atom):
    molecule_name = get_name(molecule)
    molecule_atomic = get_atomic(molecule)
    molecule_mass = get_mass(molecule)
    molecule_atomic += get_atomic(atom)
    molecule_name += get_name(atom)
    molecule_mass += get_mass(atom)
    return (molecule_name, molecule_atomic, molecule_mass)

def rename(molecule):
    raw_name = get_name(molecule)
    new = []
    if 'oxygen' in raw_name:
        n = new.count('oxygen')
        if n == 1:
            new.append('oxide')
        elif n == 2:
            new.append('dioxide')
        elif n == 3:
            new.append('trioxide')
        else:
            new.append('n' + 'oxide')
    for name in raw_name:
        if name == 'oxygen':
            continue
        n = raw_name.count(name)
        if n == 1:
            new.append(name)
            while raw_name.count(name) != 0:
                raw_name.remove(name)
        elif n == 2:
            new.append('di'+name)
            while raw_name.count(name) != 0:
                raw_name.remove(name)
        elif n == 3:
            new.append('tri'+name)
            while raw_name.count(name) != 0:
                raw_name.remove(name)
    return (new, get_atomic(molecule), get_mass(molecule))


################
## TEST CASES ##
################

H = make_atom('hydrogen', 1, 1)
O = make_atom('oxygen', 8, 16)
OH = make_molecule(O, H)
HOH = make_molecule(OH, H)
