# from sys import argv
#
# def calendar(date: str):
#     day, month, year = map(int, date.split('.'))
#     print (day, month, year)
#     if 1 <= year <= 9999:
#         if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
#             return True
#         elif month in [4, 6, 9, 11] and 1 <= day <= 30:
#             return True
#         elif 1 <= day <= 28 + is_visokos_year(year):
#             return True
#         else:
#             return False
#     return False
#
#
# def is_visokos_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# def calendar_tetminal():
#     date = argv[1]
#     print(calendar(date))