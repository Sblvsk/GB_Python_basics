def generator_klass(x, y):
    for key, val in zip(x,y[:len(x)]):
        yield key, val

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

answer = generator_klass(tutors, klasses)
print(*answer)