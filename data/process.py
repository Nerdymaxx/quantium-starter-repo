import _csv

file_path=["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]
processed_data =[]
output_file = "processed_data.csv"
def read_data(file_path):
    for file in  file_path:
        with open(file, newline = '' ) as csvfile:
            reader =_csv.reader(csvfile)
            for row in reader:
                processed_data.append(row)
read_data(file_path)

def filter_data(processed_data, value):
     
    filtered_data = []
    numbers = []
    for row in processed_data: 
       
        if row[0].lower() == value.lower():
            price = row[1].replace("$", "")
            price = float(price)

            quantity = int(row[2])
            
            
            sales = price * quantity
            numbers.append(sales)
   
            filtered_data.append(row)
            # print(f"Sales for {row[0]} on {row[3]} ${sales:.2f}")
    
    return filtered_data
filter_data(processed_data, "pink morsel") 

def write_to_csv(filtered_data, output_file):
    with open(output_file, mode = 'w', newline="") as csv_output:
        writer = _csv.writer(csv_output)
        writer.writerows(filtered_data)
    if writer:
        print("Data written to CSV successfully.")
    else:        print("Failed to write data to CSV.")

write_to_csv(filter_data(processed_data, "pink morsel"), output_file)
        

             
