# MAYOWA OBISESAN
# eye.css GENERATOR
# JUNE 15, 2022.

# This scrips generates eye.css styles.
# The use of this script is just to generate a nicely formatted string of css-styles.


# :TODO: :FUTURES:
# 2.    Introduce css filters. - June 17, 2022.
# e.g., w-4|safe
# "|" is a filter trigger, and safe means mark w-4 (=32px) as safe meaning, it will not overflow it's container.
# 3.    Use neg: pseudo classes to specify negative values with the same format as positive values. - June 18, 2022.
# e.g., "abs-y2" becomes "neg:abs-y2" same values will be produces when parsed, just different polar signs.
# 4.    Introduce portrait and landscape css eye.css custom pseudo-classes. - June 18, 2022.
# i.e., port:abs-x4 land:abs-x3 abs-y2

# JUNE 19, 2022.
# One of the philosophies of eye.css is that:
# "What should not be difficult should not be programmed unnecessarily complex."


class CSSGenerator:
    """
    This class generates eye.css file
    :Date: June 19, 2022.
    :return: A File object - an eye.css file / eye.min.css
    """

    def __init__(self) -> None:
        self.eye_css_filename = "eye_gen.css"
        self.css_file_created = False

        # Get the list of css properties. All of them.
        self.css_definitions_list = self.css_properties()
        self.formatted_css_definitions_list = self.format_css_list(
            self.css_definitions_list
        )

        with open(self.eye_css_filename, "w+") as opened_file:
            opened_file.write("")
            opened_file.close()
            self.css_file_created = True
            print(f"File: {self.eye_css_filename} successfully created.")

    @classmethod
    def format_css_list(cls, css_list):
        """:Date: inherit"""
        # css_list = [each_item.lstrip("\n").strip(" ") for each_item in css_list]
        css_list = [each_item.strip("\n").strip(" ") for each_item in css_list]
        return css_list

    def minify_css_list(self, css_list):
        """:Date: inherit"""
        css_list = [
            each_item.lstrip("\n").rstrip("\n").strip(" ").replace("\n", "")
            for each_item in css_list
        ]
        return css_list

    def css_properties(self):
        """
        All the defined css property classes.
        :Date: inherit
        """
        # css_properties_list = Squares() + FlexBox() + Paddings()
        css_properties_list = [
            *Positions().css_properties,
            *FlexBox().css_properties,
            *Widths().css_properties,
            *Heights().css_properties,
            *LineHeights().css_properties,
            *Squares().css_properties,
            *Margins().css_properties,
            *Paddings().css_properties,
            *Radius().css_properties,
            *Texts().css_properties,
            *ZIndex().css_properties,
        ]
        # print(css_properties_list)
        return css_properties_list

    def write_styles(self):
        """:Date: inherit"""
        if self.css_file_created:
            with open(self.eye_css_filename, "w+") as opened_file:
                opened_file.writelines(self.formatted_css_definitions_list)
                opened_file.close()
                print(f"CSS Properties written.")
        else:
            print("An error occured with initializing eye.css. Do Try again.")


class Positions:
    """
    CSS Position Helpers
    :Date: June 17, 2022.
    """

    def __init__(self) -> None:
        self.position_css_classes = []
        self.default_x_grid_value = 12
        self.default_y_grid_value = 8

        # Generate the position css helers
        self.static()
        self.abs()
        self.abs_x_helpers()
        self.abs_y_helpers()
        self.fixed()
        self.fixed_x_helpers()
        self.fixed_y_helpers()
        self.relative()

    @property
    def css_properties(self):
        return self.position_css_classes

    def static(self):
        """
        Initialize the .static css class.
        """
        pos_static_css = ".static {position: static;}"
        self.position_css_classes.append(pos_static_css)

    def abs(self):
        """
        Initialize the .abs css class.
        """
        abs_css = ".abs {position: absolute;}"
        self.position_css_classes.append(abs_css)
        self.abs_x_helpers()
        self.abs_y_helpers()

    def abs_x_helpers(self):
        """
        Defines CSS absolute position helper classes.
        :Date: June 17, 2022.
        :format:
        .abs-x1 {left: 0%;}
        .abs-x2 {left: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_x_grid_value, 1):
            abs_x_css = f"""
            .abs-x{i} {{left: {i / self.default_x_grid_value * 100}%;}}
            """
            self.position_css_classes.append(abs_x_css)

    def abs_y_helpers(self):
        """
        Defines CSS absolute position helper classes.
        :Date: June 18, 2022.
        :format:
        .abs-y1 {top: 0%;}
        .abs-y2 {top: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_y_grid_value, 1):
            abs_y_css = f"""
            .abs-y{i} {{top: {i / self.default_y_grid_value * 100}%;}}
            """
            self.position_css_classes.append(abs_y_css)

    def fixed(self):
        """
        Initialize the .fixed css class.
        """
        pos_fixed_css = ".fixed {position: fixed;}"
        self.position_css_classes.append(pos_fixed_css)
        # self.fixed_x_helpers()
        # self.fixed_y_helpers()

    def fixed_x_helpers(self):
        """
        Defines CSS fixed position helper classes.
        :Date: June 18, 2022.
        :format:
        .fixed-x1 {left: 0%;}
        .fixed-x2 {left: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_x_grid_value, 1):
            fixed_x_css = f"""
            .fixed-x{i} {{left: {i / self.default_x_grid_value * 100}%;}}
            """
            self.position_css_classes.append(fixed_x_css)

    def fixed_y_helpers(self):
        """
        Defines CSS fixed position helper classes.
        :Date: June 18, 2022.
        :format:
        .fixed-y1 {top: 0%;}
        .fixed-y2 {top: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_y_grid_value, 1):
            fixed_y_css = f"""
            .fixed-y{i} {{top: {i / self.default_y_grid_value * 100}%;}}
            """
            self.position_css_classes.append(fixed_y_css)

    def relative(self):
        """
        Initialize the .relative css class.
        """
        relative_css = ".relative {position: relative;}"
        self.position_css_classes.append(relative_css)
        # self.relative_x_helpers()
        # self.relative_y_helpers()

    def relative_x_helpers(self):
        """
        Defines CSS relativeolute position helper classes.
        :Date: June 18, 2022.
        :format:
        .relative-x1 {left: 0%;}
        .relative-x2 {left: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_x_grid_value, 1):
            relative_x_css = f"""
            .relative-x{i} {{left: {i / self.default_x_grid_value * 100}%;}}
            """
            self.position_css_classes.append(relative_x_css)

    def relative_y_helpers(self):
        """
        Defines CSS relativeolute position helper classes.
        :Date: June 18, 2022.
        :format:
        .relative-y1 {top: 0%;}
        .relative-y2 {top: (1/12) * 100%;}
        :return:
        """
        for i in range(1, self.default_y_grid_value, 1):
            relative_y_css = f"""
            .relative-y{i} {{top: {i / self.default_y_grid_value * 100}%;}}
            """
            self.position_css_classes.append(relative_y_css)


class FlexBox:
    """
    This class generates flexbox helpers.
    :Date: June 18, 2022.
    """

    def __init__(self) -> None:
        self.flex_css_classes = list()
        self.default_dimension_value = 8

        # Define the default flex class property.
        flex_css = ".flex {display: flex;}"
        self.flex_css_classes.append(flex_css)

        # Generate the flex properties
        self.flex_direction()
        self.flex_wrap()
        self.flex_grow()
        self.flex_shrink()
        self.flex_basis()
        self.flex_basis_percentages()
        self.justify_content()
        self.justify_items()
        self.justify_self()
        self.align_content()
        self.align_items()
        self.align_self()
        self.order()

    @property
    def css_properties(self):
        return self.flex_css_classes

    def flex_direction(self):
        """
        Defines flex-direction
        :return:
        .flex-row {flex-direction: row;}
        .flex-column {flex-direction: column;}
        :Date: June 18, 2022.
        """
        flex_direction_css = f"""
        .flex-row {{flex-direction: row;}}
        .flex-column {{flex-direction: column;}}
        """
        self.flex_css_classes.append(flex_direction_css)

    def flex_wrap(self):
        """
        Defines css flex-wrap property
        :return:
        .flex-wrap {flex-wrap: wrap;}
        .flex-nowrap {flex-wrap: nowrap;}
        .flex-wrap-reverse {flex-wrap: wrap-reverse;}
        """
        flex_wrap_css = f""".flex-wrap {{flex-wrap: wrap;}}
        .flex-nowrap {{flex-wrap: nowrap;}}
        .flex-wrap-reverse {{flex-wrap: wrap-reverse;}}
        """
        self.flex_css_classes.append(flex_wrap_css)

    def flex_grow(self):
        flex_grow_css = f"""
        .flex-grow: {{flex-grow: 1;}}
        .flex-nogrow: {{flex-grow: 0;}}
        """
        self.flex_css_classes.append(flex_grow_css)

    def flex_shrink(self):
        flex_shrink_css = f"""
        .flex-shrink: {{flex-shrink: 1;}}
        .flex-noshrink: {{flex-shrink: 0;}}
        """
        self.flex_css_classes.append(flex_shrink_css)

    def flex_basis(self):
        flex_basis_auto = f".flex-basis {{flex-basis: auto;}}"
        self.flex_css_classes.append(flex_basis_auto)
        for i in range(1, 13, 1):
            flex_basis_css = f"""
            .flex-basis-{i}: {{flex-basis: {i * self.default_dimension_value}px;}}
            """
            self.flex_css_classes.append(flex_basis_css)

        # Generate flex-basis for 2x & 3x dimensions.
        for x in range(2, 3, 1):
            for i in range(1, 13, 1):
                flex_basis_css = f"""
                .flex-basis{x}-{i}: {{flex-basis: {(i + 12) * self.default_dimension_value}px;}}
                """
                self.flex_css_classes.append(flex_basis_css)

    def flex_basis_percentages(self):
        flex_basis_auto = f".flex-basis {{flex-basis: auto;}}"
        self.flex_css_classes.append(flex_basis_auto)
        for i in range(0, 101, 1):
            flex_basis_css = f"""
            .flex-basis-{i}: {{flex-basis: {i / 12 * 100}%;}}
            """
            self.flex_css_classes.append(flex_basis_css)

    def justify_content(self):
        flex_justify_content = f"""
        .justify-unset {{justify-content: unset;}}
        .justify-initial {{justify-content: initial;}}
        .justify-inherit {{justify-content: inherit;}}
        .justify-baseline {{justify-content: baseline;}}
        .justify-start {{justify-content: flex-start;}}
        .justify-end {{justify-content: flex-end;}}
        .justify-center {{justify-content: center;}}
        .justify-stretch {{justify-content: stretch;}}
        .justify-around {{justify-content: space-around;}}
        .justify-between {{justify-content: space-between;}}
        .justify-evenly {{justify-content: space-evenly;}}
        .justify-safe {{justify-content: safe;}}
        .justify-left {{justify-content: left;}}
        .justify-right {{justify-content: right;}}
        """
        self.flex_css_classes.append(flex_justify_content)

    def justify_items(self):
        flex_justify_items = f"""
        .justify-items-unset {{justify-items: unset;}}
        .justify-items-initial {{justify-items: initial;}}
        .justify-items-inherit {{justify-items: inherit;}}
        .justify-items-start {{justify-items: start;}}
        .justify-items-end {{justify-items: end;}}
        .justify-items-center {{justify-items: center;}}
        .justify-items-stretch {{justify-items: stretch;}}
        """
        self.flex_css_classes.append(flex_justify_items)

    def justify_self(self):
        flex_justify_self = f"""
        .justify-self-unset {{justify-self: unset;}}
        .justify-self-initial {{justify-self: initial;}}
        .justify-self-inherit {{justify-self: inherit;}}
        .justify-self-auto {{justify-self: auto;}}
        .justify-self-start {{justify-self: flex-start;}}
        .justify-self-end {{justify-self: flex-end;}}
        .justify-self-center {{justify-self: center;}}
        .justify-self-stretch {{justify-self: stretch;}}
        """
        self.flex_css_classes.append(flex_justify_self)

    def align_content(self):
        flex_align_content = f"""
        .align-unset {{align-content: unset;}}
        .align-initial {{align-content: initial;}}
        .align-inherit {{align-content: inherit;}}
        .align-start {{align-content: flex-start;}}
        .align-end {{align-content: flex-end;}}
        .align-center {{align-content: center;}}
        .align-stretch {{align-content: stretch;}}
        .align-around {{align-content: space-around;}}
        .align-between {{align-content: space-between;}}
        """
        self.flex_css_classes.append(flex_align_content)

    def align_items(self):
        flex_align_items = f"""
        .align-items-unset {{align-items: unset;}}
        .align-items-initial {{align-items: initial;}}
        .align-items-inherit {{align-items: inherit;}}
        .align-items-baseline {{align-items: baseline;}}
        .align-items-start {{align-items: flex-start;}}
        .align-items-end {{align-items: flex-end;}}
        .align-items-center {{align-items: center;}}
        .align-items-stretch {{align-items: stretch;}}
        """
        self.flex_css_classes.append(flex_align_items)

    def align_self(self):
        flex_align_self = f"""
        .align-self-unset {{align-self: unset;}}
        .align-self-initial {{align-self: initial;}}
        .align-self-inherit {{align-self: inherit;}}
        .align-self-auto {{align-self: auto;}}
        .align-self-baseline {{align-self: baseline;}}
        .align-self-start {{align-self: flex-start;}}
        .align-self-end {{align-self: flex-end;}}
        .align-self-center {{align-self: center;}}
        .align-self-stretch {{align-self: stretch;}}
        """
        self.flex_css_classes.append(flex_align_self)

    def order(self):
        for i in range(0, 13, 1):
            order_css = f"""
            .order-{i} {{order: {i};}}
            """
            self.flex_css_classes.append(order_css)


class Widths:
    """
    This class generates width helpers.
    :Date: June 16, 2022.
    """

    def __init__(self) -> None:
        self.width_css_classes = list()
        self.default_dimension_value = 8
        self.gen_percent_width_helpers()
        self.gen_width_helpers()
        self.gen_width_2x_helpers()
        self.gen_width_safe_helpers()

    @property
    def css_properties(self):
        return self.width_css_classes

    def gen_percent_width_helpers(self, percent_prefix_string="pct"):
        """
        This function generates percent width helpers.
        FORMAT GENERATED:
        .pct\:w-0 {width: 0%;}
        .pct\:w-1 {width: 1%;}
        ...
        .pct\:w-100 {width: 100%;}
        :return: percentage Width helper css classes
        """
        for i in range(0, 101, 1):
            percent_width_css = f".{percent_prefix_string}\:w-{i} {{width: {i}%;}}"
            self.width_css_classes.append(percent_width_css)

    def gen_width_helpers(self):
        """
        Generates eye.css width helpers.
        Format to be returned is:
        .w-1 {width: 8px;}
        .w-2 {width: 16px;}
        :return: 1x width helper css classes
        """
        for i in range(1, 13, 1):
            width_css = f"w-{i} {{width: {i * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_css)

    def gen_width_2x_helpers(self):
        """
        Generates eye.css width 2x helpers.
        Format to be returned is:
        .w2-1 {width: 104px;}   # i.e., (1 + 12) * self.default_dimension_value
        .w2-2 {width: 112px;}   # i.e., (2 + 12) * self.default_dimension_value
        :return: 2x width helper css classes
        """
        for i in range(1, 13, 1):
            width_2x_css = f"w2-{i} {{width: {i * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_2x_css)

    def gen_width_safe_helpers(self):
        """
        Generates eye.css width helpers.
        Format to be returned is:
        .w-safe-1 {width: 8%;}
        .w-safe-2 {width: 16%;}
        :return: 1x width helper css classes
        """
        for i in range(1, 13, 1):
            width_safe_css = (
                f"w-safe-{i} {{width: {i * self.default_dimension_value}%}}"
            )
            self.width_css_classes.append(width_safe_css)


class Heights:
    """
    This class generates height helpers.
    :Date: June 16, 2022.
    """

    def __init__(self) -> None:
        self.height_css_classes = list()
        self.default_dimension_value = 8
        self.gen_percent_height_helpers()
        self.gen_height_helpers()
        self.gen_height_2x_helpers()
        self.gen_height_safe_helpers()

    @property
    def css_properties(self):
        return self.height_css_classes

    def gen_percent_height_helpers(self, percent_prefix_string="pct"):
        """
        This function generates percent height helpers.
        FORMAT GENERATED:
        .pct\:h-0 {height: 0%;}
        .pct\:h-1 {height: 1%;}
        ...
        .pct\:h-100 {height: 100%;}
        :return: percentage Width helper css classes
        """
        for i in range(0, 101, 1):
            percent_height_css = f".{percent_prefix_string}\:h-{i} {{height: {i}%;}}"
            self.height_css_classes.append(percent_height_css)

        # gen_percent_height_helpers()

    def gen_height_helpers(self):
        """
        Generates eye.css height helpers.
        Format to be returned is:
        .h-1 {height: 8px;}
        .h-2 {height: 16px;}
        :return: 1x height helper css classes
        """
        for i in range(1, 13, 1):
            height_css = f"h-{i} {{height: {i * self.default_dimension_value}px}}"
            self.height_css_classes.append(height_css)

    def gen_height_2x_helpers(self):
        """
        Generates eye.css height 2x helpers.
        Format to be returned is:
        .h2-1 {height: 104px;}   # i.e., (1 + 12) * self.default_dimension_value
        .h2-2 {height: 112px;}   # i.e., (2 + 12) * self.default_dimension_value
        :return: 2x height helper css classes
        """
        for i in range(1, 13, 1):
            height_2x_css = f"h2-{i} {{height: {i * self.default_dimension_value}px}}"
            self.height_css_classes.append(height_2x_css)

    def gen_height_safe_helpers(self):
        """
        Generates eye.css height helpers.
        Format to be returned is:
        .h-safe-1 {height: 8%;}
        .h-safe-2 {height: 16%;}
        :return: 1x height helper css classes
        """
        for i in range(1, 13, 1):
            height_safe_css = (
                f"h-safe-{i} {{height: {i * self.default_dimension_value}%}}"
            )
            self.height_css_classes.append(height_safe_css)


class Margins:
    """
    Margin Helper css classes Definition Class.
    :Date: June 16, 2022.
    """

    """
    :TODO: :FUTURES:
    Margins will have the following future definitions.
    mg-left-2: 16px;
    mg-left-2-sm: 14px;
    mg-left-2-smr: 12px;
    mg-left-2-smt: 10px;
    mg-left-2-xs: 9px;

    This means that you could reduce any css property by adding the "sm, smr, smt, xs" classes.
    That is style defining. THANK YOU JESUS.
    Note: the use of lg will not be used since any value's higher sibling can be achieved by increasing the property's figure (i.e, mg-left-3 -> mg-left-4)
    So instead of using the mg-left-3-lg property use the mg-left-4-sm property.
    THANK YOU JESUS.
    """

    def __init__(self) -> None:
        self.margin_css_classes = list()
        self.default_dimension_value = 8

        # Generate margin css helpers
        self.gen_margin_default_helpers()
        self.gen_margin_auto_helpers()
        self.gen_margin_x_helpers()
        self.gen_margin_left_helpers()
        self.gen_margin_right_helpers()
        self.gen_margin_y_helpers()
        self.gen_margin_top_helpers()
        self.gen_margin_bottom_helpers()

    @property
    def css_properties(self):
        return self.margin_css_classes

    def gen_margin_small_helpers(self):
        """
        :Date: June 27, 2022.
        """
        for i in range(1, 13, 1):
            mg_small_css = f"""
            .mg-x{i}-sm {{margin-left: {(i * 8) - 2}px;}}
            """

    def gen_margin_default_helpers(self):
        """
        :Date: June 27, 2022.
        """
        mg_default_css = f"""
        .mg-0 {{margin: 0;}}
        .mg-x-0 {{margin-left: 0; margin-right: 0;}}
        .mg-y-0 {{margin-top: 0; margin-bottom: 0;}}
        .mg-top-0 {{margin-top: 0;}}
        .mg-bottom-0 {{margin-bottom: 0;}}
        .mg-left-0 {{margin-left: 0;}}
        .mg-right-0 {{margin-right: 0;}}
        .mg-initial {{margin: initial;}}
        .mg-x-initial {{margin-left: initial; margin-right: initial;}}
        .mg-y-initial {{margin-top: initial; margin-bottom: initial;}}
        .mg-top-initial {{margin-top: initial;}}
        .mg-bottom-initial {{margin-bottom: initial;}}
        .mg-left-initial {{margin-left: initial;}}
        .mg-right-initial {{margin-right: initial;}}
        .mg-inherit {{margin: inherit;}}
        .mg-x-inherit {{margin-left: inherit; margin-right: inherit;}}
        .mg-y-inherit {{margin-top: inherit; margin-bottom: inherit;}}
        .mg-top-inherit {{margin-top: inherit;}}
        .mg-bottom-inherit {{margin-bottom: inherit;}}
        .mg-left-inherit {{margin-left: inherit;}}
        .mg-right-inherit {{margin-right: inherit;}}
        .mg-unset {{margin: unset;}}
        .mg-x-unset {{margin-left: unset; margin-right: unset;}}
        .mg-y-unset {{margin-top: unset; margin-bottom: unset;}}
        .mg-top-unset {{margin-top: unset;}}
        .mg-bottom-unset {{margin-bottom: unset;}}
        .mg-left-unset {{margin-left: unset;}}
        .mg-right-unset {{margin-right: unset;}}
        """
        self.margin_css_classes.append(mg_default_css)

    def gen_margin_auto_helpers(self):
        """Generates margin auto css class
        :format:
        .mg-auto {margin-left: auto;}
        """
        mg_auto_css = f"""
        .mg-auto {{margin: auto;}}
        .mg-x-auto {{margin-left: auto; margin-right: auto;}}
        .mg-y-auto {{margin-top: auto; margin-bottom: auto;}}
        .mg-top-auto {{margin-top: auto;}}
        .mg-bottom-auto {{margin-bottom: auto;}}
        .mg-left-auto {{margin-left: auto;}}
        .mg-right-auto {{margin-right: auto;}}
        """
        self.margin_css_classes.append(mg_auto_css)

    def gen_margin_x_helpers(self):
        """
        Generates margin_x_helpers.
        :format:
        .mg-x, .mg-x1 {margin-left: 8px; margin-right: 8px;}
        """
        # default_dimension_value = 8
        # mg_auto_css = f".mg-x-auto {{margin-left: auto; margin-right: auto;}}"
        # self.margin_css_classes.append(mg_auto_css)
        for i in range(1, 13, 1):
            mg_x_css = f"""
            .mg-x{i} {{margin-left: {self.default_dimension_value * i}px; margin-right: {self.default_dimension_value * i}px;}}
            .mg-x{i}-sm {{margin-left: {(self.default_dimension_value * i) - 2}px; margin-right: {(self.default_dimension_value * i) - 2}px;}}
            .mg-x{i}-smr {{margin-left: {(self.default_dimension_value * i) - 4}px; margin-right: {(self.default_dimension_value * i) - 4}px;}}
            .mg-x{i}-smt {{margin-left: {(self.default_dimension_value * i) - 6}px; margin-right: {(self.default_dimension_value * i) - 6}px;}}
            .mg-x{i}-xs {{margin-left: {(self.default_dimension_value * i) - 7}px; margin-right: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_x_css, end="")
            self.margin_css_classes.append(mg_x_css)

    def gen_margin_y_helpers(self):
        """
        Generates margin_y_helpers.
        :format:
        .mg-y {margin-top: 8px; margin-bottom: 8px;}
        .mg-y2 {margin-top: 16px; margin-bottom: 16px;}
        """
        for i in range(1, 13, 1):
            mg_y_css = f"""
            .mg-y{i} {{margin-top: {self.default_dimension_value * i}px; margin-bottom: {self.default_dimension_value * i}px}}
            .mg-y{i}-sm {{margin-top: {(self.default_dimension_value * i) - 2}px; margin-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .mg-y{i}-smr {{margin-top: {(self.default_dimension_value * i) - 4}px; margin-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .mg-y{i}-smt {{margin-top: {(self.default_dimension_value * i) - 6}px; margin-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .mg-y{i}-xs {{margin-top: {(self.default_dimension_value * i) - 7}px; margin-bottom: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_y_css, end="")
            self.margin_css_classes.append(mg_y_css)

    def gen_margin_left_helpers(self):
        """
        Generates margin_left_helpers.
        :format:
        .mg-left-1 {margin-left: 8px;} OR .mg-l-1 {margin-left: 8px;}
        """
        for i in range(1, 13, 1):
            mg_left_css = f"""
            .mg-left{i} {{margin-left: {self.default_dimension_value * i}px;}}
            .mg-left{i}-sm {{margin-left: {(self.default_dimension_value * i) - 2}px;}}
            .mg-left{i}-smr {{margin-left: {(self.default_dimension_value * i) - 4}px;}}
            .mg-left{i}-smt {{margin-left: {(self.default_dimension_value * i) - 6}px;}}
            .mg-left{i}-xs {{margin-left: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_left_css, end="")
            self.margin_css_classes.append(mg_left_css)

    def gen_margin_right_helpers(self):
        """
        Generates margin_right_helpers.
        :format:
        .mg-right-1 {margin-right: 8px;} OR .mg-l-1 {margin-right: 8px;}
        """
        for i in range(1, 13, 1):
            mg_right_css = f"""
            .mg-right{i} {{margin-right: {self.default_dimension_value * i}px;}}
            .mg-right{i}-sm {{margin-right: {(self.default_dimension_value * i) - 2}px;}}
            .mg-right{i}-smr {{margin-right: {(self.default_dimension_value * i) - 4}px;}}
            .mg-right{i}-smt {{margin-right: {(self.default_dimension_value * i) - 6}px;}}
            .mg-right{i}-xs {{margin-right: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_right_css, end="")
            self.margin_css_classes.append(mg_right_css)

    def gen_margin_top_helpers(self):
        """
        Generates margin_top_helpers.
        :format:
        .mg-top-1 {margin-top: 8px;} OR .mg-l-1 {margin-top: 8px;}
        """
        for i in range(1, 13, 1):
            mg_top_css = f"""
            .mg-top{i} {{margin-top: {self.default_dimension_value * i}px;}}
            .mg-top{i}-sm {{margin-top: {(self.default_dimension_value * i) - 2}px;}}
            .mg-top{i}-smr {{margin-top: {(self.default_dimension_value * i) - 4}px;}}
            .mg-top{i}-smt {{margin-top: {(self.default_dimension_value * i) - 6}px;}}
            .mg-top{i}-xs {{margin-top: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_top_css, end="")
            self.margin_css_classes.append(mg_top_css)

    def gen_margin_bottom_helpers(self):
        """
        Generates margin_bottom_helpers.
        :format:
        .mg-bottom-1 {margin-bottom: 8px;} OR .mg-l-1 {margin-bottom: 8px;}
        """
        for i in range(1, 13, 1):
            mg_bottom_css = f"""
            .mg-bottom{i} {{margin-bottom: {self.default_dimension_value * i}px;}}
            .mg-bottom{i}-sm {{margin-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .mg-bottom{i}-smr {{margin-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .mg-bottom{i}-smt {{margin-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .mg-bottom{i}-xs {{margin-bottom: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(mg_bottom_css, end="")
            self.margin_css_classes.append(mg_bottom_css)


class Paddings:
    """
    Padding Helper css classes Definition Class.
    :Date: June 16, 2022.
    """

    """
    :TODO: :FUTURES:
    Paddings will have the following future definitions.
    pad-left-2: 16px;
    pad-left-2-sm: 14px;
    pad-left-2-smr: 12px;
    pad-left-2-smt: 10px;
    pad-left-2-xs: 9px;

    This means that you could reduce any css property by adding the "sm, smr, smt, xs" classes.
    That is style defining. THANK YOU JESUS.
    Note: the use of lg will not be used since any value's higher sibling can be achieved by increasing the property's figure (i.e, pad-left-3 -> pad-left-4)
    So instead of using the pad-left-3-lg property use the pad-left-4-sm property.
    THANK YOU JESUS.
    """

    def __init__(self) -> None:
        self.default_dimension_value = 8
        self.padding_css_classes = list()
        self.gen_padding_default_helpers()
        self.gen_padding_auto_helpers()
        self.gen_padding_x_helpers()
        self.gen_padding_left_helpers()
        self.gen_padding_right_helpers()
        self.gen_padding_y_helpers()
        self.gen_padding_top_helpers()
        self.gen_padding_bottom_helpers()

    @property
    def css_properties(self):
        return self.padding_css_classes

    def gen_padding_default_helpers(self):
        """
        :Date: June 27, 2022.
        """
        pad_default_css = f"""
            .pad-0 {{padding: 0;}}
            .pad-x-0 {{padding-left: 0; padding-right: 0;}}
            .pad-y-0 {{padding-top: 0; padding-bottom: 0;}}
            .pad-top-0 {{padding-top: 0;}}
            .pad-bottom-0 {{padding-bottom: 0;}}
            .pad-left-0 {{padding-left: 0;}}
            .pad-right-0 {{padding-right: 0;}}
            .pad-initial {{padding: initial;}}
            .pad-x-initial {{padding-left: initial; padding-right: initial;}}
            .pad-y-initial {{padding-top: initial; padding-bottom: initial;}}
            .pad-top-initial {{padding-top: initial;}}
            .pad-bottom-initial {{padding-bottom: initial;}}
            .pad-left-initial {{padding-left: initial;}}
            .pad-right-initial {{padding-right: initial;}}
            .pad-inherit {{padding: inherit;}}
            .pad-x-inherit {{padding-left: inherit; padding-right: inherit;}}
            .pad-y-inherit {{padding-top: inherit; padding-bottom: inherit;}}
            .pad-top-inherit {{padding-top: inherit;}}
            .pad-bottom-inherit {{padding-bottom: inherit;}}
            .pad-left-inherit {{padding-left: inherit;}}
            .pad-right-inherit {{padding-right: inherit;}}
            .pad-unset {{padding: unset;}}
            .pad-x-unset {{padding-left: unset; padding-right: unset;}}
            .pad-y-unset {{padding-top: unset; padding-bottom: unset;}}
            .pad-top-unset {{padding-top: unset;}}
            .pad-bottom-unset {{padding-bottom: unset;}}
            .pad-left-unset {{padding-left: unset;}}
            .pad-right-unset {{padding-right: unset;}}
            """
        self.padding_css_classes.append(pad_default_css)

    def gen_padding_auto_helpers(self):
        """Generates padding auto css class
        :format:
        .pad-auto {padding-left: auto;}
        """
        pad_auto_css = f"""
        .pad-auto {{padding: auto;}}
        .pad-x-auto {{padding-left: auto; padding-right: auto;}}
        .pad-y-auto {{padding-top: auto; padding-bottom: auto;}}
        .pad-top-auto {{padding-top: auto;}}
        .pad-bottom-auto {{padding-bottom: auto;}}
        .pad-left-auto {{padding-left: auto;}}
        .pad-right-auto {{padding-right: auto;}}
        """
        self.padding_css_classes.append(pad_auto_css)

    def gen_padding_x_helpers(self):
        """
        Generates padding_x_helpers.
        :format:
        .pad-x, .pad-x1 {padding-left: 8px; padding-right: 8px;}
        """
        # default_dimension_value = 8
        # pad_auto_css = f".pad-x-auto {{padding-left: auto; padding-right: auto;}}"
        # self.padding_css_classes.append(pad_auto_css)
        for i in range(1, 13, 1):
            pad_x_css = f"""
            .pad-x{i} {{padding-left: {self.default_dimension_value * i}px; padding-right: {self.default_dimension_value * i}px;}}
            .pad-x{i}-sm {{padding-left: {(self.default_dimension_value * i) - 2}px; padding-right: {(self.default_dimension_value * i) - 2}px;}}
            .pad-x{i}-smr {{padding-left: {(self.default_dimension_value * i) - 4}px; padding-right: {(self.default_dimension_value * i) - 4}px;}}
            .pad-x{i}-smt {{padding-left: {(self.default_dimension_value * i) - 6}px; padding-right: {(self.default_dimension_value * i) - 6}px;}}
            .pad-x{i}-xs {{padding-left: {(self.default_dimension_value * i) - 7}px; padding-right: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_x_css, end="")
            self.padding_css_classes.append(pad_x_css)

    def gen_padding_y_helpers(self):
        """
        Generates padding_y_helpers.
        :format:
        .pad-x, .pad-x1 {padding-left: 8px; padding-right: 8px;}
        .pad-x2 {padding-left: 16px; padding-right: 16px;}
        .pad-y {padding-top: 8px; padding-bottom: 8px;}
        .pad-y2 {padding-top: 16px; padding-bottom: 16px;}
        """
        for i in range(1, 13, 1):
            pad_y_css = f"""
            .pad-y{i} {{padding-top: {self.default_dimension_value * i}px; padding-bottom: {self.default_dimension_value * i}px;}}
            .pad-y{i}-sm {{padding-top: {(self.default_dimension_value * i) - 2}px; padding-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .pad-y{i}-smr {{padding-top: {(self.default_dimension_value * i) - 4}px; padding-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .pad-y{i}-smt {{padding-top: {(self.default_dimension_value * i) - 6}px; padding-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .pad-y{i}-xs {{padding-top: {(self.default_dimension_value * i) - 7}px; padding-bottom: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_y_css, end="")
            self.padding_css_classes.append(pad_y_css)

    def gen_padding_left_helpers(self):
        """
        Generates padding_left_helpers.
        :format:
        .pad-left-1 {padding-left: 8px;} OR .pad-l-1 {padding-left: 8px;}
        """
        for i in range(1, 13, 1):
            pad_left_css = f"""
            .pad-left{i} {{padding-left: {self.default_dimension_value * i}px;}}
            .pad-left{i}-sm {{padding-left: {(self.default_dimension_value * i) - 2}px;}}
            .pad-left{i}-smr {{padding-left: {(self.default_dimension_value * i) - 4}px;}}
            .pad-left{i}-smt {{padding-left: {(self.default_dimension_value * i) - 6}px;}}
            .pad-left{i}-xs {{padding-left: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_left_css, end="")
            self.padding_css_classes.append(pad_left_css)

    def gen_padding_right_helpers(self):
        """
        Generates padding_right_helpers.
        :format:
        .pad-right-1 {padding-right: 8px;} OR .pad-r-1 {padding-right: 8px;}
        """
        for i in range(1, 13, 1):
            pad_right_css = f"""
            .pad-right{i} {{padding-right: {self.default_dimension_value * i}px;}}
            .pad-right{i}-sm {{padding-right: {(self.default_dimension_value * i) - 2}px;}}
            .pad-right{i}-smr {{padding-right: {(self.default_dimension_value * i) - 4}px;}}
            .pad-right{i}-smt {{padding-right: {(self.default_dimension_value * i) - 6}px;}}
            .pad-right{i}-xs {{padding-right: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_right_css, end="")
            self.padding_css_classes.append(pad_right_css)

    def gen_padding_top_helpers(self):
        """
        Generates padding_top_helpers.
        :format:
        .pad-top-1 {padding-top: 8px;} OR .pad-t-1 {padding-top: 8px;}
        """
        for i in range(1, 13, 1):
            pad_top_css = f"""
            .pad-top{i} {{padding-top: {self.default_dimension_value * i}px;}}
            .pad-top{i}-sm {{padding-top: {(self.default_dimension_value * i) - 2}px;}}
            .pad-top{i}-smr {{padding-top: {(self.default_dimension_value * i) - 4}px;}}
            .pad-top{i}-smt {{padding-top: {(self.default_dimension_value * i) - 6}px;}}
            .pad-top{i}-xs {{padding-top: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_top_css, end="")
            self.padding_css_classes.append(pad_top_css)

    def gen_padding_bottom_helpers(self):
        """
        Generates padding_bottom_helpers.
        :format:
        .pad-bottom-1 {padding-bottom: 8px;} OR .pad-b-1 {padding-bottom: 8px;}
        """
        for i in range(1, 13, 1):
            pad_bottom_css = f"""
            .pad-bottom{i} {{padding-bottom: {self.default_dimension_value * i}px;}}
            .pad-bottom{i}-sm {{padding-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .pad-bottom{i}-smr {{padding-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .pad-bottom{i}-smt {{padding-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .pad-bottom{i}-xs {{padding-bottom: {(self.default_dimension_value * i) - 7}px;}}
            """
            # print(pad_bottom_css, end="")
            self.padding_css_classes.append(pad_bottom_css)


class LineHeights:
    """
    This class generates line-height-helpers for eye.css
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        self.default_dimension_value = 8
        self.line_height_css_classes = list()

        # Run the line-height helpers
        self.gen_line_height_defaults()
        self.gen_line_height()

    @property
    def css_properties(self):
        return self.line_height_css_classes

    def gen_line_height_defaults(self):
        """_summary_
        :Date: inherit
        """
        line_height_css_defaults = f"""
        .line-height-unset {{line-height: unset;}}
        .line-height-initial {{line-height: initial;}}
        .line-height-inherit {{line-height: inherit;}}
        .line-height-normal {{line-height: normal;}}
        .line-height-100 {{line-height: 100%;}}
        """
        self.line_height_css_classes.append(line_height_css_defaults)

    def gen_line_height(self):
        """_summary_
        :Date: inherit
        """
        for i in range(1, 13, 1):
            line_height_css = f"""
            .line-height-{i} {{line-height: {i}px;}}
            """
            self.line_height_css_classes.append(line_height_css)


class ZIndex:
    """
    This Class defined z-index css properties.
    :Date: June 27, 2022.
    """

    def __init__(self) -> None:
        self.zindex_css_classes = list()
        self.zindex_default_helpers()
        self.zindex_helpers()
        self.negative_zindex_helpers()

    @property
    def css_properties(self):
        return self.zindex_css_classes

    def zindex_default_helpers(self):
        """
        :Date: June 27, 2022.
        """
        zindex_default_css = f"""
        .z-index-auto {{z-index: auto;}}
        .z-index-initial {{z-index: initial;}}
        .z-index-inherit {{z-index: inherit;}}
        .z-index-unset {{z-index: unset;}}
        .z-index-100 {{z-index: 100;}}
        .z-index-1000 {{z-index: 1000;}}
        .neg\:z-index-100 {{z-index: -100;}}
        .neg\:z-index-1000 {{z-index: -1000;}}
        """
        self.zindex_css_classes.append(zindex_default_css)

    def zindex_helpers(self):
        """
        :Date: June 27, 2022.
        """
        for i in range(0, 11, 1):
            zindex_helper_css = f"""
            z-index-{i} {{z-index: {i}}}
            """
            self.zindex_css_classes.append(zindex_helper_css)

    def negative_zindex_helpers(self):
        """
        :Date: June 27, 2022.
        """
        for i in range(0, 11, 1):
            negative_zindex_helper_css = f"""
            .neg\:z-index-{i} {{z-index: {-i}}}
            """
            self.zindex_css_classes.append(negative_zindex_helper_css)


class Radius:
    """
    Radius class generates border-radius helpers for eye.css
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        self.default_dimension_value = 8
        self.radius_css_classes = list()
        self.default_dimension_value = 8
        self.default_radius = 8
        self.default_radius_circle = "50% 50%"
        self.default_radius_round = "100px 100px"

        # Call all radius_css_helpers()
        self.radius_circle()
        self.radius_round()
        self.radius()
        self.radius_top()
        self.radius_bottom()

    @property
    def css_properties(self):
        return self.radius_css_classes

    def radius_circle(self):
        """:Date: inherit"""
        radius_circle_css = f"""
        .radius-circle {{border-radius: {self.default_radius_circle};}}
        """
        self.radius_css_classes.append(radius_circle_css)

    def radius_round(self):
        """:Date: inherit"""
        radius_round_css = f"""
        .radius-round {{border-radius: {self.default_radius_round};}}
        """
        self.radius_css_classes.append(radius_round_css)

    def radius(self):
        """:Date: inherit"""
        radius_css = f"""
        .radius {{border-radius: {self.default_radius}px;}}   /* =8px */
        .radius-sm {{border-radius: {self.default_radius - (2 * 1)}px;}}   /* =6px */
        .radius-smr {{border-radius: {self.default_radius - (2 * 2)}px;}}  /* =4px */
        .radius-smt {{border-radius: {self.default_radius - (2 * 3)}px;}}  /* =2px */
        .radius-xs {{border-radius: {self.default_radius - (2 * 4) + 1}px;}}  /* =1px */
        
        .radius2 {{border-radius: {self.default_radius * 2};}}   /* =8px * 2 */
        .radius2-sm {{border-radius: {(self.default_radius * 2) - (2 * 1)}px;}}   /* =14px i.e., (16 - 2)px */
        .radius2-smr {{border-radius: {(self.default_radius * 2) - (2 * 2)}px;}}  /* =12px i.e., (16 - 4)px */
        .radius2-smt {{border-radius: {(self.default_radius * 2) - (2 * 3)}px;}}  /* =10px i.e., (16 - 6)px */
        .radius2-xs {{border-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}  /* =9px i.e., (16 - 8 + 1)px */
        """
        self.radius_css_classes.append(radius_css)

    def radius_top(self):
        """:Date: inherit"""
        radius_top_css = f"""
        .radius-top {{border-top-left-radius: {self.default_radius}px; border-top-right-radius: {self.default_radius}px;}}
        .radius-top-sm {{border-top-left-radius: {self.default_radius - (2 * 1)}px; border-top-right-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-top-smr {{border-top-left-radius: {self.default_radius - (2 * 2)}px; border-top-right-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-top-smt {{border-top-left-radius: {self.default_radius - (2 * 3)}px; border-top-right-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-top-xs {{border-top-left-radius: {self.default_radius - (2 * 4) + 1}px; border-top-right-radius: {self.default_radius - (2 * 4) + 1}px;}}

        .radius-top-left {{border-top-left-radius: {self.default_radius}px;}}
        .radius-top-left-sm {{border-top-left-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-top-left-smr {{border-top-left-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-top-left-smt {{border-top-left-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-top-left-xs {{border-top-left-radius: {self.default_radius - (2 * 4) + 1}px;}}
        
        .radius-top-right {{border-top-right-radius: {self.default_radius}px;}}
        .radius-top-right-sm {{border-top-right-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-top-right-smr {{border-top-right-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-top-right-smt {{border-top-right-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-top-right-xs {{border-top-right-radius: {self.default_radius - (2 * 4) + 1}px;}}
        
        .radius2-top {{border-top-left-radius: {(self.default_radius * 2)}px; border-top-right-radius: {(self.default_radius * 2)}px;}}
        .radius2-top-sm {{border-top-left-radius: {(self.default_radius * 2) - (2 * 1)}px; border-top-right-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-top-smr {{border-top-left-radius: {(self.default_radius * 2) - (2 * 2)}px; border-top-right-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-top-smt {{border-top-left-radius: {(self.default_radius * 2) - (2 * 3)}px; border-top-right-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-top-xs {{border-top-left-radius: {(self.default_radius * 2) - (2 * 4) + 1}px; border-top-right-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}

        .radius2-top-left {{border-top-left-radius: {(self.default_radius * 2)}px;}}
        .radius2-top-left-sm {{border-top-left-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-top-left-smr {{border-top-left-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-top-left-smt {{border-top-left-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-top-left-xs {{border-top-left-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}
        
        .radius2-top-right {{border-top-right-radius: {(self.default_radius * 2)}px;}}
        .radius2-top-right-sm {{border-top-right-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-top-right-smr {{border-top-right-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-top-right-smt {{border-top-right-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-top-right-xs {{border-top-right-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}
        """
        self.radius_css_classes.append(radius_top_css)

    def radius_bottom(self):
        """:Date: inherit"""
        radius_bottom_css = f"""
        .radius-bottom {{border-bottom-left-radius: {self.default_radius}px; border-bottom-right-radius: {self.default_radius}px;}}
        .radius-bottom-sm {{border-bottom-left-radius: {self.default_radius - (2 * 1)}px; border-bottom-right-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-bottom-smr {{border-bottom-left-radius: {self.default_radius - (2 * 2)}px; border-bottom-right-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-bottom-smt {{border-bottom-left-radius: {self.default_radius - (2 * 3)}px; border-bottom-right-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-bottom-xs {{border-bottom-left-radius: {self.default_radius - (2 * 4) + 1}px; border-bottom-right-radius: {self.default_radius - (2 * 4) + 1}px;}}

        .radius-bottom-left {{border-bottom-left-radius: {self.default_radius}px;}}
        .radius-bottom-left-sm {{border-bottom-left-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-bottom-left-smr {{border-bottom-left-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-bottom-left-smt {{border-bottom-left-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-bottom-left-xs {{border-bottom-left-radius: {self.default_radius - (2 * 4) + 1}px;}}
        
        .radius-bottom-right {{border-bottom-right-radius: {self.default_radius}px;}}
        .radius-bottom-right-sm {{border-bottom-right-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-bottom-right-smr {{border-bottom-right-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-bottom-right-smt {{border-bottom-right-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-bottom-right-xs {{border-bottom-right-radius: {self.default_radius - (2 * 4) + 1}px;}}
        
        .radius2-bottom {{border-bottom-left-radius: {(self.default_radius * 2)}px; border-bottom-right-radius: {(self.default_radius * 2)}px;}}
        .radius2-bottom-sm {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 1)}px; border-bottom-right-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-bottom-smr {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 2)}px; border-bottom-right-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-bottom-smt {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 3)}px; border-bottom-right-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-bottom-xs {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 4) + 1}px; border-bottom-right-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}

        .radius2-bottom-left {{border-bottom-left-radius: {(self.default_radius * 2)}px;}}
        .radius2-bottom-left-sm {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-bottom-left-smr {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-bottom-left-smt {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-bottom-left-xs {{border-bottom-left-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}
        
        .radius2-bottom-right {{border-bottom-right-radius: {(self.default_radius * 2)}px;}}
        .radius2-bottom-right-sm {{border-bottom-right-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-bottom-right-smr {{border-bottom-right-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-bottom-right-smt {{border-bottom-right-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-bottom-right-xs {{border-bottom-right-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}
        """
        self.radius_css_classes.append(radius_bottom_css)


class Squares:
    """
    Squares css classes.
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        self.square_css_classes = list()
        self.default_square_value = 8

        self.gen_square()

        # square_css_header = (
        #     """
        # ///////////////////////
        # /* SQUARE CSS HEADER */
        # ///////////////////////
        # """.lstrip(
        #         "\n"
        #     )
        #     .strip(" ")
        #     .replace(" ", "")
        # )
        # square_css_comment = "{}".format(square_css_header)

        # print(self.format_css_list(self.square_css_classes))
        # with open("eye_gen.css", "w+") as open_file:
        #     open_file.write(square_css_comment)
        #     open_file.writelines(self.format_css_list(self.square_css_classes))
        #     # print(self.square_css_classes, file=open_file)
        #     open_file.close()

    # def format_css_list(self, css_list):
    #     css_list = [each_item.lstrip("\n").strip(" ") for each_item in css_list]
    #     return css_list

    # def minify_css_list(self, css_list):
    #     css_list = [
    #         each_item.lstrip("\n").rstrip("\n").strip(" ").replace("\n", "")
    #         for each_item in css_list
    #     ]
    #     return css_list

    @property
    def css_properties(self):
        return self.square_css_classes

    def gen_square(self):
        """:Date: inherit"""
        for i in range(1, 13, 1):
            square_css = f"""
            .square-{i} {{width: {i * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_css)
        # return self.square_css_classes


class Texts:
    """
    Texts css classes.
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        self.text_css_classes = list()
        self.default_text_value = 16
        self.default_font_thin = 100
        self.default_font_extralight = 200
        self.default_font_light = 300
        self.default_font_normal = 400
        self.default_font_medium = 500
        self.default_font_semibold = 600
        self.default_font_bold = 700
        self.default_font_extrabold = 800
        self.default_font_black = 900

        # generate the text css helpers
        self.text_align()
        self.text_styles()
        self.text_weight()

    @property
    def css_properties(self):
        return self.text_css_classes

    def text_align(self):
        """:Date: inherit"""
        text_align_css = f"""
        .text-center {{text-align: center;}}
        .text-left {{text-align: left;}}
        .text-right {{text-align: right;}}
        .text-justify {{text-align: justify;}}
        """
        self.text_css_classes.append(text_align_css)
        # return self.text_css_classes

    def text_styles(self):
        """:Date: inherit"""
        text_styles_css = f"""
        .font-italic {{font-style: italic;}}
        """
        self.text_css_classes.append(text_styles_css)

    def text_weight(self):
        """:Date: inherit"""
        text_weight_css = f"""
        .font-thin {{font-weight: {self.default_font_thin};}}
        .font-extralight {{font-weight: {self.default_font_extralight};}}
        .font-light {{font-weight: {self.default_font_light};}}
        .font-normal {{font-weight: {self.default_font_normal};}}
        .font-medium {{font-weight: {self.default_font_medium};}}
        .font-semibold {{font-weight: {self.default_font_semibold};}}
        .font-bold {{font-weight: {self.default_font_bold};}}
        .font-extrabold {{font-weight: {self.default_font_extrabold};}}
        .font-black {{font-weight: {self.default_font_black};}}
        """
        self.text_css_classes.append(text_weight_css)

    def text_size(self):
        """:Date: inherit"""
        text_size_css = f"""
        .text-xs {{font-size: }}
        """
        pass


class Colors:
    """
    Colors css classes.
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        pass

    def default_colors(self):
        """
        :Date: June 27, 2022.
        """
        pass


class Borders:
    """
    Border css classes.
    :Date: June 27, 2022.
    """

    def __init__(self) -> None:
        self.border_css_classes = list()

    @property
    def css_properties(self):
        return self.border_css_classes

    def border_width(self):
        """
        :Date: June 27, 2022.
        """
        border_css = f"""
        .border {{box-shadow: 0 0 0 1px lightgray;}}
        """
        self.border_css_classes.append(border_css)
        for i in range(2, 24, 2):
            border_css = f"""
            .border {{box-shadow: 0 0 0 {i}px lightgray;}}
            """
            self.border_css_classes.append(border_css)

    def border_color(self):
        pass


if "__main__" == __name__:
    CSSGenerator().write_styles()
