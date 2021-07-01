class Train():  # create a class 
    # def init function and pass the variable what you required to book the ticket like train name , soucre ,seats, etc.
    def __init__(self,train_name,train_no,source,destination,status,seats,seatNo): 
        self.seats=seats
        self.train_no=train_no
        self.train_name= train_name
        self.source=source
        self.destination=destination
        self.status=status
        self.seatNo = seatNo

    # Create the fuction to book ticket
    def bookTrain(self):
        print(f'Train name {self.train_name} and No is {self.train_no}')
        print(f'Booking form  {self.source}')
        print(f'To {self.destination}')
    
    # Create the function to check the status of train seats is available or not
    def getStatusOfTrain(self):
        print(f'Status of the train is {self.status}')
    
    # Create a function to maintain Booking status
    def bookingStatusOfTicket(self):
        if self.seats > 0:
            print(f'No. of seats available {self.seats}')
            self.seats=self.seats-1
        else:
            print(f'Seats is available {self.seats} you can try for another train or date')
    def cancelTicket(self,seatNo):
        self.seatscancel= seatNo
        print(f'{self.seatNo} ticket  canceled')

ticket=Train('Ayodhya Express',1234,'LTT','Ayodhya','confirm',3,1)
ticket.bookTrain()
ticket.bookingStatusOfTicket()
ticket.bookingStatusOfTicket()
ticket.cancelTicket(1)
ticket.bookingStatusOfTicket()
ticket.getStatusOfTrain()