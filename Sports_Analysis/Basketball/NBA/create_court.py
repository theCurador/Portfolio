import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl

def create_court(ax, color):
    
    # Short corner 3pt lines 
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)
 #3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
    
 # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))
    
# Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))
    
# Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)
   # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
# Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    
# General plot parameters
mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2
# Draw basketball court
fig = plt.figure(figsize=(4, 3.76))
ax = fig.add_axes([0, 0, 1, 1])
ax = create_court(ax, 'black')
plt.show()



def create_court2(color='black', lw=2, outer_lines=False):

    # Short corner 3pt lines 
    plt.plot([-220, -220], [0, 140], linewidth=lw, color=color)
    plt.plot([220, 220], [0, 140], linewidth=lw, color=color)
    
    # 3PT Arc
    plt.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=lw))
    
    # Lane and Key
    plt.plot([-80, -80], [0, 190], linewidth=lw, color=color)
    plt.plot([80, 80], [0, 190], linewidth=lw, color=color)
    plt.plot([-60, -60], [0, 190], linewidth=lw, color=color)
    plt.plot([60, 60], [0, 190], linewidth=lw, color=color)
    plt.plot([-80, 80], [190, 190], linewidth=lw, color=color)
    plt.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=lw))
    
    # Rim
    plt.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=lw))
    
    # Backboard
    plt.plot([-30, 30], [40, 40], linewidth=lw, color=color)

    if outer_lines:
        # Outer box of the basketball court
        plt.plot([-250, 250], [-47.5, -47.5], linewidth=lw, color=color)
        plt.plot([-250, 250], [470.5, 470.5], linewidth=lw, color=color)
        plt.plot([-250, -250], [-47.5, 470.5], linewidth=lw, color=color)
        plt.plot([250, 250], [-47.5, 470.5], linewidth=lw, color=color)

    # Remove ticks
    plt.xticks([])
    plt.yticks([])

    # Set axis limits
    plt.xlim(-250, 250)
    plt.ylim(0, 470)

    return plt.gca()
