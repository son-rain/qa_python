import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Стальная крыса', 'Фантастика'],
                                 ['Пиковый валет', 'Детективы'],
                                 ['Мадагаскар', 'Мультфильмы']
                             ]
                             )
    def test_get_books_genre_add_new_book_with_specific_genre(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre().get(name) == genre

    def test_get_book_genre_add_new_book(self):
        collector = BooksCollector()
        genre = 'Ужасы'
        name = '1408'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_book_genre(name)) > 0

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Стальная крыса', 'Фантастика'],
                                 ['Пиковый валет', 'Детективы'],
                                 ['Мадагаскар', 'Мультфильмы']
                             ]
                             )
    def test_get_books_with_specific_genre_add_three_new_books_with_different_genres(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('name', ['', 'Карамабарарпаапаороирпропарьрмрапраарраdf'])
    def test_get_books_genre_add_two_books_with_incorrect_name(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_add_book_with_existent_name(self):
        collector = BooksCollector()
        name = '1408'
        name2 = '1408'

        collector.add_new_book(name)
        collector.add_new_book(name2)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Стальная крыса', 'Фантастика'],
                                 ['Мадагаскар', 'Мультфильмы']
                             ]
                             )
    def test_get_books_for_children_add_two_new_books_for_children(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Всадник без головы', 'Ужасы'],
                                 ['Пиковый валет', 'Детективы']
                             ]
                             )
    def test_test_get_books_for_children_add_two_new_books_not_for_children(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()

    def test_get_list_of_favorites_books_add_new_book_to_favorites(self):
        collector = BooksCollector()
        genre = 'Фантастика'
        name = 'Человек-невидимка'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_new_book_and_delete_book_from_favorites(self):
        collector = BooksCollector()
        genre = 'Фантастика'
        name = 'Человек-невидимка'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)

        assert name not in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_genre_get_book_by_incorrect_genre(self):
        collector = BooksCollector()
        genre = 'Драма'
        name = 'Ромео и Джульетта'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_with_specific_genre(genre)) == 0






