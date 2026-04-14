def count_fives():
    count = 0
    inp = int(input("Оценка(0 - завершить)"))
    while inp != 0:
        if inp == 5:
            count += 1
        inp = int(input("Оценка(0 - завершить)"))

    return count
        
def print_fives():
    count = count_fives()
    if count >= 1 and count <= 3:
        return 3
    elif count >= 4 and count <= 5:
        return 5
    return 10

print("Скидка на поездуку (%): ", print_fives())