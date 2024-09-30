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
        life_exp_data = load(life_exp_path)
        gdp_data = load(gdp_path)

        if life_exp_data is None or gdp_data is None:
            print(Fore.RED + "Error: Failed to load one of the datasets")
            return None

        if '1900' not in life_exp_data.columns or \
                '1900' not in gdp_data.columns:
            print(Fore.RED + 'Error: The year 1900 is missing \
from one of the datasets')
            return None

        exp_data_1900 = life_exp_data[['country', '1900']]
        gdp_data_1900 = gdp_data[['country', '1900']]

        merged_data = pd.merge(exp_data_1900, gdp_data_1900, on='country')

        life_expectancy = merged_data['1900_x']
        gdp_per_capita = merged_data['1900_y']

        plt.figure(figsize=(7, 5))
        plt.scatter(gdp_per_capita, life_expectancy,
                    c='blue', alpha=0.7)

        plt.xscale('log')

        plt.xlim(300, 10000)
        plt.ylim(19, 55)
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.yticks([20, 25, 30, 35, 40, 45, 50, 55])

        plt.title("1900", fontsize=16)
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life expectancy")
        plt.gcf().canvas.manager.set_window_title("1900")
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
