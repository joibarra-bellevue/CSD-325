"""Jorge Ibarra
CSD 325 Module 7.2 Assignment
2/4/2026"""

# Function with optional population and optional language
def format_city_country(city, country, population=None, language=None):
   
    result = city + ", " + country

    if population is not None:  # Include population if provided
        result += " - population " + str(population)

    if language:  # Include language if provided
        if population is not None:
            result += ", " + language
        else:
            result += ", " + language

    return result


print(format_city_country("Santiago", "Chile", 5000000, "Spanish"))# Full info
print(format_city_country("Sydney", "Australia", 5300000))  # No language
print(format_city_country("Mexico City", "Mexico", language="Spanish"))  # No population
print(format_city_country("Tokyo", "Japan"))  #No population, no language