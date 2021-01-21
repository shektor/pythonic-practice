from builder_iphone import IPhoneBuilder
from builder_samsung import SamsungBuilder
from director import PhoneBuildDirector

iphone_director = PhoneBuildDirector(IPhoneBuilder())
iphone_director.build_phone()
iphone = iphone_director.get_phone()
iphone.about()

samsung_director = PhoneBuildDirector(SamsungBuilder())
samsung_director.build_phone()
samsung = samsung_director.get_phone()
samsung.about()
