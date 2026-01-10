class Profession:
#Родительский класс Профессия
    def __init__(self, name, education, salary, experience, hours):
    #5 свойств родительского класса: Имя, необходимое образование, зарплата, стаж, время работы в неделю.
        self.name = name
        self.education = education
        self.salary = salary
        self.experience = experience
        self.hours = hours

    def get_info(self):
        #Метод - получение информации
        return f"Имя: {self.name}, Образование: {self.education}"


    def calculate_salary(self):
        #Полное условие if-elif-else - недоработка / норма / переработка (метод получения зарплаты)
        if self.hours <= 20:
            return self.salary * 0.5
        elif self.hours <= 40:
            return self.salary
        else:
            return self.salary * 1.2

    def check_experience(self):
        #Метод - условие опыта
        if self.experience > 5:
            return "Опытный специалист"
        else:
            return "Начинающий специалист"

class ITSpecialist(Profession):
#Дочерний класс Программист
    def __init__(self, name, education, salary, experience, hours, languages, remote, level):
        super().__init__(name, education, salary, experience, hours)
        #3 дополнительных свойства: используемые языки, возмножность работы удалённо, уровень.
        self.languages = languages
        self.remote = remote
        self.level = level

    #3 метода дочернего класса
    def show_languages(self):
        #Цикл for - метод для получения изучаемых языков
        print(f"{self.name} знает языки:")
        for lang in self.languages:
            print(f"- {lang}")

    def can_work_remotely(self):
        #Метод условие работы из дома
        return "Может работать удаленно" if self.remote else "Работает только в офисе"

    def level_info(self):
        #Метод - получение информации об уровне
        return f"{self.get_info()}, Уровень: {self.level}"


class Doctor(Profession):
    #Дочерний класс Врач
    def __init__(self, name, education, salary, experience, hours, specialization, license, hospital):
        super().__init__(name, education, salary, experience, hours)
        # 3 дополнительных свойства:
        self.specialization = specialization
        self.license = license
        self.hospital = hospital

    #3 метода дочернего класса
    def check_license(self):
        #Условие наличия лицензии
        if self.license:
            return "Лицензия действительна"
        else:
            return "Лицензия отсутствует"

    def show_specialization(self):
        #Метод получения данных о специализации
        return f"Специализация: {self.specialization}"

    def calculate_salary(self):
        #Переопределение метода с доплатой за ночные дежурства
        special_salary = super().calculate_salary()
        if self.hours > 40:  # Если есть переработки
            return special_salary + 10000  # Доплата за переработки
        return special_salary

#Дальше Бога нет.

# IT-специалист
programmer = ITSpecialist(
    name="Эраст",
    education="Всевышнее",
    salary=120000,
    experience=3,
    hours=40,
    languages=["Python", "JavaScript", "SQL"],
    remote=True,
    level="Middle"
)

# Врач
doctor = Doctor(
    name="Рудольф",
    education="Высшее медицинское",
    salary=150000,
    experience=8,
    hours=45,
    specialization="Стоматолог",
    license=True,
    hospital="Городская больница №42"
)

print(programmer.level_info())
print(f"Зарплата: {programmer.calculate_salary()} руб.")
programmer.show_languages()
print(programmer.can_work_remotely())
print(doctor.get_info())
print(f"Зарплата: {doctor.calculate_salary()} руб.")
print(doctor.show_specialization())
print(doctor.check_license())

professions = [programmer, doctor]

for prof in professions:
    print(f"\n{prof.name}: {prof.check_experience()}")
    if hasattr(prof, 'show_specialization'):
        print(prof.show_specialization())
