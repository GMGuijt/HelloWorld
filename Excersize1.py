#Break down the code into smaller functions
#Add descriptive docstrings to each function and type hints for your function

def linebreak(a):
    """schrijf na de ingevoerde tekst een lijn onder de tekst op de volgende regel. Je kan meerdere regels invoeren, maar scheid deze met een komma tussen de strings"""
    print(a,sep='\n') 
    print("--------------------")


file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)

total = sum(float(record['Grade']) for record in records)
average = total / len(records)

linebreak(f"Average Grade: {average}")

filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

linebreak("Student Report")
for record in filtered_records:
    linebreak(f"Name: {record['Name']}",f"Grade: {record['Grade']}")




