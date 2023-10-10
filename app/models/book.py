
class Book :
    def __init__(self,bookId,bookName,authorId,price,journal) :
        self.bookId = bookId
        self.bookName = bookName
        self.authorId = authorId
        self.price = price
        self.journal = journal
    
    @staticmethod
    def fromTuple(books_tuple) :
        if len(books_tuple)==5 :
            bookId = books_tuple[0]
            bookName= books_tuple[1]
            authorId = books_tuple[2]
            price = books_tuple[3]
            journal = books_tuple[4]

            book = Book(bookId,bookName,authorId,price,journal)
            return book
        else :
            raise Exception("Value of the tuple Error")
             
    def to_dict(self) :
        return {
            "bookId" : self.bookId,
            "bookName" : self.bookName,
            "authorId" : self.authorId,
            "price" : self.price,
            "journal" : self.journal
        }