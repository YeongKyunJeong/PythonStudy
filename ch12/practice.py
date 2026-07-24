# practice.py

# path = r"ch12\file\계좌1.txt"

# data = {"김삿갓" : "597-89-000089",
#          "이수근" : "343-64-000064", 
#          "박혁거세" : "136-97-000097"}

# with open(r"ch12\file\계좌1.txt", 'w', encoding = 'utf-8') as f:
#     for i in data:
#         row = "%s %s\n" %(i, data[i])
#         f.write(row)

# # account_list = []
# # with open(path, "r", encoding = "utf-8") as f:
# #     data = f.readlines()
# #     for line in data:
# #         account_list.append(line.split(" ")[1][:-1])
# # print(account_list)

# # account_dict = {}
# # with open(path, "r", encoding = "utf-8") as f:
# #     data = f.readlines()
# #     for line in data:
# #         splited = line.split(" ")
# #         account_dict[splited[0]] = splited[1][:-1]
# # print(account_dict)

# account_new = {"강호동" : "147-12-002093", "유재석" : "146-22-102093"}
# with open(path, "a", encoding = "utf-8") as f:
#     for name in account_new:
#         f.write("%s %s\n" % (name, account_new[name]) )

# path = r".\ch12\file\order.txt"

# orderd = "주문 내역:\n - " + input("피자 주문")
# with open(path, "w", encoding = "utf-8") as f:
#     f.write(orderd)

# print(orderd)

# orderd = "\n - " + input("피자 주문")
# with open(path, "a+", encoding = "utf-8") as f:
#     f.write(orderd)
#     f.seek(0)
#     print(f.read())

# print(orderd)

from dataclasses import dataclass

# @dataclass
# class SensorLog:
#     time : str
#     equip : str
#     temp : float
#     vib : float

@dataclass
class SensorLog:
    time : str
    equip : str
    temp : float
    vib : float

log1 = SensorLog("11:23", "VS-54", 15.4, 0.1)
print(log1)
print(log1.__dict__)

def filter_high_temp_log(logs : list[SensorLog], threshold:float = 80, equip : str | None = None) -> list[SensorLog]:

    return [log for log in logs 
            if (equip is None or log.equip == equip) and log.temp > threshold]

from enum import Enum

class Equip(Enum):
    WPD_ = "WPD"
    WPV_ = "WPV"
    RAD_ = "RAD"

print(Equip.WPD_.value)
print(Equip["WPV_"].value)
print(Equip("WPV").value)