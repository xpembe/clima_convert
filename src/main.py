from conversion import Temperature


def main():
    convert = Temperature()
    temp_units = convert.conversion_units

    try:
        conversion = convert.choose_conversion("Choose conversion: ")

        # Prompt user which conversion should be entered by displaying its unit
        temp = float(input(f"Temperature in {temp_units[conversion][0]}: "))

        # Deciding which conversion to perform according to user choice
        if conversion == 1:
            result = convert.celsius_to_fahrenheit(temp)
        if conversion == 2:
            result = convert.fahrenheit_to_celsius(temp)
        if conversion == 3:
            result = convert.celsius_to_kelvin(temp)
        if conversion == 4:
            result = convert.kelvin_to_celsius(temp)
        if conversion == 5:
            result = convert.fahrenheit_to_kelvin(temp)
        if conversion == 6:
            result = convert.kelvin_to_fahrenheit(temp)

        # Display a final result of temperature with their units
        print(
            f"Temperature: {temp}{temp_units[conversion][0]}",
            f"= {result}{temp_units[conversion][-1]}",
        )
    except (ValueError, KeyError):
        print("Please enter the values as instructed and avoid using letters.")


# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
