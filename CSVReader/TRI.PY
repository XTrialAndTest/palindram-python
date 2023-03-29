def append(url):
            with open (url) as update_file:
                fileToWrite=csv.writer(update_file)
                while True:
                    name=input('what is the name of the book: ').strip()
                    author=input('what is the author of the book: ').strip()
                    Genre=input('what is the genre of the book: ').strip()
                    price=input('what is the price of the book: ').strip()
                    if name=='' or author=='' or Genre=='' or price=='':
                        print('one of the values is empty and the append is not done.')
                        continue
                    else:
                        fileToWrite.writerow(f"{name},{author},{Genre},{price} '\n'")
                        print('\n')
                        print(f"{name},{author},{Genre},{price}")
append('..\challanges\CSVReader\trl.csv')