#Break down the code into smaller functions
#Add descriptive docstrings to each function and type hints for your function

def linebreak(a):
    """schrijf na de ingevoerde tekst een lijn onder de tekst op de volgende regel. Je kan meerdere regels invoeren, maar scheid deze met een komma tussen de strings"""
    print(a,sep='\n') 
    print("--------------------")


def opencsv(name_of_array):
    """open een csv door middel van een array ervan te maken. De ingevoerde variabele is de naam van de variabele waaronder de gewenste array bekend komt te staan. Na het initialiseren wordt er gevraagd naar het pad naar, en de naam van, het gewenste bestand."""
    file_path = input("Enter the path to the CSV file: ")
    file_name = input("Enter the name of the CSV file: ") #voor deze opdracht was dit "r".
    name_of_array = []
    with open(file_path, file_name) as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name_of_array.append(row)
    return name_of_array


def average(kolomnaam,name_of_array):
    """bereken het gemiddelde van alle waarden in de ingevoerde kolom van een database. De eerste variabele is de kolomnaam die gesommeerd moet worden, de tweede de database waarin deze staat."""
    average = sum(float(record[kolomnaam]) for record in name_of_array) / len(name_of_array) #voor deze opdracht was de kolomnaam "Grade".
    linebreak(f"Average Grade: {average}")

def filter(filtered_array,name_of_array,cijfer):
    """filter de aangegeven database zodat alleen waardes overblijven waar het cijfer boven het aangegeven cijfer is. De eerste input is de variabele waaronder deze nieuwe lijst komt, de tweede is de array die gefilterd wordt en de derde is het cijfer waarop gefilterd word."""
    filtered_array = [record for record in name_of_array if float(record['Grade']) >= cijfer] #cijfer was hier eerst 80.0
    return filtered_array
    

def student_report(name_of_array):
    """schrijf de namen en de cijfers van elke student in de opgegeven array."""
    linebreak("Student Report")
    for record in name_of_array:
        linebreak(f"Name: {record['Name']}",f"Grade: {record['Grade']}")

#file_path = input("Enter the path to the CSV file: ")
#records = []
#with open(file_path, 'r') as file:
#    csv_reader = csv.DictReader(file)
#    for row in csv_reader:
#        records.append(row)

#average = sum(float(record['Grade']) for record in records) / len(records)
#linebreak(f"Average Grade: {average}")

#filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

#linebreak("Student Report")
#for record in filtered_records:
#    linebreak(f"Name: {record['Name']}",f"Grade: {record['Grade']}")



#gesugereerde oplossing die in main moet

#opencsv(records)

#average('Grade',records)

#filter(filtered_records,records,80.0)

#student_report(filteref_records)