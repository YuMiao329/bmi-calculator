def compute_BMI(mode, weight, height):
    if mode == 1:
        value = weight / (height ** 2)
    elif mode == 2:
        value = 703 * weight / (height ** 2)
    return value


def check_mode(mode):
    if mode == 1:
        weight = float(input("What's your weight in kilograms: "))
        height = float(input("What's your height in meters: "))
        keep_running = False
        return weight, height
    elif mode == 2:
        weight = float(input("What's your weight in pounds: "))
        height = float(input("What's your height in inches: "))
        keep_running = False
        return weight, height
    else:
        return False


def define_symptom(value):
    if value is None:
        return "None"
    elif value < 18.5:
        return "underweight"
    elif 18.5 <= value < 25:
        return "normal weight"
    elif 25 <= value < 29.9:
        return "overweight"
    else:
        return "obese"


def print_message(show_symptom, BMI_value):
    print("Your BMI is {}".format(BMI_value))
    print("You are {}".format(show_symptom))


def main():

    # Initialization
    keep_running = True
    weight = 0
    height = 0
    value = 0

    while keep_running:

        try:
            mode = int(input(
                "\nChoose Calculation Mode: \n1. kilograms in weight and meters in height\n2. pounds in weight and inches "
                "in height\nPlease type 1 or 2.\nYour Choice: "))
        except:
            print("Please type 1 or 2")
            continue

        try:
            weight, height = check_mode(mode)
        except TypeError:
            print("Please type 1 or 2")
            continue
        except UnboundLocalError:
            print("Please type 1 or 2")
            continue
        except ValueError:
            print("Please weight and height as a number")
            continue

        value = compute_BMI(mode, weight, height)

        show_symptom = define_symptom(value)

        print_message(show_symptom, value)

        quit()

if __name__ == "__main__":
    main()
