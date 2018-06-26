# This class will be importing all the other classes.
from enemy import Troll, Vampire, VampireKing  # import using the file name of the particular class file
# if imported module is showing red color then either our module doesn't exist or
# We are not working in the main project folder through IDE.
# Note it is not recommended to import in this way , but here each module will contain single class
# so we can do so to increase readability


# ugly_troll = Troll()
# print("UGLY TROLL : \n{}".format(ugly_troll))
# # O/P:
# # UGLY TROLL :
# # Name : Enemy	Hit_points : 0	Lives : 1
#
# another_troll = Troll("uUg", 18, 1)
# print("Another Troll : \n{}".format(another_troll))
# # O/P:
# # Another Troll :
# # Name : uUg	Hit_points : 18	Lives : 1
#
# brother = Troll("Urg", 23)
# print("Urg's Brother : \n{}".format(brother))
# # O/P:
# # Urg's Brother :
# # Name : Urg	Hit_points : 23	Lives : 1
#
# """We can observe that we are using Three different constructors even without making them.
#     we can say that its a type of constructor overloading. But this is not true.
#     This is because python does not supports method overloading.
#     If we try, the last method we defined in the coned will be the only ine be exist.
#     Actually above all constructors are same, they have different no of parameters because
#     we have specified the default values of the rest parameters in the base class.
# """

ug_troll = Troll("Ug")
print(ug_troll)
# O/p:
# Name : Ug	Hit_points : 23	Lives : 1
ug_troll.grunt()

blood_drinker = Vampire("Blood Drinker")
print(blood_drinker)
blood_drinker.take_damage(6)

print(blood_drinker)

blood_sipper = Vampire("Blood Sipper")
print(blood_sipper)

# while blood_sipper._alive:
#     blood_sipper.take_damage(1)
#     print(blood_sipper)

blood_king = VampireKing("Blood King")
print(blood_king)

while blood_king._alive:
    blood_king.take_damage(4)
    print(blood_king)
    