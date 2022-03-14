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
