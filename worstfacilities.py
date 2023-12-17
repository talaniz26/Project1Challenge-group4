# Find the index of the row with the highest "Total Releases" value
max_release_index = select_col['Total Releases'].idxmax()

# Get the Facility name and Total Releases amount for the facility with the highest releases
facility_name_with_highest_releases = select_col.loc[max_release_index, 'Facility name']
highest_total_releases = select_col.loc[max_release_index, 'Total Releases']

# Print the result
print(f"The facility with the highest Total Releases is '{facility_name_with_highest_releases}' with a total release amount of {highest_total_releases} pounds.")

# Filter the DataFrame for facilities in the state of Texas (TX)
tx_facilities = select_col[select_col['State'] == 'TX']

# Find the index of the row with the highest "Total Releases" value in Texas
max_release_index_tx = tx_facilities['Total Releases'].idxmax()

# Get the Facility name and Total Releases amount for the facility with the highest releases in Texas
facility_name_highest_releases_tx = tx_facilities.loc[max_release_index_tx, 'Facility name']
highest_total_releases_tx = tx_facilities.loc[max_release_index_tx, 'Total Releases']

# Print the result
print(f"The facility in Texas with the highest Total Releases is '{facility_name_highest_releases_tx}' with a total release amount of {highest_total_releases_tx} pounds.")

# Find the difference in total releases between the highest overall and highest in Texas
difference_in_releases = highest_total_releases - highest_total_releases_tx

# Print the difference
print(f"The difference in total releases between the highest overall and highest in Texas is {difference_in_releases} pounds.")

# Calculate the percentage difference
percentage_difference = ((highest_total_releases - highest_total_releases_tx) / highest_total_releases_tx) * 100

# Determine which value is higher
higher_value = "highest overall" if highest_total_releases > highest_total_releases_tx else "highest in Texas"

# Print the result
print(f"The {higher_value} facility has {'higher' if highest_total_releases > highest_total_releases_tx else 'lower'} total releases.")
print(f"The percentage difference between the two facilities is {abs(percentage_difference):.2f}%.")


##The facility with the highest Total Releases is 'DELAWARE CITY REFINERY' with a total release amount of 4893579.0 pounds.
## The facility in Texas with the highest Total Releases is 'VALERO REFINING - TEXAS L.P. HOUSTON REFINERY' with a total release amount of 2057066.0 pounds.
## The difference in total releases between the highest overall and highest in Texas is 2836513.0 pounds.
## The highest overall facility has higher total releases.
## The percentage difference between the two facilities is 137.89%.