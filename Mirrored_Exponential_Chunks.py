def mirrored_exponential_chunks(arr):
    '''
    def mirrored_exponential_chunks(arr):
    '''
    if len(arr) % 2:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle+1:]
    else:
        left = arr[:len(arr) // 2]
        right = arr[(len(arr) + 1) // 2:]

    left_out = []
    right_out = []
    step = 2
    while left:
        left_out.append(left[-step:])
        left = left[:-step]

        right_out.append((right[:step]))
        right = right[step:]
        step = step * 2
    left_out = left_out[::-1]
    if len(arr) % 2:
        left_out.append([arr[middle]])

    return left_out + right_out

string = [['wewe'], ['vvv'], ['yyyy'], ['iiii'], ['zzzzzzz'], ['mmmmmmm'], ['x'], ['dgrt']]

arrow = list(range(1, 100))

print(mirrored_exponential_chunks(arrow))

# [[79121.08852892419, True, 53356, 'fSwdjseOodCPutK', 463542, 15257.219971331091, 'X', 144733, 37942, False], ['PKSpaMs dp', 88610.5758347588, 'GOGbEZqMau Vob', 73150.66098017267, 227321, 48281.36655404434, 118144, 'ysZpBh', True, 24468.406407233673, 46619.21960582793, 176548, 24594, 65540.42750341249, False, 'FRA'], [78678, 582479, 838624, 'YGKdIKcffruGiq'], [305290, 347999], [86699.03193026684, 'tiCotaB'], [True, 714439, True, 67895], [549734, 'HgE xaFb', 36584.24018768771, 96565.23601996951, 794593, True, 50804.041332861736, 102600, False, True, 71923.07517836549, 'dJdIMXV', False, 'RQQ iHO cNWuCL', 'vD', 12211.262399231528], [True, 85286.65066264065, 121046, True, 'woMdw', 874910, 73208.0211873364, False, 'MYD', 926998]]
# [[79121.08852892419, True], [53356, 'fSwdjseOodCPutK', 463542, 15257.219971331091, 'X', 144733, 37942, False, 'PKSpaMs dp', 88610.5758347588, 'GOGbEZqMau Vob', 73150.66098017267, 227321, 48281.36655404434, 118144, 'ysZpBh'], [True, 24468.406407233673, 46619.21960582793, 176548, 24594, 65540.42750341249, False, 'FRA'], [78678, 582479, 838624, 'YGKdIKcffruGiq'], [305290, 347999], [86699.03193026684, 'tiCotaB'], [True, 714439, True, 67895], [549734, 'HgE xaFb', 36584.24018768771, 96565.23601996951, 794593, True, 50804.041332861736, 102600], [False, True, 71923.07517836549, 'dJdIMXV', False, 'RQQ iHO cNWuCL', 'vD', 12211.262399231528, True, 85286.65066264065, 121046, True, 'woMdw', 874910, 73208.0211873364, False], ['MYD', 926998]]