MONTHS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        print(self.isLeapYear(year))

        return self.getDaysOfMonth(year, month) + day

    def getDaysOfMonth(self, year: int, month: int) -> int:
        days = sum(MONTHS[:month])

        if self.isLeapYear(year) and month > 2:
            return days + 1

        return days

    def isLeapYear(self, year: int) -> bool:
        if year % 400 == 0: return True
        elif year % 100 == 0: return False
        elif year % 4 == 0: return True

        return False

    # def isLeapYear(self, year):
    #     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)