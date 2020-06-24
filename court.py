import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
from floatrange import floatrange

#colors
cold = 'lightblue'
#somewhat_cold = 'lightblue'
neutral = 'white'
#somewhat_hot = 'coral'
hot = 'red'

#ranges - floats multiplied by 100
rim_hot = range(65, 101)
#rim_somewhat_hot = range(56, 75)
rim_neutral = range(45, 65)
#rim_somewhat_cold = range(25, 45)
rim_cold = range(0, 45)

mid_hot = range(50, 101)
#mid_somewhat_hot = range(40, 50)
mid_neutral = range(45, 50)
#mid_somewhat_cold = range(15, 30)
mid_cold = range(0, 45)

three_hot = range(40, 101)
#three_somewhat_hot = range(35, 40)
three_neutral = range(34, 40)
#three_somewhat_cold = range(16, 25)
three_cold = range(0, 34)


def draw_court(percentage_map, ax=None, color='black', lw=2, outer_lines=False,):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False, zorder=150)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color, zorder=150)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False, zorder=150)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False, zorder=150)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False, zorder=150)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed', zorder=150)
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color, zorder=150)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color, zorder=150)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color, zorder=150)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color, zorder=150)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color, zorder=150)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color, zorder=150)


    # Percentage Zones
    rim = Arc((0, -7.5), 160, 177.5, theta1=0, theta2=180, linewidth=lw, color='grey', zorder=150)

    rim_middle = Rectangle((-30, -7.5), 60, 90, linewidth=lw, edgecolor='grey', facecolor=assign_color_rim(percentage_map['center_rim'][0]),
                          fill=True, label='center_rim')
    rim_right = Rectangle((-80, -7.5), 50, 90, linewidth=lw, edgecolor='grey', facecolor=assign_color_rim(percentage_map['right_rim'][0]),
                           fill=True, label='right_rim', zorder=50)

    rim_left = Rectangle((30, -7.5), 50, 90, linewidth=lw, edgecolor='grey', facecolor=assign_color_rim(percentage_map['left_rim'][0]),
                           fill=True, label='left_rim', zorder=50)

    mid_middle = Rectangle((-80, -7.5), 160, 247.5, linewidth=lw, edgecolor='grey', facecolor=assign_color_mid(percentage_map['center_mid'][0]),
                          fill=True, label='center_mid')
    mid_right = Rectangle((-220, -7.5), 140, 247.5, linewidth=lw, edgecolor='grey', facecolor=assign_color_mid(percentage_map['right_mid'][0]),
                           fill=True, label='right_mid',clip_on=True, zorder=50)
    mid_left = Rectangle((80, -7.5), 140, 247.5, linewidth=lw, edgecolor='grey', facecolor=assign_color_mid(percentage_map['left_mid'][0]),
                           fill=True, label='left_mid', zorder=50)

    three_middle = Rectangle((-160, 177.5), 320, 150, linewidth=lw, edgecolor='grey', facecolor=assign_color_three(percentage_map['center_three'][0]),
                          fill=True, label='center_three', zorder=0)
    three_right = Rectangle((-250, -7.5), 90, 335, linewidth=lw, edgecolor='grey', facecolor=assign_color_three(percentage_map['right_three'][0]),
                          fill=True, label='right_three', zorder=20)
    three_left = Rectangle((160, -7.5), 90, 335, linewidth=lw, edgecolor='grey', facecolor=assign_color_three(percentage_map['left_three'][0]),
                          fill=True, label='left_three', zorder=20)


    shoot_area_elements = [mid_middle, rim_left, rim_right, rim_middle,
                           mid_left, mid_right, three_middle, three_left, three_right]

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc, rim, mid_middle, rim_left, rim_right, rim_middle, mid_left, mid_right,
                      three_middle, three_left, three_right] # shoot area elements

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False, zorder=150)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    # formatting
    three_middle.set_clip_path(outer_lines)
    rim_middle.set_clip_path(rim)
    rim_left.set_clip_path(rim)
    rim_right.set_clip_path(rim)
    mid_middle.set_clip_path(three_arc)
    mid_left.set_clip_path(three_arc)
    mid_right.set_clip_path(three_arc)

    return shoot_area_elements

def assign_color_rim(percentage):
    temp = round(percentage * 100, 0)
    #print(temp)
    if temp in rim_hot:
        return hot
    #if temp in rim_somewhat_hot:
    #   print("here")
    #   return somewhat_hot
    if temp in rim_neutral:
        return neutral
    #if temp in rim_somewhat_cold:
    #    return somewhat_cold
    if temp in rim_cold:
        return cold
    
def assign_color_mid(percentage):
    temp = round(percentage * 100, 0)
    print(temp)
    if temp in mid_hot:
        return hot
    #if temp in mid_somewhat_hot:
    #    return somewhat_hot
    if temp in mid_neutral:
        return neutral
    #if temp in mid_somewhat_cold:
    #    return somewhat_cold
    if temp in mid_cold:
        return cold
    
def assign_color_three(percentage):
    temp = round(percentage * 100, 0)
    if temp in three_hot:
        return hot
    #if temp in three_somewhat_hot:
    #    return somewhat_hot
    if temp in three_neutral:
        return neutral
    #if temp in three_somewhat_cold:
    #   return somewhat_cold
    if temp in three_cold:
        return cold
    




