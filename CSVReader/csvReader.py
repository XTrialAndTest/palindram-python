import csv
listOfBooks =[]
def getBook(url):
    def BooksList(param):
        
        with open (param) as newBooks:
            newBook=csv.reader(newBooks)
            for x in newBook:
            
                listOfBooks.append({'Name': x[0],'Author': x[1], 'Genre': x[2],'price': x[3], })
    
        
        return listOfBooks 
    print(BooksList(url) ) 
    print('\n')
    what= input('what like to do search? author, Genre, price: ').strip()
    if what.lower() == 'author':
        def authorSearch(auther):
            authorList= []
            for i in listOfBooks:
                
                if i['Author'].lower()==auther.lower():
                    # print(i)
                    authorList.append(i)

            return authorList
        

        print( authorSearch(input("what is the author name: First Name, Last Name: ")))
    elif what.lower() == 'price':
        min=input('what is the minimum price: ').strip()
        max=input('what is the maximum price: ').strip()
        def priceSearch(min,max):
            priceList= []
            for i in listOfBooks:
                if i['price']>=min and i['price']<=max:
                    # print(i)
                    priceList.append(i)
        
            return priceList
        print( priceSearch(min,max))
    elif what.lower()=='genre':
        Genre=input('what is the Genre of the book you want: ').strip()
        def GenreSearch(Genre):
            GenreList= []
            for i in listOfBooks:
                if i['Genre'].lower()==Genre.lower():
                    # print(i)
                    GenreList.append(i)
            return GenreList
        print(GenreSearch(Genre))
    
getBook('..\challanges\CSVReader\csvReaderList.csv')

