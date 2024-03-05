import csv
import io

class SurveyData:
    def __init__(self, data):
        """
        Initialize the SurveyData with CSV data.
        
        Parameters:
            data (str): Multiline string in CSV format.
        """
        self.data = data

    def parse_data(self):
        """
        Parses the CSV data string into a list of dictionaries, stripping whitespace from header names.
        """
        reader = csv.DictReader(io.StringIO(self.data))
        self.data = [{k.strip(): v for k, v in row.items()} for row in reader]

    def analyze_data(self, choice):
        """
        Analyzes data based on the user choice provided.

        Parameters:
            choice (str): The user's choice for data analysis.

        Returns:
            str or float: Result of the analysis or an error message.
        """
        if choice == '1':
            return self.average_price()
        elif choice == '2':
            return self.average_mileage()
        elif choice == '3':
            return self.count_evs()
        elif choice == '4':
            return self.most_popular_make()
        else:
            return "Invalid Choice"

    def average_price(self):
        """
        Calculates the average price of vehicles, including handling errors for missing or invalid data.

        Returns:
            str or float: The average price or an error message.
        """
        try:
            total_price = sum(int(row['Price'].replace(',', '')) for row in self.data)
            average = total_price / len(self.data)
            return f"Average Price: ${average:,.2f}"
        except KeyError:
            return "Price Data is NOT Available"
        except ValueError:
            return "Invalid Price Data"

    def average_mileage(self):
        """
        Calculates the average mileage of vehicles, including handling errors for missing or invalid data.

        Returns:
            str or float: The average mileage or an error message.
        """
        try:
            total_mileage = sum(int(row['Mileage']) for row in self.data)
            average = total_mileage / len(self.data)
            return f"Average Mileage: {average:,.0f} miles"
        except KeyError:
            return "Mileage Data NOT Available"
        except ValueError:
            return "Invalid Mileage Data"

    def count_evs(self):
        """
        Counts the number of electric vehicles (EVs) in the dataset.

        Returns:
            str or int: The count of EVs or an error message.
        """
        try:
            return sum(1 for row in self.data if row['Engine'] == 'EV')
        except KeyError:
            return "Engine Type Data NOT Available."

    def most_popular_make(self):
        """
        Determines the most popular make of vehicle in the dataset.

        Returns:
            str: The most popular make.
        """
        makes = {}
        for row in self.data:
            make = row['Make']
            if make in makes:
                makes[make] += 1
            else:
                makes[make] = 1
        return max(makes, key=makes.get)

def main():
    """
    Main function to run the survey data analysis. Prompts the user for choices and displays results.
    """
    # CSV data here...
    data = """Vehicle ID, Mileage, Year, Make, Engine, Seats, Price
ABC123,50000,2003,Toyota,Petrol,5,20000
XYZ456,70000,2005,Honda,Petrol,5,18000
DEF789,30000,2018,Ford,Diesel,5,23000
GHI012,20200,2021,Chevrolet,Diesel,5,25000
JKL345,60000,2022,Nissan,EV,5,19000
MNO678,45000,2020,Hyundai,EV,7,33000
PQR901,55000,2019,BMW,Hybrid,5,35000
STU234,65000,2017,Mercedes-Benz,Diesel,5,30000
VWX567,40000,2022,Jeep,Diesel,2,28000
YZA890,35000,2020,Subaru,Petrol,5,21000"""

    # Initialize and parse data
    survey_data = SurveyData(data)
    survey_data.parse_data()

    print("Welcome to the Vehicle Survey Data Analysis Tool!")
    print("Instructions: Choose an option to get insights from the vehicle data.")

    while True:
        print("\nOptions:")
        print("1 - Average Price (in Euro)")
        print("2 - Average Mileage (in KM’s)")
        print("3 - Count of Electric Vehicles (EVs)")
        print("4 - Most Popular Vehicle Make")
        print("0 - EXIT")
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Thank You, Good Bye!")
            break
        else:
            result = survey_data.analyze_data(choice)
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
