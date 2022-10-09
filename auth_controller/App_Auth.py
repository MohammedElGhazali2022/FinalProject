from model.Book import Book
from model.Client import Client
from model.Librarian import Librarian
from model.Order import Order
from utils.utils import App_utils, Constants





class Auth:

    librarian_list : list[Librarian]=[Librarian(full_name="Ali Elghazali",id="1", employment_type=Constants.full,age="20",id_no="987654"),
                                      Librarian(full_name="omar Elghazali",id="2", employment_type=Constants.full,age="30",id_no="456789"),
                                      Librarian(full_name="mohammed Elghazali",id="3", employment_type=Constants.part,age="40",id_no="123456"),
                                      ]
    client_list : list[Client]=[Client(id="1",full_name="Ahmed Ali",age="25",id_no="147852",phone_number="0599123456"),
                                Client(id="2",full_name="khaled Rami",age="20",id_no="258963",phone_number="0599654321"),
                                Client(id="3",full_name="saif Amjad",age="29",id_no="789123",phone_number="0598123456"),
                                ]
    books_list: list[Book]=[Book(tittle="Paython", id="1",author="Saleh",status=Constants.book_active,description="( Learn Paython Language)"),
                           (Book(tittle="computer", id="2", author="Maher", status=Constants.book_active,description=" (Learn Computer Skills)")),
                            Book(tittle="Arabic", id="3", author="Majed", status=Constants.book_active,description="(Learn Arabic Grammer)"),
                            Book(tittle="Math",id="4",author="Monzer",status=Constants.book_inactive,description="(Learn Math skills)"),
                            Book(tittle="Sport",id="5",author="Medhat",status=Constants.book_inactive,description="(Type of sports)"),
                            Book(tittle="Islamic",id="6",author="Hatem",status=Constants.book_inactive,description="(Learn Islamic Rules)")]
    orders_list :list[Order]=[Order(id="1",date="01/01/2022",client_id="2",book_id="5",status=Constants.order_expired,librarian_id="2"),
                              Order(id="2",date="01/02/2022",client_id="3",book_id="6",status=Constants.order_active,librarian_id="1"),
                              Order(id="3",date="01/03/2022",client_id="2",book_id="3",status=Constants.order_active,librarian_id="3")]

    def login_librarian(self,full_name:str,id:str) -> bool:
        for item in self.librarian_list:
            if item.get_id() == id and item.get_full_name() ==full_name:
                return True
            else:
                pass

    def login_Client(self,full_name:str, id:str) -> bool:
        for item in self.client_list:
            if item.get_id()==id and item.get_full_name()==full_name:
                return True
            else:
                pass

    def register_client(self,client:Client):
        self.client_list.append(client)

    def register_librarian(self, librarian: Librarian):
            self.librarian_list.append(librarian)

    def get_client_last_id(self) -> int:
       return self.client_list[len(self.client_list) - 1 ].get_id()

    def get_librarian_last_id(self)-> int:
        return self.librarian_list[len(self.librarian_list)-1].get_id()
    def display_books_list_for_client(self):
        for item in self.books_list:
            if item.get_Book_status() == Constants.book_active:
                print(item.get_Book_id(), item.get_Book_tittle())
        else:
            pass

    def show_books_(self):
        for item in self.books_list:
            print(item.get_Book_id(), item.get_Book_tittle())


    def new_order(self,order:Order):
        self.orders_list.append(order)
    def check_client_exist(self,client_id) :
        for item in self.client_list:
            if int(client_id)==int(item.get_id()):
                return True
        else:
               print("you entered wrong client id")
               exit()

    def check_librarian_exist(self,librarian_id):
        for item in self.librarian_list:
             if librarian_id == item.get_id():
                break
        else:
                 print("you entered wrong librarian id ")
                 exit()

    def get_order_last_id(self) -> int:
        return self.orders_list[len(self.orders_list) - 1].get_id()

    def check_book_is_avalibalee(self,book_id):
        for item in self.books_list:
            if book_id == item.get_Book_id() and item.get_Book_status() == Constants.book_active:
                break
        else:
                 print("you entered wrong book id ")
                 exit()

    def change_status_to_inactive(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id and item.get_Book_status() == Constants.book_active:
                item.set_Book_status(Constants.book_inactive)
    def change_status_to_expired(self,order_id):
        for item in self.orders_list:
            if item.get_id()== order_id:
                item.set_status(Constants.order_expired)
    def change_status_to_active(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id and item.get_Book_status() == Constants.book_inactive:
                item.set_Book_status(Constants.book_active)
    def check_order_is_active(self,order_id):
        for item in self.orders_list:
            if item.get_id()== order_id:
                if item.get_status()==Constants.order_active:
                    break
                else:
                    print("the order is not active")
                    exit()
    def check_book_is_borrowed(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id and item.get_Book_status() == Constants.book_inactive:
                break
        else:
                print("the book is not borrowed")
                exit()
    def display_client_orders(self,client_id):
        for item in self.orders_list:
            if item.get_client_id()== client_id:
               print(item)
            else:
                pass
    def check_order_exist(self,order_id):
        for item in self.orders_list:
            if item.get_id()==order_id:
                break
        else:
            print("order not found")
            exit()
    def librarian_book(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id:
                print(item)

    def check_book_exist(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id:
                return True
        else:
            return False

    def display_book_details(self,book_id):
        for item in self.books_list:
            if item.get_Book_id() == book_id:
                print(item)

    def add_new_book(self,book : Book):
        self.books_list.append(book)



    def get_book_last_id(self)->int:
        return self.books_list[len(self.books_list)-1].get_Book_id()
    def display_orders(self):
        for item in self.orders_list:
            print(item)
    def display_order(self,order_id):
        for item in self.orders_list:
            if item.get_id()==order_id:
                return item
    def display_clients(self):
        for item in self.client_list:
            print(item)
    def display_client(self,client_id):
        for item in self.client_list:
            if item.get_id()==client_id:
                return item


