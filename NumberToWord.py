class Convert:
    def __init__(self, number : str):
        self.num = number
        self.NAMES = ['میلیون', 'میلیارد', 'تریلیون', 'کوادریلیون', 'کوینتیلیون', 'سیکستیلون', 'سپتیلیون', 'اکتیلیون', 'نونیلیون', 'دسیلیون', 'آندسیلیون', 'دودسیلیون', 'تریدسیلیون', 'کواتردسیلیون', 'کویندسیلیون', 'سیکسدسیلیون', 'سپتندسیلیون', 'اکتودسیلیوم', 'نومدسیلیون']

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

    def BigNumbers(self, lenght, number) -> str | None:
        for count, i in enumerate(range(7,64,3), 2):
            if lenght in range(i,i+3):
                NUMBER = self.Change(number[0: lenght-(count*3)])
                return ' '.join((NUMBER, self.NAMES[count-2]))
        return None

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

            case _:
                return self.BigNumbers(lenght, number)

    def Num2Word(self) -> str:
        numbers = self.Extract(str(self.num))
        result = [self.Change(i) for i in numbers]
        if all(result):
            lst = {k:[] for k in (*self.NAMES, 'هزار', '1')}
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