data = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1),
]

w1 = 0.0
w2 = 0.0
bias = 0.0
speed = 0.1


def predict(x1, x2):
    total = w1 * x1 + w2 * x2 + bias
    if total > 0:
        return 1
    return 0


for epoch in range(1, 21):
    errors = 0
    for inputs, answer in data:
        x1 = inputs[0]
        x2 = inputs[1]
        guess = predict(x1, x2)
        error = answer - guess
        if error != 0:
            errors = errors + 1
            w1 = w1 + speed * error * x1
            w2 = w2 + speed * error * x2
            bias = bias + speed * error
    print("Эпоха", epoch, "- ошибок:", errors)
    if errors == 0:
        break

print("Веса:", round(w1, 2), round(w2, 2), "сдвиг:", round(bias, 2))
for inputs, answer in data:
    print(inputs, "->", predict(inputs[0], inputs[1]), "(нужно", answer, ")")