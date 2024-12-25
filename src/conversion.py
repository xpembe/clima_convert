class Temperature:
    """Operation class for simple temperature conversions"""

    # Temperature conversion units
    conversion_units = {
        1: ["°C", "°F"],
        2: ["°F", "°C"],
        3: ["°C", "K"],
        4: ["K", "°C"],
        5: ["°F", "K"],
        6: ["K", "°F"],
    }

    def _available_conversions(self):
        """Display the available conversions"""
        template = """
        1. Celsius to Fahrenheit
        2. Fahrenheit to Celsius
        3. Celsius to Kelvin
        4. Kelvin to Celsius
        5. Fahrenheit to Kelvin
        6. Kelvin to Fahrenheit
        """
        print(template)

    def celsius_to_fahrenheit(self, temp_celsius):
        """Convert celsius to fahrenheit temperature"""
        return temp_celsius * (9 / 5) + 32

    def fahrenheit_to_celsius(self, temp_fahrenheit):
        """Convert fahrenheit to celsius temperature"""
        return (temp_fahrenheit - 32) * (5 / 9)

    def celsius_to_kelvin(self, temp_celsius):
        """Convert celsius to kelvin temperature"""
        return temp_celsius + 273.15

    def kelvin_to_celsius(self, temp_kelvin):
        """Convert kelvin to celsius temperature"""
        return temp_kelvin - 273.15

    def fahrenheit_to_kelvin(self, temp_fahrenheit):
        """Convert fahrenheit to kelvin temperature"""
        return (temp_fahrenheit - 32) * (5 / 9) + 273.15

    def kelvin_to_fahrenheit(self, temp_kelvin):
        """Convert kelvin to fahrenheit temperature"""
        return (temp_kelvin - 273.15) * (9 / 5) + 32

    def choose_conversion(self, prompt):
        """Returns a number for the selected conversion"""
        self._available_conversions()

        option = int(input(prompt))

        # Returns option iff it's inside a range (1-6) otherwise 0
        if option in range(1, 7):
            return option
