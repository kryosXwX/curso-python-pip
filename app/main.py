import utils
import read_csv
import charts
import pandas


def run():
  data = read_csv.read_csv('/home/josh/py-project/app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  chart_name = input('Enter the name of the first chart:')
  chart_name2 = input('Enter the name of the second chart:')
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(chart_name, countries, percentages)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(chart_name2, labels, values)


if __name__ == '__main__':
  run()

