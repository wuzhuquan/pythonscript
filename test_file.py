from xpinyin import Pinyin

p = Pinyin()
wname = p.get_initials(u"上海", u'')
print(wname)