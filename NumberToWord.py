class Convert:
    def __init__(self, number : str):
        self.num = number

    def Extract(self, lst) -> list:
        result = list()
        for index, i in enumerate(range(len(lst)-1,-1,-1)):
            token = int(lst[index])*(10**(i))
            if token:
                result.append(token)
        return result
    
    def CreateDict(self, *args) -> dict:
        return dict(
            zip(
                map(str, args[0]),
                list(args[1:])
            )
        )

    def Change(self, number : str) -> str | None:
        if not isinstance(number, str):
            number = str(number)
        lenght = len(number)
        match lenght:
            case 1:
                return self.CreateDict(
                    range(10), 'صفر', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه'
                    )[number]
            
            case 2:
                if str(number)[0] == '1':
                    return self.CreateDict(
                        range(10, 20), 'ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده'
                        )[number]
                
                return self.CreateDict(
                    range(20, 100, 10),  'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود'
                    )[number]
            case 3:
                return self.CreateDict(range(100, 1000, 100),  'صد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد')[number]
            
            case 4:
                return self.CreateDict(
                    range(1000, 10000, 1000), 'یک هزار', 'دو هزار', 'سه هزار', 'چهار هزار', 'پنج هزار', 'شش هزار', 'هفت هزار', 'هشت هزار', 'نه هزار'
                    )[number]

            case 5 | 6:
                NUMBER = self.Change(number[0:lenght-3])
                return ' '.join((NUMBER, 'هزار'))

            case 7 | 8 | 9:
                NUMBER = self.Change(number[0:lenght-6])
                return ' '.join((NUMBER, 'میلیون'))

            case 10 | 11 | 12:
                NUMBER = self.Change(number[0: lenght-9])
                return ' '.join((NUMBER, 'میلیارد'))

            case 13 | 14 | 15:
                NUMBER = self.Change(number[0: lenght-12])
                return ' '.join((NUMBER, 'تریلیون'))
            
            case 16 | 17 | 18:
                NUMBER = self.Change(number[0: lenght-15])
                return ' '.join((NUMBER, 'کوادریلیون'))
            
            case 19 | 20 | 21:
                NUMBER = self.Change(number[0: lenght-18])
                return ' '.join((NUMBER, 'کوینتیلیون'))

            case 22 | 23 | 24:
                NUMBER = self.Change(number[0: lenght-21])
                return ' '.join((NUMBER, 'سیکستیلون'))
            
            case 25 | 26 | 27:
                NUMBER = self.Change(number[0: lenght-24])
                return ' '.join((NUMBER, 'سپتیلیون'))
            
            case 28 | 29 | 30:
                NUMBER = self.Change(number[0: lenght-27])
                return ' '.join((NUMBER, 'اکتیلیون'))

            case 31 | 32 | 33:
                NUMBER = self.Change(number[0: lenght-30])
                return ' '.join((NUMBER, 'نونیلیون'))

            case 34 | 35 | 36:
                NUMBER = self.Change(number[0: lenght-33])
                return ' '.join((NUMBER, 'دسیلیون'))

            case 37 | 38 | 39:
                NUMBER = self.Change(number[0: lenght-36])
                return ' '.join((NUMBER, 'آندسیلیون'))

            case 40 | 41 | 42:
                NUMBER = self.Change(number[0: lenght-39])
                return ' '.join((NUMBER, 'دودسیلیون'))

            case 43 | 44 | 45:
                NUMBER = self.Change(number[0: lenght-42])
                return ' '.join((NUMBER, 'تریدسیلیون'))

            case 46 | 47 | 48:
                NUMBER = self.Change(number[0: lenght-45])
                return ' '.join((NUMBER, 'کواتردسیلیون'))

            case 49 | 50 | 51:
                NUMBER = self.Change(number[0: lenght-48])
                return ' '.join((NUMBER, 'کویندسیلیون'))

            case 52 | 53 | 54:
                NUMBER = self.Change(number[0: lenght-51])
                return ' '.join((NUMBER, 'سیکسدسیلیون'))

            case 55 | 56 | 57:
                NUMBER = self.Change(number[0: lenght-54])
                return ' '.join((NUMBER, 'سپتندسیلیون'))

            case 58 | 59 | 60:
                NUMBER = self.Change(number[0: lenght-57])
                return ' '.join((NUMBER, 'اکتودسیلیوم'))

            case 61 | 62 | 63:
                NUMBER = self.Change(number[0: lenght-60])
                return ' '.join((NUMBER, 'نومدسیلیون'))

            case _:
                return None

    def Num2Word(self) -> str:
        numbers = self.Extract(str(self.num))
        result = [self.Change(i) for i in numbers]
        if all(result):
            lst = {k:[] for k in ('نومدسیلیون', 'اکتودسیلیوم', 'سپتندسیلیون', 'سیکسدسیلیون', 'کویندسیلیون', 'کواتردسیلیون', 'تریدسیلیون', 'دودسیلیون', 'آندسیلیون', 'دسیلیون', 'نونیلیون', 'اکتیلیون', 'سپتیلیون', 'سیکستیلون', 'کوینتیلیون', 'کوادریلیون' ,'تریلیون' ,'میلیارد', 'میلیون', 'هزار', '1')}
            Words = str()

            for i in result:
                splited = i.split()
                if len(splited) == 1:
                    lst['1'].append(splited[0])
                    continue
                lst[splited[1]].append(splited[0])
            for k,v in lst.items():
                if v:
                    Words += ' و '.join(v)
                    if k != '1':
                        Words += ' '+k+' و '
            Words = Words.strip()
            if Words[-1] == 'و' and Words[-2] == ' ':
                Words = Words[:-1]
            return Words.strip()
        return str()

    def __str__(self) -> str:
        return self.Num2Word()