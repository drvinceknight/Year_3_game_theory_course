"""
A library to plot a histogram of feedback comments.
"""
import matplotlib.pyplot as plt
import pylab

def plot(dictionary, title):
    """
    Saves a histogram of a dictionary of the form {comment : count} to a given title.
    """
    comments = sorted(dictionary.keys(), key= lambda x: dictionary[x])  # Obtain comments sorted by count

    fig, ax = plt.subplots(figsize=(4,7))

    fig.canvas.set_window_title('title')

    rects = ax.barh(range(0, 3*len(dictionary), 3), [dictionary[c] for c in comments], align='center', height=2, color='cyan')

    ax.axis([0, max(dictionary.values()), -3, 3 * len(dictionary)])
    pylab.yticks(range(0, 3*len(dictionary), 3), comments)
    pylab.xticks(range(max(dictionary.values()) + 1))
    ax.set_title(title[:-4])
    plt.grid()
    plt.xlabel('Frequency')
    plt.savefig(title, bbox_inches='tight')
