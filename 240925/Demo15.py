exercises = {
    "BT1": ["Huynh Kiệt", "Trọng Hưng"],
    "BT2": ["Duy Thiện", "Bảo Huy"],
    "BT3": ["Huynh Kiệt", "Quang Vinh"],
    "BT4": ["Bảo Huy", "Xuân Trường"],
    "BT5": ["Quang Minh", "Phước Tuấn"]
}
students = {}
for bt, names in exercises.items():
    for name in names:
        if name not in students:
            students[name] = []
        students[name].append(bt)
for name, bts in students.items():
    print(f"{name}: {', '.join(bts)}")