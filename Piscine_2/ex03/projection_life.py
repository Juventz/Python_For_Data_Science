from load_csv import load
from colorama import init, Fore
from matplotlib import pyplot as plt
import pandas as pd

init(autoreset=True)


def visualize_projection_life(life_exp_path: str, gdp_path: str):
    """
    Visualize the projection of life expectancy and GDP per capita in 1900.
    Args:
    life_exp_path: str: The path to the life expectancy data.
    gdp_path: str: The path to the GDP data.
    """
    try:
        life_exp_data = load("life_exp_path")
        gdp_data = load("gdp_path")

        exp_data_1900 = life_exp_data[['country', '1900']]
        gdp_data_1900 = gdp_data[['country', '1900']]

        merged_data = pd.merge(exp_data_1900, gdp_data_1900, on='country')

        plt.figure(figsize=(7, 5))
        plt.scatter(merged_data['1900_x'], merged_data['1900_y'])
        plt.title("1900")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life expectancy")
        plt.legend()

        for i, row in merged_data.iterrows():
            plt.text(row['1900_x'], row['1900_y'], row['country'])

        plt.show()

    except KeyboardInterrupt:
        print(Fore.RED + "Keyboard Interrupt. Exiting...")
        return None

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None


def main():
    print(Fore.CYAN + visualize_projection_life.__doc__)
    try:
        life_exp_path = "life_expectancy_years.csv"
        gdp_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"

        visualize_projection_life(life_exp_path, gdp_path)

    except KeyboardInterrupt:
        print(Fore.RED + "Keyboard Interrupt. Exiting...")
        return None

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None


if __name__ == "__main__":
    main()
