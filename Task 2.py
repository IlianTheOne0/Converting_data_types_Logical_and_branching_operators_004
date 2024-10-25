assessment = int(input('Enter the assessment: '))

if 100 < assessment or 0 > assessment:
    print('Error: There is no such assessment')
else:
    if 60 <= assessment <= 66: print('Assessment: E')
    elif 67 <= assessment <= 74: print('Assessment: D')
    elif 75 <= assessment <= 81: print('Assessment: C')
    elif 82 <= assessment <= 89: print('Assessment: B')
    elif 90 <= assessment <= 100: print('Assessment: A')
    else: print('Not enough points for the assessment')