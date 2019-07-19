from pyseeyou import format
try:
    result = format(
        '''{GENDER, select,
                       male {He}
                     female {She}
                      other {They}
                   } found {NUM_RESULTS, plural,
                       one {1 result}}}}}
                     other {# results}
                   } in {NUM_CATEGORIES, plural,
                         one {1 category}
                       other {# categories}
                   }.''', {
            'GENDER': 'male',
            'NUM_RESULTS': 1,
            'NUM_CATEGORIES': '2'
        }, 'en')
    print(result)
except Exception:
    print("Error")


def isICUvalid(valueToCheck, values, lang):
    try:
        result = format(valueToCheck, values, lang)
        return True

    except Exception:
        return False


print(
    isICUvalid('{number, plural, =1{(# device)} other{(# devices)}}', '10',
               'en'))
