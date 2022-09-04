# MAYOWA OBISESAN
# EYE.CSS WATCHER FILE.
# JULY 2, 2022.

# Get a file to watch.
# get all the class or className from the file being watched.
# The class and className represents all the defined inline styles available within a html, jsx or tsx page.

# Have imports here.
import glob
import os
import re
import time

import yaml
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from eye_css_generator import CSSGenerator


class EyeWriter:
    """ Eye.css Writer Class.
    Re-written or if you wish Re-Optimized.
    The previously implemented format is available as "class EyeWriterOld" in old watcher.py file.
    :class created: August 9, 2022.
    :class tested complete: August 9, 2022.
    :Date:  August 9, 2022.
    :Time:  22:22 (pm)
    :Next:  Implement dynamic eye.css markup classes that can take dynamic dimensions (width, height), degrees, colors,
            font-sizes, etc.
    """
    def __init__(self) -> None:
        self.eye_css_name = "eye_gen.css"
        # self.watched_css_file_name = r"C:\Users\Mayowa Obisesan\Desktop\Blessed\nine\frontend\src\watched_eye.css"
        # self.watched_css_file_name = rf"{os.getcwd()}\{EyeWatcher.EYE_CSS_OUTPUT}"
        self.watched_css_file_name = EyeWatcher.EYE_CSS_OUTPUT
        # self.file_to_watch = r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\index.html"
        # self.file_to_watch = r"C:\Users\Mayowa Obisesan\Desktop\Blessed\nine\frontend\public\index.html"
        self.files_to_watch = Handler.FILES_TO_WATCH
        self.watched_base_classes_list: list = list()
        self.watched_pseudo_classes_list: list = list()
        self.watched_pseudo_elements_list: list = list()
        self.watched_media_query_list: list = list()
        self.watched_base_classes_dynamic_list: list = list()
        self.watched_pseudo_classes_dynamic_list: list = list()
        self.watched_pseudo_elements_dynamic_list: list = list()
        self.watched_media_query_dynamic_list: list = list()

    @classmethod
    def flatten_list(cls, list_to_flatten: list) -> list:
        """ A Function to flatten multidimensional list. """
        flat_list = list()
        for _ in list_to_flatten:
            if isinstance(_, list):
                cls.flatten_list(_)
            flat_list.extend(_)
        return flat_list

    @staticmethod
    def get_css_dict_from_css_key(eye_css_str, css_key):
        eye_css_to_dict = CSSGenerator().convert_css_to_dict(eye_css_str)

        css_dict = {css_key: f"{{{eye_css_to_dict[css_key]}}}"}
        return css_dict

    def collect_markup_css_classes_from_files(self):
        markup_css_classes_list = []
        for each_watched_file in self.files_to_watch:
            with open(each_watched_file, "r", encoding="utf-8") as opened_file:
                file_string = opened_file.read()
                opened_file.close()
                attr_class_list = EyeMarkupParser().get_attr_class_list_from_markup(EyeMarkupParser().clean_markup(file_string))
                markup_css_classes_list.extend(attr_class_list)
        return self.categorize_markup_css_classes_list(markup_css_classes_list)

    def collect_watched_files_css_classes(self):
        watched_css_class_list = list()
        for each_watched_file in self.files_to_watch:
            with open(each_watched_file, "r", encoding="utf-8") as opened_file:
                file_string = opened_file.read()
                opened_file.close()
                css_class_list = EyeMarkupParser().attr_class_list_from_file(EyeMarkupParser().clean_markup(file_string))
                watched_css_class_list.extend(css_class_list)
        return self.categorize_markup_css_classes_list(watched_css_class_list)

    def categorize_markup_css_classes_list(self, css_classes_list: list):
        eye_css_dictionary = CSSGenerator().css_dictionary()
        flat_css_list = self.flatten_list(css_classes_list)
        for each_css_class in flat_css_list:
            if EyeMarkupParser().is_base_css_class(each_css_class):
                reconstructed_base_css_class = f"{EyeMarkupParser().reconstruct_markup_base_css_class(each_css_class)}"
                if f".{reconstructed_base_css_class}" in eye_css_dictionary.keys():
                    self.watched_base_classes_list.append(reconstructed_base_css_class)
                else:
                    self.watched_base_classes_dynamic_list.append(reconstructed_base_css_class)
            elif EyeMarkupParser().is_pseudo_classes_class(each_css_class):
                reconstructed_base_css_class = f""".{EyeMarkupParser().reconstruct_markup_base_css_class(
                    EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_css_class)
                )}"""
                if reconstructed_base_css_class in eye_css_dictionary.keys():
                    self.watched_pseudo_classes_list.append(each_css_class)
                else:
                    self.watched_pseudo_classes_dynamic_list.append(each_css_class)
            elif EyeMarkupParser().is_pseudo_elements_class(each_css_class):
                reconstructed_base_css_class = f""".{EyeMarkupParser().reconstruct_markup_base_css_class(
                    EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_css_class)
                )}"""
                if reconstructed_base_css_class in eye_css_dictionary.keys():
                    self.watched_pseudo_elements_list.append(each_css_class)
                else:
                    self.watched_pseudo_elements_dynamic_list.append(each_css_class)
            elif EyeMarkupParser().is_media_query_class(each_css_class):
                reconstructed_base_css_class = f""".{EyeMarkupParser().reconstruct_markup_base_css_class(
                    EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_css_class)
                )}"""
                if reconstructed_base_css_class in eye_css_dictionary.keys():
                    self.watched_media_query_list.append(each_css_class)
                else:
                    self.watched_media_query_dynamic_list.append(each_css_class)
        pass

    def watched_css_dictionary(self):
        """
        Collect the watched css classes from files and Categorize them, so it can be used by the below code block
        """
        self.collect_watched_files_css_classes()
        watched_css: dict = dict()
        eye_css_dictionary = CSSGenerator().css_dictionary()

        base_classes_watched_css = {f".{k}": eye_css_dictionary[f'.{k}'] for k in self.watched_base_classes_list}

        pseudo_classes_watched_css = {
            f".{EyeMarkupParser().reconstruct_markup_pseudo_classes_css_class(each_pseudo_class)}":
                f"{eye_css_dictionary[f'.{EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_pseudo_class)}']}"
            for each_pseudo_class in self.watched_pseudo_classes_list
        }

        pseudo_elements_watched_css = {
            f".{EyeMarkupParser().reconstruct_markup_pseudo_elements_css_class(each_pseudo_class)}":
                f"{eye_css_dictionary[f'.{EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_pseudo_class)}']}"
            for each_pseudo_class in self.watched_pseudo_elements_list
        }

        media_query_watched_css = {
            EyeMarkupParser().reconstruct_markup_media_query_css_class(each_pseudo_class):
                f"{eye_css_dictionary[f'.{EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_pseudo_class)}']}"
            for each_pseudo_class in self.watched_media_query_list
        }
        media_query_dict = {}
        for mqs in CSSGenerator().default_media_query_dict.keys():
            media_query_dict[CSSGenerator().default_media_query_dict[mqs]] = {}
            for each_pseudo_class in self.watched_media_query_list:
                if each_pseudo_class.split(":")[0] == mqs:
                    media_query_dict[CSSGenerator().default_media_query_dict[mqs]].update({
                        EyeMarkupParser().reconstruct_markup_media_query_css_class(each_pseudo_class):
                            f"{eye_css_dictionary[f'.{EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_pseudo_class)}']}"
                    })

        watched_css.update(base_classes_watched_css)
        watched_css.update(pseudo_classes_watched_css)
        watched_css.update(pseudo_elements_watched_css)

        watched_css.update(self.process_dynamic_css_classes(self.watched_base_classes_dynamic_list))
        watched_css.update(self.process_dynamic_css_classes(self.watched_pseudo_classes_dynamic_list))

        for k, v in self.process_dynamic_css_classes(self.watched_media_query_dynamic_list).items():
            media_query_dict[CSSGenerator().default_media_query_dict[k.split(":", 1)[0].strip(".").strip("\\")]].update({k: v})

        watched_css.update(CSSGenerator().convert_dict_to_css(media_query_dict, as_dict_str=True))

        return watched_css

    def create_watched_css(self):
        # watched_css_file_name: str = self.watched_css_file_name
        with open(self.watched_css_file_name, "w") as opened_file:
            opened_file.writelines(CSSGenerator().eye_init())
            for _ in self.watched_css_dictionary().items():
                opened_file.writelines(_)
            opened_file.close()

    def process_dynamic_css_classes(self, dynamic_css_class_list: list):
        """ A Function to process the dynamic css classes.
        :Date: August 10, 2022.
        """
        dynamic_watched_css_dict = dict()
        # parsable_dynamic_eye_css_classes = sorted(set(dynamic_css_class_list).intersection(set(CSSGenerator().css_templates_dictionary())))
        eye_template_dictionary = CSSGenerator().css_templates_dictionary()

        for each_dynamic_css_class in dynamic_css_class_list:
            each_dynamic_base_css_class = EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_dynamic_css_class)
            dynamic_css_class_key = each_dynamic_base_css_class.rsplit("-", 1)[0]
            if f".{dynamic_css_class_key}-" in eye_template_dictionary.keys():
                # if len(each_dynamic_base_css_class.split("-")) > 2 skip.
                dynamic_css_dict_value = eye_template_dictionary.get(f".{dynamic_css_class_key}-")
                # Implementing classes having a negative value. without performing multiple checks in "if"-statements.
                # Thank you Holy Spirit.
                if EyeMarkupParser().ends_with_color(each_dynamic_base_css_class) and CSSGenerator().is_css_color_property(each_dynamic_base_css_class):
                    replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-color").replace("[]", f"#{each_dynamic_base_css_class.rsplit('-', 1)[-1]}")
                    dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                elif EyeMarkupParser().ends_with_digit(each_dynamic_base_css_class) or EyeMarkupParser().ends_with_float(each_dynamic_base_css_class):
                    if not CSSGenerator().is_dimensionless_css_property(dynamic_css_class_key):
                        if dynamic_css_class_key.startswith("pct"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}%")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("em"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}em")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("rem"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}rem")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("pt"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}pt")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("pc"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}pc")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("vw"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}vw")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("vh"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}vh")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                        else:
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}px")
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                    elif CSSGenerator().is_dimensionless_css_property(dynamic_css_class_key):
                        print("DIMENSIONLESS PROPERTY DETECTED.")
                        if "".join(re.findall(r'(\b^z$\b|opacity\b|scale\b)', each_dynamic_css_class)) == "z":
                            if CSSGenerator().is_zindex_dimension_valid(each_dynamic_base_css_class.rsplit('-', 1)[-1]):
                                replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}")
                                dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                            else:
                                print(f"{dynamic_css_class_key} - {each_dynamic_base_css_class.rsplit('-', 1)[-1]} is not a valid eye.css z_index value")
                        if "".join(re.findall(r'(\b^z$\b|opacity\b|scale\b)', each_dynamic_css_class)) == "scale":
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}")
                            escaped_reconstructed_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace(".", "\.")
                            dynamic_watched_css_dict.update({f".{escaped_reconstructed_css_class}": replaced_dynamic_css_dict_value})
                            print(f"TRANSFORM: SCALE FOUND: {EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}: {replaced_dynamic_css_dict_value}")
                        if "".join(re.findall(r'(\b^z$\b|opacity\b|scale\b)', each_dynamic_css_class)) == "opacity":
                            print(f"Parsed an opacity class: {dynamic_css_class_key}")
            # elif each_dynamic_css_class.startswith("shadow\:"):   # using the dynamic_css_class_key below because of pseudo nested classes.
            elif dynamic_css_class_key.startswith("shadow\:"):
                """
                Algorithm for performing dynamic shadow parsing.
                if shadow_css_class endswith shadow\:
                    1.  split shadow_css_class into its style & style_definition
                    2.  split style_definition into its variants. 
                        i.e., style_definition.split("|") if shadow classes have more than one shadow dynamically defined.
                        L>  style_definition_variant = style_definition.split("|")
                    3.  reconstruct each style definition variants and comma join them 
                        i.e., ".".join(reconstructed_style_definition_variants)
                        L>  shadow_variant_list = []
                            for each_variant in style_definition_variant:
                                split each_variant into it's configuration. i.e., each_variant.split('-')
                                L>  # each_variant_split = each_variant.split('-')
                                    each_variant_split = re.sub(r"\b(-)", " ", each_variant).split(" ")
                                    if each_variant_split[0] == "inset":
                                        shadow_inset = True
                                        each_variant_split.remove("inset")
                                    else:
                                        shadow_inset = False
                                    if CSSGenerator().is_color_code(each_variant_split[-1]):
                                        shadow_c = f"#{each_variant_split[-1]}"
                                        each_variant_split.remove(each_variant_split[-1])
                                    elif CSSGenerator().is_valid_color_name(each_variant_split[-1]):
                                        shadow_c = each_variant_split[-1]
                                        each_variant_split.remove(shadow_c)
                                    else:
                                        shadow_c = ""
                                    # The values within each_variant_split is only dimension or length values
                                    # clone each_variant_split into dimensioned_each_variant_split containing only shadow definitions having dimensions or length values
                                    dimensioned_each_variant_split = each_variant_split
                                    if len(each_variant_split) == 2:
                                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], 0, 0
                                    elif len(each_variant_split) == 3:
                                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], each_variant_split[2], 0
                                    elif len(each_variant_split) == 4:
                                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], each_variant_split[2], each_variant_split[3]
                                    shadow_variants_list.append(f"{'inset ' if shadow_inset else ''}{shadow_h} {shadow_v} {shadow_s} {shadow_w} {shadow_c}")
                            ",".join(shadow_variant_list)
                                
                """
                shadow_style_split = each_dynamic_css_class.split(":")
                shadow_style = shadow_style_split[0]
                shadow_style_definition = shadow_style_split[-1]

                shadow_style_definition_variant = shadow_style_definition.split("|")
                shadow_variant_list = []
                shadow_h, shadow_v, shadow_s, shadow_w, shadow_c = "0", "0", "0", "0", "currentColor"
                for each_variant in shadow_style_definition_variant:
                    each_variant_split = re.sub(r"\b(-)", " ", each_variant).split(" ")
                    if each_variant_split[0] == "inset":
                        shadow_inset = True
                        each_variant_split.remove("inset")
                    else:
                        shadow_inset = False
                    if CSSGenerator().is_color_code(each_variant_split[-1]):
                        shadow_c = f"#{each_variant_split[-1]}"
                        each_variant_split.remove(each_variant_split[-1])
                    elif CSSGenerator().is_valid_color_name(each_variant_split[-1]):
                        shadow_c = each_variant_split[-1]
                        each_variant_split.remove(shadow_c)

                    if len(each_variant_split) == 2:
                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], 0, 0
                    elif len(each_variant_split) == 3:
                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], each_variant_split[2], 0
                    elif len(each_variant_split) == 4:
                        shadow_h, shadow_v, shadow_s, shadow_w = each_variant_split[0], each_variant_split[1], each_variant_split[2], each_variant_split[3]
                    shadow_variant_list.append(
                        f"{'inset ' if shadow_inset else ''}{shadow_h} {shadow_v} {shadow_s} {shadow_w} {shadow_c}")
                shadow_style_value = ", ".join(shadow_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{box-shadow: {shadow_style_value};}}"})
            elif dynamic_css_class_key.startswith("drop-shadow\:"):
                shadow_style_split = each_dynamic_css_class.split(":")
                shadow_style = shadow_style_split[0]
                shadow_style_definition = shadow_style_split[-1]

                shadow_style_definition_variant = shadow_style_definition.split("|")
                shadow_variant_list = []
                shadow_h, shadow_v, shadow_s, shadow_c = "0", "0", "0", "currentColor"
                for each_variant in shadow_style_definition_variant:
                    each_variant_split = re.sub(r"\b(-)", " ", each_variant).split(" ")
                    if CSSGenerator().is_color_code(each_variant_split[-1]):
                        shadow_c = f"#{each_variant_split[-1]}"
                        each_variant_split.remove(each_variant_split[-1])
                    elif CSSGenerator().is_valid_color_name(each_variant_split[-1]):
                        shadow_c = each_variant_split[-1]
                        each_variant_split.remove(shadow_c)

                    if len(each_variant_split) == 2:
                        shadow_h, shadow_v, shadow_s = each_variant_split[0], each_variant_split[1], 0
                    elif len(each_variant_split) == 3:
                        shadow_h, shadow_v, shadow_s = each_variant_split[0], each_variant_split[1], each_variant_split[2]
                    shadow_variant_list.append(f"{shadow_h} {shadow_v} {shadow_s} {shadow_c}")
                shadow_style_value = ", ".join(shadow_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{filter: drop-shadow({shadow_style_value});}}"})
            elif dynamic_css_class_key.startswith("gradient\:"):
                gradient_style_split = each_dynamic_css_class.split(":")
                gradient_style = gradient_style_split[0]
                gradient_style_definition = gradient_style_split[-1]

                gradient_style_definition_variant = gradient_style_definition.split("|")
                gradient_variant_list = []
                for each_variant in gradient_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ").replace("-", ",")
                    gradient_variant_list.append(f"""linear-gradient({replaced_each_variant})""")
                gradient_style_value = ", ".join(gradient_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{background: {gradient_style_value.replace('pct', '%')};}}"})
            elif dynamic_css_class_key.startswith("radial-gradient\:"):
                gradient_style_split = each_dynamic_css_class.split(":")
                gradient_style = gradient_style_split[0]
                gradient_style_definition = gradient_style_split[-1]

                gradient_style_definition_variant = gradient_style_definition.split("|")
                gradient_variant_list = []
                for each_variant in gradient_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ").replace("-", ",")
                    # replaced_each_variant = re.sub(r"\b(-)", ",", each_variant.replace("_", " "))
                    gradient_variant_list.append(f"""radial-gradient({replaced_each_variant})""")
                gradient_style_value = ", ".join(gradient_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{background: {gradient_style_value.replace('pct', '%')};}}"})
            elif dynamic_css_class_key.startswith("conic-gradient\:"):
                gradient_style_split = each_dynamic_css_class.split(":")
                gradient_style = gradient_style_split[0]
                gradient_style_definition = gradient_style_split[-1]

                gradient_style_definition_variant = gradient_style_definition.split("|")
                gradient_variant_list = []
                for each_variant in gradient_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ").replace("-", ",")
                    gradient_variant_list.append(f"""conic-gradient({replaced_each_variant})""")
                gradient_style_value = ", ".join(gradient_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{background: {gradient_style_value.replace('pct', '%')};}}"})
            elif dynamic_css_class_key.startswith("repeating-linear-gradient\:"):
                self.process_dynamic_gradients(css_class=each_dynamic_css_class, dynamic_watched_css_dict=dynamic_watched_css_dict, gradient_name="repeating-linear-gradient")
            elif dynamic_css_class_key.startswith("repeating-radial-gradient\:"):
                self.process_dynamic_gradients(css_class=each_dynamic_css_class, dynamic_watched_css_dict=dynamic_watched_css_dict, gradient_name="repeating-radial-gradient")
            elif dynamic_css_class_key.startswith("repeating-conic-gradient\:"):
                self.process_dynamic_gradients(css_class=each_dynamic_css_class, dynamic_watched_css_dict=dynamic_watched_css_dict, gradient_name="repeating-conic-gradient")
            elif dynamic_css_class_key.startswith("transform\:"):
                transform_style_split = each_dynamic_css_class.split(":")
                transform_style = transform_style_split[0]
                transform_style_definition = transform_style_split[-1]

                transform_style_definition_variant = transform_style_definition.split("|")
                transform_variant_list = []
                for each_variant in transform_style_definition_variant:
                    # replaced_each_variant = each_variant.replace("_", " ").replace("-", "")
                    transform_variant_name = each_variant.rsplit("-", 1)[0]
                    transform_variant_dimension = each_variant.rsplit("-", 1)[-1]
                    transform_variant_name_type = transform_variant_name.split("-")[0]
                    transform_variant_name_plane = transform_variant_name.split("-")[-1].upper()
                    transform_variant_list.append(f"{transform_variant_name_type}{transform_variant_name_plane}({transform_variant_dimension})")
                transform_style_value = " ".join(transform_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{transform: {transform_style_value.replace('pct', '%')};}}"})
            elif dynamic_css_class_key.startswith("transform-origin\:"):
                transform_origin_style_split = each_dynamic_css_class.split(":")
                transform_origin_style = transform_origin_style_split[0]
                transform_origin_style_definition = transform_origin_style_split[-1]

                transform_origin_style_definition_variant = transform_origin_style_definition.split("|")
                transform_origin_variant_list = []
                for each_variant in transform_origin_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ")
                    transform_origin_variant_list.append(replaced_each_variant)
                transform_origin_style_value = " ".join(transform_origin_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{transform-origin: {transform_origin_style_value};}}"})
            elif dynamic_css_class_key.startswith("transition\:"):
                transition_style_split = each_dynamic_css_class.split(":")
                transition_style = transition_style_split[0]
                transition_style_definition = transition_style_split[-1]

                transition_style_definition_variant = transition_style_definition.split("|")
                transition_variant_list = []
                for each_variant in transition_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ")
                    transition_variant_list.append(replaced_each_variant)
                transition_style_value = ", ".join(transition_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{transition: {transition_style_value};}}"})
            elif dynamic_css_class_key.startswith("animation\:"):
                animation_style_split = each_dynamic_css_class.split(":")
                animation_style = animation_style_split[0]
                animation_style_definition = animation_style_split[-1]

                animation_style_definition_variant = animation_style_definition.split("|")
                animation_variant_list = []
                for each_variant in animation_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ")
                    animation_variant_list.append(replaced_each_variant)
                animation_style_value = ", ".join(animation_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{animation: {animation_style_value};}}"})

        return dynamic_watched_css_dict

    @staticmethod
    def process_dynamic_gradients(css_class, dynamic_watched_css_dict, gradient_name="linear"):
        """
        Helper Function to process dynamic gradients
        :Date: August 14, 2022.
        """
        print(f"Dynamic {gradient_name} Gradient class found.")

        gradient_style_split = css_class.split(":")
        gradient_style = gradient_style_split[0]
        gradient_style_definition = gradient_style_split[-1]

        gradient_style_definition_variant = gradient_style_definition.split("|")
        gradient_variant_list = []
        for each_variant in gradient_style_definition_variant:
            replaced_each_variant = each_variant.replace("_", " ").replace("--", "TMP").replace("-", ",").replace("TMP", "-")
            gradient_variant_list.append(f"""{gradient_name.replace("-gradient", "")}-gradient({replaced_each_variant})""")
        gradient_style_value = ", ".join(gradient_variant_list)
        reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%","\%").replace("(", "\(").replace(")", "\)")
        dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{background: {gradient_style_value.replace('pct', '%')};}}"})


class EyeWatcher:
    eye_css_config_data = dict()

    import argparse
    parser = argparse.ArgumentParser(description="Eye CSS - A Dynamic CSS Utility-first library.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="help", help="A Dynamic CSS Utility-first library. Just run this file with a configuration file, or define where to save the css for you. Also gives you a CSS cheatsheet for your projects, no need to memorize the css definitions.")
    group.add_argument("-q", "--quiet", action="help", help="A Dynamic CSS Utility-first library.")

    parser.add_argument("file", nargs="?", default="", type=str, help="Eye.css config file")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as eye_config_file:
            eye_css_config_data = yaml.safe_load(eye_config_file)
            eye_config_file.close()

    if eye_css_config_data.get("eye") is not None:
        # we do not make provision for multiple directories to be watched because the watcher library being used
        # does not support multiple directories being watched. - August 25, 2022.
        # There are alternatives to the watcher library but not using the alternatives yet. - September 4, 2022.
        DIRECTORY_TO_WATCH = eye_css_config_data.get("eye").get("input_directory", "")
        if not os.path.isabs(DIRECTORY_TO_WATCH):
            watched_directory_path = os.path.dirname(args.file)
            DIRECTORY_TO_WATCH = os.path.realpath(os.path.join(watched_directory_path, DIRECTORY_TO_WATCH))
        EXTENSIONS_TO_WATCH = eye_css_config_data.get("eye").get("input_extensions", "").split(",")

        OUTPUT_PATH = eye_css_config_data.get("eye").get("output_path", "") or os.path.dirname(args.file)
        OUTPUT_NAME = eye_css_config_data.get("eye").get("output_name", "")
        EYE_CSS_OUTPUT = os.path.join(OUTPUT_PATH, OUTPUT_NAME)

        EXACT_FILE = eye_css_config_data.get("eye").get("input_exact_files", "")

        EXCLUDE_DIRECTORY = eye_css_config_data.get("eye").get("exclude_directory", "")
        EXCLUDE_FILES = eye_css_config_data.get("eye").get("exclude_files", "")
    else:
        DIRECTORY_TO_WATCH = eye_css_config_data.get("input_directory", "")
        EXTENSIONS_TO_WATCH = eye_css_config_data.get("input_extensions", "")
        EYE_CSS_OUTPUT = eye_css_config_data.get("output_name", "")

    assert len(eye_css_config_data.keys()) > 0, "Error processing eye_css config File. Check the file once more."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
            # while self.observer.is_alive():
            #     self.observer.join(1)
        except RuntimeError as err:
            self.observer.stop()
            print("Error")
        self.observer.join()


class Handler(FileSystemEventHandler):
    FILES_TO_WATCH = []

    def __init__(self):
        # directory_to_watch = "C:/Users/Mayowa Obisesan/Desktop/Blessed/nine/frontend/src"
        # file_to_watch_extensions = ("*.js", "*.jsx", "*.html")
        directory_to_watch = EyeWatcher.DIRECTORY_TO_WATCH
        file_to_watch_extensions = EyeWatcher.EXTENSIONS_TO_WATCH
        exact_file_to_watch = EyeWatcher.EXACT_FILE
        if exact_file_to_watch != "":
            self.FILES_TO_WATCH.append(exact_file_to_watch) if os.path.isabs(exact_file_to_watch) else self.FILES_TO_WATCH.append(os.path.join(directory_to_watch, exact_file_to_watch))
        elif exact_file_to_watch == "":
            for ext in file_to_watch_extensions:
                self.FILES_TO_WATCH.extend(glob.glob(f"{directory_to_watch}/**/{ext}", recursive=True))
        # self.files_to_watch = [r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\index.html"]
        # self.files_to_watch = [r"C:\Users\Mayowa Obisesan\Desktop\Blessed\nine\frontend\public\index.html"]
        # self.files_to_watch = [r"C:\Users\Mayowa Obisesan\Desktop\Blessed\nine\frontend\src\**\*.js"]
        print(f"Hello, I am EYE. \nI am WATCHING: {','.join(self.FILES_TO_WATCH)}")

    def on_any_event(self, event):
        # DIRECTORY_TO_IGNORE = [".git"]
        # FILES_TO_EXCLUDE = [".gitignore"]
        DIRECTORY_TO_IGNORE = EyeWatcher.EXCLUDE_DIRECTORY
        FILES_TO_IGNORE = EyeWatcher.EXCLUDE_FILES

        if event.src_path not in FILES_TO_IGNORE:
            if event.is_directory:
                return None

            elif event.event_type == 'created':
                # Take any action here when a file is first created.
                print("Received created event - %s." % event.src_path)

            elif event.event_type == 'modified':
                # Take any action here when a file is modified.
                print("Received modified event - %s." % event.src_path)

                if event.src_path in self.FILES_TO_WATCH:
                    EyeWriter().create_watched_css()

    # def on_modified(self, event):
    #     if event.src_path in self.files_to_watch:
    #         EyeWriter().parse_eye_css()


class EyeMarkupParser:
    """
    Class to Parse the markup containing the css classes.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def clean_markup(markup_string):
        """
        :Date: inherit
        Clean the markup by:
        1.  Collapse: Removing all newline characters so regex can be performed on the minified returned string
        2.  Substringing: Removing commented markups
        3.  Minification: Removing spaces and tabs.
        """
        collapse_markup_string = markup_string.replace("\n", "")
        # substring_markup_string = re.sub(r"""((\{/\*)([\w*-<:|/\d*]\s*)(\*/}))""", "", collapse_markup_string)
        substring_markup_string = re.sub(r"""\{/\*[<:-|/]*\s*\w*\d*[<:-|/]*\*/}""", "", collapse_markup_string)
        # substring_markup_string = re.sub(r"""(\{/\*.+<.+\*/})""", "", collapse_markup_string)
        # substring_markup_string = re.sub(r"""(\{/\*.+<.+\*/}|<!--.+<.+-->)""", "", collapse_markup_string)
        minify_markup_string = re.sub(r""">\s+<""", "><", substring_markup_string)
        cleaned_markup_string = minify_markup_string
        # print(f"CLEANED MARKUP STRING: {cleaned_markup_string}")
        return cleaned_markup_string

    def get_attr_class_data_from_markup(self, markup_string: str) -> list:
        """
        Gets all the class="..." in the markup string.
        :Date: inherit
        """
        # attr_list = re.match(r"""class(Name)?=(["']).*(['"])""", markup_string)
        # attr_list = re.findall(r"""((class|className)=["|'].*['|"])""", markup_string)
        # attr_list = re.findall(r"""<.+(class[Name]+=["|'].*['|"])""", markup_string)
        cleaned_markup_string = self.clean_markup(markup_string)
        attr_class_data = re.findall(r"""((class\b|className)="([\w*-:|/]\s*)+")""", cleaned_markup_string)
        # attr_class_script_data = re.findall(r"""(|((\bclassList\.add\b)"([\w*-:|/]\s*)+"))""", cleaned_markup_string)

        # print(f"ATTR CLASS LIST: {attr_class_data}")
        return attr_class_data

    def get_attr_class_list_from_markup(self, markup_string: str) -> list:
        # attr_classes = [
        #     re.sub(r"((class\b|className)=)", "", each_attr[0]).replace("'", "").replace('"', '').split(" ")
        #     for each_attr in self.get_attr_class_data_from_markup(markup_string)
        # ]
        attr_classes = [
            each_attr[0].split("=")[-1].replace("'", "").replace('"', '').split(" ")
            for each_attr in self.get_attr_class_data_from_markup(markup_string)
        ]
        # print(attr_classes)
        return attr_classes

    def get_attr_class_data_from_file(self, file_str: str) -> list:
        """
        Function to parse all watched files and get the class attrs from the file
        :param file_str: The file content to parse as a string.
        :return: A list of class attributes from markup files and from scripts.
        :Date: August 13, 2022.
        """
        # js_css_classes_data = re.findall("""(classList.add)\(['"](([\w+-:|]+\s*)+)['"]\)""",
        #                                  "button.classList.add('bg-green pct:w-100')")
        # markups_css_classes_data = re.findall(r"""(class\b|className\b)=\"(([\w*-:|/]\s*)+)\"""",
        #                                       """<section class="working-css-parts check-validity
        #                                       is-it-working"></section><div name="color"
        #                                       className="bg-green relative d-block"></div>""")

        js_css_classes_data = re.findall("""(classList.add)\(['"](([\w+-:|#()%]+\s*)+)['"]\)""", file_str, re.MULTILINE)
        markups_css_classes_data = re.findall(r"""(class\b|className\b)=\"\s*(([\w*-:|#()%/]\s*)+)\"""", file_str)

        # print(js_css_classes_data)
        # print(markups_css_classes_data)
        watched_files_css_classes_data = [*markups_css_classes_data, *js_css_classes_data]
        return watched_files_css_classes_data

    def attr_class_list_from_file(self, file_str: str) -> list:
        """
        Function to get the css classes from the attr_class_data as an argument
        :param file_str: The parsed attr class data from the file
        :return: A list of css classes.
        :Date: August 13, 2022.
        """
        css_classes_list = [
            each_css_class[1].split(" ")
            for each_css_class in self.get_attr_class_data_from_file(file_str)
        ]
        return css_classes_list

    def base_classes_list_from_attr_class_list(self, attr_class_list: list) -> list:
        """ Gets base_css_class from attr_class_list
        :Date: August 5, 2022.
        """
        base_class_list = [attr_class_list.remove(_) for _ in attr_class_list if _.__contains__(":")]
        return base_class_list

    def pseudo_classes_list_from_attr_class_list(self, attr_class_list: list) -> list:
        """ Gets pseudo_classes_css_class from attr_class_list
        :Date: August 5, 2022.
        """
        base_class_list = [attr_class_list.remove(_) for _ in attr_class_list if _.__contains__(":")]
        return base_class_list

    def pseudo_elements_list_from_attr_class_list(self, attr_class_list: list) -> list:
        """ Gets pseudo_elements_css_class from attr_class_list
        :Date: August 5, 2022.
        """
        base_class_list = [attr_class_list.remove(_) for _ in attr_class_list if _.__contains__(":")]
        return base_class_list

    def is_base_css_class(self, css_class_str) -> bool:
        """ A Function to check if a css class str is a base css class
        :param css_class_str: the css class string to check.
        :return: True or False
        :Date: August 7, 2022.
        """
        # res_match = re.match(r"((\bneg:\b|\bpct:\b)+[\w-]+)", css_class_str)
        # re.findall(r"\b[^0-9][\w-]+\s*", "radius mg-blue pad-y3 4gft")
        # re.findall(r"\bpct:\b[^0-9][\w-]+\s*", "radius mg-blue pad-y3 4gft")
        # re.findall(r"\bneg:\b[^0-9][\w-]+\s*", "radius mg-blue pad-y3 4gft")
        # re.findall(r"\bneg:pct:\b[^0-9][\w-]+\s*", "radius mg-blue pad-y3 4gft")
        # return res_match is None
        pseudo_classes = CSSGenerator().default_pseudo_class_list
        pseudo_elements = CSSGenerator().default_pseudo_element_list
        media_queries = CSSGenerator().default_media_query_list
        if css_class_str.startswith((*pseudo_classes, *pseudo_elements, *media_queries)):
            return False
        return True

    @staticmethod
    def is_pseudo_classes_class(css_class_str) -> bool:
        """ A Function to check if a css class str is a pseudo class css class
        :param css_class_str: the css class string to check.
        :return: bool.
        :Date: August 7, 2022.
        """
        pseudo_classes = CSSGenerator().default_pseudo_class_list
        if css_class_str.startswith(pseudo_classes):
            return True
        return False

    @staticmethod
    def is_pseudo_elements_class(css_class_str) -> bool:
        """ A Function to check if a css class str is a pseudo-element css class.
        :param css_class_str: the css class string to check.
        :return: bool.
        :Date: August 7, 2022.
        """
        pseudo_elements = CSSGenerator().default_pseudo_element_list
        if css_class_str.startswith(pseudo_elements):
            return True
        return False

    @staticmethod
    def is_media_query_class(css_class_str) -> bool:
        """ A Function to check if a css class str is a media query css class
        :param css_class_str: the css class string to check.
        :return: bool.
        :Date: August 7, 2022.
        """
        media_query = CSSGenerator().default_media_query_dict.keys()
        if css_class_str.startswith(tuple(media_query)):
            return True
        return False

    def get_base_class_from_pseudo_selector_str(self, css_class_str: str) -> str:
        """ Get the base_css_class from a pseudo_css_string
        :param css_class_str: the css class string to get base_class from
        :return: the base_class or css_class_str
        :rtype: str
        :Date: August 5, 2022.
        """
        # Is there a pseudo class or a pseudo-element?
        # base_class_list = re.findall(r"\w*:*([neg|pct:]+[\w+-]+)", css_class_str)
        # base_class_list = re.findall(r"\w*:*((\bneg:\b|\bpct:\b)*[\w+-]+)", css_class_str)
        # base_class_list = re.findall(r"((\bneg:\b|\bpct:\b)*\b[a-z]+[\w-]+)\s*", css_class_str)
        # return "".join(base_class_list)
        # if css_class_str.startswith(("pct:", "neg:", "pct\:", "neg\:")):
        # return css_class_str.rpartition(":")[-1]
        # print(f'{css_class_str.partition(":")[-1]}:::{css_class_str.partition(":")}')
        if css_class_str.__contains__(":"):
            if css_class_str.startswith(CSSGenerator().first_level_base_class_pseudo):
                return css_class_str
            natural_base_css_class = css_class_str.rsplit(":", 1)[-1]
            pseudo_css_class = css_class_str.rsplit(":", 1)[0]
            pseudo_base_css_class_list = list()
            for _ in pseudo_css_class.split(":"):
                if _ in CSSGenerator().first_level_base_class_pseudo:
                    pseudo_base_css_class_list.append(f"{_}:")
            base_css_class = "".join([*pseudo_base_css_class_list, *natural_base_css_class])
            return self.reconstruct_markup_base_css_class(base_css_class)
        return css_class_str

    def get_pseudo_element_from_pseudo_css_str(self, css_class_str: str) -> str:
        """ Get the pseudo_element from a pseudo_css_string
        :param css_class_str: the css class string to get pseudo_class from.
        :return: the pseudo_class or the css_class_str
        :rtype: str
        :Date: August 5, 2022.
        """
        matched_pseudo_element_list = re.findall(r"(\w+:)", css_class_str)
        return "".join(matched_pseudo_element_list) if "".join(matched_pseudo_element_list) in CSSGenerator().default_pseudo_element_list else ""

    def get_pseudo_class_from_pseudo_css_str(self, css_class_str: str) -> str:
        """ Get the pseudo_class from a pseudo_css_string.
        :Date: August 5, 2022.
        """
        assert not css_class_str.startswith(("pct", "neg")), "CSS String is not a valid pseudo class."

        default_pseudo_class_list = ("hover", "focus", "focus-within", "focus-visible", "active", "visited", "target",
                                     "first-child", "last-child", "only-child", "nth-child(odd)", "nth-child(even)",
                                     "first-of-type", "last-of-type", "only-of-type", "empty", "disabled", "checked",
                                     "indeterminate", "default", "required", "valid", "invalid", "in-range",
                                     "out-of-range", "placeholder-shown", "autofill", "read-only")
        matched_pseudo_class_list = re.findall(r"(\w+):", css_class_str)
        # print(f"MATCHED PSEUDO CLASS LIST: {matched_pseudo_class_list}")
        # pseudo_class = set(default_pseudo_class_list).intersection(set(matched_pseudo_class_list))
        # return "".join(pseudo_class)
        return "".join(matched_pseudo_class_list) if "".join(matched_pseudo_class_list) in default_pseudo_class_list else ""

    @classmethod
    def categorize_eye_css_class_name(cls, eye_css_class_name: str):
        """
        Split and categorize eye.css class names as css_class_key and css_class_value
        e.g., "radius-16" => ("radius-", "16") & scroll-padding-120 => ("scroll-padding-", "120")
        :return: Tuple of eye_css_class_key and eye_css_class_value
        :Date: inherit;
        """
        return eye_css_class_name.rsplit("-", 1)

    @classmethod
    def digit_extractor(cls, eye_css_class_name: str):
        """
        Extracts digits from the end of class names.
        e.g., mg-bl-25 will return ("mg-bl-", "25")
        :return: The Digit which ends a valid eye.css class name.
        :Date: July 25, 2022.
        """
        extracted_digit_list = re.findall(r"[a-z]*(\d+)", eye_css_class_name)
        return eye_css_class_name.partition(extracted_digit_list[0] if len(extracted_digit_list) > 0 else " ")

    def is_split_eye_css_class_valid(self, eye_css_class_name: str) -> bool:
        """
        Checks if an eye class_name declaration is valid.
        Performs check from the eye.css "css-dictionary"
        :params eye_css_class_name: The eye.css class name to validate.
        :return: True or False
        :Date: July 25, 2022.
        """
        css_class_name, css_digit, after_css_digit = self.digit_extractor(eye_css_class_name)
        return True if re.search(rf"{css_class_name}*", ",".join(CSSGenerator().css_dictionary().keys())) is not None else False

    @staticmethod
    def ends_with_digit(eye_css_class_name: str) -> bool:
        """
        Performs a check to know if an eye_css_class_name ends with digit
        :param eye_css_class_name: The eye.css class name to validate.
        :return: True or False
        :Date: July 25, 2022.
        """
        return eye_css_class_name.split("-")[-1].isdigit()

    @staticmethod
    def ends_with_color(eye_css_class_name: str) -> bool:
        """
        Performs a check to know if an eye_css_class_name ends with a color code
        :param eye_css_class_name: The eye.css class name to validate.
        :return: True or False
        :Date: August 10, 2022.
        """
        return CSSGenerator().is_color_code(eye_css_class_name.split("-")[-1])

    @staticmethod
    def ends_with_float(eye_css_class_name: str) -> bool:
        """
        Performs a check to know if an eye_css_class_name ends with float
        :Date: August 15, 2022
        :param eye_css_class_name: The eye.css class name to validate.
        :return: True or False
        """
        return True if len(re.findall(r"\d+\.\d+", eye_css_class_name)) > 0 else False

    def reconstruct_css_class(self, css_class: str) -> str:
        """
        Reconstructs css_class by escaping those characters that needs to be escaped
        :param css_class: The css_class to reconstruct
        :return: reconstructed(escaped) css class.
        :Date: August 14, 2022.
        """
        if self.is_base_css_class(css_class):
            return self.reconstruct_markup_base_css_class(css_class)
        elif self.is_pseudo_classes_class(css_class):
            return self.reconstruct_markup_pseudo_classes_css_class(css_class)
        elif self.is_pseudo_elements_class(css_class):
            return self.reconstruct_markup_pseudo_elements_css_class(css_class)
        elif self.is_media_query_class(css_class):
            return self.reconstruct_markup_media_query_css_class(css_class)

    @staticmethod
    def reconstruct_markup_base_css_class(css_class: str) -> str:
        """ A Function to reconstruct eye.css classes from markup file.
        e.g., pct:w-48 ==> pct\:w-48 {...}
        How: ??
        1.  Replace all ":" with "\:"
        :param css_class: the base-css-class to reconstruct
        :return: the reconstructed base css class
        :Date: August 5, 2022.
        """
        return css_class.replace("\:", ":").replace(":", "\:")

    @staticmethod
    def reconstruct_markup_pseudo_classes_css_class(css_class: str) -> str:
        """ A Function to reconstruct eye.css pseudo-classes from markup file.
        e.g., .hover:pct:w-48 ==> .hover\:pct\:w-48:hover {...}
        .sm:focus:bg-light ==> @media (max-width) {.focus\:bg-light:focus {...}}
        How: ??
        1.  Replace all ":" with "\:"
        2.  Add pseudo classes to end of the css class. e.g., .hover:bg-lighter => .hover\:bg-lighter:hover {...}
        :param css_class: the pseudo-css-class to reconstruct
        :return: the reconstructed pseudo_css_class
        :Date: August 5, 2022.
        """
        # Get the pseudo_classes from the markup css_classes and perform substitution and addition.
        replaced_css = css_class.replace(":", "\:")
        pseudo_class = css_class.split(":", 1)[0]
        return f"{replaced_css}:{pseudo_class}"

    def reconstruct_markup_pseudo_elements_css_class(self, css_class: str) -> str:
        """ A Function to reconstruct eye.css pseudo-elements classes from markup file.
        e.g., .placeholder:font-bold ==> .placeholder\:font-bold::placeholder {...}
        .sm:placeholder:bg-light ==> @media (max-width) {.placeholder\:bg-light:placeholder {...}}
        How: ??
        1.  Replace all ":" with "\:"
        2.  Add pseudo-elements to end of the css class. e.g., .hover:bg-lighter => .hover\:bg-lighter:hover {...}
        :param css_class: the pseudo-elements-css-classes to reconstruct
        :return: the reconstructed pseudo-elements-css-classes
        :Date: August 5, 2022.
        """
        # Get the pseudo_classes from the markup css_classes and perform substitution and addition.
        replaced_css = css_class.replace(":", "\:")
        pseudo_class = self.get_pseudo_element_from_pseudo_css_str(css_class)
        return f"{replaced_css}::{pseudo_class}"

    def reconstruct_markup_media_query_css_class(self, css_class: str):
        """ A Function to reconstruct eye.css media-query css class.
        How: ??
        1.  Get the "css_class" argument,
        2.  create media_query string and add "1." to it
        :param css_class: the media-query-css-class to reconstruct
        :return: the reconstructed media-query-css-class
        :Date: August 5, 2022.
        """
        partitioned_css_class: tuple = css_class.partition(":")
        media_type: str = partitioned_css_class[0]
        after_media_query_css_str: str = partitioned_css_class[-1]
        reconstructed_after_media_query_str: str = ""

        if self.is_base_css_class(after_media_query_css_str):
            reconstructed_after_media_query_str = f".{media_type}\:{self.reconstruct_markup_base_css_class(after_media_query_css_str)}"
        elif self.is_pseudo_classes_class(after_media_query_css_str):
            reconstructed_after_media_query_str = f".{media_type}\:{self.reconstruct_markup_pseudo_classes_css_class(after_media_query_css_str)}"
        elif self.is_pseudo_elements_class(after_media_query_css_str):
            reconstructed_after_media_query_str = f".{media_type}\:{self.reconstruct_markup_pseudo_elements_css_class(after_media_query_css_str)}"
        return reconstructed_after_media_query_str

    def base_class_list_from_markup_list(self, markup_css_list):
        return [_[0] for _ in re.findall(r"((\bneg:\b|\bpct:\b)*\b[a-z]+[\w-]+)\s*",
                                         "radius mg-blue pad-y3 4gft pct:w-12 neg:pct:h-4 relative pad-y2-sm")]


if __name__ == '__main__':
    w = EyeWatcher()
    w.run()
