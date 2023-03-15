from ortools.sat.python import cp_model
import time


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

    model.Add(englishman == red)  # 英国人住在红色的房子里
    model.Add(spaniard == dog)  # 西班牙人养了一条狗
    model.Add(japanese == painter)  # 日本人是一个油漆工
    model.Add(italian == tea)  # 意大利人喜欢喝茶
    model.Add(green == white + 1)  # 绿房子在白房子的右边
    model.Add(photographer == snails)  # 摄影师养了一只蜗牛
    model.Add(diplomat == yellow)  # 外交官住在黄房子里
    model.Add(milk == 3)  # 中间那个房子的人喜欢喝牛奶
    model.Add(norwegian == 1)  # 挪威人住在左边的第一个房子里
    model.Add(coffee == green)  # 喜欢喝咖啡的人住在绿房子里

    # 挪威人住在蓝色的房子旁边
    diff_norwegian_blue = model.NewIntVar(-4, 4, 'diff_norwegian_blue')
    model.Add(diff_norwegian_blue == norwegian - blue)
    model.AddAbsEquality(1, diff_norwegian_blue)

    model.Add(violinist == fruit_juice)  # 小提琴家喜欢喝橘子汁

    # 养狐狸的人所住的房子与医生的房子相邻
    diff_fox_doctor = model.NewIntVar(-4, 4, 'diff_fox_doctor')
    model.Add(diff_fox_doctor == fox - doctor)
    model.AddAbsEquality(1, diff_fox_doctor)

    # 养马的人所住的房子与外交官的房子相邻
    diff_horse_diplomat = model.NewIntVar(-4, 4, 'diff_horse_diplomat')
    model.Add(diff_horse_diplomat == horse - diplomat)
    model.AddAbsEquality(1, diff_horse_diplomat)

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

# 计时
start = time.perf_counter()
solve_zebra()
end = time.perf_counter()
print('程序运行的时间为{}秒'.format(end - start))