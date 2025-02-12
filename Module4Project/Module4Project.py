# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        # Added three new seasonal drinks to Coffee Drinks
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Cold Press", "Latte", "Americano", "Cappuccino", 
                            "Iced Caramel Macchiato", "Peppermint Hot Chocolate", 
                            "Vanilla Bean Frappuccino"],  # Added new seasonal drinks
            "Breakfast": ["Bagel", "Muffin", "Scone", "Fruit Cup"],  # Added Fruit Cup
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Prices encapsulated within the class
        # Updated prices to match expected output
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Cold Press": 4.49, "Latte": 4.99, "Americano": 3.99, "Cappuccino": 4.99,
            "Iced Caramel Macchiato": 5.49, "Peppermint Hot Chocolate": 4.99, 
            "Vanilla Bean Frappuccino": 5.49,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99, "Fruit Cup": 3.49,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99,        
        }

        # Delivery locations and number of minutes to deliver to the location
        self.delivery_locations = {
            "Library": 10,  # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

        # Store delivery ratings
        self.delivery_ratings = []

    # New method for Part 2: Rate delivery feature
    def rate_delivery(self, rating):
        """Allows customers to rate their delivery from 1-5 stars"""
        try:
            rating = float(rating)
            if 1 <= rating <= 5:
                self.delivery_ratings.append(rating)
                print(f"\nThank you for your {rating}-star rating!")
                return True
            else:
                print("Please provide a rating between 1 and 5 stars.")
                return False
        except ValueError:
            print("Please enter a valid number between 1 and 5.")
            return False

    # New method for Part 2: Search by price feature
    def search_by_price(self, max_price):
        """Find all items under a specified price"""
        affordable_items = []
        print(f"\nItems under ${max_price:.2f}:")
        for item, price in self.prices.items():
            if price <= max_price:
                affordable_items.append(item)
                print(f"- {item}: ${price:.2f}")
        return affordable_items

    # Show the menu of items available for delivery
    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    # Updated method for Part 2: Added priority delivery option
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        """Calculate total cost including priority delivery option"""
        # Calculate the base total
        total = sum(self.prices[item] for item in items)
        
        # Add priority delivery fee if selected
        if priority_delivery:
            total += 2.0  # $2 extra for priority delivery
        
        # Apply student discount after delivery fee
        if has_student_id and total > 10:
            total *= 0.9
            
        return total

    # Updated method for Part 2: Added priority delivery timing
    def estimate_delivery(self, location, current_hour, priority=False):
        """Calculate delivery time, with option for priority delivery"""
        base_time = self.delivery_locations[location]
        
        # Add extra time during peak hours
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5
        
        # Reduce time for priority delivery
        if priority:
            base_time = max(2, base_time - 3)  # Ensure delivery time doesn't go below 2 minutes
            
        return base_time

    # Updated method for Part 2: Added priority delivery to receipt
    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        """Prints a nice receipt for the customer"""
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        
        if priority_delivery:
            print("Priority Delivery Selected (+$2.00)")
        
        print("\nItems ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)
        
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")
        
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

def main():
    # Create a new delivery object
    delivery = DunnDelivery()

    # Show menu
    delivery.show_menu("Coffee Drinks")

    # Sample order matching expected output
    order = ["Cold Press", "Bagel", "Fruit Cup"]
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True)

    # Demonstrate new features
    print("\n--- Additional Features Demo ---")
    
    # Demo price search
    delivery.search_by_price(5.00)
    
    # Demo delivery rating
    rating = input("\nPlease rate your delivery (1-5 stars): ")
    delivery.rate_delivery(rating)

    # Demo priority delivery
    print("\nPriority Delivery Order Example:")
    priority_order = ["Latte", "Muffin"]
    delivery.print_order("Library", priority_order, 9, has_student_id=False, priority_delivery=True)

if __name__ == "__main__":
    main()
    


    
