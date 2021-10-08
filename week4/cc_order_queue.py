class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops >= 1 and scoops <= 3:
            print("Order created!")
        elif flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
        elif scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print('\nAll Pending Ice Cream Orders:')
        for customer in self.orders.items:
            # customer_data = f"Customer: {customer['customer']} -- Flavor: {customer['flavor']} -- Scoops: {customer['scoops']}"
            if customer['flavor'] in self.flavors and customer['scoops'] >= 1 and customer['scoops'] <= 3:
                customer_data = f"Customer: {customer['customer']} -- Flavor: {customer['flavor']} -- Scoops: {customer['scoops']}"
                print(customer_data)

    def next_order(self):
        print('\nNext Order Up!')
        customer = self.orders.dequeue()
        print(
            f"Customer: {customer['customer']} -- Flavor: {customer['flavor']} -- Scoops: {customer['scoops']}"
        )


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
