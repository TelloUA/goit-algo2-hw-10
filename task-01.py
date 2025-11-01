from teacher import Teacher
import heapq

def create_schedule(subjects, teachers):
    schedule = []
    remaining_subjects = subjects.copy()
    remaining_teachers = teachers.copy()

    while remaining_subjects:
        max_count = 0
        heap_teachers = []
        for teacher in remaining_teachers:
            count = len(remaining_subjects & teacher.can_teach_subjects)
            if count > max_count:
                max_count = count
                heap_teachers = []
                heapq.heappush(heap_teachers, (teacher.age, teacher))
            elif count == max_count:
                heapq.heappush(heap_teachers, (teacher.age, teacher))

        if heap_teachers:
            teacher = heap_teachers[0][1]
            teacher.assigned_subjects = teacher.can_teach_subjects & remaining_subjects
            remaining_subjects = remaining_subjects - teacher.assigned_subjects
            remaining_teachers.remove(teacher)
            schedule.append(teacher)
        else:
            schedule = None
            return schedule
        
    return schedule

if __name__ == '__main__':
    teachers_data = [
        ["Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}],
        ["Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}],
        ["Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}],
        ["Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}],
        ["Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}],
        ["Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}],
    ]

    teachers = [Teacher(*data) for data in teachers_data]

    subjects = set(["Математика", "Фізика", "Хімія", "Інформатика", "Біологія"])

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")