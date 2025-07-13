# Python Crash Course, 2Ed, writtern by Eric Matthes

countries = ["Deutsch", "Japan", "Great Britain", "Taiwan"]

print(f"Countries I want to go: {countries}.")

countries_sorted = countries
countries_sorted.sort()
print(f"Countries I want to go: {countries_sorted}.")
countries_sorted_reverse = countries
countries_sorted_reverse.sort(reverse=True)
print(f"Countries I want to go: {countries_sorted_reverse}.")
print(f"Countries I want to go: {sorted(countries)}.")
countries_reversed = countries
countries_reversed.reverse()
print(f"Countries I want to go: {countries_reversed}.")
