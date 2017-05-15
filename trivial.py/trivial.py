# Source Generated with Decompyle++
# File: trivial.pyc (Python 2.7)

import json
import sys

def check(flag):
    processed = flag[::-1]
    processed = processed.decode('base64')
    final = json.loads(processed)
    if final['check_code'] != 'AK4782':
        return False
    if None['flag_content']['numbers'] * 2 != 18529313:
        return False
    if None['flag_content']['change'] != 'standardisation'[::2]:
        return False
    if None['flag_content']['settled'] != 'CrossCTF{%s_%d_%s}':
        return False
    temp = None['flag_content']
    return temp['settled'] % (temp['change'], temp['numbers'], final['check_code'])


def main():
    if len(sys.argv) != 2:
        print 'No'
        sys.exit()
    result = check(sys.argv[1])
    if result:
        print result
    else:
        print 'No'

if __name__ == '__main__':
    main()
