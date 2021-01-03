"""전기 자동차를 나타낼 때 쓸 수 있는 클래스 세트"""

from car import Car

class Battery:
    """전기 자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size=75):
        """배터리 속성 초기화"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """배터리가 제공하는 주행 가능 거리를 출력한다"""

        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 85:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """베터리 크기 확인하고 용량 바꾸기"""
        
        if self.battery_size != 85:
           self.battery_size = 85

class ElectricCar(Car):
    """전기 자동차에만 해당하는 특징을 나타낸다"""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화하고
        전기자동차에만 해당하는 속성을 초기화한다
        """
        super().__init__(make, model, year) # super()는 부모 클래스를 호출하는 함수
        self.battery = Battery()

    def fill_gas_tank(self): # Car 클래스에 이 메서드가 있다고 가정하고 여기서 오버라이드
        """전기 자동차에는 연료 탱크가 없습니다."""
        print("This car doesn't need a gas tank!")