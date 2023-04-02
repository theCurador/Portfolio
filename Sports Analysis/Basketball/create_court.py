import matplotlib.pyplot as plt 

def create_court():
    #Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 11))
    
    #Draw half-court lines 
    ax.plot([-250, 250], [-47.5,-47.5], linewidth=2, color='black')
    ax.plot([-250, 250], [422.5,422.5], linewidth=2, color='black')
    ax.plot([-250, -250], [-47.5,422.5], linewidth=2, color='black')
    ax.plot([250, 250], [-47.5,422.5], linewidth=2, color='black')
    ax.plot([0, 0], [-47.5,422.5], linewidth=2, color='black')
    
    #Draw key and basket
    ax.plot([-80, -80], [-47.5, 142.5], linewidth=2, color='black')
    ax.plot([80, 80], [47.5, 142.5], linewidth=2, color='black')
    ax.plot([-80, 80], [142.5, 142.5], linewidth=2, color='black')
    ax.add_artist(plt.Circle((0, 142.5), radius=60, linewidth=2, color='black', fill=False))
    ax.add_artist(plt.Circle((0, 142.5), radius=6, linewidht=2, color='black', fill=False))
    
    #Draw corner three lines 
    ax.plot([220, 220], [-47.5, 92.5], linewidth=2, color='black')
    ax.plot([-220, -220], [-47.5, 92.5], linewidth=2, color='black')
    ax.plot([220, 250], [92.5, 92.5], linewidth=2, color='black')
    ax.plot([-220, -250], [92.5, 92.5], linewidth=2, color='black')
    ax.plot([220, 250], [-47.5, -47.5], linewidth=2, color='black')
    ax.plot([-220, -250], [-47.5, -47.5], linewidth=2, color='black')

    
# Draw wing three lines 
    ax.plot([250, 220], [142.5, 92.5], linewidth=2, color='black')
    ax.plot([-250, -220], [142.5, 92.5], linewidth=2, color='black')
    ax.plot([250, 250], [92.5, 142.5], linewidth=2, color='black')
    ax.plot([-250, -250], [92.5, 142.5], linewidth=2,color='black')
    
# Draw top of the key three lines 
    ax.plot([80, 120], [422.5, 382.5], linewidth=2, color='black')
    ax.plot([-80, -120], [422.5, 382.5], linewidth=2, color='black')
    ax.plot([80, 80], [422.5, 352.5], linewidth=2, color='black')
    ax.plot([-80, -80], [422.5, 352.5], linewidth=2, color='black')
    ax.plot([120, 120], [422.5, 352.5], linewidth=2, color='black')
    ax.plot([-120, -120], [422.5, 352.5], linewidth=2, color='black')
    
    #Draw free throw circle 
    t = np.linspace(0, np.pi*2, 100)
    x = 60 * np.cos(t)
    y = 60 * np.sin(t) + 142.5
    ax.plt(x, y, color='black', linewidth=2)
    
    # Draw restriced area 
    ax.add_patch(patches.Rectangel((-40, 0), 80, 190, linewidth=2, edgecolor='black', facecolor='none'))
    
    # Set the limits of the plot to match the court dimensions 
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    
    return ax