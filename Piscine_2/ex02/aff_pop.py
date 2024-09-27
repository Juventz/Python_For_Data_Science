from load_csv import load
from colorama import init, Fore
import matplotlib.pyplot as plt

init(autoreset=True)


def convert_millions(x, pos):
    """
    Convert the population to millions.
    Args:
        x (int): The value.
        pos (int): The position.
    Returns:
        str: The value in millions.
    """
    return f'{x:,.0f}M'


def visualize_pop(file_path, my_campus, campus_choice):
    """
    Display the population data for the campus and the chosen campus.
    Args:
        file_path (str): The path to the file.
        my_campus (str): The name of the campus.
        campus_choice (str): The name of the chosen campus.
    """
    try:
        data = load(file_path)

        if 'country' not in data.columns:
            print(Fore.RED + 'The column "country" is missing')
            return None

        campus_data = data[data['country'] == my_campus]
        campus_choice_data = data[data['country'] == campus_choice]

        if campus_data.empty:
            print(Fore.RED + f"Campus not found : {my_campus}")
            return None
        if campus_choice_data.empty:
            print(Fore.RED + f"Campus not found : {campus_choice}")
            return None

        campus_data_series = campus_data.iloc[0].drop('country')
        campus_ch_data_series = campus_choice_data.iloc[0].drop('country')

        campus_data_series.index = campus_data_series.index.astype(int)
        campus_ch_data_series.index = campus_ch_data_series.index.astype(int)

        campus_data_series = campus_data_series[
            (campus_data_series.index >= 1800) &
            (campus_data_series.index <= 2050)]
        campus_ch_data_series = campus_ch_data_series[
            (campus_ch_data_series.index >= 1800) &
            (campus_ch_data_series.index <= 2050)]

        print(Fore.YELLOW + f"campus_data_series: {campus_data_series}")
        print(Fore.YELLOW + f"campus_ch_data_series: {campus_ch_data_series}")

        plt.figure(figsize=(7, 5))
        plt.plot(campus_data_series.index, campus_data_series / 1e6,
                 label=my_campus, color="g")
        plt.plot(campus_ch_data_series.index, campus_ch_data_series / 1e6,
                 label=campus_choice, color="b")
        plt.title("Population Projections")
        plt.xlabel('Year')
        plt.ylabel('Population')

        plt.yticks([20, 40, 60])

        max_population = max(campus_data_series.max(),
                             campus_ch_data_series.max()) / 1e6

        plt.ylim(0, max_population * 1.1)
        plt.xlim(1790, 2060)

        ax = plt.gca()
        ax.yaxis.set_major_formatter(plt.FuncFormatter(convert_millions))
        plt.xticks(ticks=range(1800, 2050, 40))
        plt.legend(loc="lower right")
        plt.gcf().canvas.manager.set_window_title(f" {my_campus} and \
{campus_choice} Population Projections")

        plt.show()

    except Exception as e:
        print(Fore.RED + f"{type(e).__name__}: {e}")
        return None


def main():
    # print(Fore.CYAN + visualize_pop.__doc__)
    try:
        file_path = 'population_total.csv'
        my_campus = 'France'
        campus_choice = 'Belgium'

        visualize_pop(file_path, my_campus, campus_choice)

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
