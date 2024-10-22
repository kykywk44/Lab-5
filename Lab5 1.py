class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = str(year)
    def get_info(self):
        print(f"Название книги: {self.title} \nАвтор: {self.author} \nГод выпуска: {self.year} год")

book1 = Book('Обломов', 'И.С.Тургенев', 1859)
book2 = Book('Гарри Поттер и философский камень', 'Дж.К.Роулинг', 1997)

book1.get_info()