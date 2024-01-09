class SurveyData:
  def __init__(self, data):
    self.data = data

  def import_data(self, file_path):
      pass

  def parse_data(self):
      pass

  import csv

  def import_data(self, file_path):
    with open(file_path, 'r') as file:
      reader = csv.reader(file)
      self.data = [row for row in reader]

  def analyze_data(self):
    insights ={}
    return insights

  def export_results(insights, export_path):
    with open(export_path, 'w') as file:
      for key, value in insights.items():
        file.write(f"{key}: {value}\n")
        







# Write your code to expect a terminal of 80 characters wide and 24 rows high
