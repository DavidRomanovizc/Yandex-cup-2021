with open("input_B_2.txt") as input_file:
    count_all = int(input_file.readline())
    delivery_id = input_file.readline().split()
    parent_id = input_file.readline().split()
    out_delivery_count = int(input_file.readline())
    out_pozition = input_file.readline().split()


posilki = {}
for i in range(count_all):
    # Если поставка ещё не обработана
    if delivery_id[i] not in posilki:
        posilki[delivery_id[i]] = {"bag": True, "palete": False, "ids": []}

    if parent_id[i] == "0":  # Если палета
        posilki[delivery_id[i]]["palete"] = True
    elif parent_id[i] == delivery_id[i]:  # если лежит на палете
        posilki[delivery_id[i]]["ids"].append(parent_id[i])  # добавляем на склад
    elif parent_id[i] in posilki[delivery_id[i]]["ids"]:  # есть коробка куда вложить
        posilki[delivery_id[i]]["ids"].append(parent_id[i])  # добавляем на склад
    else:
        posilki[delivery_id[i]]["bag"] = False
        if parent_id[i] in posilki:
            posilki[parent_id[i]]["bag"] = False

if out_delivery_count != 0:
    for out_poz in range(out_delivery_count):
        if out_poz in delivery_id:
            posilki[delivery_id[out_pozition[i]]]["bag"] = False

ans = []
for i in posilki:
    if posilki[i]["bag"] and posilki[i]["palete"]:
        ans.append(i)

print(len(ans))
print(" ".join(ans))
