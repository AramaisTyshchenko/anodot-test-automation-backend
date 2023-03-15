from pytemp import pytemp


def test_fahrenheit_kelvin():
    """
    link to test description
    """
    fahrenheit = pytemp(40, 'kelvin', 'fahrenheit')
    kelvin = pytemp(fahrenheit, 'fahrenheit', 'kelvin')

    assert fahrenheit == -387.66999999999996, 'fahrenheit expected value is not correct'
    assert kelvin == 40.0, 'kelvin expected value is not correct'


def test_fahrenheit_kelvin_new_syntax():
    """
    link to test description
    """
    fahrenheit = pytemp(40, 'k', 'f')
    kelvin = pytemp(fahrenheit, 'f', 'k')
    assert fahrenheit == -387.66999999999996, 'fahrenheit expected value is not correct'
    assert kelvin == 40.0, 'kelvin expected value is not correct'


def test_celsius_fahrenheit():
    """
    link to test description
    """
    fahrenheit = pytemp(40, 'celsius', 'fahrenheit')
    celsius = pytemp(fahrenheit, 'fahrenheit', 'celsius')
    assert fahrenheit == 104.0, 'fahrenheit expected value is not correct'
    assert celsius == 40.0, 'celsius expected value is not correct'


def test_celsius_kelvin():
    """
    link to test description
    """
    celsius = pytemp(40, 'kelvin', 'celsius')
    kelvin = pytemp(celsius, 'celsius', 'kelvin')
    assert celsius == -233.14999999999998, 'celsius expected value is not correct'
    assert kelvin == 40.0, 'kelvin expected value is not correct'


def test_kelvin_celsius_with_huge_value():
    """
    link to test description
    """
    celsius = pytemp(999999999999999999999999999, 'kelvin', 'celsius')
    assert celsius == 1e+27, 'celsius expected value is not correct'


def test_kelvin_celsius_with_float_value():
    """
    link to test description
    """
    celsius = pytemp(1.111, 'kelvin', 'celsius')
    assert celsius == -272.039, 'celsius expected value is not correct'


def test_kelvin_celsius_with_incorrect_input():
    """
    link to test description
    """
    error = 'NOT RECEIVED'
    try:
        pytemp('', 'kelvin', 'celsius')
    except SystemExit as e:
        error = str(e)

    assert error == 'cannot convert  from kelvin to celsius', 'Expected error message is not correct'


def test_kelvin_celsius_with_incorrect_initial_temp():
    """
    link to test description
    """
    error = 'NOT RECEIVED'
    try:
        pytemp(1, '', 'celsius')
    except SystemExit as e:
        error = str(e)

    assert error == 'initial temperature unit must be one of the fahrenheit, f, celsius, c, kelvin or k', \
        'Expected error message is not correct'


def test_kelvin_celsius_with_incorrect_expected_temp_unit():
    """
    link to test description
    """
    error = 'NOT RECEIVED'
    try:
        pytemp(1, 'kelvin', 'cel')
    except SystemExit as e:
        error = str(e)

    assert error == 'expected temperature unit must be one of the fahrenheit, f, celsius, c, kelvin or k', \
        'Expected error message is not correct'


def test_kelvin_with_incorrect_expected_temp_unit():
    """
    link to test description
    """
    error = 'NOT RECEIVED'
    try:
        pytemp(1, 'kelvin', 'kelvin')
    except SystemExit as e:
        error = str(e)

    assert error == 'cannot convert 1 from kelvin to kelvin', \
        'Expected error message is not correct'
