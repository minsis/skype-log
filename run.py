from skype_log import Skypper

my_log = Skypper()

print(my_log.get_skype_path())
print(my_log.get_skype_user())
print(my_log.get_skype_database_path())

my_log2 = Skypper(skype_user="no_one")
#print(my_log2.get_skype_user())
