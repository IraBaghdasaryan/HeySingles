#alldata

list_correct_username_pass = [("aaaaaa@aaa.aaa", "aaaaaa"), ("bbbbbb@bbb.bbb", "bbbbbb")]

list_wrong_username = [("aaa", "aaaaaa"), ("aaaa@1111", "bbbbbba"), ("%111@11.aaa", "cccccc")]

list_wrong_pass = [("aaaaaa@aaa.aaa", "azx"), ("bbbbbb@bbb.bbb", "124"), ("cccccc@ccc.ccc", "!E#$22221g")]


biometric_cancel = (None, 532, 1842, 3) #suren's mobile


#FilterSwipe
class Filter_Swipe:
    filter_men = (None, 192, 488, 3) #suren's mobile
    filter_women = (None, 537, 488, 3) #suren's mobile
    filter_both = (None, 888, 488, 3) #suren's mobile
    filter_location = (None, 461, 1014, 1) #suren's mobile

class Swipe_up:
    press = (None, 504, 1689)
    move = (None, 598, 121)