def func():  
     print("We are in first function")  
     def func1():  
           print("This is first child function")  
     def func2():  
           print(" This is second child function")  
     func1()  
     func2()  
func()  