# MAYOWA OBISESAN
# EYE CSS - FONT GENERATOR
# JUNE 30, 2022.


def font_size_template():
    font_size_sequence_template = "0.08, 0.08, 0.08, 0.09"
    return font_size_sequence_template.replace(" ", "").split(",")


def gen_font_size(nth_size=20):
    from decimal import Decimal
    prev_ = Decimal("0.01")
    for index, i in enumerate(font_size_template() * nth_size, 1):
        prev_ += Decimal(i).quantize(Decimal("0.00"))
        # print(f"{index} - {i} - {prev_}")
        print(f".font-{index} {{font-size: {prev_}rem;}}")


# print(font_size_template() * 10)
gen_font_size()
