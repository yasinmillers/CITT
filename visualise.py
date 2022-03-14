from turtle import color


def Artist():
    import matplotlib.pyplot as plt
    artist = ["rihahna", "sia", "ariana", "eminem", "lil pump", "lil wayne", "lil uzi vert",
              "lil wayne", "lil uzi vert", "lil pump", "eminem", "ariana", "sia", "rihahna"]
    sales = [19500, 2909, 36500, 44455, 5999, 645,
             709, 890, 945, 1000, 16771, 1209, 13787]
    color = ["red", "blue", "green", "yellow", "black", "pink", "orange",
             "purple", "brown", "grey", "white", "cyan", "magenta"]  # color list

    fig, ax = plt.subplots(nrows=2, ncols=2)

    fig.suptitle("Artist and Sales", fontsize=20)

    ax[0, 0].set_title("Artist")
    ax[0, 0].set_xlabel("Artist")
    ax[0, 0].set_ylabel("Sales")
    ax[0, 0].bar(artist, sales, color=color)
    # pie chart
    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ax[0, 1].set_title("Artist")
    ax[0, 1].pie(sales, explode=explode, labels=artist, colors=color,
                 autopct="%1.1f%%", shadow=True, startangle=90)
    # line chart
    ax[1, 1].plot(artist, sales, color=color)
    ax[1, 1].set_title("line chart")

    # scatter graph
    sizes = [sales[i]/100 for i in range(len(sales))]
    ax[1, 0].scatter(artist, sales, colors=color, s=sizes, alpha=0.5,
                     marker='o', edgecolors='black')
    ax[1, 0].set_xlabel('Artists')
    ax[1, 0].set_ylabel('Sales')
    ax[1, 0].set_title('Scatter graph')
    # histogram
    ax[0, 2].hist(sales, color='b', edgecolor='black', linewidth=1.5)
    ax[0, 2].set_xlabel('Artists')
    ax[1, 0].set_ylabel('Sales')
    ax[1, 0].set_title('Histogram graph')

    # density graph
    ax[1, 2].plot(artist, sales, 'o')
    ax[1, 2].set_xlabel('Sales')
    ax[1, 2].set_ylabel('Artists')
    ax[1, 2].set_title('Density plot')

    plt.show()


Artist()
