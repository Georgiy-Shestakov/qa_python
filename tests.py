from main import BooksCollector
import pytest

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
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест 1. Метод add_new_book - книга с названием длиннее 40 символов не добавляется
    def test_add_new_book_name_longer_than_forty(self):
        collector = BooksCollector()
        
        collector.add_new_book('Голос внутри нас: путешествие к самопознанию через столетия')
        assert len(collector.books_genre) == 0

    # Тест 2. Метод set_book_genre - можно добавить жанр, если он существует в self.genre
    def test_set_book_genre_add_existing_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Тест')
        collector.set_book_genre(name='Тест', genre='Комедии')
        assert collector.books_genre.get('Тест') == 'Комедии'

    # Тест 3. Метод get_book_genre - ввели имя, получили жанр
    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Тест')
        collector.set_book_genre(name='Тест', genre='Комедии')
        assert collector.get_book_genre('Тест') == 'Комедии'

    # Тест 4. Метод get_books_with_specific_genre - ввели жанр, получили список книг, соотвествующих жанру
    def test_get_books_with_specific_genre_returns_two_from_three(self):
        collector = BooksCollector()

        collector.add_new_book('Тест_1')
        collector.set_book_genre(name='Тест_1', genre='Комедии')
        collector.add_new_book('Тест_2')
        collector.set_book_genre(name='Тест_2', genre='Ужасы')
        collector.add_new_book('Тест_3')
        collector.set_book_genre(name='Тест_3', genre='Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Тест_2', 'Тест_3']

    # Тест 5. Метод get_books_genre - добавляем книги и жанры к ним, по методу получаем все книги и их жанры
    def test_get_books_genre_shows_all_books(self):
        collector = BooksCollector()

        collector.add_new_book('Тест_1')
        collector.set_book_genre(name='Тест_1', genre='Детективы')
        collector.add_new_book('Тест_2')
        collector.set_book_genre(name='Тест_2', genre='Мультфильмы')
        collector.add_new_book('Тест_3')
        collector.set_book_genre(name='Тест_3', genre='Фантастика')
        assert collector.get_books_genre() == {'Тест_1': 'Детективы', 'Тест_2': 'Мультфильмы', 'Тест_3': 'Фантастика'}

    # Тест 6. Метод get_books_for_children - получаем только книги != self.genre_age_rating = ['Ужасы', 'Детективы']
    def test_get_books_for_children_shows_no_restricted_categories(self):
        collector = BooksCollector()

        collector.add_new_book('Взрослая_1')
        collector.set_book_genre(name='Взрослая_1', genre='Детективы')
        collector.add_new_book('Детская')
        collector.set_book_genre(name='Детская', genre='Мультфильмы')
        collector.add_new_book('Взрослая_2')
        collector.set_book_genre(name='Взрослая_2', genre='Ужасы')
        assert collector.get_books_for_children() == ['Детская']

    # Тест 7. Метод add_book_in_favorites - книга добавляется в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

        collector.add_new_book('Тест')
        collector.add_book_in_favorites('Тест')
        assert 'Тест' in collector.favorites

    # Тест 8. Метод delete_book_from_favorites - книга удаляется из избранного
    def test_delete_book_from_favorites_deletes_book(self):
        collector = BooksCollector()

        collector.add_new_book('Тест')
        collector.add_book_in_favorites('Тест')
        collector.delete_book_from_favorites('Тест')
        assert 'Тест' not in collector.favorites

    # Тест 9. Метод get_list_of_favorites_books - можем получить список избранных книг
    def test_get_list_of_favorites_books_shows_list(self):
        collector = BooksCollector()

        collector.add_new_book('Тест_1')
        collector.add_book_in_favorites('Тест_1')
        collector.add_new_book('Тест_2')
        collector.add_book_in_favorites('Тест_2')
        assert collector.get_list_of_favorites_books() == ['Тест_1', 'Тест_2']

    # Тест 10. Метод add_new_book - можно добавить 1 символ и 40 символов
    @pytest.mark.parametrize('name', ['Я', 'Путешествия и приключения капитана Крюка'])
    def test_add_new_book_boundary_values_allowed(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert name in collector.books_genre

