end = 1
list1 = []
type (list1)
while (end != "0" ):

    name = input("Введите наименование товара - " )
    price = input("Введите цену товара - " )
    price = float(price)
    name = str(name)
    if (price > 0):
        price = (price + (price / 100 * 15))
        if ((price % 5) != 0):
            x = (price % 5)
            y = (price % 10)
            if ((5 - x) < (10 - x)):
                price = price + (5 - x)
            if ((5 - x) > (10 - x)):
                price = price + (10 - y)
        list1.append(name + " " +str(price))
        print("Наименование товара - ", name)
        print("Цена товара - ", price)
        if (input("Чтобы увидеть список всех товаров нажмите - 2 ") == "2" ):
            print(list1)
        end = input("Нажмите Enter, чтобы продолжить или введите 0, чтобы закончить ")
    else:
        print("Ошибка! Введено не действительное число")
