from auth_controller.App_Auth import Auth
from model.Book import Book
from auth_controller import App_Auth
from model.Client import Client
from model.Librarian import Librarian
from model.Order import Order
from utils.utils import App_utils, Constants


at = Auth()





print("welcome \n for client enter C\n for a librarian enter L ")
user_type=input("write your type:")
App_utils.check_input_is_empty(user_type)

if user_type!="C" and user_type!="L":
    print("error")

if user_type=="C":
     print("enter 1 to log in\nenter 2 to register")
     log_type=input(":")
     if log_type != "1" and log_type != "2":
         print("error")
     App_utils.check_input_is_empty(log_type)


     if log_type=="1":
      log_client_full_name=input("write your full name:")
      log_client_id=input("write your id:")
      App_utils.check_input_is_digit(log_client_full_name)
      if at.login_Client(log_client_full_name, log_client_id):
          pass
      else:
          print("you entered a wrong name or id")
          exit()
      App_utils.check_input_is_empty(log_client_full_name,log_client_id)


     if log_type=="2":
      full_name=input("write your full name:")
      age =input("write your age:")
      phone_number =input("write your phone number:")
      id_no=input("write your id number:")
      App_utils.check_input_is_digit(full_name)
      App_utils.check_input_is_empty(full_name, age,phone_number,id_no)

      at.register_client(Client(full_name = full_name,age = age,phone_number = phone_number,id_no=id_no,id= int(at.get_client_last_id())+1))
      print(" your id number is ",str(at.get_client_last_id()))



     client_operation=input("you can choose one of this three options \n1- borrow  book\n2- your  orders \n3-return  book\n write your option:")
     App_utils.check_input_is_empty(client_operation)
     if client_operation == "1" or client_operation == "borrow  book":
        print(" this is the list of the books that you can borrow")
        print("book id, book tittle ")
        at.display_books_list_for_client()
        borrowed_book_id=input("write the the book id:")
        client_id=input("write your id:")
        date=input("write the date:")
        librarian_id=input("write the  librarian id:")
        App_utils.check_input_is_empty(borrowed_book_id,client_id,date,librarian_id)
        at.check_client_exist(client_id=client_id)
        at.check_librarian_exist(librarian_id=librarian_id)
        at.check_book_is_avalibalee(book_id=borrowed_book_id)
        at.new_order(Order(book_id=borrowed_book_id,client_id=client_id,date=date,librarian_id=librarian_id,status=Constants.order_active,id=int(at.get_order_last_id())+1))
        at.change_status_to_inactive(book_id=borrowed_book_id)



        print(" your order done successfully \n here is your order id ", at.get_order_last_id())

     if client_operation=="2" or client_operation=="your  orders":
        client_id=input("write your id")
        client_name=input("write your full name")
        App_utils.check_input_is_digit(client_name)
        App_utils.check_input_is_empty(client_id,client_name)
        if at.login_Client(client_name, client_id):
            pass
        else:
            print("you entered wrong name or id")
            exit()
        at.check_client_exist(client_id=client_id)
        print("order id , client id ,librarian id,book id,status(3'active' 4'expired' 5'canceled'),date")
        at.display_client_orders(client_id=client_id)






     if client_operation=="3" or client_operation=="return  book":
        order_id=input("write the order id: ")
        client_id= input("write your id:")
        book_id=input("write the book id ")
        App_utils.check_input_is_empty(order_id,client_id,book_id)
        at.check_order_exist(order_id=order_id)
        at.check_order_is_active(order_id=order_id)
        at.check_book_is_borrowed(book_id=book_id)
        at.change_status_to_expired(order_id=order_id)
        at.change_status_to_active(book_id=book_id)
        print(" done sucessfully")










if user_type=="L":
    print("enter 1 to log in\nenter 2 to register")
    log_type = input("write here:")
    if log_type != "1" and log_type != "2":
        print("error")
    App_utils.check_input_is_empty(log_type)

    if log_type=="1":
        librarian_full_name=input("write your full name:")
        librarian_id=input("write your id:")
        App_utils.check_input_is_digit(librarian_full_name)
        if at.login_librarian(librarian_full_name,librarian_id):
            pass
        else:
            print("you entered wrong name or id")
            exit()
        if App_utils.check_input_is_empty(librarian_id,librarian_full_name):
            pass
    if log_type=="2":
        librarian_full_name = input("write your full name:")
        age = input("write your age:")
        employment_type=input('write your employment type (enter 1 to full time ,enter 2 to part time)')
        App_utils.check_input_is_digit(librarian_full_name)
        if employment_type=="1":
            emp_type=Constants.full
        elif employment_type=="2":
            emp_type=Constants.part
        else:
            print("you entered wrong employment type")
            exit()

        id_no = input("write your id number:")
        App_utils.check_input_is_empty(librarian_full_name, age, employment_type, id_no)

        at.register_librarian(Librarian(full_name= librarian_full_name, age=age,id_no=id_no,employment_type=emp_type,id=int(at.get_librarian_last_id()) + 1))
        print(" your id number is", str(at.get_librarian_last_id()))


    librarian_operation=input("you can choose one of this four options\n1- display all books\n2- add  new book\n3- display all  orders\n4- display all clients\nwrite here:")
    App_utils.check_input_is_empty(librarian_operation)
    if librarian_operation=="1"or librarian_operation=="display all books":
       print("this is all the books")
       at.show_books_()

       second_librarian_operation=input("1- search for a  book\n2- leave\nwrite here:")
       App_utils.check_input_is_empty(second_librarian_operation)
       if second_librarian_operation=="1" or second_librarian_operation=="search for a  book":
          book_id=input("write the book id:")
          App_utils.check_input_is_empty(book_id)
          if at.check_book_exist(book_id=book_id):
               pass
          else:
               print("the book doesnt exist")
               exit()
          print("book id , book tittle ,   description   , status(1'active',0'inactive'),author")
          at.display_book_details(book_id=book_id)
       elif second_librarian_operation=="2" or second_librarian_operation=="leave":
           exit()
       else:
           print(" you entered wrong data")
           exit()
    if librarian_operation=="2" or librarian_operation=="add new book":
       book_tittle=input("write  book tittle:")
       book_description=input("write  book description:")
       book_author=input("write  book author:")
       App_utils.check_input_is_digit(book_author,book_description,book_tittle)
       App_utils.check_input_is_empty(book_author,book_description,book_author)
       at.add_new_book(Book(tittle=book_tittle,description=book_description,author=book_author,status=Constants.book_active,id=int(at.get_book_last_id())+1))
       print(" done successfully , this is the new book id ",at.get_book_last_id())
    if librarian_operation=="3" or librarian_operation=="display all orders":
        print("order id, client id, librarian id, book id, status(3'active'4'expired'5'canceled' , date")
        at.display_orders()
        second_librarian_operation=input("1- search for  order\n2-leave\nwrite here:")
        App_utils.check_input_is_empty(second_librarian_operation)
        if second_librarian_operation=="1"or second_librarian_operation=="search for  order":
           order_id=input("write  order id:")
           at.check_order_exist(order_id=order_id)
           print("order id, client id, librarian id, book id, status(3'active'4'expired'5'canceled' , date")
           print(at.display_order(order_id=order_id))
        elif second_librarian_operation == "2" or second_librarian_operation == "exit":
            exit()
        else:
            print("you entered wrong data")
            exit()
    if librarian_operation=="4" or librarian_operation=="display all clients":
        print(" id,    name    ,  age , id number , phone number")
        at.display_clients()
        second_librarian_operation = input("1- search for  client\n2-leave\nwrite here:")
        App_utils.check_input_is_empty(second_librarian_operation)
        if second_librarian_operation=="1"or second_librarian_operation=="search for  client":
            client_id=input("write  client id:")
            App_utils.check_input_is_empty(client_id)
            at.check_client_exist(client_id=client_id)
            print(" id,    name    ,  age , id number , phone number")
            print(at.display_client(client_id=client_id))
        elif second_librarian_operation== "2" or second_librarian_operation== "leave":
            exit()
        else:
            print("you entered wrong dat")
            exit()
