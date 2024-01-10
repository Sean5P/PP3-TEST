import csv
import io


class SurveyData:
    def __init__(self, data):
        self.data = data

    def parse_data(self):
        """
        Convert CSV Data String to List of Dictionaries.
        """
        reader = csv.DictReader(io.StringIO(self.data))
        self.data = [row for row in reader]

    def analyze_data(self, choice):
        """
        Analyse Data Based on User Choice.
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
        total_price = sum(int(row['Price'].replace(',', '') for row in self.data)
        return total_price / len(self.data)

    def average_mileage(self):
        total_mileage = sum(int(row['Mileage']) for row in self.data)
        return total_mileage / len(self.data)

    def count_evs(self):
        return sum(1 for row in self.data if row['Engine'] == 'EV')

    def most_popular_make(self):
        makes = {}
        for row in self.data:
            make = row['Make']
            if make in makes:
                makes[make] += 1
            else:
                makes[make] = 1
        return max(makes, key=makes.get)


def main():
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

    survey_data = SurveyData(data)
    survey_data.parse_data()

    while True:
        print("\nChoose an Insight to View:")
        print("1 - Average Price")
        print("2 - Average Mileage")
        print("3 - Count of EVs")
        print("4 - Most Popular Make")
        print("0 - EXIT")
        choice = input("Enter your choice: ")

        if choice == '0':
            break
        else:
            result = survey_data.analyze_data(choice)
            print(f"Result: {result}")


if __name__ == "__main__":
    main()


# Write your code to expect a terminal of 80 characters wide and 24 rows high
