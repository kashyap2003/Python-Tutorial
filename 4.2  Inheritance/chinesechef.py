from chef import Chef

class ChineseChef(Chef): # It inherited Chef in ChineseChef.

    def make_special_dish(self):  # IT overwrites this in ChineseChef so It will print this in Chinesechef
        print("The chef makes Orange chicken")

    def make_fried_rice(self):
        print("The chef makes a Fried rice")