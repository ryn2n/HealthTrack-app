import matplotlib.pyplot as plt
import numpy as np
from utils.menus import print_error

def plot_graph_weight(data, limit):
    if not data:
        print_error("Invalid Request: No data available to plot.")
        return
    
    # Unpack with * into separate lists
    dates, weights = zip(*data)

    # Create a figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Plot all-time data (first plot)
    ax1.plot(dates, weights, label="Weights", marker='o', linestyle='-', color='b')
    ax1.set_title('Weight Over All Time')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Weight (kg)')
    ax1.tick_params(axis='x', rotation=45)
    # Trendline
    ordinals = [d.toordinal() for d in dates]
    trend = np.polyfit(ordinals, weights, 1)
    line = np.poly1d(trend)
    ax1.plot(dates, line(ordinals), linestyle='--', color='g')

    # Plot last N points (second plot)
    recent_dates = dates[(-limit):]  # Get last N dates
    recent_weights = weights[(-limit):]  # Get last N weights
    ax2.plot(recent_dates, recent_weights, marker='o', linestyle='-', color='r')
    ax2.set_title(f'Weight Over Last {limit} Entries')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Weight (kg)')
    ax2.tick_params(axis='x', rotation=45)
    # Trendline
    recent_ordinals = [d.toordinal() for d in recent_dates]
    recent_trend = np.polyfit(recent_ordinals, recent_weights, 1)
    recent_line = np.poly1d(recent_trend)
    ax2.plot(recent_dates, recent_line(recent_ordinals), linestyle='--', color='g')

    # Display plot
    plt.tight_layout()
    plt.show()