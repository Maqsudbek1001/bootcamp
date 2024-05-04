def float_range(start, stop, step):
    while start < stop:
        yield round(start, 10)
        start += step
for i in float_range(0, 2, 0.5):
    print(i)

