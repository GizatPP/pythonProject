def retT(movies):

    for i in movies:
        for j, v in i.items():
            if j == "imdb":
                if v >= 5.5:
                    print(True) #prints True if imdb of movie is more than 5.5
            else:
                print(False)
def new(movies):
    lis = []
    for i in movies:
        for j, v in i.items():
            if j == "imdb":
                if v >= 5.5:
                    lis.append(i)
    for i in lis: #returns name of movies which imdb is more than 5.5
        for j, v in i.items():
            if j == "name":
                print(v)

def neww(movies):
    myList = []
    for i in movies:
        for j, v in i.items():
            if v == category:
                myList.append(i)
    for i in myList:
        for j, v in i.items():
            if j == "name":
                print(v)

def newww(movies):
    list1 = []
    sum1 = 0
    for i in movies:
        for j, v in i.items():
            if j == "imdb":
                list1.append(v)
    for i in list1:
        sum1 += i
    print(len(list1))
    print(sum1)
    print(sum1 / len(list1))

def nnew(movies):
    lt = []
    l = []
    s = 0
    for i in movies:
        for j, v in i.items():
            if v == category:
                lt.append(i)
    for i in lt:
        for j, v in i.items():
            if j == "imdb":
                l.append(v)
    for i in l:
        s += i
    print(s / len(l))

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

category = str(input("Write category : "))
print(movies)
retT(movies)
neww(movies)
new(movies)
newww(movies)
nnew(movies)



