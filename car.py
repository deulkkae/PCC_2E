"""자동차를 표현할 때 쓸 수 있는 클래스"""

class Car:
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """주행거리를 주어진 값으로 바꿈"""
        """주행거리를 더 작은 값으로 바꾸려고 하면 거부"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("Yon can't roll back an odometer!")

    def inccrememt_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘린다"""
        if miles < 0:
            print("Yon can't roll back an odometer!")
        else:
            self.odometer_reading += miles

