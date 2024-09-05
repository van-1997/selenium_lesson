class Car():

    def __init__(self,car_name,year):
        self.car_name = car_name
        self.year = year

    def car_color(self):
        if self.year <= 2010 :
            print("До",self.year, "годов выпускались машины цветами : Коричневый, Белый, черный, Серии.")
        else:
            print("От",self.year,"машины выпускались цветами радуги как глянцевые так и матовые.")


# a = Car("Hundai",2011)
# a.car_color()
class Horse_Links(Car):

    def __init__(self,car_name,year,torque_nm,rpm):
        self.torque_nm = torque_nm
        self.rpm = rpm

        Car.__init__(self,car_name,year)

    def calculate_horsepower(self):
        col = round((self.torque_nm * self.rpm) / 7127)
        return col



    def fuel_consumption(self):
        print("Приближенная мощность в лошадиных силах", self.calculate_horsepower())
        print("Расход топлива в литрах на 100 км :",self.calculate_horsepower() * 0.1)



a = Horse_Links("hyundai",2010,150,5000)
a.car_color()
a.calculate_horsepower()
a.fuel_consumption()