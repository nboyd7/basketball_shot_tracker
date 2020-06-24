import pandas as pd
import math

percent_column = 17
shot_made_column = 15
shot_attempts_column = 16


def excel_handler(filename, sheetname):
    data = pd.read_excel(filename, sheet_name=sheetname, index_col=0, header=None)
    print(data)

    # extract data
    perc = data.get(percent_column).tolist()
    attempts = data.get(shot_attempts_column).tolist()
    made = data.get(shot_made_column).tolist()

    left_rim = (perc[20], made[20], attempts[20])
    center_rim = (perc[22], made[22], attempts[22])
    right_rim = (perc[24], made[24], attempts[24])
    left_mid = (perc[29], made[29], attempts[29])
    center_mid = (perc[32], made[32], attempts[32])
    right_mid = (perc[34], made[34], attempts[34])
    left_three = (perc[41], made[41], attempts[41])
    center_three = (perc[43], made[43], attempts[43])
    right_three = (perc[45], made[45], attempts[45])

    map = {'left_rim': left_rim, 'center_rim': center_rim, 'right_rim': right_rim,
     'left_mid': left_mid, 'center_mid': center_mid, 'right_mid': right_mid,
     'left_three': left_three, 'center_three': center_three,
     'right_three': right_three}

    for key in map.keys():
        if math.isnan(map[key][0]):
            map[key] = (0.0, map[key][1])

    return map
