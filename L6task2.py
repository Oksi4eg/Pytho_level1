class Road:

    def __init__(self, length, width):
        self._length = length
        self._wight = width

    def weight(self, weight_sqsm, sm):
        road_weight = self._length * self._wight * weight_sqsm * sm / 1000
        print(f'{road_weight} тонн')


road1 = Road(20, 5000)
road1.weight(25, 5)
