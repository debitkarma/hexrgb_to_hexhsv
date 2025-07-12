def degrees_dec_to_hex(deg: int) -> int:
    return round(deg*255/360)


def percent_dec_to_hex(perc: int) -> int:
    return round(perc*255/100)


def convert_hsv_dec_to_hex(hue: int, sat: int, val: int):
    hsv_in_dec_not = ( degrees_dec_to_hex(hue), percent_dec_to_hex(sat), percent_dec_to_hex(val) )
    return set(
            [ hex(num) for num in hsv_in_dec_not ]
        )


def convert_hex_to_hsv_dec(hex_color: str):
    hex_color = hex_color.strip("#")
    if len(hex_color) != 6:
        raise ValueError("argument should be a hex color value 6 digits long")
    red = hex_color[0:2]
    blue = hex_color[2:4]
    green = hex_color[4:]
    return


def main():
    # figure out calc for hsv to rgb
    pass


if __name__ == "__main__":
    main()
