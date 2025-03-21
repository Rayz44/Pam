print ("hello world")
favorite_language = {
    'jen':'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}
print (favorite_language)
#more examples
favorite_language = {
    'jen' :'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

for name, language in favorite_language.items():
    print (f"{name.title()}'s favorite language is {language.upper()}")