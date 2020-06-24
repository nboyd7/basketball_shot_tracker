from court import *
from data_handler import excel_handler


def main(filename, sheet_name):

    percentages = excel_handler(filename, sheet_name)
    print(percentages)
    #court_elements = draw_court(percentages)
    plt.figure(figsize=(12, 11))
    plt.text(-350, -200, sheet_name + ' Shooting Percentages', size=20)
    court_elements = draw_court(percentages, outer_lines=True)

    for elem in court_elements:
        label = elem.get_label()
        adjustment = { # for adjustment of location of some labels that don't need to be in the center
            'left_rim':(60, -20),
            'right_rim':(-60, -20),
            'center_rim': (0, 10),
            'center_mid':(0, 40),
            'left_three':(0, 20),
            'right_three':(0, 20)
        }

        adjustX = adjustment.get(label, (0,0))[0]
        adjustY = adjustment.get(label, (0,0))[1]

        nums = percentages[label]
        plt.annotate('{:.1%}'.format(nums[0]) + '\n(%d/%d)' % (nums[1], nums[2])
                     , (elem.get_x() + (elem.get_width()/2) + adjustX, elem.get_y() + (elem.get_height()/2) + adjustY), fontsize = 15, weight='bold', horizontalalignment='center', zorder=200)

    plt.xlim(-300, 300)
    plt.ylim(-100, 500)
    plt.show()

if __name__ == '__main__':
    main("resources\D Tendencies.xlsx", "Final")
