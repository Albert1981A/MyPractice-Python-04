
class CarBL:
    def __init__(self):
        self.__cars = [{"id": 1, "model": "Mazda"}, {"id": 2, "model": "BMW"}]


    def get_all_cars(self):
        return self.__cars


    def get_car(self, id):
        arr = list(filter(lambda x : x["id"] == int(id), self.__cars))
        return arr[0]


    def add_car(self, obj):
        self.__cars.append(obj)
        return "Car added !"


    def update_car(self, id, obj):
        # Option 1
        # for car in self.__cars:
        #     if car["id"] == int(id):
        #         car["model"] = obj["model"]
        #         break

        # Option2
        for i in range(len(self.__cars)):
            if self.__cars[i]["id"] == int(id):
                self.__cars[i] = obj
                break
        return "Car updated !"


    def delete_car(self, id):
        index = -1
        for i in range(len(self.__cars)):
            if self.__cars[i]["id"] == int(id):
                index = i
                break
        self.__cars.pop(index)
        return "Car deleted !"