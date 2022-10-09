class Constants:
    full  = 1
    part = 2
    book_active = 1
    book_inactive = 0
    order_active = 3
    order_expired = 4
    order_canceled = 5


class App_utils:

    @staticmethod
    def check_input_is_empty(*input):
        for item in input:
            if item.isspace() or item=="":
                print("empty input")
                exit()
            else :
                pass

    @staticmethod
    def check_input_is_digit(*input):
        for item in input:
            if str(item).isdigit():
                print("wrong input,please try again")
                exit()

