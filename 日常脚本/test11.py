data = ['abc',['a','b','c'],('a','b','c')]


for i in data:
    i *= 2
    print(i[3])

langs = {"Python", "Java", "Perl"}
langs2 = {"Python", "PHP", "C#"}
langs3 = {"Lisp", "PHP", "Perl"}
langs4 = langs.difference(langs2, langs3)
print(langs4)