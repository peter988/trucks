import openpyxl
from .models import Product, Category 

def import_products_from_excel(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for idx, row in enumerate(sheet.iter_rows(min_row=3, values_only=True)):
            if idx < 58:
                category_name = row[4]
                no = row[3]
                description = row[2]
                price = int(row[5]) 
                title = f"{no} {category_name}"
                photo = None

                # Normalize category names
                if 'pressure' in category_name.lower():
                    category_name = 'Pressure Sensors'
                elif 'temperature' in category_name.lower():
                    category_name = 'Temperature Sensors'
                elif 'speed' in category_name.lower() or 'position' in category_name.lower():
                    category_name = 'Position and Speed Sensors'
                else:
                    if 'sensor' in category_name.lower():
                        category_name = 'Speciality Sensors'
                    else:
                        category_name = 'Mechanical Parts'
                        

                        # Get or create the category
                        category, _ = Category.objects.get_or_create(name=category_name)

                        # Create a Product
                        Product.objects.create(
                            title=title,
                            price=price,
                            description=description,
                            photo=photo,
                            category=category,
                        )

                        print(f"Added product: {title}")

        print("Successfully imported products!")

    except Exception as e:
        print(f"Error: {str(e)}")