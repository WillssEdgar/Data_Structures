'''
Implements a FIFO Queue, a Priority Queue, and a Sorted Queue

Classes:
    FIFOQueue
'''


class fifoqueue:
    '''
    Implements a FIFO Queue

    Functions:
        __init__(self)
        enqueue(self, any type)
        dequeue(self) -> any type
        peek(self) -> any type
        find(any type) -> any type
        index(self, any type) -> int
        remove(self, any type)
        __len__(self) -> int
        isEmpty(self) -> boolean
        __str__(self) -> string
        newIterator -> QueueIterator

    '''

    def __init__(self):
        '''
        Constructor - initializes the queue to be empty

        Parameters:
            None

        Returns:
            None
        '''
        self.queue = []

    def enqueue(self, x):
        '''
        Enqueues the value x at the end of the line.

        Parameters:
            x: any value

        Returns:
            None
        '''

        self.queue.append(x)

    def dequeue(self):
        '''
        Removes and returns the value at the front

        Parameters:
            None

        Returns:
            the value: any type
        '''
        valueAtFront = self.queue[0]
        if self.isEmpty() != True:

            self.queue.pop(0)
            return ("Value that was removed " + str(valueAtFront) +
                    ". New value at the front " + str(self.queue[0]) + ".")
        else:
            return "The queue is Emtpy"

    def peek(self):
        '''
        Returns (BUT DOES NOT REMOVE) the value at the front

        Parameters:
            None

        Returns:
            the value: any type
        '''
        return self.queue[0]

    def find(self, x):
        '''
        Finds the first occurrence of x in the queue.  It is assumed that
        the equals operator (==) can be applied to the values in the queue.

        Parameters:
            x: any value

        Returns:
            that payload that matches or None if the value is not found: any type
        '''
        for i in self.queue:
            if i == x:
                return i
            else:
                return None

    def index(self, x):
        '''
        Finds the first occurrence of x in the list and returns its index.
        It is assumed that the equals operator (==) can be applied to the
        values in the list. The value at the front is at index 0.

        Parameters:
            x: any value

        Returns:
            the index of the first payload that matches or -1 if
            the value cannot be found: int
        '''
        count = 0
        for i in self.queue:
            if i == x:
                return count
            else:
                count += 1
        return -1

    def remove(self, x):
        '''
        Removes the first occurrence of the value from the list
        It is assumed that the equals operator (==) can be applied to the
        values in the list. If the value is not found, nothing is removed.
        Parameters:
            x: any type
        Returns:
            None
        '''
        try:
            self.queue.remove(x)
        except ValueError:
            pass

    def isEmpty(self):
        '''
        Checks to see if the queue is empty

        Parameters:
            None

        Returns:
            boolean
        '''
        if len(self.queue) == 0:
            return True
        else:
            return False

    def __str__(self):
        '''
        Returns a string of the values in the queue. This overloads the str()
        operator so that you can do things like print(myQueue). It is
        assumed that each value in the list also can be converted to a string
        by using str(value).

        Parameters:
            None

        Returns:
            string
        '''
        result = []
        if self.isEmpty():
            return "The queue is Emtpy"
        else:
            return f"{self.queue}"
