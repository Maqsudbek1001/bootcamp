def cheksiz_generator():
    i = 0
    while True:
        yield f"Bu loop hech qachon to'xtamaydi: {i}"
        i += 1

for item in cheksiz_generator():
    print(item)