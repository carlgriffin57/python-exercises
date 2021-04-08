# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they 
# love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day 
# is 3 dollars, how much will you have to pay?
num_of_little_mermaid_days = 3
num_of_brother_bear_days = 5
num_of_hercules_days = 1
price_per_day = 3
total_price = (num_of_little_mermaid_days + num_of_brother_bear_days + num_of_hercules_days) * price_per_day
print(total_price, "dollars")

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different 
# rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in 
# payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_pay_per_hour = 400
amazon_pay_per_hour = 380
facebook_pay_per_hour = 350
total_payment = (google_pay_per_hour * 6) + (amazon_pay_per_hour * 4) + (facebook_pay_per_hour * 10)
print(total_payment, "dollars")

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict 
# with her current schedule.
class_full = True
conflicting_schedule = True
student_enrollment = not class_full or not conflicting_schedule
print(student_enrollment)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium 
# members do not need to buy a specific amount of products.
item_count = 3
offer_expired = False
premium_member = True
product_offer = (item_count > 2 and not offer_expired) or (premium_member and not offer_expired)
print(product_offer)

username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
password_length = len(password) >= 5
print(password_length)

# the username must be no more than 20 characters
username_length = len(username) < 21
print(username_length)

# the password must not be the same as the username
different = password != username
print(different)

# bonus neither the username or password can start or end with whitespace
bonus_answer = 
