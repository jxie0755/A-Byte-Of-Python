passphrase = "CC74EB"

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    "3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead"
    """
    import hashlib
    return hashlib.sha224(p.encode("utf-8")).hexdigest()



# Q1 Next Fibonacci Object
class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            N = Fib(1)
        else:
            N = Fib(self.prev + self.value)

        N.prev = self.value
        return N

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine("candy", 10)
    >>> v.vend()
    "Machine is out of stock."
    >>> v.deposit(15)
    "Machine is out of stock. Here is your $15."
    >>> v.restock(2)
    "Current candy stock: 2"
    >>> v.vend()
    "You must deposit $10 more."
    >>> v.deposit(7)
    "Current balance: $7"
    >>> v.vend()
    "You must deposit $3 more."
    >>> v.deposit(5)
    "Current balance: $12"
    >>> v.vend()
    "Here is your candy and $2 change."
    >>> v.deposit(10)
    "Current balance: $10"
    >>> v.vend()
    "Here is your candy."
    >>> v.deposit(15)
    "Machine is out of stock. Here is your $15."

    >>> w = VendingMachine("soda", 2)
    >>> w.restock(3)
    "Current soda stock: 3"
    >>> w.restock(3)
    "Current soda stock: 6"
    >>> w.deposit(2)
    "Current balance: $2"
    >>> w.vend()
    "Here is your soda."
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0

    def restock(self, added):
        self.stock += added
        return f"Current {self.product} stock: {self.stock}"


    def vend(self):
        if self.stock:
            if self.balance >= self.price:
                self.stock -= 1
                change = self.balance - self.price
                self.balance = 0
                if change != 0:
                    return f"Here is your {self.product} and ${change} change."
                else:
                    return f"Here is your {self.product}."
            else:
                return f"You must deposit ${self.price - self.balance} more."
        else:
            return "Machine is out of stock."


    def deposit(self, deposit):
        if self.stock:
            self.balance += deposit
            return f"Current balance: ${self.balance}"
        else:
            return f"Machine is out of stock. Here is your ${deposit}."
