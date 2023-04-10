import csv
class Trial:

    hourly_Rate=15
    overtime_Rate=20
    all=[]
   
    def __init__(self,name:str,no_days:int,hours_day:int,overtime_day ,overtime:int):
        
        assert no_days>=0 , f"you cannot work {no_days}"
        assert overtime>=0 , f"you cannot work {overtime}"
        assert hours_day>=0 , f"you cannot work {hours_day}"
        assert overtime_day>=0 , f"you cannot work {overtime_day}"
        self.name = name
        self.no_days = no_days
        self.overtime = overtime
        self.overtime_day = overtime_day
        self.hours_day=hours_day

        Trial.all.append(self)


    def weekly(self):
        total=self.no_days*self.hours_day*self.hourly_Rate+self.overtime_day* self.overtime*self.overtime_Rate
        return total
    @classmethod
    def iniator(cls):
        with open('./CSVReader/jj.csv', 'r') as f:
            reader=csv.DictReader(f)
            trials=list(reader)
        for trial in trials:
            Trial(
                name=trial.get('name'),
                no_days=int(trial['no_days']),
                hours_day=int(trial['hours_day']),
                overtime_day=int(trial['overtime_day']),
                overtime=int(trial['overtime'])


            )

    def __repr__(self):
        return f"Trial(name= {self.name}, no_days= {self.no_days}, hours_day= {self.hours_day}, overtime_days= {self.overtime_day},horus_overtime= {self.overtime})"


# person1=Trial('John', 6, 8, 2, 6)
# person2=Trial('Sadaq', 4, 10, 1, 4)
# person1.hourly_Rate=20
# print(person1.weekly())
# print(Trial.all)

Trial.iniator()