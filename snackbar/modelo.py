class Ingredient():
    def __init__(self, idx, name, value, amount):
        self._id = idx
        self._name = name
        self._value = value
        self._amount = amount
    
    @property
    def id(self):
        return self._id 
    
    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def value(self):
        return self._value
    
    @name.setter
    def name(self, new_value):
        self._value = new_value

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, new_amout):
        self._amount = new_amout

class Snacks(list):
    def __init__(self, idx, name_snack, snack_img, ingredients_list):
        self._id = idx
        self._name_snack = name_snack
        self._snack_img = snack_img
        self._ingredients_list = ingredients_list
        self._price = 0

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def name_snack(self):
        return self._name_snack
    
    @name_snack.setter
    def name_snack(self, new_snack_name):
        self._name_snack = new_snack_name

    @property
    def snack_img(self):
        return self._snack_img
    
    @snack_img.setter
    def snack_img(self, new_snack_img):
        self._snack_img = new_snack_img

    @property
    def ingredients_list(self):
        return self._ingredients_list
    
    @ingredients_list.setter
    def ingredients_list(self, new_ingredients_list):
        self._ingredients_list = new_ingredients_list

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price