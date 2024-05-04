try:
    my_dict = {'name': 'John', 'age': 30}
    print(my_dict['gender'])

    my_list = [10, 20, 30]
    print(my_list[3])
    x = 5
    y = "hello"
    result = x + y
    print(result)
except (IndexError, TypeError, KeyError):
    print("Xatolik Mavjud")
