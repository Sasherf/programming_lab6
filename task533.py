dictionary = {
    "Guido van Rossum": "Python",
    "James Gosling": "Java",
    "Dennis Ritchie": "C",
    "Bjarne Stroustrup": "C++",
    "Robert Griesemer": "Go",
    "Rob Pike": "Go",
    "Ken Thompson": "Go",
    "Larry Wall": "Perl",
    "Yukihiro Matsumoto": "Ruby"
}

for i in range(2):
    name = input()
    
    for key in dictionary:
        if name in key:
            print(dictionary[key])
            break
    else:
        print("Name not found in the dictionary.")