class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)

    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of authors who have contracts for this book."""
        return list(set(contract.author for contract in self.contracts()))



class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books that the author has contracts for."""
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract object."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total amount of royalties the author has earned."""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []  # This should track all contract instances

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)  # Use Contract.all instead of all_contracts

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match the given date."""
        return [contract for contract in cls.all if contract.date == date]
