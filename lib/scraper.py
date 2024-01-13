from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://moringaschool.com/our-courses/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# Use a try-except block to handle the possibility of no matching elements
try:
    # Use .select_one instead of .select to get only the first matching element
    course = doc.select_one('.heading-60-black.color-black.mb-20')

    if course:
        print(course.contents[0].strip())
    else:
        print("No matching elements found.")
except IndexError as e:
    print(f"Error: {e}")
