# MAYOWA OBISESAN
# eye.css GENERATOR
# JUNE 15, 2022.

# This script generates eye.css styles.
# The use of this script is just to generate a nicely formatted string of css-styles.

# JUNE 19, 2022.
# One of the philosophies of eye.css is that:
# "What should not be difficult should not be programmed unnecessarily complex."

# JULY 18, 2022.
# 1.    Another eye.css philosophy: Use the simplest form of any value. - July 18, 2022.
# e.g., define border-top-style and border-right-style instead of defining border-top-right-style in eye.css
# 2.    All values that are rarely used should be explicitly defined. - July 18, 2022.
# e.g., "border-right-style-revert-layer"

import os
import re


class CSSGenerator:
    """
    This class generates eye.css file
    :Date: June 19, 2022.
    :return: A File object - an eye.css file / eye.min.css
    """

    def __init__(self) -> None:
        self.eye_css_filename = "eye_gen.css"
        self.css_file_created = False
        self.first_level_base_class_pseudo = ("pct", "em", "pc", "pt", "rem", "vw", "vh", "neg", "shadow",
                                              "drop-shadow", "gradient", "radial-gradient", "conic-gradient",
                                              "repeating-linear-gradient", "repeating-radial-gradient",
                                              "repeating-conic-gradient", "transform", "transform-origin",
                                              "transition", "animation", "border", "outline")
        self.default_pseudo_element_list = ("after", "before", "first-letter", "first-line", "marker", "placeholder",
                                            "selection", "motion-reduce", "motion-safe", "contrast-more", "print",
                                            "portrait", "landscape")
        self.default_pseudo_group_list = ("all", "parent", "child", "every", "children", "sibling")
        self.default_pseudo_class_list = ('hover', 'focus', 'focus-within', 'focus-visible', 'active', 'visited',
                                          'target', 'first-child', 'last-child', 'only-child', 'nth-child(odd)',
                                          'nth-child(even)', 'first-of-type', 'last-of-type', 'only-of-type',
                                          'empty', 'disabled', 'checked', 'indeterminate', 'default', 'required',
                                          'valid', 'invalid', 'in-range', 'out-of-range', 'placeholder-shown',
                                          'autofill', 'read-only')
        self.default_pseudo_theme_list = ("dark",)
        self.default_media_query_list = ("sm", "md", "lg", "xl", "xxl")

        # MEDIA QUERIES - DEFINITIONS
        self.sm_media_query_definition = "@media (min-width: 640px)"
        self.md_media_query_definition = "@media (min-width: 768px)"
        self.lg_media_query_definition = "@media (min-width: 1024px)"
        self.xl_media_query_definition = "@media (min-width: 1280px)"
        self.xxl_media_query_definition = "@media (min-width: 1536px)"

        """
        NOVEMBER 07, 2022.
        Based on w3schools media breakpoints
        /* Extra small devices (phones, 600px and down) */
        @media only screen and (max-width: 600px) {...}
        
        /* Small devices (portrait tablets and large phones, 600px and up) */
        @media only screen and (min-width: 600px) {...}
        
        /* Medium devices (landscape tablets, 768px and up) */
        @media only screen and (min-width: 768px) {...}
        
        /* Large devices (laptops/desktops, 992px and up) */
        @media only screen and (min-width: 992px) {...}
        
        /* Extra large devices (large laptops and desktops, 1200px and up) */
        @media only screen and (min-width: 1200px) {...}
        """

        self.default_media_query_dict = {
            "sm": "@media (min-width: 640px)",
            "md": "@media (min-width: 768px)",
            "lg": "@media (min-width: 1024px)",
            "xl": "@media (min-width: 1280px)",
            "xxl": "@media (min-width: 1536px)"
        }
        self.dimension_type_list = ("px", "pct", "em", "rem", "pc", "pt", "vh", "vw", "vmin", "vmax")
        self.positions_type_list = ("top", "right", "bottom", "left")
        self.positions_abbreviation_type_list = ("x", "y", "t", "r", "b", "l")

    def create_css_generator_file(self):
        with open(self.eye_css_filename, "w+") as opened_file:
            opened_file.write("")
            opened_file.close()
            self.css_file_created = True

    @classmethod
    def format_css_list(cls, css_list):
        """:Date: inherit"""
        css_list = [re.sub(r"\n\s*", "\n", each_item) for each_item in css_list]
        return css_list

    @staticmethod
    def minify_css_list(css_list):
        """:Date: inherit"""
        css_list = [
            re.sub(r"\n\s*", "", each_item)
            for each_item in css_list
        ]
        return css_list

    @staticmethod
    def eye_init():
        """:Date: July 1, 2022."""
        eye_init_css = f"""
        * {{
            -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;
            text-rendering: auto;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: antialiased; /* | grayscale*/
            /* font-family: "system-ui" */
        }}
        *::-webkit-scrollbar {{
            width: 8px;
            height: 100%;
            min-height: 8px;    /* For horizontal scrollbar to display. */
            max-height: 8px;    /* For horizontal scrollbar to display. */
            background-color: #EEEEEE;
        }}
        *::-webkit-scrollbar-thumb {{
            background-color: #D7D7D7;
        }}
        *::-webkit-scrollbar-track {{
            background-color: #F3F3F3;
        }}
        *::-webkit-scrollbar-track-piece {{}}
        *::-webkit-scrollbar-corner {{}}
        *::-webkit-resizer {{}}
        """
        return [eye_init_css]

    def css_properties(self):
        """
        All the defined css property classes.
        :Date: inherit
        """
        # css_properties_list = Squares() + FlexBox() + Paddings()
        css_properties_list = [
            *self.eye_init(),
            *Root().css_properties,
            *Positions().css_properties,
            *Displays().css_properties,
            *VerticalAlign().css_properties,
            *FlexBox().css_properties,
            *Widths().css_properties,
            *Heights().css_properties,
            *LineHeights().css_properties,
            *Squares().css_properties,
            *Squircles().css_properties,
            *Margins().css_properties,
            *Paddings().css_properties,
            *Radius().css_properties,
            *Texts().css_properties,
            *ZIndex().css_properties,
            *Borders().css_properties,
            *Outlines().css_properties,
            *Colors().css_properties,
            *Backgrounds().css_properties,
            *Overflows().css_properties,
            *Legacys().css_properties,
            *BoxShadows().css_properties,
            *Opacity().css_properties,
            *Object().css_properties,
            *OverScrolls().css_properties,
            *Isolation().css_properties,
            *Resize().css_properties,
            *PointerEvents().css_properties,
            *AccentColor().css_properties,
            *BackFace().css_properties,
            *BlockSize().css_properties,
            *Separator().css_properties,
            *BackDrops().css_properties,
            *Filters().css_properties,
            *ScrollBehaviors().css_properties,
            *ScrollSnaps().css_properties,
            *Transforms().css_properties,
            *List().css_properties,
            *Visibility().css_properties,
        ]
        # print(css_properties_list)
        return css_properties_list

    def css_dictionary(self):
        """
        All the defined css property classes as a dict.
        :Date: July 25, 2022.
        """
        css_properties_text = "".join(self.css_properties())
        return self.convert_css_to_dict(css_properties_text, add_braces=True)

    def css_templates(self):
        """ All CSS Templates property classes.
        :Date: August 9, 2022.
        """
        css_templates_list = [
            *Positions().css_template,
            *Widths().css_template,
            *Heights().css_template,
            *Paddings().css_template,
            *Margins().css_template,
            *LineHeights().css_template,
            *ZIndex().css_template,
            *Opacity().css_template,
            *Texts().css_template,
            *Colors().css_template,
            *Backgrounds().css_template,
            *AccentColor().css_template,
            *Borders().css_template,
            *Outlines().css_template,
            *Separator().css_template,
            *Transforms().css_template,
        ]
        return css_templates_list

    def css_templates_dictionary(self):
        """ All CSS Templates as a Dictionary.
        :Date: August 10, 2022.
        """
        css_properties_text = "".join(self.css_templates())
        return self.convert_css_to_dict(css_properties_text, add_braces=True)

    @staticmethod
    def float_range(start, stop=None, step=None):
        # Copied from https://www.techbeamers.com/python-float-range/ - July 19, 2022.
        # Use float number in range() function
        # if stop and step argument is null set start=0.0 and step = 1.0
        if stop is None:
            stop = start + 0.0
            start = 0.0
        if step is None:
            step = 1.0
        while True:
            if step > 0 and start >= stop:
                break
            elif step < 0 and start <= stop:
                break
            yield "%g" % start  # return float number
            start = start + step

    @staticmethod
    def iter_range(start, stop, step):
        # Another way to perform float range. - July 19, 2022. - https://www.techbeamers.com/python-float-range/
        from itertools import islice, count

        if step == 0:
            raise ValueError("Step could not be NULL")
        length = int(abs(stop - start) / step)
        return islice(count(start, step), length)

        # for it in iter_range(0, 10, 1.10):
        #     print("{0:.1f}".format(it), end=" ")

    @staticmethod
    def convert_css_to_dict(css_text: str, add_braces: bool = False):
        """
        A helper function to convert css to dict.
        :Date: July 25, 2022. - Added to CSSGenerator class from EyeWriter class.
        """
        css_dict = dict()

        css_list = css_text.rsplit('}')
        for each_css_rule in CSSGenerator.minify_css_list(css_list):
            if each_css_rule not in [None, ""]:
                css_rule_token = each_css_rule.split('{')
                cleaned_css_key = css_rule_token[0].replace(" ", "")
                cleaned_css_values = css_rule_token[1]
                if add_braces:
                    cleaned_css_values = f"{{{cleaned_css_values}}}"
                css_dict[cleaned_css_key] = cleaned_css_values

        return css_dict

    @staticmethod
    def convert_dict_to_css(css_dict: dict, as_list=False, as_dict_str=False) -> (str|list|dict):
        """
        A helper function to convert a dict to css
        :param css_dict: The dictionary to convert to a css string
        :param as_list: A boolean argument to indicate whether to return the css as a list.
        :Date: August 13, 2022.
        """
        assert isinstance(css_dict, dict), "argument must be a dictionary instance."

        css_as_dict_store = {}
        css_as_str_store = ""
        css_as_list_store = []
        for k, v in css_dict.items():
            if type(v) is dict:
                if len(v) > 0:
                    vres = ""
                    for i, j in v.items():
                        vres += f"{i} {j}"
                    css_as_str_store += f"{k} {{{vres}}}"
                    css_as_dict_store[k] = f"{{{vres}}}"
                    css_as_list_store.append(f"{k} {{{vres}}}")
                else:
                    css_as_str_store += f"{k} {v}"
                    css_as_dict_store[k] = f"{v}"
                    css_as_list_store.append(f"{k} {v}")
            else:
                css_as_str_store += f"{k} {v}"
                css_as_dict_store[k] = f"{v}"
                css_as_list_store.append(f"{k} {v}")

        if as_list:
            return css_as_list_store
        elif as_dict_str:
            return css_as_dict_store
        return css_as_str_store

    def is_base_css_class_valid(self, css_class_str) -> bool:
        """ Function to check if a base css class is valid.
        How??:
        1.  Check the css_class_str against eye.css default css dictionary
        2.  If (1.) above is false, it means css_class_str is a dynamically defined css property,
        3.  Check if css_class_str partitioned "lhs" is contained within eye.css default css dictionary
        :param css_class_str: An eye.css css_class_str
        :return: bool
        :rtype: bool
        :Date: August 7, 2022.
        """
        if css_class_str in self.css_dictionary().keys():
            return True
        return False

    def is_base_css_class_dynamically_defined(self, css_class_str) -> bool:
        """ Function to check if a base_css class is dynamically defined.
        :Date: August 8, 2022.
        """
        pass

    @staticmethod
    def is_css_color_property(css_class_str) -> bool:
        """ A Function to detect if a css_class_str is a valid color property.
        For instance, .pct:w-100 is not a valid color property, .border-34ECB2 is a valid color property
        :param css_class_str: The css_class_str to validate. e.g., opacity-0.45, border-35 not "border" or "outline"
        :return: bool
        :Date: August 10, 2022.
        """
        eye_css_color_property_element_list = ["bg", "color", "border", "accent", "outline", "sep"]
        if css_class_str.lstrip(".").split("-")[0] in eye_css_color_property_element_list:
            return True
        return False

    @staticmethod
    def is_color_code(color_code) -> bool:
        """ Function to validate a hex color code
        :param color_code: The color_code to validate.
        :return: bool
        :Date: August 10, 2022.
        """
        # Convert the color code to upper.
        color_code = color_code.upper()
        if len(color_code) in [3, 4, 6, 8] and re.match(r"\b[0-9A-F]{3,4}\b|\b[0-9A-F]{6}\b|\b[0-9A-F]{8}\b", color_code):
            return True  # Color code is valid
        return False

    @staticmethod
    def is_valid_color_name(color_name: str) -> bool:
        """
        Function to validate a color name as a standard color name
        :param color_name: The color_name to validate
        :Date: August 14, 2022
        """
        if color_name.lower() in Root().color_dictionary().keys():
            return True
        return False

    @staticmethod
    def is_dimensionless_css_property(css_class_str: str) -> bool:
        """ A Function to detect if a css_class_str is a dimensionless_css_property, not if a token is
        i.e., css_class_str must be of the form: ".opacity-0.4", not just "opacity"
        :param css_class_str: The css_class_str to validate. e.g., opacity-0.45, border-35 not "border" or "outline"
        :Date: August 10, 2022.
        """
        dimensionless_css_property_list = ["z", "opacity", "scale"]
        # if css_class_str.split("-")[0].split(":")[-1].strip(".").strip("\\") in dimensionless_css_property_list:
        if "".join(re.findall(r'(\b^z$\b|\b^opacity$\b|\b^scale$\b)', css_class_str)) in dimensionless_css_property_list:
            return True
        return False

    @staticmethod
    def is_zindex_dimension_valid(value: (int | str)) -> bool:
        if str(value).isdigit() and int(value) <= 10000:
            return True
        return False


class Root:
    """ :Date: June 30, 2022. """

    def __init__(self) -> None:
        self.default_dimension_px_value = 8
        self.root_css_classes = list()
        self.color_table_list = list()
        # self.colors_dict = dict()
        self.default_color_white = "hsla(0, 0%, 100%, .9)"
        self.default_color_white_solid = "hsla(0, 0%, 100%, 1)"
        self.default_color_white_disabled = "hsla(0, 0%, 60%, 0.2)"
        self.default_color_white_transparent = "hsla(0, 0%, 100%, .8)"

        self.default_color_black = "hsla(0, 0%, 0%, 1)"
        self.default_color_black_transparent = "hsla(0, 0%, 0%, .9)"

        self.default_color_light = "hsla(0, 0%, 82.7%, 0.9)"
        self.default_color_light_hover = "hsla(0, 0%, 72.7%, 0.9)"
        self.default_color_light_disabled = "hsla(0, 0%, 62.7%, 0.8)"
        self.default_color_light_solid = "hsla(0, 0%, 82.7%, 1)"

        self.default_color_lighter = "hsla(0, 0%, 96.1%, 0.9)"
        self.default_color_lighter_hover = "hsla(0, 0%, 86.1%, 0.9)"
        self.default_color_lighter_disabled = "hsla(0, 0%, 76.1%, 0.9)"
        self.default_color_lighter_solid = "hsla(0, 0%, 96.1%, 1)"

        self.default_color_green = "hsla(120, 76.5%, 33.3%, 0.7)"
        self.default_color_green_hover = "hsla(120, 96.5%, 23.3%, 0.7)"
        self.default_color_green_inverse = "hsla(120, 76.5%, 33.3%, 0.2)"
        self.default_color_green_inverse_hover = "hsla(120, 76.5%, 33.3%, 0.4)"
        self.default_color_green_border = "hsla(120, 76.5%, 33.3%, 0.4)"
        self.default_color_green_dark = "hsl(120, 76.5%, 33.3%)"
        self.default_color_green_disabled = "hsla(120, 76.5%, 23.3%, 0.2)"
        self.default_color_green_solid = "hsla(120, 76.5%, 33.3%, 1)"

        self.default_color_blue = "hsla(208, 95.2%, 58.8%, 0.9)"
        self.default_color_blue_hover = "hsla(210, 85.2%, 48.8%, 0.9)"
        self.default_color_blue_inverse = "hsla(206.1, 95.8%, 52.9%, 0.2)"
        self.default_color_blue_inverse_hover = "hsla(206.1, 95.8%, 52.9%, 0.4)"
        self.default_color_blue_dark = "hsl(208, 95.8%, 52.9%)"
        self.default_color_blue_border = "hsla(208, 95.8%, 52.9%, 0.4)"
        self.default_color_blue_disabled = "hsla(208, 85.8%, 42.9%, 0.4)"
        self.default_color_blue_solid = "hsla(208, 95.2%, 58.8%, 1)"

        self.default_color_red = "hsla(0, 88.3%, 40.4%, 0.9)"
        self.default_color_red_hover = "hsla(0, 88.3%, 45.4%, 0.9)"
        self.default_color_red_disabled = "hsla(0, 48.3%, 70.4%, 0.8)"
        self.default_color_red_inverse = "hsla(0, 88.3%, 60.4%, 0.2)"
        self.default_color_red_inverse_hover = "hsla(0, 88.3%, 60.4%, 0.4)"
        self.default_color_red_border = "hsla(0, 68.3%, 60.4%, 0.2)"
        self.default_color_red_dark = "hsl(0, 88.3%, 60.4%)"
        self.default_color_red_solid = "hsla(0, 88.3%, 40.4%, 1)"

        self.default_color_itheirs = "hsla(48, 95.2%, 58.8%, 0.9)"

        self.default_color_itheirs_hover = "hsla(48, 95.2%, 48.8%, 0.9)"
        self.default_color_itheirs_disabled = "hsla(48, 95.2%, 48.8%, 0.2)"
        self.default_color_itheirs_border = "hsla(36, 90.9%, 78.4%, 0.9)"
        self.default_color_itheirs_inverse = "hsla(48, 95.2%, 48.8%, 0.3)"
        self.default_color_itheirs_inverse_hover = "hsla(48, 95.2%, 58.8%, 0.5)"
        self.default_color_itheirs_dark = "hsl(39, 95.2%, 58.8%)"
        self.default_color_itheirs_solid = "hsla(48, 95.2%, 58.8%, 1)"

        self.default_color_purple = "hsla(278, 100%, 19.2%, 0.9)"
        self.default_color_purple_hover = "hsla(278, 100%, 24.2%, 0.9)"
        self.default_color_purple_disabled = "hsla(278, 40%, 59.2%, 0.9)"
        self.default_color_purple_inverse = "hsla(278, 100%, 39.2%, 0.15)"
        self.default_color_purple_inverse_hover = "hsla(278, 100%, 39.2%, 0.3)"
        self.default_color_purple_border = "hsla(278, 50%, 39.2%, 0.4)"
        self.default_color_purple_dark = "hsl(278, 50%, 29.2%)"
        self.default_color_purple_solid = "hsla(278, 100%, 19.2%, 1)"

        self.gen_root()
        self.default_variables()
        self.color_table()

    @staticmethod
    def default_variables():
        f"""
            /* DEFINING COLORS TO BE USED ON iTheirs - 021021. */
            /*lightgray == #D3D3D3 == rgb(211, 211, 211) = hsl(0, 0%, 82.7%);*/
            /* iTheirs COLORS - 05TH OCTOBER, 2021. */
            
            /*--default_color_gold = "hsla(40, 88.3%, 50.4%, 0.96);*/
            /*--default_color_red = "hsla(0, 68.3%, 60.4%, 0.9);*/
            /*
            1.  On hover of colors, it becomes darker and looses some or all of it's transparency.
            Think of a Plantain leaf. When it is covered, it's color becomes darker and less transparent. - 05TH OCTOBER, 2021.
            2.  Disabled:  Light colors become dark when disabled, and Dark colors becomes Light when Disabled.;
            3.  Hover: Dark Colors becomes Lighter and Light Colors become dark;
            4.  Hover: Increase the Saturation and Reduce the Lightness for a Beautiful Hover Color.;
            */
        """
        pass

    @property
    def css_properties(self):
        """ :Date: inherit """
        return self.root_css_classes

    def gen_root(self):
        """ :Date: inherit """
        # --font-small: calc((14/16) * 1rem); /* 14px */
        # --font-default: calc((16/16) * 1rem); /* 16px */
        # --font-large: calc((24/16) * 1rem); /* 24px */
        root_css = f""":root {{
            --default_font_h1: {(32 / 16) * 1}rem;
            --default_font_h2: {(24 / 16) * 1}rem;
            --default_font_h3: {(18.72 / 16) * 1}rem;
            --default_font_h4: {(16 / 16) * 1}rem;
            --default_font_h5: {(13.28 / 16) * 1}rem;
            --default_font_h6: {(10.72 / 16) * 1}rem;
            
            /* Define css colors variables - July 1, 2022. */
            --default_color_white: hsla(0, 0 %, 100 %, .9);
            --default_color_white_solid: hsla(0, 0 %, 100 %, 1);
            --default_color_white_disabled: hsla(0, 0 %, 60 %, 0.2);
            --default_color_white_transparent: hsla(0, 0 %, 100 %, .8);
        }}"""
        self.root_css_classes.append(root_css)

    def appearance(self):
        appearance_css = f"""
        .appearance-none {{appearance: none;}}
        """
        self.root_css_classes.append(appearance_css)

    def box_sizing(self):
        box_sizing_css = f"""
        .box-border {{box-sizing: border-box;}}
        .box-content {{box-sizing: content-box;}}
        """
        self.root_css_classes.append(box_sizing_css)

    def colors_groups(self):
        """
        Colors definition for eye.css
        This color codes are the default colors acceptable in all browsers with years of support.
        :Date: July 28, 2022. """
        # PINK COLOR GROUP
        self.color_pink = ("pink", "#FFC0CB")
        self.color_lightpink = ("lightpink", "#FFB6C1")
        self.color_hotpink = ("hotpink", "#FF69B4")
        self.color_deeppink = ("deeppink", "#FF1493")
        self.color_palevioletred = ("palevioletred", "#DB7093")
        self.color_mediumvioletred = ("mediumvioletred", "#C71585")

        # PURPLE COLOR GROUP
        self.color_lavender = ("lavender", "#E6E6FA")
        self.color_thistle = ("thistle", "#D8BFD8")
        self.color_plum = ("plum", "#DDA0DD")
        self.color_orchid = ("orchid", "#DA70D6")
        self.color_violet = ("violet", "#EE82EE")
        self.color_fuchsia = ("fuchsia", "#FF00FF")
        self.color_magenta = ("magenta", "#FF00FF")
        self.color_mediumorchid = ("mediumorchid", "#BA55D3")
        self.color_darkorchid = ("darkorchid", "#9932CC")
        self.color_darkviolet = ("darkviolet", "#9400D3")
        self.color_blueviolet = ("blueviolet", "#8A2BE2")
        self.color_darkmagenta = ("darkmagenta", "#8B008B")
        self.color_purple = ("purple", "#800080")
        self.color_mediumpurple = ("mediumpurple", "#9370DB")
        self.color_mediumslateblue = ("mediumslateblue", "#7B68EE")
        self.color_slateblue = ("slateblue", "#6A5ACD")
        self.color_darkslateblue = ("darkslateblue", "#483D8B")
        self.color_rebeccapurple = ("rebeccapurple", "#663399")
        self.color_indigo = ("indigo", "#4B0082")

        # RED COLOR GROUP
        self.lightsalmon = ("lightsalmon", "#FFA07A")
        self.salmon = ("salmon", "#FA8072")
        self.darksalmon = ("darksalmon", "#E9967A")
        self.lightcoral = ("lightcoral", "#F08080")
        self.indianred = ("indianred", "#CD5C5C")
        self.crimson = ("crimson", "#DC143C")
        self.red = ("red", "#FF0000")
        self.firebrick = ("firebrick", "#B22222")
        self.darkred = ("darkred", "#8B0000")

        # ORANGE COLOR GROUP
        self.orange = ("orange", "#FFA500")
        self.darkorange = ("darkorange", "#FF8C00")
        self.coral =( "coral", "#FF7F50")
        self.tomato = ("tomato", "#FF6347")
        self.orangered = ("orangered", "#FF4500")

        # YELLOW COLOR GROUP
        self.gold = ("gold", "#FFD700")
        self.yellow = ("yellow", "#FFFF00")
        self.lightyellow = ("lightyellow", "#FFFFE0")
        self.lemonchiffon = ("lemonchiffon", "#FFFACD")
        self.lightgoldenrodyellow = ("lightgoldenrodyellow", "#FAFAD2")
        self.papayawhip = ("papayawhip", "#FFEFD5")
        self.moccasin = ("moccasin", "#FFE4B5")
        self.peachpuff = ("peachpuff", "#FFDAB9")
        self.palegoldenrod = ("palegoldenrod", "#EEE8AA")
        self.khaki = ("khaki", "#F0E68C")
        self.darkkhaki = ("darkkhaki", "#BDB76B")

        # GREEN COLOR GROUP
        self.greenyellow = ("greenyellow", "#ADFF2F")
        self.chartreuse = ("chartreuse", "#7FFF00")
        self.lawngreen = ("lawngreen", "#7CFC00")
        self.lime = ("lime", "#00FF00")
        self.limegreen = ("limegreen", "#32CD32")
        self.palegreen = ("palegreen", "#98FB98")
        self.lightgreen = ("lightgreen", "#90EE90")
        self.mediumspringgreen = ("mediumspringgreen", "#00FA9A")
        self.springgreen = ("springgreen", "#00FF7F")
        self.mediumseagreen = ("mediumseagreen", "#3CB371")
        self.seagreen = ("seagreen", "#2E8B57")
        self.forestgreen = ("forestgreen", "#228B22")
        self.green = ("green", "#008000")
        self.darkgreen = ("darkgreen", "#006400")
        self.yellowgreen = ("yellowgreen", "#9ACD32")
        self.olivedrab = ("olivedrab", "#6B8E23")
        self.darkolivegreen = ("darkolivegreen", "#556B2F")
        self.mediumaquamarine = ("mediumaquamarine", "#66CDAA")
        self.darkseagreen = ("darkseagreen", "#8FBC8F")
        self.lightseagreen = ("lightseagreen", "#20B2AA")
        self.darkcyan = ("darkcyan", "#008B8B")
        self.teal = ("teal", "#008080")

        # CYAN COLOR GROUP
        self.aqua = ("aqua", "#00FFFF")
        self.cyan = ("cyan", "#00FFFF")
        self.lightcyan = ("lightcyan", "#E0FFFF")
        self.paleturquoise = ("paleturquoise", "#AFEEEE")
        self.aquamarine = ("aquamarine", "#7FFFD4")
        self.turquoise = ("turquoise", "#40E0D0")
        self.mediumturquoise = ("mediumturquoise", "#48D1CC")
        self.darkturquoise = ("darkturquoise", "#00CED1")

        # BLUE COLOR GROUP
        self.cadetblue = ("cadetblue", "#5F9EA0")
        self.steelblue = ("steelblue", "#4682B4")
        self.lightsteelblue = ("lightsteelblue", "#B0C4DE")
        self.lightblue = ("lightblue", "#ADD8E6")
        self.powderblue = ("powderblue", "#B0E0E6")
        self.lightskyblue = ("lightskyblue", "#87CEFA")
        self.skyblue = ("skyblue", "#87CEEB")
        self.cornflowerblue = ("cornflowerblue", "#6495ED")
        self.deepskyblue = ("deepskyblue", "#00BFFF")
        self.dodgerblue = ("dodgerblue", "#1E90FF")
        self.royalblue = ("royalblue", "#4169E1")
        self.blue = ("blue", "#0000FF")
        self.mediumblue = ("mediumblue", "#0000CD")
        self.darkblue = ("darkblue", "#00008B")
        self.navy = ("navy", "#000080")
        self.midnightblue = ("midnightblue", "#191970")

        # BROWN COLOR GROUP
        self.cornsilk = ("cornsilk", "#FFF8DC")
        self.blanchedalmond = ("blanchedalmond", "#FFEBCD")
        self.bisque = ("bisque", "#FFE4C4")
        self.navajowhite = ("navajowhite", "#FFDEAD")
        self.wheat = ("wheat", "#F5DEB3")
        self.burlywood = ("burlywood", "#DEB887")
        self.tan = ("tan", "#D2B48C")
        self.rosybrown = ("rosybrown", "#BC8F8F")
        self.sandybrown = ("sandybrown", "#F4A460")
        self.goldenrod = ("goldenrod", "#DAA520")
        self.darkgoldenrod = ("darkgoldenrod", "#B8860B")
        self.peru = ("peru", "#CD853F")
        self.chocolate = ("chocolate", "#D2691E")
        self.olive = ("olive", "#808000")
        self.saddlebrown = ("saddlebrown", "#8B4513")
        self.sienna = ("sienna", "#A0522D")
        self.brown = ("brown", "#A52A2A")
        self.maroon = ("maroon", "#800000")

        # WHITE COLOR GROUP
        self.white = ("white", "#FFFFFF")
        self.snow = ("snow", "#FFFAFA")
        self.honeydew = ("honeydew", "#F0FFF0")
        self.mintcream = ("mintcream", "#F5FFFA")
        self.azure = ("azure", "#F0FFFF")
        self.aliceblue = ("aliceblue", "#F0F8FF")
        self.ghostwhite = ("ghostwhite", "#F8F8FF")
        self.whitesmoke = ("whitesmoke", "#F5F5F5")
        self.seashell = ("seashell", "#FFF5EE")
        self.beige = ("beige", "#F5F5DC")
        self.oldlace = ("oldlace", "#FDF5E6")
        self.floralwhite = ("floralwhite", "#FFFAF0")
        self.ivory = ("ivory", "#FFFFF0")
        self.antiquewhite = ("antiquewhite", "#FAEBD7")
        self.linen = ("linen", "#FAF0E6")
        self.lavenderblush = ("lavenderblush", "#FFF0F5")
        self.mistyrose = ("mistyrose", "#FFE4E1")

        # GREY COLOR GROUP
        self.gainsboro = ("gainsboro", "#DCDCDC")
        self.lightgray = ("lightgray", "#D3D3D3")
        self.silver = ("silver", "#C0C0C0")
        self.darkgray = ("darkgray", "#A9A9A9")
        self.dimgray = ("dimgray", "#696969")
        self.gray = ("gray", "#808080")
        self.lightslategray = ("lightslategray", "#778899")
        self.slategray = ("slategray", "#708090")
        self.darkslategray = ("darkslategray", "#2F4F4F")
        self.black = ("black", "#000000")

    def color_table(self):
        """
        Eye.css color list.
        The colors are from legacy css color
        :Date: July 29, 2022. """
        self.color_table_list = [
            ("pink", "#FFC0CB"),
            ("lightpink", "#FFB6C1"),
            ("hotpink", "#FF69B4"),
            ("deeppink", "#FF1493"),
            ("palevioletred", "#DB7093"),
            ("mediumvioletred", "#C71585"),
            ("lavender", "#E6E6FA"),
            ("thistle", "#D8BFD8"),
            ("plum", "#DDA0DD"),
            ("orchid", "#DA70D6"),
            ("violet", "#EE82EE"),
            ("fuchsia", "#FF00FF"),
            ("magenta", "#FF00FF"),
            ("mediumorchid", "#BA55D3"),
            ("darkorchid", "#9932CC"),
            ("darkviolet", "#9400D3"),
            ("blueviolet", "#8A2BE2"),
            ("darkmagenta", "#8B008B"),
            ("purple", "#800080"),
            ("mediumpurple", "#9370DB"),
            ("mediumslateblue", "#7B68EE"),
            ("slateblue", "#6A5ACD"),
            ("darkslateblue", "#483D8B"),
            ("rebeccapurple", "#663399"),
            ("indigo", "#4B0082"),
            ("lightsalmon", "#FFA07A"),
            ("salmon", "#FA8072"),
            ("darksalmon", "#E9967A"),
            ("lightcoral", "#F08080"),
            ("indianred", "#CD5C5C"),
            ("crimson", "#DC143C"),
            ("red", "#FF0000"),
            ("firebrick", "#B22222"),
            ("darkred", "#8B0000"),
            ("orange", "#FFA500"),
            ("darkorange", "#FF8C00"),
            ("coral", "#FF7F50"),
            ("tomato", "#FF6347"),
            ("orangered", "#FF4500"),
            ("gold", "#FFD700"),
            ("yellow", "#FFFF00"),
            ("lightyellow", "#FFFFE0"),
            ("lemonchiffon", "#FFFACD"),
            ("lightgoldenrodyellow", "#FAFAD2"),
            ("papayawhip", "#FFEFD5"),
            ("moccasin", "#FFE4B5"),
            ("peachpuff", "#FFDAB9"),
            ("palegoldenrod", "#EEE8AA"),
            ("khaki", "#F0E68C"),
            ("darkkhaki", "#BDB76B"),
            ("greenyellow", "#ADFF2F"),
            ("chartreuse", "#7FFF00"),
            ("lawngreen", "#7CFC00"),
            ("lime", "#00FF00"),
            ("limegreen", "#32CD32"),
            ("palegreen", "#98FB98"),
            ("lightgreen", "#90EE90"),
            ("mediumspringgreen", "#00FA9A"),
            ("springgreen", "#00FF7F"),
            ("mediumseagreen", "#3CB371"),
            ("seagreen", "#2E8B57"),
            ("forestgreen", "#228B22"),
            ("green", "#008000"),
            ("darkgreen", "#006400"),
            ("yellowgreen", "#9ACD32"),
            ("olivedrab", "#6B8E23"),
            ("darkolivegreen", "#556B2F"),
            ("mediumaquamarine", "#66CDAA"),
            ("darkseagreen", "#8FBC8F"),
            ("lightseagreen", "#20B2AA"),
            ("darkcyan", "#008B8B"),
            ("teal", "#008080"),
            ("aqua", "#00FFFF"),
            ("cyan", "#00FFFF"),
            ("lightcyan", "#E0FFFF"),
            ("paleturquoise", "#AFEEEE"),
            ("aquamarine", "#7FFFD4"),
            ("turquoise", "#40E0D0"),
            ("mediumturquoise", "#48D1CC"),
            ("darkturquoise", "#00CED1"),
            ("cadetblue", "#5F9EA0"),
            ("steelblue", "#4682B4"),
            ("lightsteelblue", "#B0C4DE"),
            ("lightblue", "#ADD8E6"),
            ("powderblue", "#B0E0E6"),
            ("lightskyblue", "#87CEFA"),
            ("skyblue", "#87CEEB"),
            ("cornflowerblue", "#6495ED"),
            ("deepskyblue", "#00BFFF"),
            ("dodgerblue", "#1E90FF"),
            ("royalblue", "#4169E1"),
            ("blue", "#0000FF"),
            ("mediumblue", "#0000CD"),
            ("darkblue", "#00008B"),
            ("navy", "#000080"),
            ("midnightblue", "#191970"),
            ("cornsilk", "#FFF8DC"),
            ("blanchedalmond", "#FFEBCD"),
            ("bisque", "#FFE4C4"),
            ("navajowhite", "#FFDEAD"),
            ("wheat", "#F5DEB3"),
            ("burlywood", "#DEB887"),
            ("tan", "#D2B48C"),
            ("rosybrown", "#BC8F8F"),
            ("sandybrown", "#F4A460"),
            ("goldenrod", "#DAA520"),
            ("darkgoldenrod", "#B8860B"),
            ("peru", "#CD853F"),
            ("chocolate", "#D2691E"),
            ("olive", "#808000"),
            ("saddlebrown", "#8B4513"),
            ("sienna", "#A0522D"),
            ("brown", "#A52A2A"),
            ("maroon", "#800000"),
            ("white", "#FFFFFF"),
            ("snow", "#FFFAFA"),
            ("honeydew", "#F0FFF0"),
            ("mintcream", "#F5FFFA"),
            ("azure", "#F0FFFF"),
            ("aliceblue", "#F0F8FF"),
            ("ghostwhite", "#F8F8FF"),
            ("whitesmoke", "#F5F5F5"),
            ("seashell", "#FFF5EE"),
            ("beige", "#F5F5DC"),
            ("oldlace", "#FDF5E6"),
            ("floralwhite", "#FFFAF0"),
            ("ivory", "#FFFFF0"),
            ("antiquewhite", "#FAEBD7"),
            ("linen", "#FAF0E6"),
            ("lavenderblush", "#FFF0F5"),
            ("mistyrose", "#FFE4E1"),
            ("gainsboro", "#DCDCDC"),
            ("lightgray", "#D3D3D3"),
            ("silver", "#C0C0C0"),
            ("darkgray", "#A9A9A9"),
            ("dimgray", "#696969"),
            ("gray", "#808080"),
            ("lightslategray", "#778899"),
            ("slategray", "#708090"),
            ("darkslategray", "#2F4F4F"),
            ("black", "#000000")
        ]

    def color_dictionary(self) -> dict:
        """
        Eye.css color dictionary.
        The Legacy css colors as a dictionary.
        :return: dict
        :Date: July 29, 2022.
        """
        color_dictionary = dict()
        color_dictionary.update(self.color_table_list)
        # for each_color in self.color_table_list:
        #     color_dictionary[each_color[0]] = each_color[1]
        return color_dictionary

    def color_variable_dictionary(self) -> dict:
        """
        EYE CSS COLOR VARIABLE DEFINITION
        :return: the color variable dictionary
        :Date: July 29, 2022.
        """
        color_variable = dict()
        for each_color in self.color_table_list:
            color_variable[f"--eye_color_{each_color[0]}"] = each_color[1]
        return color_variable


class Positions:
    """
    CSS Position Helpers
    :Date: June 17, 2022.
    """

    def __init__(self) -> None:
        self.position_css_classes = []
        self.default_x_grid_value = 12
        self.default_y_grid_value = 8

        # Generate the position css helpers
        self.static()
        self.abs()
        self.abs_x_helpers()
        self.abs_y_helpers()
        self.fixed()
        self.fixed_x_helpers()
        self.fixed_y_helpers()
        self.relative()
        self.sticky()
        self.left_helpers()
        self.right_helpers()
        self.top_helpers()
        self.bottom_helpers()

    @property
    def css_properties(self):
        return self.position_css_classes

    @property
    def css_template(self):
        position_template = [
            ".top- {top: [];}",
            ".neg\:top- {top: -[];}",
            ".right- {right: [];}",
            ".neg\:right- {right: -[];}",
            ".bottom- {bottom: [];}",
            ".neg\:bottom- {bottom: -[];}",
            ".left- {left: [];}",
            ".neg\:left- {left: -[];}"
        ]
        # for _ in CSSGenerator().dimension_type_list:
        for _ in CSSGenerator().dimension_type_list:
            for j in CSSGenerator().positions_type_list:
                position_template.extend([f".{_}\:{j}- {{{j}: [];}}", f".{_}\:neg\:{j}- {{{j}: -[];}}"])
        return position_template

    def css_to_dict(self):
        css_text = "".join(self.position_css_classes)
        return CSSGenerator.convert_css_to_dict(css_text, add_braces=True)

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
        :format:
        .abs-x1 {left: 0%;}
        .abs-x2 {left: (1/12) * 100%;}
        :return:
        :Date: June 17, 2022.
        """
        for i in range(0, self.default_x_grid_value + 1, 1):
            abs_x_css = f"""
            .abs-x{i} {{left: {i / self.default_x_grid_value * 100}%;}}
            """
            self.position_css_classes.append(abs_x_css)

    def abs_y_helpers(self):
        """
        Defines CSS absolute position helper classes.
        :format:
        .abs-y1 {top: 0%;}
        .abs-y2 {top: (1/12) * 100%;}
        :return:
        :Date: June 18, 2022.
        """
        for i in range(0, self.default_y_grid_value + 1, 1):
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
        :format:
        .fixed-x1 {left: 0%;}
        .fixed-x2 {left: (1/12) * 100%;}
        :return:
        :Date: June 18, 2022.
        """
        for i in range(0, self.default_x_grid_value + 1, 1):
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
        for i in range(0, self.default_y_grid_value + 1, 1):
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
        :format:
        .relative-x1 {left: 0%;}
        .relative-x2 {left: (1/12) * 100%;}
        :return:
        :Date: June 18, 2022.
        """
        for i in range(0, self.default_x_grid_value + 1, 1):
            relative_x_css = f"""
            .relative-x{i} {{left: {i / self.default_x_grid_value * 100}%;}}
            """
            self.position_css_classes.append(relative_x_css)

    def relative_y_helpers(self):
        """
        Defines CSS relativeolute position helper classes.
        :format:
        .relative-y1 {top: 0%;}
        .relative-y2 {top: (1/12) * 100%;}
        :return:
        :Date: June 18, 2022.
        """
        for i in range(0, self.default_y_grid_value + 1, 1):
            relative_y_css = f"""
            .relative-y{i} {{top: {i / self.default_y_grid_value * 100}%;}}
            """
            self.position_css_classes.append(relative_y_css)

    def sticky(self):
        """
        Initialize the .sticky css class.
        :Date: July 1, 2022.
        """
        sticky_css = ".sticky {position: sticky;}"
        self.position_css_classes.append(sticky_css)

    def left_helpers(self):
        """:Date: July 1, 2022."""
        left_css_defaults = f"""
        .left-unset {{left: unset;}}
        .left-initial {{left: initial;}}
        .left-inherit {{left: inherit;}}
        .left-revert {{left: revert;}}
        .left-revert-layer {{left: revert-layer;}}
        """
        self.position_css_classes.append(left_css_defaults)

        for i in range(0, 101, 1):
            left_css = f"""
            .left-{i} {{left: {i}%;}}
            .neg\:left-{i} {{left: {-i}%;}}
            """
            self.position_css_classes.append(left_css)

    def right_helpers(self):
        """:Date: July 1, 2022."""
        right_css_defaults = f"""
        .right-unset {{right: unset;}}
        .right-initial {{right: initial;}}
        .right-inherit {{right: inherit;}}
        .right-revert {{right: revert;}}
        .right-revert-layer {{right: revert-layer;}}
        """
        self.position_css_classes.append(right_css_defaults)

        for i in range(0, 101, 1):
            right_css = f"""
            .right-{i} {{right: {i}%;}}
            .neg\:right-{i} {{right: {-i}%;}}
            """
            self.position_css_classes.append(right_css)

    def top_helpers(self):
        """:Date: July 1, 2022."""
        top_css_defaults = f"""
        .top-unset {{top: unset;}}
        .top-initial {{top: initial;}}
        .top-inherit {{top: inherit;}}
        .top-revert {{top: revert;}}
        .top-revert-layer {{top: revert-layer;}}
        """
        self.position_css_classes.append(top_css_defaults)

        for i in range(0, 101, 1):
            top_css = f"""
            .top-{i} {{top: {i}%;}}
            .neg\:top-{i} {{top: {-i}%;}}
            """
            self.position_css_classes.append(top_css)

    def bottom_helpers(self):
        """:Date: July 1, 2022."""
        bottom_css_defaults = f"""
        .bottom-unset {{bottom: unset;}}
        .bottom-initial {{bottom: initial;}}
        .bottom-inherit {{bottom: inherit;}}
        .bottom-revert {{bottom: revert;}}
        .bottom-revert-layer {{bottom: revert-layer;}}
        """
        self.position_css_classes.append(bottom_css_defaults)

        for i in range(0, 101, 1):
            bottom_css = f"""
            .bottom-{i} {{bottom: {i}%;}}
            .neg\:bottom-{i} {{bottom: {-i}%;}}
            """
            self.position_css_classes.append(bottom_css)


class Displays:
    """:Date: July 1, 2022."""

    def __init__(self) -> None:
        self.display_css_classes = list()
        self.block_helpers()

    @property
    def css_properties(self):
        return self.display_css_classes

    def block_helpers(self):
        """:Date: inherit """
        display_css = f"""
        .d-unset {{display: unset;}}
        .d-initial {{display: initial;}}
        .d-inherit {{display: inherit;}}
        .d-none {{display: none;}}
        .d-inline {{display: inline;}}
        .d-block {{display: block;}}
        .d-inline-block {{display: inline-block;}}
        .d-contents {{display: contents;}}
        """
        return self.display_css_classes.append(display_css)


class VerticalAlign:
    """:Date: July 1, 2022."""

    def __init__(self) -> None:
        self.vertical_align_css_classes = list()
        self.vertical_align_helpers()

    @property
    def css_properties(self):
        return self.vertical_align_css_classes

    def vertical_align_helpers(self):
        """:Date: inherit """
        vertical_align_css = f"""
        .v-align-unset {{vertical-align: unset;}}
        .v-align-inherit {{vertical-align: inherit;}}
        .v-align-initial {{vertical-align: initial;}}
        .v-align-revert {{vertical-align: revert;}}
        .v-align-revert-layer {{vertical-align: revert-layer;}}
        .v-align-auto {{vertical-align: auto;}}
        .v-align-baseline {{vertical-align: baseline;}}
        .v-align-bottom {{vertical-align: bottom;}}
        .v-align-middle {{vertical-align: middle;}}
        .v-align-top {{vertical-align: top;}}
        .v-align-super {{vertical-align: super;}}
        .v-align-texttop {{vertical-align: texttop;}}
        .v-align-textbottom {{vertical-align: textbottom;}}
        .v-align-top {{vertical-align: top;}}
        """
        return self.vertical_align_css_classes.append(vertical_align_css)


class Grid:
    """
    Eye.css Grid Implementation
    :Date: September 20, 2022.
    """
    def __init__(self) -> None:
        self.grid_css_classes = list()

    @property
    def css_properties(self):
        return self.grid_css_classes

    @property
    def css_template(self):
        grid_template = [".grid- {grid: [];}"]
        return grid_template

    def grid_rows(self):
        pass


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
        :format:
        .flex-row {flex-direction: row;}
        .flex-column {flex-direction: column;}
        :return: flexBox direction styles
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
        .flex-wrap {flex-wrap: wrap;}
        .flex-nowrap {flex-wrap: nowrap;}
        .flex-wrap-reverse {flex-wrap: wrap-reverse;}
        :return: flexBox wrap style
        """
        flex_wrap_css = f""".flex-wrap {{flex-wrap: wrap;}}
        .flex-nowrap {{flex-wrap: nowrap;}}
        .flex-wrap-reverse {{flex-wrap: wrap-reverse;}}
        """
        self.flex_css_classes.append(flex_wrap_css)

    def flex_grow(self):
        flex_grow_css = f"""
        .flex-grow {{flex-grow: 1;}}
        .flex-nogrow {{flex-grow: 0;}}
        """
        self.flex_css_classes.append(flex_grow_css)

    def flex_shrink(self):
        flex_shrink_css = f"""
        .flex-shrink {{flex-shrink: 1;}}
        .flex-noshrink {{flex-shrink: 0;}}
        """
        self.flex_css_classes.append(flex_shrink_css)

    def flex_basis(self):
        flex_basis_auto = f".flex-basis {{flex-basis: auto;}}"
        self.flex_css_classes.append(flex_basis_auto)
        for i in range(1, 13, 1):
            flex_basis_css = f"""
            .flex-basis-{i} {{flex-basis: {i * self.default_dimension_value}px;}}
            """
            self.flex_css_classes.append(flex_basis_css)

        # Generate flex-basis for 2x & 3x dimensions.
        for x in range(2, 3, 1):
            for i in range(1, 13, 1):
                flex_basis_css = f"""
                .flex-basis{x}-{i} {{flex-basis: {(i + 12) * self.default_dimension_value}px;}}
                """
                self.flex_css_classes.append(flex_basis_css)

    def flex_basis_percentages(self):
        flex_basis_auto = f".flex-basis {{flex-basis: auto;}}"
        self.flex_css_classes.append(flex_basis_auto)
        for i in range(0, 101, 1):
            flex_basis_css = f"""
            .pct\:flex-basis-{i} {{flex-basis: {i}%;}}
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
        self.default_width_helpers()
        self.gen_percent_width_helpers()
        self.gen_width_helpers()
        self.gen_width_2x_helpers()
        self.gen_width_3x_helpers()
        self.gen_width_4x_helpers()
        self.gen_width_safe_helpers()
        self.gen_percent_width_helpers(constraint="min-")
        self.gen_width_helpers(constraint="min-")
        self.gen_width_2x_helpers(constraint="min-")
        self.gen_width_3x_helpers(constraint="min-")
        self.gen_width_4x_helpers(constraint="min-")
        self.gen_width_safe_helpers(constraint="min-")
        self.gen_percent_width_helpers(constraint="max-")
        self.gen_width_helpers(constraint="max-")
        self.gen_width_2x_helpers(constraint="max-")
        self.gen_width_3x_helpers(constraint="max-")
        self.gen_width_4x_helpers(constraint="max-")
        self.gen_width_safe_helpers(constraint="max-")

    @property
    def css_properties(self):
        return self.width_css_classes

    @property
    def css_template(self):
        """ Function to return css template which can be used dynamically.
        :Date: August 9, 2022.
        """
        # width_template = """
        # .w-{} {width: [];}
        # .pct\:w-{} {width: {}%;}
        # .pt\:w-{} {width: {}pt;}
        # .pc\:w-{} {width: {}pc;}
        # .em\:w-{} {width: {}em;}
        # .rem\:w-{} {width: {}rem;}
        # .vw\:w-{} {width: {}vw;}
        # """
        width_template = [
            ".w- {width: [];}",
            ".pct\:w- {width: [];}",
            ".pt\:w- {width: [];}",
            ".pc\:w- {width: [];}",
            ".em\:w- {width: [];}",
            ".rem\:w- {width: [];}",
            ".vw\:w- {width: [];}",
            ".vmin\:w- {width: [];}",
            ".vmax\:w- {width: [];}",
            ".neg\:w- {width: -[];}",
            ".min-w- {min-width: [];}",
            ".pct\:min-w- {min-width: [];}",
            ".pt\:min-w- {min-width: [];}",
            ".pc\:min-w- {min-width: [];}",
            ".em\:min-w- {min-width: [];}",
            ".rem\:min-w- {min-width: [];}",
            ".vw\:min-w- {min-width: [];}",
            ".vmin\:min-w- {min-width: [];}",
            ".vmax\:min-w- {min-width: [];}",
            ".neg\:min-w- {min-width: -[];}",
            ".neg\:pct\:min-w- {min-width: -[];}",
            ".neg\:pt\:min-w- {min-width: -[];}",
            ".neg\:pc\:min-w- {min-width: -[];}",
            ".neg\:em\:min-w- {min-width: -[];}",
            ".neg\:rem\:min-w- {min-width: -[];}",
            ".neg\:vw\:min-w- {min-width: -[];}"
            ".neg\:vmin\:min-w- {min-width: -[];}"
            ".neg\:vmax\:min-w- {min-width: -[];}"
            ".max-w- {max-width: [];}",
            ".pct\:max-w- {max-width: [];}",
            ".pt\:max-w- {max-width: [];}",
            ".pc\:max-w- {max-width: [];}",
            ".em\:max-w- {max-width: [];}",
            ".rem\:max-w- {max-width: [];}",
            ".vw\:max-w- {max-width: [];}",
            ".vmin\:max-w- {max-width: [];}",
            ".vmax\:max-w- {max-width: [];}",
            ".neg\:max-w- {max-width: -[];}",
            ".neg\:pct\:max-w- {max-width: -[];}",
            ".neg\:pt\:max-w- {max-width: -[];}",
            ".neg\:pc\:max-w- {max-width: -[];}",
            ".neg\:em\:max-w- {max-width: -[];}",
            ".neg\:rem\:max-w- {max-width: -[];}",
            ".neg\:vw\:max-w- {max-width: -[];}"
            ".neg\:vmin\:max-w- {max-width: -[];}"
            ".neg\:vmax\:max-w- {max-width: -[];}"
        ]
        return width_template

    def default_width_helpers(self, constraint=""):
        """:Date: July 1, 2022."""
        default_width_css = f"""
        .{constraint}w-auto {{{constraint}width: auto;}}
        .{constraint}w-initial {{{constraint}width: initial;}}
        .{constraint}w-inherit {{{constraint}width: inherit;}}
        .{constraint}w-unset {{{constraint}width: unset;}}
        .{constraint}w-0 {{{constraint}width: 0;}}
        """
        self.width_css_classes.append(default_width_css)

    def gen_percent_width_helpers(self, percent_prefix_string="pct", constraint=""):
        """
        This function generates percent width helpers.
        FORMAT GENERATED:
        .pct\:w-0 {width: 0%;}
        .pct\:w-1 {width: 1%;}
        ...
        .pct\:w-100 {width: 100%;}
        :return: percentage Width helper css classes
        """
        for i in range(0, 201, 1):
            percent_width_css = f".{percent_prefix_string}\:{constraint}w-{i} {{{constraint}width: {i}%;}}"
            self.width_css_classes.append(percent_width_css)

    def gen_width_helpers(self, constraint=""):
        """
        Generates eye.css width helpers.
        Format to be returned is:
        .w-1 {width: 8px;}
        .w-2 {width: 16px;}
        :return: 1x width helper css classes
        """
        for i in range(1, 13, 1):
            width_css = f".{constraint}w-{i} {{{constraint}width: {i * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_css)

    def gen_width_2x_helpers(self, constraint=""):
        """
        Generates eye.css width 2x helpers.
        Format to be returned is:
        .w2-1 {width: 104px;}   # i.e., (1 + 12) * self.default_dimension_value
        .w2-2 {width: 112px;}   # i.e., (2 + 12) * self.default_dimension_value
        :return: 2x width helper css classes
        """
        for i in range(1, 13, 1):
            width_2x_css = f".{constraint}w2-{i} {{{constraint}width: {(i + 12) * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_2x_css)

    def gen_width_3x_helpers(self, constraint=""):
        """
        Generates eye.css width 3x helpers.
        Format to be returned is:
        .w3-1 {width: 104px;}   # i.e., (1 + 12 + 12) * self.default_dimension_value
        .w3-2 {width: 112px;}   # i.e., (2 + 12 + 12) * self.default_dimension_value
        :return: 3x width helper css classes
        """
        for i in range(1, 13, 1):
            width_3x_css = f".{constraint}w3-{i} {{{constraint}width: {(i + 12 + 12) * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_3x_css)

    def gen_width_4x_helpers(self, constraint=""):
        """
        Generates eye.css width 4x helpers.
        Format to be returned is:
        .w4-1 {width: 104px;}   # i.e., (1 + 12 + 12 + 12) * self.default_dimension_value
        .w4-2 {width: 112px;}   # i.e., (2 + 12 + 12 + 12) * self.default_dimension_value
        :return: 4x width helper css classes
        """
        for i in range(1, 13, 1):
            width_4x_css = f".{constraint}w3-{i} {{{constraint}width: {(i + 12 + 12) * self.default_dimension_value}px}}"
            self.width_css_classes.append(width_4x_css)

    def gen_width_safe_helpers(self, constraint=""):
        """
        Generates eye.css width helpers.
        Format to be returned is:
        .w-safe-1 {width: 8%;}
        .w-safe-2 {width: 16%;}
        :return: 1x width helper css classes
        """
        for i in range(1, 13, 1):
            width_safe_css = (
                f".{constraint}w-safe-{i} {{{constraint}width: {i * self.default_dimension_value}%}}"
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
        self.default_height_helpers()
        self.gen_percent_height_helpers()
        self.gen_height_helpers()
        self.gen_height_2x_helpers()
        self.gen_height_3x_helpers()
        self.gen_height_4x_helpers()
        self.gen_height_5x_helpers()
        self.gen_height_6x_helpers()
        self.gen_height_safe_helpers()
        self.gen_percent_height_helpers(constraint="min-")
        self.gen_height_helpers(constraint="min-")
        self.gen_height_2x_helpers(constraint="min-")
        self.gen_height_3x_helpers(constraint="min-")
        self.gen_height_4x_helpers(constraint="min-")
        self.gen_height_5x_helpers(constraint="min-")
        self.gen_height_6x_helpers(constraint="min-")
        self.gen_height_safe_helpers(constraint="min-")
        self.gen_percent_height_helpers(constraint="max-")
        self.gen_height_helpers(constraint="max-")
        self.gen_height_2x_helpers(constraint="max-")
        self.gen_height_3x_helpers(constraint="max-")
        self.gen_height_4x_helpers(constraint="max-")
        self.gen_height_5x_helpers(constraint="max-")
        self.gen_height_6x_helpers(constraint="max-")
        self.gen_height_safe_helpers(constraint="max-")

    @property
    def css_properties(self):
        return self.height_css_classes

    @property
    def css_template(self):
        """ Templates for dynamic css height.
        :Date: August 9, 2022.
        """
        height_template = [
            ".h- {height: [];}",
            ".pct\:h- {height: [];}",
            ".pt\:h- {height: [];}",
            ".pc\:h- {height: [];}",
            ".em\:h- {height: [];}",
            ".rem\:h- {height: [];}",
            ".vh\:h- {height: [];}",
            ".vmin\:h- {height: [];}",
            ".vmax\:h- {height: [];}",
            ".neg\:h- {height: -[];}",
            ".min-h- {min-height: [];}",
            ".pct\:min-h- {min-height: [];}",
            ".pt\:min-h- {min-height: [];}",
            ".pc\:min-h- {min-height: [];}",
            ".em\:min-h- {min-height: [];}",
            ".rem\:min-h- {min-height: [];}",
            ".vh\:min-h- {min-height: [];}",
            ".vmin\:min-h- {min-height: [];}",
            ".vmax\:min-h- {min-height: [];}",
            ".neg\:min-h- {min-height: -[];}",
            ".neg\:pct\:min-h- {min-height: -[];}",
            ".neg\:pt\:min-h- {min-height: -[];}",
            ".neg\:pc\:min-h- {min-height: -[];}",
            ".neg\:em\:min-h- {min-height: -[];}",
            ".neg\:rem\:min-h- {min-height: -[];}",
            ".neg\:vh\:min-h- {min-height: -[];}"
            ".neg\:vmin\:min-h- {min-height: -[];}"
            ".neg\:vmax\:min-h- {min-height: -[];}"
            ".max-h- {max-height: [];}",
            ".pct\:max-h- {max-height: [];}",
            ".pt\:max-h- {max-height: [];}",
            ".pc\:max-h- {max-height: [];}",
            ".em\:max-h- {max-height: [];}",
            ".rem\:max-h- {max-height: [];}",
            ".vh\:max-h- {max-height: [];}",
            ".vmin\:max-h- {max-height: [];}",
            ".vmax\:max-h- {max-height: [];}",
            ".neg\:max-h- {max-height: -[];}",
            ".neg\:pct\:max-h- {max-height: -[];}",
            ".neg\:pt\:max-h- {max-height: -[];}",
            ".neg\:pc\:max-h- {max-height: -[];}",
            ".neg\:em\:max-h- {max-height: -[];}",
            ".neg\:rem\:max-h- {max-height: -[];}",
            ".neg\:vh\:max-h- {max-height: -[];}"
            ".neg\:vmin\:max-h- {max-height: -[];}"
            ".neg\:vmax\:max-h- {max-height: -[];}"
        ]
        return height_template

    def default_height_helpers(self, constraint=""):
        """:Date: July 1, 2022."""
        default_height_css = f"""
        .{constraint}h-auto {{{constraint}height: auto;}}
        .{constraint}h-initial {{{constraint}height: initial;}}
        .{constraint}h-inherit {{{constraint}height: inherit;}}
        .{constraint}h-unset {{{constraint}height: unset;}}
        .{constraint}h-0 {{{constraint}height: 0;}}
        """
        self.height_css_classes.append(default_height_css)

    def gen_percent_height_helpers(self, percent_prefix_string="pct", constraint=""):
        """
        This function generates percent height helpers.
        FORMAT GENERATED:
        .pct\:h-0 {height: 0%;}
        .pct\:h-1 {height: 1%;}
        ...
        .pct\:h-100 {height: 100%;}
        :return: percentage Width helper css classes
        """
        for i in range(0, 201, 1):
            percent_height_css = f".{percent_prefix_string}\:{constraint}h-{i} {{{constraint}height: {i}%;}}"
            self.height_css_classes.append(percent_height_css)

        # gen_percent_height_helpers()

    def gen_height_helpers(self, constraint=""):
        """
        Generates eye.css height helpers.
        Format to be returned is:
        .h-1 {height: 8px;}
        .h-2 {height: 16px;}
        :return: 1x height helper css classes
        """
        for i in range(1, 13, 1):
            height_css = f".{constraint}h-{i} {{{constraint}height: {i * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_css)

    def gen_height_2x_helpers(self, constraint=""):
        """
        Generates eye.css height 2x helpers.
        Format to be returned is:
        .h2-1 {height: 104px;}   # i.e., (1 + 12) * self.default_dimension_value
        .h2-2 {height: 112px;}   # i.e., (2 + 12) * self.default_dimension_value
        :return: 2x height helper css classes
        """
        for i in range(1, 13, 1):
            height_2x_css = f".{constraint}h2-{i} {{{constraint}height: {(i + 12) * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_2x_css)

    def gen_height_3x_helpers(self, constraint=""):
        """
        Generates eye.css height 3x helpers.
        Format to be returned is:
        .h3-1 {height: 104px;}   # i.e., (1 + 12 + 12) * self.default_dimension_value
        .h3-2 {height: 112px;}   # i.e., (2 + 12 + 12) * self.default_dimension_value
        :return: 3x height helper css classes
        """
        for i in range(1, 13, 1):
            height_3x_css = f".{constraint}h3-{i} {{{constraint}height: {(i + 12 + 12) * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_3x_css)

    def gen_height_4x_helpers(self, constraint=""):
        """
        Generates eye.css height 4x helpers.
        Format to be returned is:
        .h4-1 {height: ...px;}   # i.e., (1 + 12 + 12 + 12) * self.default_dimension_value
        .h4-2 {height: ...px;}   # i.e., (2 + 12 + 12 + 12) * self.default_dimension_value
        :return: 4x height helper css classes
        """
        for i in range(1, 13, 1):
            height_4x_css = f".{constraint}h4-{i} {{{constraint}height: {(i + 12 + 12 + 12) * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_4x_css)

    def gen_height_5x_helpers(self, constraint=""):
        """
        Generates eye.css height 5x helpers.
        Format to be returned is:
        .h5-1 {height: ...px;}   # i.e., (1 + 12 + 12 + 12 + 12) * self.default_dimension_value
        .h5-2 {height: ...px;}   # i.e., (2 + 12 + 12) * self.default_dimension_value
        :return: 5x height helper css classes
        """
        for i in range(1, 13, 1):
            height_5x_css = f".{constraint}h5-{i} {{{constraint}height: {(i + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_5x_css)

    def gen_height_6x_helpers(self, constraint=""):
        """
        Generates eye.css height 6x helpers.
        Format to be returned is:
        .h6-1 {height: ...px;}   # i.e., (1 + 12 + 12 + 12 + 12) * self.default_dimension_value
        .h6-2 {height: ...px;}   # i.e., (2 + 12 + 12) * self.default_dimension_value
        :return: 6x height helper css classes
        """
        for i in range(1, 13, 1):
            height_6x_css = f".{constraint}h6-{i} {{{constraint}height: {(i + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}"
            self.height_css_classes.append(height_6x_css)

    def gen_height_safe_helpers(self, constraint=""):
        """
        Generates eye.css height helpers.
        Format to be returned is:
        .h-safe-1 {height: 8%;}
        .h-safe-2 {height: 16%;}
        :return: 1x height helper css classes
        """
        for i in range(1, 13, 1):
            height_safe_css = (
                f".{constraint}h-safe-{i} {{{constraint}height: {i * self.default_dimension_value}%;}}"
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

    @property
    def css_template(self):
        """ Margin CSS Template.
        :Date: August 10, 2022.
        """
        margin_template = [
            ".mg- {margin: [];}",
            ".mg-x- {margin-left: []; margin-right: [];}",
            ".mg-y- {margin-top: []; margin-bottom: [];}",
            ".mg-t- {margin-top: [];}",
            ".mg-r- {margin-right: [];}",
            ".mg-b- {margin-bottom: [];}",
            ".mg-l- {margin-left: [];}"
        ]
        # for _ in CSSGenerator().dimension_type_list:
        #     margin_template.extend([
        #         f".{_}\:mg- {{margin: [];}}",
        #         f".{_}\:mg-x- {{margin-left: []; margin-right: [];}}",
        #         f".{_}\:mg-y- {{margin-top: []; margin-bottom: [];}}",
        #         f".{_}\:mg-t- {{margin-top: [];}}",
        #         f".{_}\:mg-r- {{margin-right: [];}}",
        #         f".{_}\:mg-b- {{margin-bottom: [];}}",
        #         f".{_}\:mg-l- {{margin-left: [];}}"
        #     ])
        return margin_template

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
        .mg-t-0 {{margin-top: 0;}}
        .mg-b-0 {{margin-bottom: 0;}}
        .mg-l-0 {{margin-left: 0;}}
        .mg-r-0 {{margin-right: 0;}}
        .mg-top-0 {{margin-top: 0;}}
        .mg-bottom-0 {{margin-bottom: 0;}}
        .mg-left-0 {{margin-left: 0;}}
        .mg-right-0 {{margin-right: 0;}}
        .mg-initial {{margin: initial;}}
        .mg-x-initial {{margin-left: initial; margin-right: initial;}}
        .mg-y-initial {{margin-top: initial; margin-bottom: initial;}}
        .mg-t-initial {{margin-top: initial;}}
        .mg-b-initial {{margin-bottom: initial;}}
        .mg-l-initial {{margin-left: initial;}}
        .mg-r-initial {{margin-right: initial;}}
        .mg-top-initial {{margin-top: initial;}}
        .mg-bottom-initial {{margin-bottom: initial;}}
        .mg-left-initial {{margin-left: initial;}}
        .mg-right-initial {{margin-right: initial;}}
        .mg-inherit {{margin: inherit;}}
        .mg-x-inherit {{margin-left: inherit; margin-right: inherit;}}
        .mg-y-inherit {{margin-top: inherit; margin-bottom: inherit;}}
        .mg-t-inherit {{margin-top: inherit;}}
        .mg-b-inherit {{margin-bottom: inherit;}}
        .mg-l-inherit {{margin-left: inherit;}}
        .mg-r-inherit {{margin-right: inherit;}}
        .mg-top-inherit {{margin-top: inherit;}}
        .mg-bottom-inherit {{margin-bottom: inherit;}}
        .mg-left-inherit {{margin-left: inherit;}}
        .mg-right-inherit {{margin-right: inherit;}}
        .mg-unset {{margin: unset;}}
        .mg-x-unset {{margin-left: unset; margin-right: unset;}}
        .mg-y-unset {{margin-top: unset; margin-bottom: unset;}}
        .mg-t-unset {{margin-top: unset;}}
        .mg-b-unset {{margin-bottom: unset;}}
        .mg-l-unset {{margin-left: unset;}}
        .mg-r-unset {{margin-right: unset;}}
        .mg-top-unset {{margin-top: unset;}}
        .mg-bottom-unset {{margin-bottom: unset;}}
        .mg-left-unset {{margin-left: unset;}}
        .mg-right-unset {{margin-right: unset;}}
        .mg-revert {{margin: revert;}}
        .mg-x-revert {{margin-left: revert; margin-right: revert;}}
        .mg-y-revert {{margin-top: revert; margin-bottom: revert;}}
        .mg-t-revert {{margin-top: revert;}}
        .mg-b-revert {{margin-bottom: revert;}}
        .mg-l-revert {{margin-left: revert;}}
        .mg-r-revert {{margin-right: revert;}}
        .mg-top-revert {{margin-top: revert;}}
        .mg-bottom-revert {{margin-bottom: revert;}}
        .mg-left-revert {{margin-left: revert;}}
        .mg-right-revert {{margin-right: revert;}}
        .mg-revert-layer {{margin: revert-layer;}}
        .mg-x-revert-layer {{margin-left: revert-layer; margin-right: revert-layer;}}
        .mg-y-revert-layer {{margin-top: revert-layer; margin-bottom: revert-layer;}}
        .mg-t-revert-layer {{margin-top: revert-layer;}}
        .mg-b-revert-layer {{margin-bottom: revert-layer;}}
        .mg-l-revert-layer {{margin-left: revert-layer;}}
        .mg-r-revert-layer {{margin-right: revert-layer;}}
        .mg-top-revert-layer {{margin-top: revert-layer;}}
        .mg-bottom-revert-layer {{margin-bottom: revert-layer;}}
        .mg-left-revert-layer {{margin-left: revert-layer;}}
        .mg-right-revert-layer {{margin-right: revert-layer;}}
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
        .mg-t-auto {{margin-top: auto;}}
        .mg-b-auto {{margin-bottom: auto;}}
        .mg-l-auto {{margin-left: auto;}}
        .mg-r-auto {{margin-right: auto;}}
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
        # .mg-{} {{margin: {}px;}}
        # .mg-x-{} {{margin-left: {}px; margin-right: {}px;}}
        # .mg-y-{} {{margin-top: {}px; margin-bottom: {}px;}}
        # .mg-t-{} {{margin-top: {}px;}}
        # .mg-r-{} {{margin-right: {}px;}}
        # .mg-b-{} {{margin-bottom: {}px;}}
        # .mg-l-{} {{margin-left: {}px;}}
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
            .mg-l{i} {{margin-left: {self.default_dimension_value * i}px;}}
            .mg-left{i}-sm {{margin-left: {(self.default_dimension_value * i) - 2}px;}}
            .mg-l{i}-sm {{margin-left: {(self.default_dimension_value * i) - 2}px;}}
            .mg-left{i}-smr {{margin-left: {(self.default_dimension_value * i) - 4}px;}}
            .mg-l{i}-smr {{margin-left: {(self.default_dimension_value * i) - 4}px;}}
            .mg-left{i}-smt {{margin-left: {(self.default_dimension_value * i) - 6}px;}}
            .mg-l{i}-smt {{margin-left: {(self.default_dimension_value * i) - 6}px;}}
            .mg-left{i}-xs {{margin-left: {(self.default_dimension_value * i) - 7}px;}}
            .mg-l{i}-xs {{margin-left: {(self.default_dimension_value * i) - 7}px;}}
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
            .mg-r{i} {{margin-right: {self.default_dimension_value * i}px;}}
            .mg-right{i}-sm {{margin-right: {(self.default_dimension_value * i) - 2}px;}}
            .mg-r{i}-sm {{margin-right: {(self.default_dimension_value * i) - 2}px;}}
            .mg-right{i}-smr {{margin-right: {(self.default_dimension_value * i) - 4}px;}}
            .mg-r{i}-smr {{margin-right: {(self.default_dimension_value * i) - 4}px;}}
            .mg-right{i}-smt {{margin-right: {(self.default_dimension_value * i) - 6}px;}}
            .mg-r{i}-smt {{margin-right: {(self.default_dimension_value * i) - 6}px;}}
            .mg-right{i}-xs {{margin-right: {(self.default_dimension_value * i) - 7}px;}}
            .mg-r{i}-xs {{margin-right: {(self.default_dimension_value * i) - 7}px;}}
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
            .mg-t{i} {{margin-top: {self.default_dimension_value * i}px;}}
            .mg-top{i}-sm {{margin-top: {(self.default_dimension_value * i) - 2}px;}}
            .mg-t{i}-sm {{margin-top: {(self.default_dimension_value * i) - 2}px;}}
            .mg-top{i}-smr {{margin-top: {(self.default_dimension_value * i) - 4}px;}}
            .mg-t{i}-smr {{margin-top: {(self.default_dimension_value * i) - 4}px;}}
            .mg-top{i}-smt {{margin-top: {(self.default_dimension_value * i) - 6}px;}}
            .mg-t{i}-smt {{margin-top: {(self.default_dimension_value * i) - 6}px;}}
            .mg-top{i}-xs {{margin-top: {(self.default_dimension_value * i) - 7}px;}}
            .mg-t{i}-xs {{margin-top: {(self.default_dimension_value * i) - 7}px;}}
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
            .mg-b{i} {{margin-bottom: {self.default_dimension_value * i}px;}}
            .mg-bottom{i}-sm {{margin-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .mg-b{i}-sm {{margin-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .mg-bottom{i}-smr {{margin-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .mg-b{i}-smr {{margin-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .mg-bottom{i}-smt {{margin-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .mg-b{i}-smt {{margin-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .mg-bottom{i}-xs {{margin-bottom: {(self.default_dimension_value * i) - 7}px;}}
            .mg-b{i}-xs {{margin-bottom: {(self.default_dimension_value * i) - 7}px;}}
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
        self.gen_padding_helpers()
        self.gen_padding_x_helpers()
        self.gen_padding_left_helpers()
        self.gen_padding_right_helpers()
        self.gen_padding_y_helpers()
        self.gen_padding_top_helpers()
        self.gen_padding_bottom_helpers()

    @property
    def css_properties(self):
        return self.padding_css_classes

    @property
    def css_template(self):
        """ Padding CSS Template.
        :Date: August 9, 2022.
        """
        padding_template = [
            ".pad- {padding: [];}",
            ".pad-x- {padding-left: []; padding-right: [];}",
            ".pad-y- {padding-top: []; padding-bottom: [];}",
            ".pad-t- {padding-top: [];}",
            ".pad-r- {padding-right: [];}",
            ".pad-b- {padding-bottom: [];}",
            ".pad-l- {padding-left: [];}"
        ]
        # for _ in CSSGenerator().dimension_type_list:
        #     padding_template.extend([
        #         f".{_}\:pad- {{padding: [];}}",
        #         f".{_}\:pad-x- {{padding-left: []; padding-right: [];}}",
        #         f".{_}\:pad-y- {{padding-top: []; padding-bottom: [];}}",
        #         f".{_}\:pad-t- {{padding-top: [];}}",
        #         f".{_}\:pad-r- {{padding-right: [];}}",
        #         f".{_}\:pad-b- {{padding-bottom: [];}}",
        #         f".{_}\:pad-l- {{padding-left: [];}}"
        #     ])
        return padding_template

    def gen_padding_default_helpers(self):
        """
        :Date: June 27, 2022.
        """
        pad_default_css = f"""
            .pad-0 {{padding: 0;}}
            .pad-x-0 {{padding-left: 0; padding-right: 0;}}
            .pad-y-0 {{padding-top: 0; padding-bottom: 0;}}
            .pad-t-0 {{padding-top: 0;}}
            .pad-r-0 {{padding-right: 0;}}
            .pad-b-0 {{padding-bottom: 0;}}
            .pad-l-0 {{padding-left: 0;}}
            .pad-top-0 {{padding-top: 0;}}
            .pad-right-0 {{padding-right: 0;}}
            .pad-bottom-0 {{padding-bottom: 0;}}
            .pad-left-0 {{padding-left: 0;}}
            .pad-initial {{padding: initial;}}
            .pad-x-initial {{padding-left: initial; padding-right: initial;}}
            .pad-y-initial {{padding-top: initial; padding-bottom: initial;}}
            .pad-t-initial {{padding-top: initial;}}
            .pad-r-initial {{padding-right: initial;}}
            .pad-b-initial {{padding-bottom: initial;}}
            .pad-l-initial {{padding-left: initial;}}
            .pad-top-initial {{padding-top: initial;}}
            .pad-right-initial {{padding-right: initial;}}
            .pad-bottom-initial {{padding-bottom: initial;}}
            .pad-left-initial {{padding-left: initial;}}
            .pad-inherit {{padding: inherit;}}
            .pad-x-inherit {{padding-left: inherit; padding-right: inherit;}}
            .pad-y-inherit {{padding-top: inherit; padding-bottom: inherit;}}
            .pad-t-inherit {{padding-top: inherit;}}
            .pad-r-inherit {{padding-right: inherit;}}
            .pad-b-inherit {{padding-bottom: inherit;}}
            .pad-l-inherit {{padding-left: inherit;}}
            .pad-top-inherit {{padding-top: inherit;}}
            .pad-right-inherit {{padding-right: inherit;}}
            .pad-bottom-inherit {{padding-bottom: inherit;}}
            .pad-left-inherit {{padding-left: inherit;}}
            .pad-unset {{padding: unset;}}
            .pad-x-unset {{padding-left: unset; padding-right: unset;}}
            .pad-y-unset {{padding-top: unset; padding-bottom: unset;}}
            .pad-t-unset {{padding-top: unset;}}
            .pad-r-unset {{padding-right: unset;}}
            .pad-b-unset {{padding-bottom: unset;}}
            .pad-l-unset {{padding-left: unset;}}
            .pad-top-unset {{padding-top: unset;}}
            .pad-right-unset {{padding-right: unset;}}
            .pad-bottom-unset {{padding-bottom: unset;}}
            .pad-left-unset {{padding-left: unset;}}
            .pad-revert {{padding: revert;}}
            .pad-x-revert {{padding-left: revert; padding-right: revert;}}
            .pad-y-revert {{padding-top: revert; padding-bottom: revert;}}
            .pad-t-revert {{padding-top: revert;}}
            .pad-r-revert {{padding-right: revert;}}
            .pad-b-revert {{padding-bottom: revert;}}
            .pad-l-revert {{padding-left: revert;}}
            .pad-top-revert {{padding-top: revert;}}
            .pad-right-revert {{padding-right: revert;}}
            .pad-bottom-revert {{padding-bottom: revert;}}
            .pad-left-revert {{padding-left: revert;}}
            .pad-revert-layer {{padding: revert-layer;}}
            .pad-x-revert-layer {{padding-left: revert-layer; padding-right: revert-layer;}}
            .pad-y-revert-layer {{padding-top: revert-layer; padding-bottom: revert-layer;}}
            .pad-t-revert-layer {{padding-top: revert-layer;}}
            .pad-r-revert-layer {{padding-right: revert-layer;}}
            .pad-b-revert-layer {{padding-bottom: revert-layer;}}
            .pad-l-revert-layer {{padding-left: revert-layer;}}
            .pad-top-revert-layer {{padding-top: revert-layer;}}
            .pad-right-revert-layer {{padding-right: revert-layer;}}
            .pad-bottom-revert-layer {{padding-bottom: revert-layer;}}
            .pad-left-revert-layer {{padding-left: revert-layer;}}
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
        .pad-t-auto {{padding-top: auto;}}
        .pad-r-auto {{padding-right: auto;}}
        .pad-b-auto {{padding-bottom: auto;}}
        .pad-l-auto {{padding-left: auto;}}
        .pad-top-auto {{padding-top: auto;}}
        .pad-right-auto {{padding-right: auto;}}
        .pad-bottom-auto {{padding-bottom: auto;}}
        .pad-left-auto {{padding-left: auto;}}
        """
        self.padding_css_classes.append(pad_auto_css)

    def gen_padding_helpers(self):
        """ :Date: July 24, 2022. """
        for i in range(1, 13, 1):
            pad_css = f"""
            .pad-{i} {{padding: {self.default_dimension_value * i}px;}}
            .pad-{i}-sm {{padding: {(self.default_dimension_value * i) - 2}px;}}
            .pad-{i}-smr {{padding: {(self.default_dimension_value * i) - 4}px;}}
            .pad-{i}-smt {{padding: {(self.default_dimension_value * i) - 6}px;}}
            .pad-{i}-xs {{padding: {(self.default_dimension_value * i) - 7}px;}}
            """
            self.padding_css_classes.append(pad_css)

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
            .pad-l{i} {{padding-left: {self.default_dimension_value * i}px;}}
            .pad-left{i}-sm {{padding-left: {(self.default_dimension_value * i) - 2}px;}}
            .pad-l{i}-sm {{padding-left: {(self.default_dimension_value * i) - 2}px;}}
            .pad-left{i}-smr {{padding-left: {(self.default_dimension_value * i) - 4}px;}}
            .pad-l{i}-smr {{padding-left: {(self.default_dimension_value * i) - 4}px;}}
            .pad-left{i}-smt {{padding-left: {(self.default_dimension_value * i) - 6}px;}}
            .pad-l{i}-smt {{padding-left: {(self.default_dimension_value * i) - 6}px;}}
            .pad-left{i}-xs {{padding-left: {(self.default_dimension_value * i) - 7}px;}}
            .pad-l{i}-xs {{padding-left: {(self.default_dimension_value * i) - 7}px;}}
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
            .pad-r{i} {{padding-right: {self.default_dimension_value * i}px;}}
            .pad-right{i}-sm {{padding-right: {(self.default_dimension_value * i) - 2}px;}}
            .pad-r{i}-sm {{padding-right: {(self.default_dimension_value * i) - 2}px;}}
            .pad-right{i}-smr {{padding-right: {(self.default_dimension_value * i) - 4}px;}}
            .pad-r{i}-smr {{padding-right: {(self.default_dimension_value * i) - 4}px;}}
            .pad-right{i}-smt {{padding-right: {(self.default_dimension_value * i) - 6}px;}}
            .pad-r{i}-smt {{padding-right: {(self.default_dimension_value * i) - 6}px;}}
            .pad-right{i}-xs {{padding-right: {(self.default_dimension_value * i) - 7}px;}}
            .pad-r{i}-xs {{padding-right: {(self.default_dimension_value * i) - 7}px;}}
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
            .pad-t{i} {{padding-top: {self.default_dimension_value * i}px;}}
            .pad-top{i}-sm {{padding-top: {(self.default_dimension_value * i) - 2}px;}}
            .pad-t{i}-sm {{padding-top: {(self.default_dimension_value * i) - 2}px;}}
            .pad-top{i}-smr {{padding-top: {(self.default_dimension_value * i) - 4}px;}}
            .pad-t{i}-smr {{padding-top: {(self.default_dimension_value * i) - 4}px;}}
            .pad-top{i}-smt {{padding-top: {(self.default_dimension_value * i) - 6}px;}}
            .pad-t{i}-smt {{padding-top: {(self.default_dimension_value * i) - 6}px;}}
            .pad-top{i}-xs {{padding-top: {(self.default_dimension_value * i) - 7}px;}}
            .pad-t{i}-xs {{padding-top: {(self.default_dimension_value * i) - 7}px;}}
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
            .pad-b{i} {{padding-bottom: {self.default_dimension_value * i}px;}}
            .pad-bottom{i}-sm {{padding-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .pad-b{i}-sm {{padding-bottom: {(self.default_dimension_value * i) - 2}px;}}
            .pad-bottom{i}-smr {{padding-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .pad-b{i}-smr {{padding-bottom: {(self.default_dimension_value * i) - 4}px;}}
            .pad-bottom{i}-smt {{padding-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .pad-b{i}-smt {{padding-bottom: {(self.default_dimension_value * i) - 6}px;}}
            .pad-bottom{i}-xs {{padding-bottom: {(self.default_dimension_value * i) - 7}px;}}
            .pad-b{i}-xs {{padding-bottom: {(self.default_dimension_value * i) - 7}px;}}
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
        self.gen_line_height_2x()
        self.gen_line_height_3x()
        self.gen_line_height_4x()
        self.gen_line_height_5x()
        self.gen_line_height_6x()

    @property
    def css_properties(self):
        return self.line_height_css_classes

    @property
    def css_template(self):
        """ Line Heights CSS Template.
        :Date: August 9, 2022.
        """
        lh_template = [".lh- {line-height: [];}"]
        return lh_template

    def gen_line_height_defaults(self):
        """_summary_
        :Date: inherit
        """
        line_height_css_defaults = f"""
        .line-height-unset {{line-height: unset;}}
        .line-height-initial {{line-height: initial;}}
        .line-height-inherit {{line-height: inherit;}}
        .line-height-revert {{line-height: revert;}}
        .line-height-revert-layer {{line-height: revert-layer;}}
        .line-height-normal {{line-height: normal;}}
        .line-height-100 {{line-height: 100%;}}

        .lh-unset {{line-height: unset;}}
        .lh-initial {{line-height: initial;}}
        .lh-inherit {{line-height: inherit;}}
        .lh-revert {{line-height: revert;}}
        .lh-revert-layer {{line-height: revert-layer;}}
        .lh-normal {{line-height: normal;}}
        .lh-100 {{line-height: 100%;}}
        """
        self.line_height_css_classes.append(line_height_css_defaults)

    def gen_line_height(self):
        """_summary_
        :Date: inherit
        """
        for i in range(1, 13, 1):
            line_height_css = f"""
            .line-height-{i} {{line-height: {i * self.default_dimension_value}px;}}
            .lh-{i} {{line-height: {i * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_css)

    def gen_line_height_2x(self):
        """_summary_
        :Date: August 14, 2022.
        """
        for i in range(1, 13, 1):
            line_height_2x_css = f"""
            .line-height2-{i} {{line-height: {(i + 12) * self.default_dimension_value}px;}}
            .lh2-{i} {{line-height: {(i + 12) * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_2x_css)

    def gen_line_height_3x(self):
        """_summary_
        :Date: August 14, 2022.
        """
        for i in range(1, 13, 1):
            line_height_3x_css = f"""
            .line-height3-{i} {{line-height: {(i + 12 + 12) * self.default_dimension_value}px;}}
            .lh3-{i} {{line-height: {(i + 12 + 12) * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_3x_css)

    def gen_line_height_4x(self):
        """_summary_
        :Date: August 14, 2022.
        """
        for i in range(1, 13, 1):
            line_height_4x_css = f"""
            .line-height4-{i} {{line-height: {(i + 12 + 12 + 12) * self.default_dimension_value}px;}}
            .lh4-{i} {{line-height: {(i + 12 + 12 + 12) * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_4x_css)

    def gen_line_height_5x(self):
        """_summary_
        :Date: August 14, 2022.
        """
        for i in range(1, 13, 1):
            line_height_5x_css = f"""
            .line-height5-{i} {{line-height: {(i + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}
            .lh5-{i} {{line-height: {(i + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_5x_css)

    def gen_line_height_6x(self):
        """_summary_
        :Date: August 14, 2022.
        """
        for i in range(1, 13, 1):
            line_height_6x_css = f"""
            .line-height6-{i} {{line-height: {(i + 12 + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}
            .lh6-{i} {{line-height: {(i + 12 + 12 + 12 + 12 + 12) * self.default_dimension_value}px;}}
            """
            self.line_height_css_classes.append(line_height_6x_css)


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

    @property
    def css_template(self):
        zindex_template = [".z- {z-index: [];}", ".neg\:z- {z-index: -[];}"]
        return zindex_template

    def zindex_default_helpers(self):
        """
        :Date: June 27, 2022.
        """
        zindex_default_css = f"""
        .z-auto {{z-index: auto;}}
        .z-initial {{z-index: initial;}}
        .z-inherit {{z-index: inherit;}}
        .z-unset {{z-index: unset;}}
        .z-100 {{z-index: 100;}}
        .z-1000 {{z-index: 1000;}}
        .neg\:z-100 {{z-index: -100;}}
        .neg\:z-1000 {{z-index: -1000;}}
        """
        self.zindex_css_classes.append(zindex_default_css)

    def zindex_helpers(self):
        """
        :Date: June 27, 2022.
        """
        for i in range(0, 11, 1):
            zindex_helper_css = f"""
            .z-{i} {{z-index: {i}}}
            """
            self.zindex_css_classes.append(zindex_helper_css)

    def negative_zindex_helpers(self):
        """
        :Date: June 27, 2022.
        """
        for i in range(0, 11, 1):
            negative_zindex_helper_css = f"""
            .neg\:z-{i} {{z-index: {-i}}}
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
        self.radius_defaults()
        self.radius_circle()
        self.radius_round()
        self.radius()
        self.radius_top()
        self.radius_bottom()

    @property
    def css_properties(self):
        return self.radius_css_classes

    def radius_defaults(self):
        """ :Date: August 10, 2022. """
        radius_defaults_css = f"""
        .radius-unset {{border-radius: unset;}}
        .radius-inherit {{border-radius: inherit;}}
        .radius-initial {{border-radius: initial;}}
        .radius-revert {{border-radius: revert;}}
        .radius-revert-layer {{border-radius: revert-layer;}}
        """
        self.radius_css_classes.append(radius_defaults_css)

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
        .radius {{border-radius: {self.default_radius}px;}}
        .radius-sm {{border-radius: {self.default_radius - (2 * 1)}px;}}
        .radius-smr {{border-radius: {self.default_radius - (2 * 2)}px;}}
        .radius-smt {{border-radius: {self.default_radius - (2 * 3)}px;}}
        .radius-xs {{border-radius: {self.default_radius - (2 * 4) + 1}px;}}
        
        .radius2 {{border-radius: {self.default_radius * 2}px;}}
        .radius2-sm {{border-radius: {(self.default_radius * 2) - (2 * 1)}px;}}
        .radius2-smr {{border-radius: {(self.default_radius * 2) - (2 * 2)}px;}}
        .radius2-smt {{border-radius: {(self.default_radius * 2) - (2 * 3)}px;}}
        .radius2-xs {{border-radius: {(self.default_radius * 2) - (2 * 4) + 1}px;}}
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
        self.gen_2x_square()
        self.gen_3x_square()
        self.gen_4x_square()
        self.gen_5x_square()
        self.gen_6x_square()
        self.gen_7x_square()
        self.gen_8x_square()

    @property
    def css_properties(self):
        return self.square_css_classes

    def gen_square(self):
        """:Date: inherit"""
        for i in range(1, 13, 1):
            square_css = f"""
            .square-{i} {{width: {i * self.default_square_value}px; height: {i * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_css)
        # return self.square_css_classes

    def gen_2x_square(self):
        """:Date: July 1, 2022. """
        for i in range(1, 13, 1):
            square_2x_css = f"""
            .square2-{i} {{width: {(i + 12) * self.default_square_value}px; height: {(i + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_2x_css)
        # return self.square_css_classes

    def gen_3x_square(self):
        """:Date: July 1, 2022. """
        for i in range(1, 13, 1):
            square_3x_css = f"""
            .square3-{i} {{width: {(i + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_3x_css)
        # return self.square_css_classes

    def gen_4x_square(self):
        """:Date: August 14, 2022. """
        for i in range(1, 13, 1):
            square_4x_css = f"""
            .square4-{i} {{width: {(i + 12 + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_4x_css)
        # return self.square_css_classes

    def gen_5x_square(self):
        """:Date: August 14, 2022. """
        for i in range(1, 13, 1):
            square_5x_css = f"""
            .square5-{i} {{width: {(i + 12 + 12 + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12 + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_5x_css)
        # return self.square_css_classes

    def gen_6x_square(self):
        """:Date: August 14, 2022. """
        for i in range(1, 13, 1):
            square_6x_css = f"""
            .square6-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_6x_css)
        # return self.square_css_classes

    def gen_7x_square(self):
        """:Date: September 4, 2022. """
        for i in range(1, 13, 1):
            square_7x_css = f"""
            .square7-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_7x_css)

    def gen_8x_square(self):
        """:Date: September 4, 2022. """
        for i in range(1, 13, 1):
            square_8x_css = f"""
            .square8-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px; height: {(i + 12 + 12 + 12 + 12 + 12 + 12 + 12) * self.default_square_value}px;}}
            """
            self.square_css_classes.append(square_8x_css)


class Squircles:
    """
    Squircles css classes.
    :Date: June 22, 2022.
    """

    def __init__(self) -> None:
        self.squircle_css_classes = list()
        self.default_squircle_value = 8
        self.default_squircle_border_radius = "42% 42% 42% 42% / 42% 42% 42% 42%"

        self.gen_squircle()
        self.gen_2x_squircle()
        self.gen_3x_squircle()
        self.gen_4x_squircle()
        self.gen_5x_squircle()
        self.gen_6x_squircle()
        self.gen_7x_squircle()
        self.gen_8x_squircle()

    @property
    def css_properties(self):
        return self.squircle_css_classes

    def gen_squircle(self):
        """:Date: inherit"""
        for i in range(1, 13, 1):
            squircle_css = f"""
            .squircle-{i} {{width: {i * self.default_squircle_value}px; height: {i * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius};}}
            """
            self.squircle_css_classes.append(squircle_css)
        # return self.squircle_css_classes

    def gen_2x_squircle(self):
        """:Date: inherit """
        for i in range(1, 13, 1):
            squircle_2x_css = f"""
            .squircle2-{i} {{width: {(i + 12) * self.default_squircle_value}px; height: {(i + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_2x_css)
        # return self.squircle_css_classes

    def gen_3x_squircle(self):
        """:Date: inherit """
        for i in range(1, 13, 1):
            squircle_3x_css = f"""
            .squircle3-{i} {{width: {(i + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_3x_css)
        # return self.squircle_css_classes

    def gen_4x_squircle(self):
        """:Date: inherit """
        for i in range(1, 13, 1):
            squircle_4x_css = f"""
            .squircle4-{i} {{width: {(i + 12 + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_4x_css)
        # return self.squircle_css_classes

    def gen_5x_squircle(self):
        """:Date: August 14, 2022. """
        for i in range(1, 13, 1):
            squircle_5x_css = f"""
            .squircle5-{i} {{width: {(i + 12 + 12 + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12 + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_5x_css)
        # return self.squircle_css_classes

    def gen_6x_squircle(self):
        """:Date: August 14, 2022. """
        for i in range(1, 13, 1):
            squircle_6x_css = f"""
            .squircle6-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_6x_css)
        # return self.squircle_css_classes

    def gen_7x_squircle(self):
        """:Date: September 4, 2022. """
        for i in range(1, 13, 1):
            squircle_7x_css = f"""
            .squircle7-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_7x_css)

    def gen_8x_squircle(self):
        """:Date: September 4, 2022. """
        for i in range(1, 13, 1):
            squircle_8x_css = f"""
            .squircle8-{i} {{width: {(i + 12 + 12 + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; height: {(i + 12 + 12 + 12 + 12 + 12 + 12 + 12) * self.default_squircle_value}px; border-radius: {self.default_squircle_border_radius}}}
            """
            self.squircle_css_classes.append(squircle_8x_css)


class Texts(Root):
    """
    Texts css classes.
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        super().__init__()
        self.text_css_classes = list()
        self.default_text_value = 16
        self.default_font_thin = 100
        self.default_font_extralight = 200
        self.default_font_light = 300
        self.default_font_regular = 400
        self.default_font_medium = 500
        self.default_font_semibold = 600
        self.default_font_bold = 700
        self.default_font_extrabold = 800
        self.default_font_black = 900

        # generate the text css helpers
        self.text_align()
        self.text_styles()
        self.text_weight()
        self.text_overflow()
        self.default_font_size()
        self.gen_font_size()
        self.font_size()
        self.font_family()
        self.font_smoothing()
        self.text_decoration_default()
        self.text_decoration_line()
        self.text_decoration_style()
        self.text_decoration_color()
        self.text_decoration_thickness()
        self.text_break()
        self.text_underline_offset()
        self.text_transform()
        self.text_overflow_helpers()
        self.text_indent()

    @property
    def css_properties(self):
        return self.text_css_classes

    @property
    def css_template(self):
        """ Text CSS Template.
        :Date: August 9, 2022.
        """
        font_template = [
            ".decoration- {text-decoration(): [];}"
        ]
        return font_template

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
        .font-regular {{font-weight: {self.default_font_regular};}}
        .font-medium {{font-weight: {self.default_font_medium};}}
        .font-semibold {{font-weight: {self.default_font_semibold};}}
        .font-bold {{font-weight: {self.default_font_bold};}}
        .font-extrabold {{font-weight: {self.default_font_extrabold};}}
        .font-black {{font-weight: {self.default_font_black};}}
        """
        self.text_css_classes.append(text_weight_css)

    def font_size(self):
        """:Date: August 28, 2022."""
        font_size_css = f"""
        .font-size-unset {{font-size: unset;}}
        .font-size-initial {{font-size: initial;}}
        .font-size-inherit {{font-size: inherit;}}
        .font-size-revert {{font-size: revert;}}
        .font-size-revert-layer {{font-size: revert-layer;}}
        """
        self.text_css_classes.append(font_size_css)

    @staticmethod
    def font_size_template():
        """:Date: July 1, 2022."""
        font_size_sequence_template = "0.08, 0.08, 0.08, 0.09"
        return font_size_sequence_template.replace(" ", "").split(",")

    def gen_font_size(self, nth_size=40):
        """ :Date: July 1, 2022. """
        from decimal import Decimal
        prev_ = Decimal("0.01")
        for index, i in enumerate(self.font_size_template() * nth_size, 1):
            prev_ += Decimal(i).quantize(Decimal("0.00"))
            font_size_css = f".font-{index} {{font-size: {prev_}rem;}}"
            self.text_css_classes.append(font_size_css)

    def default_font_size(self):
        """:Date: inherit (Modified: July 1, 2022)
        Define font_sizes using rem according to css-tricks
        Also, let the environment define your styles, don't make assumptions. - Also from csstricks.com
        Embrace a diverse web!
        The bottom line is this: we don’t have control over how content is consumed. Users have personal browser
        settings, the ability to zoom in and out, and various other ways to customize their reading experience.
        But we do have best CSS best practices we can use to maintain a good user experience alongside those preferences

        Work with proportions instead of explicit sizes.
        Rely on default browser font sizes instead of setting it on the :root, <html> or <body>.
        Use rem units to help scale content with a user’s personal preferences.
        Avoid making assumptions and let the environment decide how your content is being consumed.

        :root {
          --font-size--small: calc((14/16) * 1rem); /* 14px */
          --font-size--default: calc((16/16) * 1rem); /* 16px */
          --font-size--large: calc((24/16) * 1rem); /* 24px */
        }
        """
        # .font2-h {{font-size: }}
        default_font_size_css = f"""
        .font-h1 {{font-size: {(32 / 16) * 1}rem;}}
        .font-h2 {{font-size: {(24 / 16) * 1}rem;}}
        .font-h3 {{font-size: {(18.72 / 16) * 1}rem;}}
        .font-h4 {{font-size: {(16 / 16) * 1}rem;}}
        .font-h5 {{font-size: {(13.28 / 16) * 1}rem;}}
        .font-h6 {{font-size: {(10.72 / 16) * 1}rem;}}
        """
        self.text_css_classes.append(default_font_size_css)

    def text_overflow(self):
        """:Date: July 1, 2022."""
        text_overflow_css = f"""
        .overflow-unset {{text-overflow: unset;}}
        .overflow-initial {{text-overflow: initial;}}
        .overflow-inherit {{text-overflow: inherit;}}
        .overflow-ellipsis {{text-overflow: ellipsis;}}
        .overflow-clip {{text-overflow: clip;}}
        """
        self.text_css_classes.append(text_overflow_css)

    def font_family(self):
        """ :Date: July 18, 2022. """
        font_family_css = f"""
        .font-family-inherit {{font-family: inherit}}
        .font-family-initial {{font-family: initial}}
        .font-family-unset {{font-family: unset}}
        .font-family-revert {{font-family: revert}}
        .font-family-revert-layer {{font-family: revert-layer}}
        .font-sans {{font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";}}
        .font-serif {{font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;}}
        .font-mono {{font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;}}
        """
        self.text_css_classes.append(font_family_css)

    def font_smoothing(self):
        """ :Date: July 18, 2022. """
        font_family_css = f"""
        .smooth-antialised {{-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;}}
        .smooth-auto {{-webkit-font-smoothing: auto; -moz-osx-font-smoothing: auto;}}
        """
        self.text_css_classes.append(font_family_css)

    def text_decoration_default(self):
        """:Date: August 28, 2022."""
        text_decoration_css = f"""
        .decoration-unset {{text-decoration: unset;}}
        .decoration-initial {{text-decoration: initial;}}
        .decoration-inherit {{text-decoration: inherit;}}
        .decoration-revert {{text-decoration: revert;}}
        .decoration-revert-layer {{text-decoration: revert-layer;}}
        .decoration-none {{text-decoration: none;}}
        """
        self.text_css_classes.append(text_decoration_css)

    def text_decoration_line(self):
        """:Date: August 28, 2022."""
        text_decoration_css = f"""
        .underline {{text-decoration: underline;}}
        .overline {{text-decoration: overline;}}
        .line-through {{text-decoration: line-through;}}
        """
        self.text_css_classes.append(text_decoration_css)

    def text_decoration_style(self):
        """:Date: August 28, 2022."""
        text_decoration_css = f"""
        .decoration-solid {{text-decoration-style: solid;}}
        .decoration-double {{text-decoration-style: double;}}
        .decoration-dotted {{text-decoration-style: dotted;}}
        .decoration-dashed {{text-decoration-style: dashed;}}
        .decoration-wavy {{text-decoration-style: wavy;}}
        """
        self.text_css_classes.append(text_decoration_css)

    def text_decoration_color(self):
        """:Date: August 28, 2022."""
        for k, v in self.color_dictionary().items():
            text_decoration_css = f"""
            .decoration-{k} {{text-decoration-color: {v};}}
            """
            self.text_css_classes.append(text_decoration_css)

    def text_decoration_thickness(self):
        """:Date: August 28, 2022."""
        text_decoration_css = f"""
        .decoration-auto {{text-decoration-thickness: auto;}}
        .decoration-from-font {{text-decoration-thickness: from-font;}}
        """
        for i in range(1, 13, 1):
            text_decoration_thickness_css = f"""
            .decoration-{i} {{text-decoration-thickness: {i}px;}}
            """
            self.text_css_classes.append(text_decoration_thickness_css)
        self.text_css_classes.append(text_decoration_css)

    def text_break(self):
        """:Date: December 28, 2022."""
        text_break_css = f"""
        .break-normal {{overflow-wrap: normal; word-break: normal;}}
        .break-word {{overflow-wrap: break-word;}}
        .break-all {{word-break: break-all;}}
        """
        self.text_css_classes.append(text_break_css)

    def text_underline_offset(self):
        """:Date: December 28, 2022."""
        text_underline_offset_default_css = f"""
        .underline-offset-auto {{text-underline-offset: auto;}}
        .underline-offset-0 {{text-underline-offset: 0;}}
        .underline-offset-unset {{text-underline-offset: unset;}}
        .underline-offset-initial {{text-underline-offset: initial;}}
        .underline-offset-inherit {{text-underline-offset: inherit;}}
        .underline-offset-revert {{text-underline-offset: revert;}}
        .underline-offset-revert-layer {{text-underline-offset: revert-layer;}}
        """
        for i in range(1, 13, 1):
            text_underline_offset_css = f"""
            .underline-offset-{i} {{text-underline-offset: {i}px;}}
            """
            self.text_css_classes.append(text_underline_offset_css)
        self.text_css_classes.append(text_underline_offset_default_css)

    def text_transform(self):
        """:Date: December 28, 2022."""
        text_transform_css = f"""
        .normal-case {{text-transform: none;}}
        .uppercase {{text-transform: uppercase;}}
        .lowercase {{text-transform: lowercase;}}
        .capitalize {{text-transform: capitalize;}}
        """
        self.text_css_classes.append(text_transform_css)

    def text_overflow_helpers(self):
        """:Date: December 28, 2022."""
        text_overflow_css = f"""
        .text-ellipsis {{overflow-x: hidden; white-space: nowrap; text-overflow: ellipsis;}}
        .text-clip {{overflow-x: hidden; white-space: nowrap; text-overflow: clip;}}
        """
        self.text_css_classes.append(text_overflow_css)

    def text_indent(self):
        """:Date: December 28, 2022."""
        text_indent_default_css = f"""
        .indent-initial {{text-indent: initial;}}
        .indent-inherit {{text-indent: inherit;}}
        .indent-unset {{text-indent: unset;}}
        .indent-revert {{text-indent: revert;}}
        .indent-revert-layer {{text-indent: revert-layer;}}
        .indent-0 {{text-indent: 0;}}
        """
        for i in range(1, 13, 1):
            for j in range(1, 13, 1):
                text_indent_css = f"""
                indent{i if i > 1 else ''}-{j} {{text-underline-offset: {i*j}px;}}
                """
                self.text_css_classes.append(text_indent_css)


class Colors(Root):
    """
    Colors css classes.
    :Date: June 19, 2022.
    """

    def __init__(self) -> None:
        super().__init__()
        self.color_css_classes = list()
        self.color_helpers()
        self.color_default()
        self.white_color()
        self.black_color()
        self.light_color()
        self.lighter_color()
        self.green_color()
        self.blue_color()
        self.red_color()
        self.purple_color()
        self.yellow_color()

    @property
    def css_properties(self):
        return self.color_css_classes

    @property
    def css_template(self):
        """ A Function that returns the templates of color.
        :Date: August 9, 2022.
        """
        color_template = [".color- {color: [];}"]
        return color_template

    def color_template(self):
        """ Color Template method.
        :Date: July 30, 2022.
        """
        color_template = """
        .color-{} {color: [];}
        """
        return color_template

    def create_color_css(self, key, value):
        """ Eye.css Color CSS Class Create method."""
        self.color_template()

    def color_helpers(self):
        """ Color helper method.
        :Date: July 30, 2022.
        """
        for k, v in self.color_dictionary().items():
            color = f"""
            .color-{k} {{color: {v};}}
            """
            self.color_css_classes.append(color)

    def color_default(self):
        """
        :Date: June 27, 2022.
        """
        color_default = f"""
        .color-unset {{color: unset;}}
        .color-initial {{color: initial;}}
        .color-inherit {{color: inherit;}}
        .color-revert {{color: revert;}}
        .color-revert-layer {{color: revert-layer;}}
        .color-current {{color: currentColor;}}
        .color-transparent {{color: transparent;}}
        """
        self.color_css_classes.append(color_default)

    def black_color(self):
        """ :Date: July 1, 2022. """
        black_color = f"""
        .color-black {{color: {self.default_color_black};}}
        .color-black-transparent {{color: {self.default_color_black_transparent};}}
        """
        self.color_css_classes.append(black_color)

    def white_color(self):
        """ :Date: July 1, 2022. """
        white_color = f"""
        .color-white {{color: {self.default_color_white};}}
        .color-white-solid {{color: {self.default_color_white_solid};}}
        .color-white-transparent {{color: {self.default_color_white_transparent};}}
        .color-white-disabled {{color: {self.default_color_white_disabled};}}
        """
        self.color_css_classes.append(white_color)

    def light_color(self):
        """ :Date: July 1, 2022. """
        light_color = f"""
        .color-light {{color: {self.default_color_light};}}
        .color-light-solid {{color: {self.default_color_light_solid};}}
        .color-light-hover {{color: {self.default_color_light_hover};}}
        .color-light-disabled {{color: {self.default_color_light_disabled};}}
        """
        self.color_css_classes.append(light_color)

    def lighter_color(self):
        """ :Date: July 1, 2022. """
        lighter_color = f"""
        .color-lighter {{color: {self.default_color_lighter};}}
        .color-lighter-solid {{color: {self.default_color_lighter_solid};}}
        .color-lighter-hover {{color: {self.default_color_lighter_hover};}}
        .color-lighter-disabled {{color: {self.default_color_lighter_disabled};}}
        """
        self.color_css_classes.append(lighter_color)

    def green_color(self):
        """ :Date: July 1, 2022. """
        green_color = f"""
        .color-green {{color: {self.default_color_green};}}
        .color-green-solid {{color: {self.default_color_green_solid};}}
        .color-green-hover {{color: {self.default_color_green_hover};}}
        .color-green-disabled {{color: {self.default_color_green_disabled};}}
        .color-green-dark {{color: {self.default_color_green_dark};}}
        .color-green-border {{color: {self.default_color_green_border};}}
        .color-green-inverse {{color: {self.default_color_green_inverse};}}
        .color-green-inverse-hover {{color: {self.default_color_green_inverse_hover};}}
        """
        self.color_css_classes.append(green_color)

    def blue_color(self):
        """ :Date: July 1, 2022. """
        blue_color = f"""
        .color-blue {{color: {self.default_color_blue};}}
        .color-blue-solid {{color: {self.default_color_blue_solid};}}
        .color-blue-hover {{color: {self.default_color_blue_hover};}}
        .color-blue-disabled {{color: {self.default_color_blue_disabled};}}
        .color-blue-dark {{color: {self.default_color_blue_dark};}}
        .color-blue-border {{color: {self.default_color_blue_border};}}
        .color-blue-inverse {{color: {self.default_color_blue_inverse};}}
        .color-blue-inverse-hover {{color: {self.default_color_blue_inverse_hover};}}
        """
        self.color_css_classes.append(blue_color)

    def red_color(self):
        """ :Date: July 1, 2022. """
        red_color = f"""
        .color-red {{color: {self.default_color_red};}}
        .color-red-solid {{color: {self.default_color_red_solid};}}
        .color-red-hover {{color: {self.default_color_red_hover};}}
        .color-red-disabled {{color: {self.default_color_red_disabled};}}
        .color-red-dark {{color: {self.default_color_red_dark};}}
        .color-red-border {{color: {self.default_color_red_border};}}
        .color-red-inverse {{color: {self.default_color_red_inverse};}}
        .color-red-inverse-hover {{color: {self.default_color_red_inverse_hover};}}
        """
        self.color_css_classes.append(red_color)

    def purple_color(self):
        """ :Date: July 1, 2022. """
        purple_color = f"""
        .color-purple {{color: {self.default_color_purple};}}
        .color-purple-solid {{color: {self.default_color_purple_solid};}}
        .color-purple-hover {{color: {self.default_color_purple_hover};}}
        .color-purple-disabled {{color: {self.default_color_purple_disabled};}}
        .color-purple-dark {{color: {self.default_color_purple_dark};}}
        .color-purple-border {{color: {self.default_color_purple_border};}}
        .color-purple-inverse {{color: {self.default_color_purple_inverse};}}
        .color-purple-inverse-hover {{color: {self.default_color_purple_inverse_hover};}}
        """
        self.color_css_classes.append(purple_color)

    def yellow_color(self):
        """ :Date: July 1, 2022. """
        yellow_color = f"""
        .color-yellow {{color: {self.default_color_itheirs};}}
        .color-yellow-solid {{color: {self.default_color_itheirs_solid};}}
        .color-yellow-hover {{color: {self.default_color_itheirs_hover};}}
        .color-yellow-disabled {{color: {self.default_color_itheirs_disabled};}}
        .color-yellow-dark {{color: {self.default_color_itheirs_dark};}}
        .color-yellow-border {{color: {self.default_color_itheirs_border};}}
        .color-yellow-inverse {{color: {self.default_color_itheirs_inverse};}}
        .color-yellow-inverse-hover {{color: {self.default_color_itheirs_inverse_hover};}}
        """
        self.color_css_classes.append(yellow_color)


class Backgrounds(Root):
    """
    Background css classes.
    :Date: July 1, 2022.
    """

    def __init__(self) -> None:
        super().__init__()
        self.bg_css_classes = list()
        self.bg_helpers()
        self.default_bg()
        self.white_bg()
        self.black_bg()
        self.light_bg()
        self.lighter_bg()
        self.green_bg()
        self.blue_bg()
        self.red_bg()
        self.purple_bg()
        self.yellow_bg()
        self.mica_bg()
        self.bg_blend()
        self.mix_blend()
        self.bg_attachment()
        self.bg_clip()
        self.bg_image()
        self.bg_origin()
        self.bg_position()
        self.bg_repeat()
        self.bg_size()

    @property
    def css_properties(self):
        return self.bg_css_classes

    def css_templates(self):
        """ Background templates.
        :Date: August 9, 2022.
        """
        background_template = [".bg-"]
        return background_template

    @property
    def css_template(self):
        """ :Date: July 30, 2022. """
        bg_template = """
        .bg- {background: [];}
        .bg-image- {background-image: [];}
        .bg-blend- {background-blend-mode: [];}
        .mix-blend- {mix-blend-mode: [];}
        .bg-attachment- {background-attachment: [];}
        .bg-clip- {background-clip: [];}
        .bg-origin- {background-origin: [];}
        .bg-position- {background-position: [];}
        .bg-pos- {background-position: [];}
        .bg-repeat- {background-repeat: [];}
        .bg-size- {background-size: [];}
        """
        return bg_template

    def bg_helpers(self):
        """ Background Color helper method.
        :Date: August 14, 2022.
        """
        for k, v in self.color_dictionary().items():
            bg_color = f"""
             .bg-{k} {{background-color: {v};}}
             """
            self.bg_css_classes.append(bg_color)

    def default_bg(self):
        """
        :Date: inherit.
        """
        background_defaults = f"""
        .bg-unset {{background: unset;}}
        .bg-initial {{background: initial;}}
        .bg-inherit {{background: inherit;}}
        .bg-fixed {{background: fixed;}}
        .bg-local {{background: local;}}
        .bg-none {{background: none;}}
        .bg-scroll {{background: scroll;}}
        .bg-transparent {{background: transparent;}}
        .bg-content-box {{background: content-box;}}
        .bg-current-color {{background: currentColor;}}
        """
        return self.bg_css_classes.append(background_defaults)

    def black_bg(self):
        """ :Date: July 1, 2022. """
        black_bg = f"""
        .bg-black {{background-color: {self.default_color_black};}}
        .bg-black-transparent {{background-color: {self.default_color_black_transparent};}}
        """
        self.bg_css_classes.append(black_bg)

    def white_bg(self):
        """ :Date: July 1, 2022. """
        white_bg = f"""
        .bg-white {{background-color: {self.default_color_white};}}
        .bg-white-solid {{background-color: {self.default_color_white_solid};}}
        .bg-white-transparent {{background-color: {self.default_color_white_transparent};}}
        .bg-white-disabled {{background-color: {self.default_color_white_disabled};}}
        """
        self.bg_css_classes.append(white_bg)

    def light_bg(self):
        """ :Date: July 1, 2022. """
        light_bg = f"""
        .bg-light {{background-color: {self.default_color_light};}}
        .bg-light-solid {{background-color: {self.default_color_light_solid};}}
        .bg-light-hover {{background-color: {self.default_color_light_hover};}}
        .bg-light-disabled {{background-color: {self.default_color_light_disabled};}}
        """
        self.bg_css_classes.append(light_bg)

    def lighter_bg(self):
        """ :Date: July 1, 2022. """
        lighter_bg = f"""
        .bg-lighter {{background-color: {self.default_color_lighter};}}
        .bg-lighter-solid {{background-color: {self.default_color_lighter_solid};}}
        .bg-lighter-hover {{background-color: {self.default_color_lighter_hover};}}
        .bg-lighter-disabled {{background-color: {self.default_color_lighter_disabled};}}
        """
        self.bg_css_classes.append(lighter_bg)

    def green_bg(self):
        """ :Date: July 1, 2022. """
        green_bg = f"""
        .bg-green {{background-color: {self.default_color_green};}}
        .bg-green-solid {{background-color: {self.default_color_green_solid};}}
        .bg-green-hover {{background-color: {self.default_color_green_hover};}}
        .bg-green-disabled {{background-color: {self.default_color_green_disabled};}}
        .bg-green-dark {{background-color: {self.default_color_green_dark};}}
        .bg-green-border {{background-color: {self.default_color_green_border};}}
        .bg-green-inverse {{background-color: {self.default_color_green_inverse};}}
        .bg-green-inverse-hover {{background-color: {self.default_color_green_inverse_hover};}}
        """
        self.bg_css_classes.append(green_bg)

    def blue_bg(self):
        """ :Date: July 1, 2022. """
        blue_bg = f"""
        .bg-blue {{background-color: {self.default_color_blue};}}
        .bg-blue-solid {{background-color: {self.default_color_blue_solid};}}
        .bg-blue-hover {{background-color: {self.default_color_blue_hover};}}
        .bg-blue-disabled {{background-color: {self.default_color_blue_disabled};}}
        .bg-blue-dark {{background-color: {self.default_color_blue_dark};}}
        .bg-blue-border {{background-color: {self.default_color_blue_border};}}
        .bg-blue-inverse {{background-color: {self.default_color_blue_inverse};}}
        .bg-blue-inverse-hover {{background-color: {self.default_color_blue_inverse_hover};}}
        """
        self.bg_css_classes.append(blue_bg)

    def red_bg(self):
        """ :Date: July 1, 2022. """
        red_bg = f"""
        .bg-red {{background-color: {self.default_color_red};}}
        .bg-red-solid {{background-color: {self.default_color_red_solid};}}
        .bg-red-hover {{background-color: {self.default_color_red_hover};}}
        .bg-red-disabled {{background-color: {self.default_color_red_disabled};}}
        .bg-red-dark {{background-color: {self.default_color_red_dark};}}
        .bg-red-border {{background-color: {self.default_color_red_border};}}
        .bg-red-inverse {{background-color: {self.default_color_red_inverse};}}
        .bg-red-inverse-hover {{background-color: {self.default_color_red_inverse_hover};}}
        """
        self.bg_css_classes.append(red_bg)

    def purple_bg(self):
        """ :Date: July 1, 2022. """
        purple_bg = f"""
        .bg-purple {{background-color: {self.default_color_purple};}}
        .bg-purple-solid {{background-color: {self.default_color_purple_solid};}}
        .bg-purple-hover {{background-color: {self.default_color_purple_hover};}}
        .bg-purple-disabled {{background-color: {self.default_color_purple_disabled};}}
        .bg-purple-dark {{background-color: {self.default_color_purple_dark};}}
        .bg-purple-border {{background-color: {self.default_color_purple_border};}}
        .bg-purple-inverse {{background-color: {self.default_color_purple_inverse};}}
        .bg-purple-inverse-hover {{background-color: {self.default_color_purple_inverse_hover};}}
        """
        self.bg_css_classes.append(purple_bg)

    def yellow_bg(self):
        """ :Date: July 1, 2022. """
        yellow_bg = f"""
        .bg-yellow {{background-color: {self.default_color_itheirs};}}
        .bg-yellow-solid {{background-color: {self.default_color_itheirs_solid};}}
        .bg-yellow-hover {{background-color: {self.default_color_itheirs_hover};}}
        .bg-yellow-disabled {{background-color: {self.default_color_itheirs_disabled};}}
        .bg-yellow-dark {{background-color: {self.default_color_itheirs_dark};}}
        .bg-yellow-border {{background-color: {self.default_color_itheirs_border};}}
        .bg-yellow-inverse {{background-color: {self.default_color_itheirs_inverse};}}
        .bg-yellow-inverse-hover {{background-color: {self.default_color_itheirs_inverse_hover};}}
        """
        self.bg_css_classes.append(yellow_bg)

    def mica_bg(self):
        """:Date: July 1, 2022."""
        mica_bg = f"""
        .bg-mica {{backdrop-filter: blur(8px);}}
        .bg-mica-sm {{backdrop-filter: blur(6px);}}
        .bg-mica-smr {{backdrop-filter: blur(4px);}}
        .bg-mica-smt {{backdrop-filter: blur(2px);}}
        .bg-mica-xs {{backdrop-filter: blur(1px);}}
        """
        self.bg_css_classes.append(mica_bg)

        for i in range(2, 8, 1):
            mica_bg = f"""
            .bg-mica{i} {{backdrop-filter: blur({(i * 8)}px);}}
            .bg-mica{i}-sm {{backdrop-filter: blur({(i * 8) - 2}px);}}
            .bg-mica{i}-smr {{backdrop-filter: blur({(i * 8) - 4}px);}}
            .bg-mica{i}-smt {{backdrop-filter: blur({(i * 8) - 6}px);}}
            .bg-mica{i}-xs {{backdrop-filter: blur({(i * 8) - 7}px);}}
            """
            self.bg_css_classes.append(mica_bg)

    def bg_blend(self):
        """ :Date: July 18, 2022. """
        blend_bg_css = f"""
        .bg-blend-normal {{background-blend-mode: normal;}}
        .bg-blend-multiply {{background-blend-mode: multiply;}}
        .bg-blend-screen {{background-blend-mode: screen;}}
        .bg-blend-overlay {{background-blend-mode: overlay;}}
        .bg-blend-darken {{background-blend-mode: darken;}}
        .bg-blend-lighten {{background-blend-mode: lighten;}}
        .bg-blend-dodge {{background-blend-mode: dodge;}}
        .bg-blend-burn {{background-blend-mode: burn;}}
        .bg-blend-hard {{background-blend-mode: hard;}}
        .bg-blend-soft {{background-blend-mode: soft;}}
        .bg-blend-difference {{background-blend-mode: difference;}}
        .bg-blend-exclusion {{background-blend-mode: exclusion;}}
        .bg-blend-hue {{background-blend-mode: hue;}}
        .bg-blend-saturation {{background-blend-mode: saturation;}}
        .bg-blend-color {{background-blend-mode: color;}}
        .bg-blend-luminosity {{background-blend-mode: luminosity;}}
        """
        self.bg_css_classes.append(blend_bg_css)

    def mix_blend(self):
        """ :Date: July 18, 2022. """
        mix_blend_css = f"""
        .mix-blend-normal {{mix-blend-mode: normal;}}
        .mix-blend-multiply {{mix-blend-mode: multiply;}}
        .mix-blend-screen {{mix-blend-mode: screen;}}
        .mix-blend-overlay {{mix-blend-mode: overlay;}}
        .mix-blend-darken {{mix-blend-mode: darken;}}
        .mix-blend-lighten {{mix-blend-mode: lighten;}}
        .mix-blend-dodge {{mix-blend-mode: dodge;}}
        .mix-blend-burn {{mix-blend-mode: burn;}}
        .mix-blend-hard {{mix-blend-mode: hard;}}
        .mix-blend-soft {{mix-blend-mode: soft;}}
        .mix-blend-difference {{mix-blend-mode: difference;}}
        .mix-blend-exclusion {{mix-blend-mode: exclusion;}}
        .mix-blend-hue {{mix-blend-mode: hue;}}
        .mix-blend-saturation {{mix-blend-mode: saturation;}}
        .mix-blend-color {{mix-blend-mode: color;}}
        .mix-blend-luminosity {{mix-blend-mode: luminosity;}}
        """
        self.bg_css_classes.append(mix_blend_css)

    def bg_attachment(self):
        """ :Date: July 18, 2022. """
        bg_attachment_css = f"""
        .bg-attachment-inherit {{background-attachment: inherit;}}
        .bg-attachment-initial {{background-attachment: initial;}}
        .bg-attachment-unset {{background-attachment: unset;}}
        .bg-attachment-revert {{background-attachment: revert;}}
        .bg-attachment-revert-layer {{background-attachment: revert-layer;}}
        .bg-attachment-scroll {{background-attachment: scroll;}}
        .bg-attachment-fixed {{background-attachment: fixed;}}
        .bg-attachment-local {{background-attachment: local;}}
        """
        self.bg_css_classes.append(bg_attachment_css)

    def bg_clip(self):
        """ :Date: July 18, 2022. """
        bg_clip_css = f"""
        .bg-clip-unset {{background-clip: unset;}}
        .bg-clip-initial {{background-clip: initial;}}
        .bg-clip-inherit {{background-clip: inherit;}}
        .bg-clip-revert {{background-clip: revert;}}
        .bg-clip-revert-layer {{background-clip: revert-layer;}}
        .bg-clip-border {{background-clip: border-box;}}
        .bg-clip-content {{background-clip: content-box;}}
        .bg-clip-padding {{background-clip: padding-box;}}
        .bg-clip-text {{background-clip: text; -webkit-background-clip: text;}}
        """
        self.bg_css_classes.append(bg_clip_css)

    def bg_image(self):
        """ :Date: July 18, 2022. """
        bg_image_css = f"""
        .bg-image-unset {{background-image: unset;}}
        .bg-image-initial {{background-image: initial;}}
        .bg-image-inherit {{background-image: inherit;}}
        .bg-image-revert {{background-image: revert;}}
        .bg-image-revert-layer {{background-image: revert-layer;}}
        """
        # .bg-image-url {{background-image: url;}}
        self.bg_css_classes.append(bg_image_css)

    def bg_origin(self):
        """ :Date: July 18, 2022. """
        bg_origin_css = f"""
        .bg-origin-unset {{background-origin: unset;}}
        .bg-origin-initial {{background-origin: initial;}}
        .bg-origin-inherit {{background-origin: inherit;}}
        .bg-origin-revert {{background-origin: revert;}}
        .bg-origin-revert-layer {{background-origin: revert-layer;}}
        .bg-origin-border {{background-origin: border-box;}}
        .bg-origin-content {{background-origin: content-box;}}
        .bg-origin-padding {{background-origin: padding-box;}}
        """
        self.bg_css_classes.append(bg_origin_css)

    def bg_position(self):
        """ :Date: July 18, 2022. """
        bg_position_css = f"""
        .bg-pos-unset {{background-position: unset;}}
        .bg-pos-initial {{background-position: initial;}}
        .bg-pos-inherit {{background-position: inherit;}}
        .bg-pos-revert {{background-position: revert;}}
        .bg-pos-revert-layer {{background-position: revert-layer;}}
        .bg-pos-center {{background-position: center;}}
        .bg-pos-top {{background-position: top;}}
        .bg-pos-bottom {{background-position: bottom;}}
        .bg-pos-left {{background-position: left;}}
        .bg-pos-right {{background-position: right;}}

        .bg-pos-x-unset {{background-position-x: unset;}}
        .bg-pos-x-initial {{background-position-x: initial;}}
        .bg-pos-x-inherit {{background-position-x: inherit;}}
        .bg-pos-x-revert {{background-position-x: revert;}}
        .bg-pos-x-revert-layer {{background-position-x: revert-layer;}}
        .bg-pos-x-center {{background-position-x: center;}}
        .bg-pos-x-top {{background-position-x: top;}}
        .bg-pos-x-bottom {{background-position-x: bottom;}}
        .bg-pos-x-left {{background-position-x: left;}}
        .bg-pos-x-right {{background-position-x: right;}}

        .bg-pos-y-unset {{background-position-y: unset;}}
        .bg-pos-y-initial {{background-position-y: initial;}}
        .bg-pos-y-inherit {{background-position-y: inherit;}}
        .bg-pos-y-revert {{background-position-y: revert;}}
        .bg-pos-y-revert-layer {{background-position-y: revert-layer;}}
        .bg-pos-y-center {{background-position-y: center;}}
        .bg-pos-y-top {{background-position-y: top;}}
        .bg-pos-y-bottom {{background-position-y: bottom;}}
        .bg-pos-y-left {{background-position-y: left;}}
        .bg-pos-y-right {{background-position-y: right;}}

        .bg-pos-inline-unset {{background-position-inline: unset;}}
        .bg-pos-inline-initial {{background-position-inline: initial;}}
        .bg-pos-inline-inherit {{background-position-inline: inherit;}}
        .bg-pos-inline-revert {{background-position-inline: revert;}}
        .bg-pos-inline-revert-layer {{background-position-inline: revert-layer;}}
        .bg-pos-inline-center {{background-position-inline: center;}}
        .bg-pos-inline-top {{background-position-inline: top;}}
        .bg-pos-inline-bottom {{background-position-inline: bottom;}}
        .bg-pos-inline-left {{background-position-inline: left;}}
        .bg-pos-inline-right {{background-position-inline: right;}}

        .bg-pos-block-unset {{background-position-block: unset;}}
        .bg-pos-block-initial {{background-position-block: initial;}}
        .bg-pos-block-inherit {{background-position-block: inherit;}}
        .bg-pos-block-revert {{background-position-block: revert;}}
        .bg-pos-block-revert-layer {{background-position-block: revert-layer;}}
        .bg-pos-block-center {{background-position-block: center;}}
        .bg-pos-block-top {{background-position-block: top;}}
        .bg-pos-block-bottom {{background-position-block: bottom;}}
        .bg-pos-block-left {{background-position-block: left;}}
        .bg-pos-block-right {{background-position-block: right;}}
        """
        self.bg_css_classes.append(bg_position_css)

    def bg_repeat(self):
        """ :Date: July 18, 2022. """
        bg_repeat_css = f"""
        .bg-repeat-unset {{background-repeat: unset;}}
        .bg-repeat-inherit {{background-repeat: inherit;}}
        .bg-repeat-initial {{background-repeat: initial;}}
        .bg-repeat-revert {{background-repeat: revert;}}
        .bg-repeat-revert-layer {{background-repeat: revert-layer;}}
        .bg-repeat-x {{background-repeat: x;}}
        .bg-repeat-y {{background-repeat: y;}}
        .bg-repeat-space {{background-repeat: space;}}
        .bg-repeat-round {{background-repeat: round;}}
        .bg-norepeat {{background-repeat: no-repeat;}}
        .bg-repeat {{background-repeat: repeat;}}
        """
        self.bg_css_classes.append(bg_repeat_css)

    def bg_size(self):
        """ :Date: July 18, 2022. """
        bg_size_css = f"""
        .bg-size-unset {{background-size: unset;}}
        .bg-size-inherit {{background-size: inherit;}}
        .bg-size-initial {{background-size: initial;}}
        .bg-size-revert {{background-size: revert;}}
        .bg-size-revert-layer {{background-size: revert-layer;}}
        .bg-size-auto {{background-size: auto;}}
        .bg-size-contain {{background-size: contain;}}
        .bg-size-cover {{background-size: cover;}}
        """
        self.bg_css_classes.append(bg_size_css)


class Borders(Root):
    """
    Border css classes.
    :Date: June 27, 2022.
    """

    def __init__(self) -> None:
        super().__init__()
        self.border_css_classes = list()
        self.border_defaults()
        self.border_width_defaults()
        self.border_color()
        self.border_style()

    @property
    def css_properties(self):
        return self.border_css_classes

    @property
    def css_template(self):
        border_template = [
            ".border- {border(): [];}",
            ".border-x- {border-left(): []; border-right(): [];}",
            ".border-y- {border-top(): []; border-bottom(): [];}",
            ".border-t- {border-top(): [];}",
            ".border-r- {border-right(): [];}",
            ".border-b- {border-bottom(): [];}",
            ".border-l- {border-left(): [];}",
            ".border-top- {border-top(): [];}",
            ".border-right- {border-right(): [];}",
            ".border-bottom- {border-bottom(): [];}",
            ".border-left- {border-left(): [];}",

            ".em\:border- {border-width: [];}",
            ".em\:border-x- {border-left-width: []; border-right-width: [];}",
            ".em\:border-y- {border-top-width: []; border-bottom-width: [];}",
            ".em\:border-t- {border-top-width: [];}",
            ".em\:border-r- {border-right-width: [];}",
            ".em\:border-b- {border-bottom-width: [];}",
            ".em\:border-l- {border-left-width: [];}",
            ".em\:border-top- {border-top-width: [];}",
            ".em\:border-right- {border-right-width: [];}",
            ".em\:border-bottom- {border-bottom-width: [];}",
            ".em\:border-left- {border-left-width: [];}",
        ]
        return border_template

    def border_defaults(self):
        """:Date: july 1, 2022."""
        border_defaults_css = f"""
        .border-0 {{border: 0;}}
        .border-initial {{border: initial;}}
        .border-inherit {{border: inherit;}}
        .border-inset {{border: inset;}}
        .border-transparent {{border: transparent;}}
        .border-unset {{border: unset;}}
        """
        return self.border_css_classes.append(border_defaults_css)

    def border_color(self):
        """ :Date: July 30, 2022. """
        border_color_list = list()
        for i in ['', '-top', '-right', '-bottom', '-left']:
            for k, v in self.color_dictionary().items():
                border_color = f"""
                .border{i[:2] if len(i) > 0 else ""}-{k} {{border{i}-color: {v};}}
                """
                border_color_list.append(border_color)
        self.border_css_classes.extend(border_color_list)

    def border_style(self):
        """ :Date: July 18, 2022. """
        border_style_list = list()
        for i in ['', '-top', '-right', '-bottom', '-left']:
            border_style_css = f"""
            .border{i}-none {{border{i}-style: none;}}
            .border{i}-hidden {{border{i}-style: hidden;}}
            .border{i}-dotted {{border{i}-style: dotted;}}
            .border{i}-dashed {{border{i}-style: dashed;}}
            .border{i}-solid {{border{i}-style: solid;}}
            .border{i}-double {{border{i}-style: double;}}
            .border{i}-groove {{border{i}-style: groove;}}
            .border{i}-ridge {{border{i}-style: ridge;}}
            .border{i}-inset {{border{i}-style: inset;}}
            .border{i}-outset {{border{i}-style: outset;}}
            .border{i}-style-unset {{border{i}-style: unset;}}
            .border{i}-style-inherit {{border{i}-style: inherit;}}
            .border{i}-style-initial {{border{i}-style: initial;}}
            .border{i}-style-revert {{border{i}-style: revert;}}
            .border{i}-style-revert-layer {{border{i}-style: revert-layer;}}
            """
            border_style_list.append(border_style_css)

        self.border_css_classes.extend(border_style_list)

    def border_width_defaults(self):
        """ :Date: July 18, 2022. """
        for i in ['', '-top', '-right', '-bottom', '-left']:
            border_width_css = f"""
            .border{i[:2] if len(i) > 0 else ""}-thin {{border{i}-width: thin;}}
            .border{i[:2] if len(i) > 0 else ""}-medium {{border{i}-width: medium;}}
            .border{i[:2] if len(i) > 0 else ""}-thick {{border{i}-width: thick;}}
            .border{i[:2] if len(i) > 0 else ""}-width-unset {{border{i}-width: unset;}}
            .border{i[:2] if len(i) > 0 else ""}-width-inherit {{border{i}-width: inherit;}}
            .border{i[:2] if len(i) > 0 else ""}-width-initial {{border{i}-width: initial;}}
            .border{i[:2] if len(i) > 0 else ""}-width-revert {{border{i}-width: revert;}}
            .border{i[:2] if len(i) > 0 else ""}-width-revert-layer {{border{i}-width: revert-layer;}}
            """
            self.border_css_classes.append(border_width_css)


class Outlines(Root):
    """ :Date: July 24, 2022. """
    def __init__(self) -> None:
        super().__init__()
        self.outline_css_classes = list()
        self.outline_width_defaults()
        self.outline_color()
        self.outline_style()

    @property
    def css_properties(self):
        return self.outline_css_classes

    @property
    def css_template(self):
        outline_template = [
            ".outline- {outline(): [];}",
            ".em\:outline- {outline-width: [];}",
            ".outline-offset- {outline-offset: [];}",
            ".em\:outline-offset- {outline-offset: [];}"
            ".neg\:outline- {outline(): -[];}",
            ".neg\:em\:outline- {outline-width: -[];}",
            ".neg\:outline-offset- {outline-offset: -[];}",
            ".neg\:em\:outline-offset- {outline-offset-: [];}"
        ]
        return outline_template

    def outline_style(self):
        """ :Date: inherit """
        outline_style_list = list()
        outline_style_css = f"""
        .outline-none {{outline-style: none;}}
        .outline-hidden {{outline-style: hidden;}}
        .outline-dotted {{outline-style: dotted;}}
        .outline-dashed {{outline-style: dashed;}}
        .outline-solid {{outline-style: solid;}}
        .outline-double {{outline-style: double;}}
        .outline-groove {{outline-style: groove;}}
        .outline-ridge {{outline-style: ridge;}}
        .outline-inset {{outline-style: inset;}}
        .outline-outset {{outline-style: outset;}}
        .outline-style-unset {{outline-style: unset;}}
        .outline-style-inherit {{outline-style: inherit;}}
        .outline-style-initial {{outline-style: initial;}}
        .outline-style-revert {{outline-style: revert;}}
        .outline-style-revert-layer {{outline-style: revert-layer;}}
        """
        self.outline_css_classes.append(outline_style_css)

    def outline_color(self):
        """ :Date: July 30, 2022. """
        outline_color_list = list()
        for k, v in self.color_dictionary().items():
            outline_color = f"""
            .outline-{k} {{outline-color: {v};}}
            """
            outline_color_list.append(outline_color)
        self.outline_css_classes.extend(outline_color_list)

    def outline_width_defaults(self):
        """ :Date: inherit """
        outline_width_css = f"""
        .outline-thin {{outline-width: thin;}}
        .outline-medium {{outline-width: medium;}}
        .outline-thick {{outline-width: thick;}}
        .outline-width-unset {{outline-width: unset;}}
        .outline-width-inherit {{outline-width: inherit;}}
        .outline-width-initial {{outline-width: initial;}}
        .outline-width-revert {{outline-width: revert;}}
        .outline-width-revert-layer {{outline-width: revert-layer;}}
        """
        self.outline_css_classes.append(outline_width_css)


class Overflows:
    """ :Date: July 1, 2022. """

    def __init__(self) -> None:
        self.overflow_css_classes = list()
        self.overflow_helpers()

    @property
    def css_properties(self):
        return self.overflow_css_classes

    def overflow_helpers(self):
        """:Date: inherit"""
        overflow_css = f"""
        .overflow-initial {{overflow: initial}}
        .overflow-inherit {{overflow: inherit}}
        .overflow-revert {{overflow: revert}}
        .overflow-revert-layer {{overflow: revert-layer}}
        .overflow-visible {{overflow: visible}}
        .overflow-hidden {{overflow: hidden}}
        .overflow-clip {{overflow: clip}}
        .overflow-scroll {{overflow: scroll}}
        .overflow-auto {{overflow: auto}}
        .overflow-x-visible {{overflow-x: visible}}
        .overflow-x-hidden {{overflow-x: hidden}}
        .overflow-x-clip {{overflow-x: clip}}
        .overflow-x-scroll {{overflow-x: scroll}}
        .overflow-x-auto {{overflow-x: auto}}
        .overflow-y-visible {{overflow-y: visible}}
        .overflow-y-hidden {{overflow-y: hidden}}
        .overflow-y-clip {{overflow-y: clip}}
        .overflow-y-scroll {{overflow-y: scroll}}
        .overflow-y-auto {{overflow-y: auto}}
        """
        self.overflow_css_classes.append(overflow_css)


class Legacys:
    """
    These are the legacy css properties which do not have collections, just one-off properties,
    but very important to the working properly of other css properties.
    This class is called Legacy because there are substitutes for this css properties,
    but they are still very much supported across browsers, devices and platforms
    e.g., float, clear, white-space, etc.
    :Date: July 2, 2022."""

    def __init__(self) -> None:
        self.legacy_css_classes = list()
        self.legacy_whitespace_helpers()
        self.legacy_clear_helpers()
        self.legacy_float_helpers()
        self.legacy_cursor_helpers()
        self.legacy_content_helpers()

    @property
    def css_properties(self):
        return self.legacy_css_classes

    def legacy_whitespace_helpers(self):
        legacy_whitespace_css = f"""
        .white-space-nowrap {{white-space: nowrap;}}
        .white-space-pre {{white-space: pre;}}
        .white-space-prewrap {{white-space: pre-wrap;}}
        .white-space-preline {{white-space: pre-line;}}
        .white-space-normal {{white-space: normal;}}
        .white-space-unset {{white-space: unset;}}
        .white-space-initial {{white-space: initial;}}
        .white-space-inherit {{white-space: inherit;}}
        """
        self.legacy_css_classes.append(legacy_whitespace_css)

    def legacy_clear_helpers(self):
        legacy_clear_css = f"""
        .clear-unset {{clear: unset;}}
        .clear-initial {{clear: initial;}}
        .clear-inherit {{clear: inherit;}}
        .clear-both {{clear: both;}}
        .clear-left {{clear: left;}}
        .clear-right {{clear: right;}}
        .clear-none {{clear: none;}}
        """
        self.legacy_css_classes.append(legacy_clear_css)

    def legacy_float_helpers(self):
        legacy_float_css = f"""
        .float-unset {{float: unset;}}
        .float-initial {{float: initial;}}
        .float-inherit {{float: inherit;}}
        .float-left {{float: left;}}
        .float-right {{float: right;}}
        .float-none {{float: none;}}
        """
        self.legacy_css_classes.append(legacy_float_css)

    def legacy_cursor_helpers(self):
        """:Date:July 2, 2022."""
        cursor_css = f"""
        .cursor-auto {{cursor: auto;}}
        .cursor-inherit {{cursor: inherit;}}
        .cursor-none {{cursor: none;}}
        .cursor-unset {{cursor: unset;}}
        .cursor-initial {{cursor: initial;}}
        .cursor-default {{cursor: default;}}
        .cursor-pointer {{cursor: pointer;}}
        .cursor-not-allowed {{cursor: not-allowed;}}
        .cursor-move {{cursor: move;}}
        .cursor-n-resize {{cursor: n-resize;}}
        .cursor-e-resize {{cursor: e-resize;}}
        .cursor-ne-resize {{cursor: ne-resize;}}
        .cursor-nw-resize {{cursor: nw-resize;}}
        .cursor-ns-resize {{cursor: ns-resize;}}
        .cursor-w-resize {{cursor: w-resize;}}
        .cursor-s-resize {{cursor: s-resize;}}
        .cursor-sw-resize {{cursor: sw-resize;}}
        .cursor-se-resize {{cursor: se-resize;}}
        .cursor-ew-resize {{cursor: ew-resize;}}
        .cursor-nesw-resize {{cursor: nesw-resize;}}
        .cursor-nwse-resize {{cursor: nwse-resize;}}
        .cursor-row-resize {{cursor: row-resize;}}
        .cursor-col-resize {{cursor: col-resize;}}
        .cursor-all-scroll {{cursor: all-scroll;}}
        .cursor-zoom-in {{cursor: zoom-in;}}
        .cursor-zoom-out {{cursor: zoom-out;}}
        .cursor-progress {{cursor: progress;}}
        .cursor-text {{cursor: text;}}
        .cursor-context-menu {{cursor: context-menu;}}
        .cursor-help {{cursor: help;}}
        .cursor-wait {{cursor: wait;}}
        .cursor-cell {{cursor: cell;}}
        .cursor-crosshair {{cursor: crosshair;}}
        .cursor-vertical-text {{cursor: vertical-text;}}
        .cursor-alias {{cursor: alias;}}
        .cursor-copy {{cursor: copy;}}
        .cursor-no-drop {{cursor: no-drop;}}
        """
        self.legacy_css_classes.append(cursor_css)

    def legacy_content_helpers(self):
        legacy_content_css = f"""
        .content {{content: '';}}
        """
        self.legacy_css_classes.append(legacy_content_css)


class BoxShadows(Root):
    """ Date: July 12, 2022. """

    def __init__(self) -> None:
        super().__init__()
        self.box_shadow_default_dimen = 8
        self.box_shadow_css_classes = list()
        self.box_shadow_default_helpers()
        self.box_shadow_helpers()

    @property
    def css_properties(self):
        return self.box_shadow_css_classes

    @property
    def css_template(self):
        """ BoxShadows CSS Template.
        :Date: August 9, 2022.
        """
        shadow_template = [
            ".shadow-",
            ".shadow-t-",
            ".shadow-r-",
            ".shadow-b-",
            ".shadow-l-",
            ".shadow-top-",
            ".shadow-right-",
            ".shadow-bottom-",
            ".shadow-left-",
        ]
        return shadow_template

    def box_shadow_default_helpers(self):
        """ :Date: July 22, 2022. """
        box_shadow_default_css = f"""
        .shadow-0 {{box-shadow: 0px 0px 0px 0px transparent;}}
        .shadow-unset {{box-shadow: unset;}}
        .shadow-initial {{box-shadow: initial;}}
        .shadow-inherit {{box-shadow: inherit;}}
        .shadow-revert {{box-shadow: revert;}}
        .shadow-revert-layer {{box-shadow: revert-layer;}}
        """
        self.box_shadow_css_classes.append(box_shadow_default_css)

    def box_shadow_helpers(self):
        box_shadow_css = f"""
        .shadow {{box-shadow: 0px 0px {self.box_shadow_default_dimen}px 0px {self.default_color_light};}}
        .shadow-sm {{box-shadow: 0px 0px {self.box_shadow_default_dimen - 2}px 0px {self.default_color_light};}}
        .shadow-smr {{box-shadow: 0px 0px {self.box_shadow_default_dimen - 4}px 0px {self.default_color_light};}}
        .shadow-smt {{box-shadow: 0px 0px {self.box_shadow_default_dimen - 6}px 0px {self.default_color_light};}}
        .shadow-xs {{box-shadow: 0px 0px {self.box_shadow_default_dimen - 7}px 0px {self.default_color_light};}}
        
        .shadow2 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 2)}px 0px {self.default_color_light};}}
        .shadow2-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 2) - 2}px 0px {self.default_color_light};}}
        .shadow2-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 2) - 4}px 0px {self.default_color_light};}}
        .shadow2-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 2) - 6}px 0px {self.default_color_light};}}
        .shadow2-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 2) - 7}px 0px {self.default_color_light};}}
        
        .shadow3 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 3)}px 0px {self.default_color_light};}}
        .shadow3-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 3) - 2}px 0px {self.default_color_light};}}
        .shadow3-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 3) - 4}px 0px {self.default_color_light};}}
        .shadow3-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 3) - 6}px 0px {self.default_color_light};}}
        .shadow3-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 3) - 7}px 0px {self.default_color_light};}}
        
        .shadow4 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 4)}px 0px {self.default_color_light};}}
        .shadow4-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 4) - 2}px 0px {self.default_color_light};}}
        .shadow4-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 4) - 4}px 0px {self.default_color_light};}}
        .shadow4-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 4) - 6}px 0px {self.default_color_light};}}
        .shadow4-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 4) - 7}px 0px {self.default_color_light};}}
        
        .shadow5 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 5)}px 0px {self.default_color_light};}}
        .shadow5-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 5) - 2}px 0px {self.default_color_light};}}
        .shadow5-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 5) - 4}px 0px {self.default_color_light};}}
        .shadow5-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 5) - 6}px 0px {self.default_color_light};}}
        .shadow5-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 5) - 7}px 0px {self.default_color_light};}}

        .shadow6 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 6)}px 0px {self.default_color_light};}}
        .shadow6-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 6) - 2}px 0px {self.default_color_light};}}
        .shadow6-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 6) - 4}px 0px {self.default_color_light};}}
        .shadow6-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 6) - 6}px 0px {self.default_color_light};}}
        .shadow6-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 6) - 7}px 0px {self.default_color_light};}}

        .shadow7 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 7)}px 0px {self.default_color_light};}}
        .shadow7-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 7) - 2}px 0px {self.default_color_light};}}
        .shadow7-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 7) - 4}px 0px {self.default_color_light};}}
        .shadow7-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 7) - 6}px 0px {self.default_color_light};}}
        .shadow7-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 7) - 7}px 0px {self.default_color_light};}}

        .shadow8 {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 8)}px 0px {self.default_color_light};}}
        .shadow8-sm {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 8) - 2}px 0px {self.default_color_light};}}
        .shadow8-smr {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 8) - 4}px 0px {self.default_color_light};}}
        .shadow8-smt {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 8) - 6}px 0px {self.default_color_light};}}
        .shadow8-xs {{box-shadow: 0px 0px {(self.box_shadow_default_dimen * 8) - 7}px 0px {self.default_color_light};}}
        """
        self.box_shadow_css_classes.append(box_shadow_css)


class Opacity:
    """ Date: July 18, 2022. """

    def __init__(self) -> None:
        self.opacity_css_classes = list()
        self.opacity_defaults()
        self.opacity_helpers()

    @property
    def css_properties(self):
        return self.opacity_css_classes

    @property
    def css_template(self):
        """ Opacity css template
        :Date: August 9, 2022.
        """
        opacity_template = [".opacity- {opacity: [];}"]
        return opacity_template

    def opacity_defaults(self):
        """ :Date: September 4, 2022. """
        opacity_default_css = f"""
        .opacity-unset {{opacity: unset;}}
        .opacity-initial {{opacity: initial;}}
        .opacity-inherit {{opacity: inherit;}}
        .opacity-revert {{opacity: revert;}}
        .opacity-revert-layer {{opacity: revert-layer;}}
        """
        self.opacity_css_classes.append(opacity_default_css)

    def opacity_helpers(self):
        for i in range(0, 101, 1):
            opacity_css = f"""
            .opacity-{i} {{opacity: {i / 100};}}
            """
            self.opacity_css_classes.append(opacity_css)


class Object:
    """ :Date: July 18, 2022. """

    def __init__(self) -> None:
        self.object_css_classes = list()
        self.object_fit_css_helpers()
        self.object_position_css_helpers()

    @property
    def css_properties(self):
        return self.object_css_classes

    def object_fit_css_helpers(self):
        object_fit_css = f"""
        .object-fit-unset {{object-fit: unset;}}
        .object-fit-inherit {{object-fit: inherit;}}
        .object-fit-initial {{object-fit: initial;}}
        .object-fit-revert {{object-fit: revert;}}
        .object-fit-revert-layer {{object-fit: revert-layer;}}
        .object-contain {{object-fit: contain;}}
        .object-cover {{object-fit: cover;}}
        .object-fill {{object-fit: fill;}}
        .object-none {{object-fit: none;}}
        .object-scale-down {{object-fit: scale-down;}}
        """
        self.object_css_classes.append(object_fit_css)

    def object_position_css_helpers(self):
        object_position_css = f"""
        .object-pos-unset {{object-position: unset;}}
        .object-pos-inherit {{object-position: inherit;}}
        .object-pos-initial {{object-position: initial;}}
        .object-pos-revert {{object-position: revert;}}
        .object-pos-revert-layer {{object-position: revert-layer;}}
        .object-center {{object-position: center;}}
        .object-top {{object-position: top;}}
        .object-bottom {{object-position: bottom;}}
        .object-left {{object-position: left;}}
        .object-left-top {{object-position: left top;}}
        .object-left-bottom {{object-position: left bottom;}}
        .object-right {{object-position: right;}}
        .object-right-top {{object-position: right top;}}
        .object-right-bottom {{object-position: right bottom;}}
        """
        self.object_css_classes.append(object_position_css)


class OverScrolls:
    """ :Date: July 18, 2022. """

    def __init__(self) -> None:
        self.overscroll_css_classes = list()
        self.overscroll_defaults()
        self.overscroll_helpers()

    @property
    def css_properties(self):
        return self.overscroll_css_classes

    def overscroll_defaults(self):
        """ :Date: September 4, 2022. """
        overscroll_default_css = f"""
        .overscroll-unset {{overscroll-behavior: unset;}}
        .overscroll-initial {{overscroll-behavior: initial;}}
        .overscroll-inherit {{overscroll-behavior: inherit;}}
        .overscroll-revert {{overscroll-behavior: revert;}}
        .overscroll-revert-layer {{overscroll-behavior: revert-layer;}}
        """
        self.overscroll_css_classes.append(overscroll_default_css)

    def overscroll_helpers(self):
        overscroll_css = f"""
        .overscroll-none {{overscroll-behavior: none;}}
        .overscroll-auto {{overscroll-behavior: auto;}}
        .overscroll-contain {{overscroll-behavior: contain;}}
        .overscroll-x-none {{overscroll-behavior-x: none;}}
        .overscroll-x-auto {{overscroll-behavior-x: auto;}}
        .overscroll-x-contain {{overscroll-behavior-x: contain;}}
        .overscroll-y-none {{overscroll-behavior-y: none;}}
        .overscroll-y-auto {{overscroll-behavior-y: auto;}}
        .overscroll-y-contain {{overscroll-behavior-y: contain;}}
        """
        self.overscroll_css_classes.append(overscroll_css)


class Isolation:
    """ :Date: July 18, 2022. """

    def __init__(self) -> None:
        self.isolation_css_classes = list()
        self.isolation_defaults()
        self.isolation_css_helpers()

    @property
    def css_properties(self):
        return self.isolation_css_classes

    def isolation_defaults(self):
        """ :Date: September 4, 2022. """
        isolation_default_css = f"""
        .isolation-unset {{isolation: unset;}}
        .isolation-initial {{isolation: initial;}}
        .isolation-inherit {{isolation: inherit;}}
        .isolation-revert {{isolation: revert;}}
        .isolation-revert-layer {{isolation: revert-layer;}}
        """
        self.isolation_css_classes.append(isolation_default_css)

    def isolation_css_helpers(self):
        """ :Date: inherit; """
        isolation_css = f"""
        .isolation-auto {{isolation: auto;}}
        .isolate {{isolation: isolate;}}
        """
        self.isolation_css_classes.append(isolation_css)


class Resize:
    """ :Date: July 18, 2022. """

    def __init__(self) -> None:
        self.resize_css_classes = list()
        self.resize_defaults()
        self.resize_helpers()

    @property
    def css_properties(self):
        return self.resize_css_classes

    def resize_defaults(self):
        """ :Date: September 4, 2022. """
        resize_default_css = f"""
        .resize-unset {{resize: unset;}}
        .resize-initial {{resize: initial;}}
        .resize-inherit {{resize: inherit;}}
        .resize-revert {{resize: revert;}}
        .resize-revert-layer {{resize: revert-layer;}}
        """
        self.resize_css_classes.append(resize_default_css)

    def resize_helpers(self):
        resize_css = f"""
        .resize-none {{resize: none;}}
        .resize-x {{resize: x;}}
        .resize-y {{resize: y;}}
        .resize-both {{resize: both;}}
        """
        self.resize_css_classes.append(resize_css)


class PointerEvents:
    """ :Date: July 18, 2022. """

    def __init__(self) -> None:
        self.pointer_events_css_classes = list()
        self.pointer_events_helpers()

    @property
    def css_properties(self):
        return self.pointer_events_css_classes

    def pointer_events_helpers(self):
        pointer_events_css = f"""
            .pointer-events-none {{pointer-events: none;}}
            .pointer-events-auto {{pointer-events: auto;}}
            """
        self.pointer_events_css_classes.append(pointer_events_css)


class AccentColor:
    """ :Date: July 18, 2022. """
    def __init__(self) -> None:
        self.accent_color_css_classes = list()
        self.accent_color_default_helpers()

    @property
    def css_properties(self):
        return self.accent_color_css_classes

    @property
    def css_template(self):
        """ Template for Accent CSS Properties.
        :Date: August 9, 2022.
        """
        accent_template = [".accent- {accent-color: [];}"]
        return accent_template

    def accent_color_default_helpers(self):
        """ :Date: inherit """
        accent_color_css = f"""
        .accent-auto {{accent-color: auto;}}
        .accent-inherit {{accent-color: inherit;}}
        .accent-initial {{accent-color: initial;}}
        .accent-revert {{accent-color: revert;}}
        .accent-revert-layer {{accent-color: revert-layer;}}
        .accent-unset {{accent-color: unset;}}
        .accent-current-color {{accent-color: current-color;}}
        """
        self.accent_color_css_classes.append(accent_color_css)

    def accent_color_helpers(self):
        """ :Date: inherit """
        accent_color_css = f"""
        .accent- {{accent-color: }}
        """
        self.accent_color_css_classes.append(accent_color_css)


class BackFace:
    """ :Date: July 18, 2022. """
    def __init__(self) -> None:
        self.backface_css_classes = list()
        self.backface_helpers()

    @property
    def css_properties(self):
        return self.backface_css_classes

    def backface_helpers(self):
        backface_css = f"""
        .backface-unset {{backface-visibility: unset;}}
        .backface-inherit {{backface-visibility: inherit;}}
        .backface-initial {{backface-visibility: initial;}}
        .backface-revert {{backface-visibility: revert;}}
        .backface-revert-layer {{backface-visibility: revert-layer;}}
        .backface-visible {{backface-visibility: visible;}}
        .backface-hidden {{backface-visibility: hidden;}}
        """
        self.backface_css_classes.append(backface_css)


class BlockSize:
    """ :Date: July 18, 2022. """
    def __init__(self) -> None:
        self.block_size_css_classes = list()
        self.block_size_helpers()

    @property
    def css_properties(self):
        return self.block_size_css_classes

    def block_size_helpers(self):
        """ :Date: inherit """
        block_size_css = f"""
        .block-size-auto {{block-size: auto;}}
        .block-size-unset {{block-size: unset;}}
        .block-size-inherit {{block-size: inherit;}}
        .block-size-initial {{block-size: initial;}}
        .block-size-revert {{block-size: revert;}}
        .block-size-revert-layer {{block-size: revert-layer;}}
        .block-size-max {{block-size: max-content;}}
        .block-size-min {{block-size: min-content;}}
        """
        self.block_size_css_classes.append(block_size_css)


class Separator(Root):
    """ :Date: July 19, 2022. """
    def __init__(self) -> None:
        super(Separator, self).__init__()
        self.separator_css_classes = list()
        self.separator_style()
        self.separator_width()
        self.separator_color()

    @property
    def css_properties(self):
        return self.separator_css_classes

    @property
    def css_template(self):
        """ Template for Separator CSS Properties.
        :Date: August 9, 2022.
        """
        separator_template = [".sep- {border(): [];}"]
        return separator_template

    def separator_style(self):
        """ :Date: inherit """
        separator_css = f"""
        .sep-unset {{border-style: unset;}}
        .sep-initial {{border-style: initial;}}
        .sep-inherit {{border-style: inherit;}}
        .sep-revert {{border-style: revert;}}
        .sep-none {{border-style: none;}}
        .sep-hidden {{border-style: hidden;}}
        .sep-dotted {{border-style: dotted;}}
        .sep-dashed {{border-style: dashed;}}
        .sep-solid {{border-style: solid;}}
        .sep-double {{border-style: double;}}
        .sep-groove {{border-style: groove;}}
        .sep-ridge {{border-style: ridge;}}
        .sep-inset {{border-style: inset;}}
        .sep-outset {{border-style: outset;}}
        """
        self.separator_css_classes.append(separator_css)

    def separator_width(self):
        """ :Date: inherit """
        separator_width_list = list()
        for i in ['', '-top', '-right', '-bottom', '-left']:
            for j in CSSGenerator.float_range(0.05, 1.0, 0.05):
                separator_width_css = f"""
                .sep{i[:2] if len(i) > 0 else ""}{j*100} {{border{i}-width: {j};}}
                """
                separator_width_list.append(separator_width_css)
        self.separator_css_classes.extend(separator_width_list)

    def separator_color(self):
        """ :Date: July 30, 2022. """
        separator_color_list = list()
        for i in ['', '-top', '-right', '-bottom', '-left']:
            for k, v in self.color_dictionary().items():
                separator_color = f"""
                .sep{i[:2] if len(i) > 0 else ""}-{k} {{border{i}-color: {v};}}
                """
                separator_color_list.append(separator_color)
        self.separator_css_classes.extend(separator_color_list)

    def separator_margin(self):
        separator_margin_list = list()
        for i in ['', '-top', '-right', '-bottom', '-left']:
            for j in range(1, 13, 1):
                sep_margin_css = f"""
                .sep{i[:2] if len(i) > 0 else ""}-{j} {{margin{i}: {self.default_dimension_px_value * j}px; margin{i}: {self.default_dimension_px_value * j}px;}}
                .sep{i[:2] if len(i) > 0 else ""}-{j}-sm {{margin{i}: {(self.default_dimension_px_value * j) - 2}px; margin{i}: {(self.default_dimension_px_value * j) - 2}px;}}
                .sep{i[:2] if len(i) > 0 else ""}-{j}-smr {{margin{i}: {(self.default_dimension_px_value * j) - 4}px; margin{i}: {(self.default_dimension_px_value * j) - 4}px;}}
                .sep{i[:2] if len(i) > 0 else ""}-{j}-smt {{margin{i}: {(self.default_dimension_px_value * j) - 6}px; margin{i}: {(self.default_dimension_px_value * j) - 6}px;}}
                .sep{i[:2] if len(i) > 0 else ""}-{j}-xs {{margin{i}: {(self.default_dimension_px_value * j) - 7}px; margin{i}: {(self.default_dimension_px_value * j) - 7}px;}}
                """
                separator_margin_list.append(sep_margin_css)
        self.separator_css_classes.extend(separator_margin_list)


class BackDrops:
    """ :Date: July 24, 2022. """
    def __init__(self) -> None:
        self.backdrop_css_classes = list()
        self.backdrop_blur()
        self.backdrop_brightness()
        self.backdrop_contrast()
        self.backdrop_grayscale()
        self.backdrop_hue_rotate()
        self.backdrop_invert()
        self.backdrop_opacity()
        self.backdrop_saturate()
        self.backdrop_sepia()

    @property
    def css_properties(self):
        return self.backdrop_css_classes

    def backdrop_blur(self):
        """:Date: July 24, 2022."""
        for i in range(0, 81, 1):
            backdrop_blur_css = f"""
            .backdrop-blur {{backdrop-filter: blur({i}px);}}
            """
            self.backdrop_css_classes.append(backdrop_blur_css)

    def backdrop_brightness(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_brightness_css = f"""
            .backdrop-brightness{i} {{backdrop-filter: brightness({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_brightness_css)

    def backdrop_contrast(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_contrast_css = f"""
            .backdrop-contrast{i} {{backdrop-filter: contrast({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_contrast_css)

    def backdrop_grayscale(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_grayscale_css = f"""
            .backdrop-grayscale{i} {{backdrop-filter: grayscale({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_grayscale_css)

    def backdrop_hue_rotate(self):
        """:Date: July 24, 2022."""
        for i in range(0, 360 + 15, 15):
            backdrop_hue_rotate_css = f"""
            .backdrop-hue-rotate{i} {{backdrop-filter: hue-rotate({i}deg);}}
            """
            self.backdrop_css_classes.append(backdrop_hue_rotate_css)

    def backdrop_invert(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_invert_css = f"""
            .backdrop-invert{i} {{backdrop-filter: invert({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_invert_css)

    def backdrop_opacity(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_opacity_css = f"""
            .backdrop-opacity{i} {{backdrop-filter: opacity({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_opacity_css)

    def backdrop_saturate(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_saturate_css = f"""
            .backdrop-saturate{i} {{backdrop-filter: saturate({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_saturate_css)

    def backdrop_sepia(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            backdrop_sepia_css = f"""
            .backdrop-sepia{i} {{backdrop-filter: sepia({i}%);}}
            """
            self.backdrop_css_classes.append(backdrop_sepia_css)


class Filters:
    """ :Date: July 24, 2022. """
    def __init__(self) -> None:
        self.filter_css_classes = list()
        self.filter_blur()
        self.filter_brightness()
        self.filter_contrast()
        self.filter_grayscale()
        self.filter_hue_rotate()
        self.filter_hue_rotate()
        self.filter_invert()
        self.filter_opacity()
        self.filter_saturate()
        self.filter_sepia()

    @property
    def css_properties(self):
        return self.filter_css_classes

    def filter_blur(self):
        """ :Date: inherit; """
        for i in range(0, 81, 1):
            filter_blur_css = f"""
            .blur{i} {{filter: blur({i}px);}}
            """
            self.filter_css_classes.append(filter_blur_css)

    def filter_brightness(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            brightness_css = f"""
            .brightness{i} {{filter: brightness({i}%);}}
            """
            self.filter_css_classes.append(brightness_css)

    def filter_contrast(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            contrast_css = f"""
            .contrast{i} {{filter: contrast({i}%);}}
            """
            self.filter_css_classes.append(contrast_css)

    def filter_grayscale(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            grayscale_css = f"""
            .grayscale{i} {{filter: grayscale({i}%);}}
            """
            self.filter_css_classes.append(grayscale_css)

    def filter_hue_rotate(self):
        """:Date: July 24, 2022."""
        for i in range(0, 180 + 15, 15):
            hue_rotate_css = f"""
            .hue-rotate{i} {{filter: hue-rotate({i}deg);}}
            """
            self.filter_css_classes.append(hue_rotate_css)

    def filter_invert(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            invert_css = f"""
            .invert{i} {{filter: invert({i}%);}}
            """
            self.filter_css_classes.append(invert_css)

    def filter_opacity(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            opacity_css = f"""
            .opacity{i} {{filter: opacity({i/100});}}
            """
            self.filter_css_classes.append(opacity_css)

    def filter_saturate(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            saturate_css = f"""
            .saturate{i} {{filter: saturate({i}%);}}
            """
            self.filter_css_classes.append(saturate_css)

    def filter_sepia(self):
        """:Date: July 24, 2022."""
        for i in range(0, 101, 1):
            sepia_css = f"""
            .sepia{i} {{filter: sepia({i}%);}}
            """
            self.filter_css_classes.append(sepia_css)


class ScrollBehaviors:
    """ :Date: July 24, 2022. """
    def __init__(self) -> None:
        self.scroll_behavior_css_classes = list()
        self.scroll_behavior_helpers()

    @property
    def css_properties(self):
        return self.scroll_behavior_css_classes

    def scroll_behavior_helpers(self):
        """ :Date: inherit; """
        scroll_behavior_css = f"""
        .scroll-auto {{scroll-behavior: auto;}}
        .scroll-smooth {{scroll-behavior: smooth;}}
        """
        self.scroll_behavior_css_classes.append(scroll_behavior_css)


class ScrollSnaps:
    """ :Date: July 24, 2022. """
    def __init__(self) -> None:
        self.scroll_snap_css_classes = list()
        self.scroll_snap_strictness = "mandatory"
        self.scroll_snap_align()
        self.scroll_snap_type()
        self.scroll_snap_stop()

    @property
    def css_properties(self):
        return self.scroll_snap_css_classes

    @property
    def css_template(self):
        """ :Date: September 4, 2022. """
        scroll_snap_dimensions_variants = list()
        scroll_snap = [
            ".scroll-pad- {scroll-padding: [];}"
            ".pct\:scroll-pad- {scroll-padding: [];}"
            ".em\:scroll-pad- {scroll-padding: [];}"
        ]
        for _ in CSSGenerator().dimension_type_list:
            scroll_snap_dimensions_variants.append(f".{_}\:scroll-pad- {{scroll-padding: [];}}")

        return [*scroll_snap, *scroll_snap_dimensions_variants]

    def scroll_snap_align(self):
        """ :Date: inherit; """
        scroll_snap_align_css = f"""
        .snap-align-none {{scroll-snap-align: none;}}
        .snap-start {{scroll-snap-align: start;}}
        .snap-end {{scroll-snap-align: end;}}
        .snap-center {{scroll-snap-align: center;}}
        """
        self.scroll_snap_css_classes.append(scroll_snap_align_css)

    def scroll_snap_type(self):
        """ :Date: inherit; """
        scroll_snap_type_css = f"""
        .snap-type-none {{scroll-snap-type: none;}}
        .snap-x-mandatory {{scroll-snap-type: x mandatory;}}
        .snap-x-proximity {{scroll-snap-type: x proximity;}}
        .snap-y-mandatory {{scroll-snap-type: y mandatory;}}
        .snap-y-proximity {{scroll-snap-type: y proximity;}}
        .snap-both {{scroll-snap-type: both var(--{self.scroll_snap_strictness});}}
        """
        self.scroll_snap_css_classes.append(scroll_snap_type_css)

    def scroll_snap_stop(self):
        """ :Date: inherit; """
        scroll_snap_stop_css = f"""
        .snap-normal {{scroll-snap-stop: normal;}}
        .snap-always {{scroll-snap-stop: always;}}
        """
        self.scroll_snap_css_classes.append(scroll_snap_stop_css)


class Transforms:
    """
    Eye.css Transform function.
    :Date: August 14, 2022.
    """
    def __init__(self) -> None:
        self.transform_css_classes = list()
        self.skew()
        self.rotate()
        self.transform_style()
        self.transform_box()

    @property
    def css_properties(self):
        return self.transform_css_classes

    @property
    def css_template(self):
        """
        :Date: inherit
        """
        translate_template = list()
        for _ in CSSGenerator().dimension_type_list:
            translate_template.append(f".{_}\:translate- {{transform: translate([]);}}")
            translate_template.append(f".{_}\:translate-x- {{transform: translateX([]);}}")
            translate_template.append(f".{_}\:translate-y- {{transform: translateY([]);}}")
            translate_template.append(f".{_}\:translate-z- {{transform: translateZ([]);}}")
        perspective_template = [f".{_}\:perspective- {{transform: perspective([]);}}" for _ in CSSGenerator().dimension_type_list]
        transform_template = [
            ".perspective- {transform: perspective([]);}",
            ".translate- {transform: translate([]);}",
            ".translate-x- {transform: translateX([]);}",
            ".translate-y- {transform: translateY([]);}",
            ".translate-z- {transform: translateZ([]);}",
            ".scale- {transform: scale([]);}",
            ".scale-x- {transform: scaleX([]);}",
            ".scale-y- {transform: scaleY([]);}",
            ".scale-z- {transform: scaleZ([]);}",
            ".skew- {transform: skew([]deg);}",
            ".skew-x- {transform: skewX([]deg);}",
            ".skew-y- {transform: skewY([]deg);}",
            ".rotate- {transform: rotate([]deg);}",
            ".rotate-x- {transform: rotateX([]deg);}",
            ".rotate-y- {transform: rotateY([]deg);}",
            ".rotate-z- {transform: rotateZ([]deg);}"
        ]
        return [*transform_template, *translate_template, *perspective_template]

    def transform_style(self):
        """
        Transform style classes.
        :Date: August 16, 2022.
        """
        transform_style = f"""
        .transform-flat {{transform-style: flat;}}
        .transform-3d {{transform-style: preserve-3d;}}
        """
        self.transform_css_classes.append(transform_style)

    def transform_box(self):
        """
        Transform box classes.
        :Date: August 16, 2022.
        """
        transform_box = f"""
        .transform-box-inherit {{transform-box: inherit;}}
        .transform-box-initial {{transform-box: initial;}}
        .transform-box-revert {{transform-box: revert;}}
        .transform-box-revert-layer {{transform-box: revert-layer;}}
        .transform-box-unset {{transform-box: unset;}}
        .transform-box-content {{transform-box: content-box;}}
        .transform-box-border {{transform-box: border-box;}}
        .transform-box-fill {{transform-box: fill-box;}}
        .transform-box-stroke {{transform-box: stroke-box;}}
        .transform-box-view {{transform-box: view-box;}}
        """
        self.transform_css_classes.append(transform_box)

    def translate(self):
        """
        Transform translate classes.
        :Date: August 15, 2022.
        """
        pass

    def skew(self):
        """
        Transform skew classes.
        :Date: August 15, 2022.
        """
        for i in range(0, 361, 1):
            skew_css = f"""
            .skew-{i} {{transform: skew({i}deg);}}
            .skew-x-{i} {{transform: skewX({i}deg);}}
            .skew-y-{i} {{transform: skewY({i}deg);}}
            """
            self.transform_css_classes.append(skew_css)

    def rotate(self):
        """
        Transform rotate classes.
        :Date: August 15, 2022.
        """
        for i in range(0, 361, 1):
            rotate_css = f"""
            .rotate-{i} {{transform: rotate({i}deg);}}
            .rotate-x-{i} {{transform: rotateX({i}deg);}}
            .rotate-y-{i} {{transform: rotateY({i}deg);}}
            .rotate-z-{i} {{transform: rotateZ({i}deg);}}
            """
            self.transform_css_classes.append(rotate_css)


class Transitions:
    """
    Eye.css Transitions function.
    :Date: August 16, 2022.
    """
    def __init__(self) -> None:
        self.transition_css_classes = list()


class List:
    """
    List Style classes.
    :Date: August 31, 2022.
    """
    def __init__(self):
        self.list_style_css_classes = list()
        self.list_style_type()
        self.list_style_position()

    @property
    def css_properties(self):
        return self.list_style_css_classes

    @property
    def css_template(self):
        """
        :Date: inherit
        """
        return

    def list_style_type(self):
        """ :Date: inherit """
        list_style_type_css = f"""
        .list-disc {{list-style-type: disc;}}
        .list-circle {{list-style-type: circle;}}
        .list-square {{list-style-type: square;}}
        .list-decimal {{list-style-type: decimal;}}
        .list-dlz {{list-style-type: decimal-leading-zero;}}
        .list-georgian {{list-style-type: georgian;}}
        .list-trad-chinese-informal {{list-style-type: trad-chinese-informal;}}
        .list-kannada {{list-style-type: kannada;}}
        .list-upper-roman {{list-style-type: upper-roman;}}
        .list-lower-roman {{list-style-type: lower-roman;}}
        .list-type-none {{list-style-type: none;}}
        .list-type-inherit {{list-style-type: inherit;}}
        .list-type-unset {{list-style-type: unset;}}
        .list-type-initial {{list-style-type: initial;}}
        .list-type-revert {{list-style-type: revert;}}
        .list-type-revert-layer {{list-style-type: revert-layer;}}
        """
        self.list_style_css_classes.append(list_style_type_css)

    def list_style_position(self):
        """ :Date: inherit """
        list_style_position_css = f"""
        .list-inside {{list-style-position: inside;}}
        .list-outside {{list-style-position: outside;}}
        .list-position-inherit {{list-style-position: inherit;}}
        .list-position-initial {{list-style-position: initial;}}
        .list-position-revert {{list-style-position: revert;}}
        .list-position-revert-layer {{list-style-position: revert-layer;}}
        .list-position-unset {{list-style-position: unset;}}
        """
        self.list_style_css_classes.append(list_style_position_css)


class Visibility:
    """
    Visibility classes.
    Date: January 29, 2023.
    """
    def __init__(self):
        self.visibility_style_css_classes = list()
        self.visibility_helpers()

    @property
    def css_properties(self):
        return self.visibility_style_css_classes

    def visibility_helpers(self):
        pointer_events_css = f"""
                .visible-inherit {{visibility: inherit;}}
                .visible-auto {{visibility: auto;}}
                .visible-unset {{visibility: unset;}}
                .visible-revert {{visibility: revert;}}
                .visible-revert-layer {{visibility: revert-layer;}}
                .visible {{visibility: visible;}}
                .invisible {{visibility: hidden;}}
                """
        self.visibility_style_css_classes.append(pointer_events_css)
