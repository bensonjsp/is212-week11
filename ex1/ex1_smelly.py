class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

        # Step 2: Calculate total price
        total_price = self.calculate_total_price(order)

        # Step 3: Apply discounts if applicable
        if order.get("discount_code") == "SUMMER20":
            total_price *= 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            total_price *= 0.9  # 10% discount

        # Step 4: Update inventory
        self.update_inventory(order)

        # Step 5: Generate receipt
        receipt = self.generate_receipt(order, total_price)

        # Step 6: Send confirmation email
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt

    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def calculate_total_price(self, order):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price

