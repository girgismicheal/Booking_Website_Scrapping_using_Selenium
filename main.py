from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

# Launch Chrome and go to the Booking.com search page
driver = webdriver.Chrome()
driver.get('https://www.booking.com')

# Enter search criteria for Hurghada hotels
search_box = driver.find_element(By.NAME, "ss")
search_box.send_keys('Hurghada')
search_box.submit()

# Wait for search results to load
driver.implicitly_wait(10)

# Scrape the hotel information for the first 10 search results
hotel_names = []
rating_scores = []
rating_values = []
num_reviews = []

results = driver.find_elements(By.XPATH, "//div[@class='fcab3ed991 a23c043802']")[:10]
for i in results:
    hotel_names.append(i.text)

results = driver.find_elements(By.XPATH, "//div[@class='b5cd09854e d10a6220b4']")[:10]
for i in results:
    rating_scores.append(i.text)

results = driver.find_elements(By.XPATH, "//div[@class='d8eab2cf7f c90c0a70d3 db63693c62']")[:10]
for i in results:
    rating_values.append(i.text)

results = driver.find_elements(By.XPATH, "//div[@class='b5cd09854e f0d4d6a2f5 e46e88563a']")[:10]
for i in results:
    num_reviews.append(i.text)

# Save the results to a CSV file
with open('booking.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Hotel Name', 'Rating Score', 'Rating Value', 'Number of Reviews'])
    for (hotel_name, rating_score, rating_value, num_review) in zip(hotel_names, rating_scores, rating_values, num_reviews):
        writer.writerow([hotel_name, rating_score, rating_value, num_review])

# Close the browser
driver.quit()