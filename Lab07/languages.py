from Lab07.programminglanguage import ProgrammingLangauge

java = ProgrammingLangauge('Java', 'Static', True, 1995)
cpp = ProgrammingLangauge('C++', 'Static', False, 1983)
python = ProgrammingLangauge('Python', 'Dynamic', False, 1991)
visual_basic = ProgrammingLangauge('Visual Basic', 'Static', False, 1991)
ruby = ProgrammingLangauge('Ruby', 'Dynamic', True, 1995)

languages = [java, cpp, python, visual_basic, ruby]

ruby.is_dynamic()
print(ruby)

print("The dynamically typed languages are: ")
for language in languages:
    if language.is_dynamic():
        print(language.name)
