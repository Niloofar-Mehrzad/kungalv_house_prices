import os
from bs4 import BeautifulSoup
import csv

# Path to the folder containing the extracted HTML files
html_folder_path = "C:/Users/kungalv_slutpriser/" 

# Path to save the output CSV
csv_file_path = "C:/Users/kungalv_house_prices.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow([
        "Date of Sale", "Address", "Location", 
        "Boarea (m2)", "Biarea (m2)", "Totalarea (m2)", 
        "Number of Rooms", "Plot Area (m2)", "Closing Price (kr)"
    ])
    
    # Loop through all HTML files in the folder
    for filename in os.listdir(html_folder_path):
        if filename.endswith(".html"):  # Process only HTML files
            file_path = os.path.join(html_folder_path, filename)
            
            # Open and parse the HTML file
            with open(file_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
                
                # Extract data from the file
                try:
                    date_of_sale = soup.find("span", class_="hcl-label hcl-label--state hcl-label--sold-at").text.split('Såld ')[1]
                except AttributeError:
                    date_of_sale = None
                
                try:
                    address = soup.find("h2", class_="sold-property-listing__heading qa-selling-price-title hcl-card__title").text.split()
                except AttributeError:
                    address = None
                
                try:
                    location = soup.find("span", class_="property-icon property-icon--result").text.strip()
                except AttributeError:
                    location = None
                
                try:
                    area_text = soup.find("span", class_="area").text.strip()
                    areas = area_text.split("+") if area_text else [None, None]
                    boarea = areas[0].strip() if len(areas) > 0 else None
                    biarea = areas[1].strip() if len(areas) > 1 else None
                    totalarea = int(boarea) + int(biarea) if boarea and biarea else None
                except AttributeError:
                    boarea = biarea = totalarea = None
                
                try:
                    number_of_rooms = soup.find("span", class_="rooms").text.strip()
                except AttributeError:
                    number_of_rooms = None
                
                try:
                    plot_area = soup.find("span", class_="plot-area").text.strip()
                except AttributeError:
                    plot_area = None
                
                try:
                    closing_price = soup.find("span", class_="price").text.strip()
                except AttributeError:
                    closing_price = None
                
                # Write the data to the CSV
                writer.writerow([
                    date_of_sale, address, location, boarea, biarea, totalarea, 
                    number_of_rooms, plot_area, closing_price
                ])

print(f"Data extraction complete! CSV saved at: {csv_file_path}")
