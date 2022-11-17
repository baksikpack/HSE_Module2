class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass

    def check_grade(self):
        pass


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
        self.check_grade()

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()

    def check_grade(self):
        if self.grade < ((self.seniority // 5) + 1):
            for _ in range(((self.seniority // 5) + 1) - self.grade):
                self.grade_up()


class Designer(Employee):
    """Дочерний класс Designer родительского класса Employee увелиивает грейд за каждые 7 баллов
    (1 балл за каждую акрредитацию, 2 балла за каждую международную премию)"""

    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority)
        self.add_award(awards)
        self.check_grade()
#При инициализации двойная проверка. Плохо по стилю

    def add_award(self, award):
        """Параметр метода - количество добавляемых премий"""
        if award:
            self.seniority += award * 2
            self.check_grade()

    def check_grade(self):
        if self.grade < ((self.seniority // 7) + 1):
            for _ in range(((self.seniority // 7) + 1) - self.grade):
                self.grade_up()

    def check_if_it_is_time_for_upgrade(self):
        """Проверка необходимости повышения.
        Повышение на 1 грейд проводится за каждые 7 баллов.
        1 балл дается за факт прохождения аккредитации, 2 балла - за получение(наличие) международной премии"""
        self.seniority += 1
        # условия повышения сотрудника - 7 баллов
        if self.seniority % 7 == 0:
            self.grade_up()

        # вывод результатов
        return self.publish_grade()
