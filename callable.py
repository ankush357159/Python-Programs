class Product:
    def __init__(self):
        print("Instance created")

    def __call__(self, a,b):
        print(a * b)

ans = Product()

ans(10,20)