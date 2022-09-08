import json
import os
import sys

class ProductBL():
    def __init__(self):
        self.__path = os.path.join(sys.path[0], "Data/products.json")

    def get_all_products(self):
        with open(self.__path, 'r') as file:
            data = json.load(file)    
            return data["products"]


    def get_product(self, id):
        with open(self.__path, 'r') as file:
            data = json.load(file)
            arr = data["products"]
            arr = list(filter(lambda x : x["id"] == int(id), self.__cars))
            return arr[0]


    def add_product(self, obj):
        data2 = {"products": []}
        with open(self.__path, 'r') as file:
            data = json.load(file)
            arr = data["products"]
            arr.append(obj)
            data2["products"] = arr
            file.close()
            with open(self.__path, 'w') as file2:
                json.dump(data2, file2)
        return "Car added !"


    def update_product(self, id, obj):
        data2 = {"products": []}
        with open(self.__path, 'r') as file:
            data = json.load(file)
            arr = data["products"]
            for i in range(len(arr)):
                if arr[i]["id"] == int(id):
                    arr[i] = obj
                    break
            data2["products"] = arr
            file.close()
            with open(self.__path, 'w') as file2:
                json.dump(data2, file2)
        return "Car updated !"


    def delete_product(self, id):
        data2 = {"products": []}
        index = -1
        with open(self.__path, 'r') as file:
            data = json.load(file)
            arr = data["products"]
            for i in range(len(arr)):
                if arr[i]["id"] == int(id):
                    index = i
                    break
            arr.pop(index)
            data2["products"] = arr
            file.close()
            with open(self.__path, 'w') as file2:
                json.dump(data2, file2)
        return "Car deleted !"
