import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()


def book_by_id(id_):
    """ Giving information about book by id. """
    data = {}
    for book in root.findall('Book'):
        for elem in book:
            book_id = book.attrib['id']
            if int(book_id) == id_:
                data['id'] = book.attrib['id']
                data[elem.tag] = elem.text
    return data


def book_by_isbn(ISBN):
    """ Giving information about book by ISBN. """
    data = {}
    for book in root.findall('Book'):
        for elem in book:
            isbn = book.find('ISBN').text
            if isbn == ISBN:
                data['id'] = book.attrib['id']
                data[elem.tag] = elem.text
    return data


def books_by_year(year):
    """ Counting the number of books by published year. """
    lst = []
    for book in root.findall('Book'):
        published_year = book.find('Year_of_publishing').text
        if int(published_year) == year:
            lst.append(book)
    return len(lst)


def average():
    """ Calculating the average cost of books of each publisher. """
    dict_ = {}
    lst = []
    average_cost = {}
    for book in root.findall('Book'):
        publisher = book.find('Publisher').text
        price = book.find('Price').text
        lst.append(publisher)
        if publisher not in dict_:
            dict_[publisher] = float(price)
        else:
            dict_[publisher] += float(price)
    publishers = {i: lst.count(i) for i in lst}
    for key1, value1 in dict_.items():
        for key2, value2 in publishers.items():
            if key1 == key2:
                average_cost[key1] = round(value1 / value2, 2)
    return average_cost


def the_most_expensive(publisher, year):
    """ Giving information about the most expensive book(s) by publisher and published year. """
    data = {}
    the_most_exp = {}
    for book in root.findall('Book'):
        publisher_of_book = book.find('Publisher').text
        published_year = book.find('Year_of_publishing').text
        price = book.find('Price').text
        if publisher_of_book == publisher or publisher_of_book == publisher + '.' and int(published_year) == year:
            data[book.attrib['id']] = float(price)
    for i in data.keys():
        if data[i] == max(data.values()):
            the_most_exp[i] = data[i]
    for i in the_most_exp.keys():
        i = int(i)
        return book_by_id(i)


def main():
    """ The main function of the programme. """
    while True:
        tasks = ['1. Вывести полную информацию по id книги.',
                 '2. Вывести полную информацию о книге по ISBN.',
                 '3. Подсчитать количество книг по заданному году издания.',
                 '4. Подсчитать среднюю стоимость книг по каждому издательству.',
                 '5. Вывести информацию о самой дорогой книге(ах) по заданным издательству и году издания.',
                 '6. Завершить работу программы.']
        for i in tasks:
            print(i)

        while True:
            try:
                choice = int(input('Введите номер операции от 1 до 6: '))
                if choice < 1 or choice > 6:
                    raise Exception
                break
            except:
                print('Неверный ввод, попробуйте еще раз.')

        if choice == 1:
            while True:
                try:
                    input_id = int(input('Введите id книги: '))
                    break
                except:
                    print('Неверный ввод, попробуйте еще раз.')
            if book_by_id(input_id) == {}:
                print('К сожалению,нет книги с таким id.')
            else:
                for key, value in book_by_id(input_id).items():
                    print(key + ':', value)

        elif choice == 2:
            while True:
                try:
                    input_isbn = input('Введите ISBN книги: ')
                    input_isbn = input_isbn.split('-')
                    new_isbn = ''
                    for i in range(len(input_isbn)-1):
                        new_isbn += str(input_isbn[i]) + '-'
                    new_isbn = new_isbn + input_isbn[-1]
                    break
                except:
                    print('Неверный ввод, попробуйте еще раз.')
            if book_by_isbn(new_isbn) == {}:
                print('К сожалению,нет книги с таким ISBN.')
            else:
                for key, value in book_by_isbn(new_isbn).items():
                    print(key + ':', value)

        elif choice == 3:
            while True:
                try:
                    input_year = int(input('Введите год: '))
                    break
                except:
                    print('Неверный ввод, попробуйте еще раз.')
            if books_by_year(input_year) == 0:
                print('К сожалению,нет книг такого года издания.')
            else:
                print(books_by_year(input_year))

        elif choice == 4:
            for key, value in average().items():
                print(key + ':', value)

        elif choice == 5:
            while True:
                try:
                    input_publisher = input('Введите издательство: ')
                    input_year = int(input('Введите год: '))
                    break
                except:
                    print('Неверный ввод, попробуйте еще раз.')
            if the_most_expensive(input_publisher, input_year) == {}:
                print('К сожалению, нет такой книги(книг).')
            else:
                for key, value in the_most_expensive(input_publisher, input_year).items():
                    print(key + ':', value)

        elif choice == 6:
            break


if __name__ == '__main__':
    main()
