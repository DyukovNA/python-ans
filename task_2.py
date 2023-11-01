def find_common_participants(str1, str2, div=","):
    set1 = set(str1.split(div))
    set2 = set(str2.split(div))
    return list(set1.intersection(set2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(
    participants_first_group, participants_second_group, "|")
)
