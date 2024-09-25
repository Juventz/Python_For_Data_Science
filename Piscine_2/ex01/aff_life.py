from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt
from colorama import Fore, init

init(autoreset=True)


def visualize(file_path, campus):
    """
    Visualize the data.
    Args:
        data (pd.DataFrame): The data to visualize.
    """
    try:
        data = load(file_path)

        # if data is None:
        #     raise ValueError(Fore.RED + 'Data is empty')

        campus_data = data[data['country'] == campus]

        if campus_data.empty:
            raise ValueError(Fore.RED + f"Campus not found {campus}")

        campus_data = campus_data.set_index('country').T

        print(Fore.YELLOW + 'Visualizing data')

        plt.figure(figsize=(12, 6))
        data.plot(campus_data.index, campus_data[campus], marker='o',
                  label=campus)
        plt.title(f" {campus} life expectancy Projections")
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.legend()
        plt.gcf.canvas.manager.set_window_title(f" {campus} Life expectancy Projections")

        plt.grid()
        plt.show()

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None


if __name__ == '__main__':
    visualize('data/life_expectancy.csv', 'France')