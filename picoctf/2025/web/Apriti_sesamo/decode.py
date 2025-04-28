import base64
import sys
import re

arg = sys.argv

def main():
    encoded_string = arg[1]
    decoded_chars = []
    i = 0
    while i < len(encoded_string):
        if encoded_string[i:i+2] == "\\x":
            hex_value = encoded_string[i+2:i+4]
            decoded_chars.append(chr(int(hex_value, 16)))
            i += 4
        elif encoded_string[i] == "\\":
            octal_match = re.match(r"\\([0-7]{3})", encoded_string[i:])
            octal_value = "0" + encoded_string[i+1:i+3]
            if octal_match:
                octal_value = encoded_string[i+1:i+4]
            decoded_chars.append(chr(int(octal_value, 8)))
            i += 3
            if octal_match:
                i += 1
            
    print(base64.b64decode("".join(decoded_chars))) # base64でデコードする

if __name__ == "__main__":
    main()