class MyCalendarTwo:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


myCalendarTwo = MyCalendarTwo()
myCalendarTwo.book(10, 20) # return True, The event can be booked. 
myCalendarTwo.book(50, 60) # return True, The event can be booked. 
myCalendarTwo.book(10, 40) # return True, The event can be double booked. 
myCalendarTwo.book(5, 15) # return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10) # return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55) # return True, The event can be booked, as the time in [25, 40) 
                        # will be double booked with the third event, the time [40, 50) will be 
                        # single booked, and the time [50, 55) will be double booked with the second event.