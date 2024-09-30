from load_csv import load
from matplotlib import pyplot as plt
from colorama import Fore, init

init(autoreset=True)


def visualize_life(file_path, campus):
    """
    Visualize the data.
    Args:
        data (pd.DataFrame): The data to visualize.
    """
    try:
        data = load(file_path)

        campus_data = data[data['country'] == campus]

        if campus_data.empty:
            raise ValueError(Fore.RED + f"Campus not found {campus}")

        campus_data = campus_data.set_index('country').T

        campus_data.index = campus_data.index.astype(int)

        print(Fore.YELLOW + 'Visualizing data')

        plt.figure(figsize=(12, 6))
        plt.plot(campus_data.index, campus_data[campus], label=campus)
        plt.title(f" {campus} Life Expectancy Projections")
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.xticks(ticks=range(1800, 2110, 40))
        plt.gcf().canvas.manager.set_window_title(f" {campus} Life expectancy \
Projections")

        plt.show()

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None


def main():
    print(Fore.CYAN + visualize_life.__doc__)
    try:
        file_path = 'life_expectancy_years.csv'
        campus = 'Afghanistan'

        visualize_life(file_path, campus)

    except KeyboardInterrupt:
        print(Fore.RED + 'Keyboard interrupt detected')
        return None

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None

    finally:
        print(Fore.YELLOW + 'Exiting...')


if __name__ == '__main__':
    main()
