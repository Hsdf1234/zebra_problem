from ortools.sat.python import cp_model


# pylint: disable=too-many-statements
def solve_zebra():
    """Solves the zebra problem."""

    # Create the model.
    model = cp_model.CpModel()

    red = model.NewIntVar(1, 5, '红色')
    green = model.NewIntVar(1, 5, '绿色')
    yellow = model.NewIntVar(1, 5, '黄色')
    blue = model.NewIntVar(1, 5, '蓝色')
    white = model.NewIntVar(1, 5, '白色')

    englishman = model.NewIntVar(1, 5, '英国人')
    spaniard = model.NewIntVar(1, 5, '西班牙人')
    japanese = model.NewIntVar(1, 5, '日本人')
    italian = model.NewIntVar(1, 5, '意大利人')
    norwegian = model.NewIntVar(1, 5, '挪威人')

    dog = model.NewIntVar(1, 5, '狗')
    snails = model.NewIntVar(1, 5, '蜗牛')
    fox = model.NewIntVar(1, 5, '狐狸')
    zebra = model.NewIntVar(1, 5, '斑马')
    horse = model.NewIntVar(1, 5, '马')

    tea = model.NewIntVar(1, 5, '茶')
    coffee = model.NewIntVar(1, 5, '咖啡')
    water = model.NewIntVar(1, 5, '矿泉水')
    milk = model.NewIntVar(1, 5, '牛奶')
    fruit_juice = model.NewIntVar(1, 5, '橘子汁')

    photographer = model.NewIntVar(1, 5, '摄影师')
    diplomat = model.NewIntVar(1, 5, '外交官')
    doctor = model.NewIntVar(1, 5, '医生')
    violinist = model.NewIntVar(1, 5, '小提琴家')
    painter = model.NewIntVar(1, 5, '油漆工')

    model.AddAllDifferent(red, green, yellow, blue, white)
    model.AddAllDifferent(englishman, spaniard, japanese, italian, norwegian)
    model.AddAllDifferent(dog, snails, fox, zebra, horse)
    model.AddAllDifferent(tea, coffee, water, milk, fruit_juice)
    model.AddAllDifferent(painter, diplomat, doctor, violinist,
                          photographer)

    model.Add(englishman == red)
    model.Add(spaniard == dog)
    model.Add(coffee == green)
    model.Add(italian == tea)
    model.Add(green == white + 1)
    model.Add(photographer == snails)
    model.Add(diplomat == yellow)
    model.Add(milk == 3)
    model.Add(norwegian == 1)

    diff_fox_chesterfields = model.NewIntVar(-4, 4, 'diff_fox_chesterfields')
    model.Add(diff_fox_chesterfields == fox - doctor)
    model.AddAbsEquality(1, diff_fox_chesterfields)

    diff_horse_diplomat = model.NewIntVar(-4, 4, 'diff_horse_diplomat')
    model.Add(diff_horse_diplomat == horse - diplomat)
    model.AddAbsEquality(1, diff_horse_diplomat)

    model.Add(violinist == fruit_juice)
    model.Add(japanese == painter)

    diff_norwegian_blue = model.NewIntVar(-4, 4, 'diff_norwegian_blue')
    model.Add(diff_norwegian_blue == norwegian - blue)
    model.AddAbsEquality(1, diff_norwegian_blue)

    # Solve and print out the solution.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        people = [norwegian, italian, englishman, spaniard, japanese]
        color = [red, green, yellow, blue, white]
        pet = [dog, snails, fox, zebra, horse]
        drink = [tea, coffee, water, milk, fruit_juice]
        job = [photographer, diplomat, doctor, violinist, painter]
        for p in people:
            print((p.Name(),
                   [j.Name() for j in job if solver.Value(p) == solver.Value(j)][0],
                   [d.Name() for d in drink if solver.Value(p) == solver.Value(d)][0],
                   [pe.Name() for pe in pet if solver.Value(p) == solver.Value(pe)][0],
                   [c.Name() for c in color if solver.Value(p) == solver.Value(c)][0]))
    else:
        print('No solutions to the zebra problem, this is unusual!')


solve_zebra()