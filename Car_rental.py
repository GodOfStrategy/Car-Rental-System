class car:
    def __init__(self,numberPlate,company,model,color):
        self.numberPlate=numberPlate
        self.company=company
        self.model=model
        self.color=color
class customer:
    def __init__(self,name,phone,customer_id):
        self.name=name
        self.phone=phone
        self.customer_id=customer_id
        self.rental_history=[]
class rental:
    def __init__(self):
        self.car=[]
        self.customer=[]
    def add_car(self,numberPlate,company,model,color):
        new_car=car(numberPlate,company,model,color)
        self.car.append(new_car)
        print(f"Car{self.company}{self.model} added with number plate{self.numberPlate}")
    def add_customer(self,name,customer_id):
        new_customer=customer(name,customer_id)
        self.customer.append(new_customer)
        print(f"Customer{self.name} added with ID{self.customer_id}")

    def rent_car(self,customer_id,numberPlate):
        for customer in self.customers:
            if customer.customer_id==customer_id:
                for car in self.car:
                    if car.numberPlate==numberPlate:
                        customer.rental_history.append(car)
                        self.car.remove(car)
                        print(f"Car{car.company}{car.model} rented by {customer.name}")

            else:
                print(f"Customer with I{customer_id} not found")
                add_customer()
    def return_car(self,customer_id,numberPlate):
        for customer in self.customer
        if customer.custoer_id==customer_id:
            for car in customer.rental_history:
                if car.numberPlate==numberPlate:
                    customer.rental_history.remove(car)
                    self.car.append(car)
                    print(f"car {car.company}{car.model} returned by {customer.name}")
                else:
                    print("Car is not in our fleet")
        else:
            print(f"Customer with ID{customer_id} not found")

    def view_rental_history(self,customer_id):