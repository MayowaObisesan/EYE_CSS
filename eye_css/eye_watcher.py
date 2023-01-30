# MAYOWA OBISESAN
# EYE.CSS WATCHER FILE.
# JULY 2, 2022.

# Get a file to watch.
# get all the class or className from the file being watched.
# The class and className represents all the defined inline styles available within a html, js(x) or ts(x) file.

# Have imports here.
import glob
import logging
import os
import re
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from eye_css.__main__ import Eye
from eye_css.eye_css_generator import CSSGenerator

# eye_template_dictionary = CSSGenerator().css_templates_dictionary()


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
        self.watched_css_file_name = Eye.EYE_CSS_OUTPUT
        self.files_to_watch = Handler.FILES_TO_WATCH
        self.watched_base_classes_list: list = list()
        self.watched_pseudo_elements_list: list = list()
        self.watched_pseudo_group_list: list = list()
        self.watched_pseudo_classes_list: list = list()
        self.watched_media_query_list: list = list()
        self.watched_base_classes_dynamic_list: list = list()
        self.watched_pseudo_elements_dynamic_list: list = list()
        self.watched_pseudo_classes_dynamic_list: list = list()
        self.watched_pseudo_group_dynamic_list: list = list()
        self.watched_media_query_dynamic_list: list = list()

    @classmethod
    def flatten_list(cls, list_to_flatten: list) -> list:
        """ A Function to flatten multidimensional list. """
        flat_list = list()
        for _ in list_to_flatten:
            if isinstance(_, list):
                cls.flatten_list(_)
            flat_list.extend(_) if isinstance(_, list) else flat_list.append(_)
        return flat_list

    @staticmethod
    def get_css_dict_from_css_key(eye_css_str, css_key):
        eye_css_to_dict = CSSGenerator().convert_css_to_dict(eye_css_str)

        css_dict = {css_key: f"{{{eye_css_to_dict[css_key]}}}"}
        return css_dict

    def generate_base_css_classes(self, eye_css_list: list):
        """
        Generates the css counterpart of inputted eye_css classes
        eye_css_list: list
        date: January 29, 2023.
        return: A dictionary of eye_css and the generated counterpart.
        example: [text-center, color-pink] => {
            .text-center: {
                text-align: center;
            }
            .color-pink: {
                color: pink;
            }
        }
        """
        eye_css_dictionary = CSSGenerator().css_dictionary()
        base_css_dict = dict()
        for each_eye_css in eye_css_list:
            # In case of classes such as sibling-*:bg-blue, clean each of the css from the eye_css_list
            if each_eye_css.__contains__(":"):
                grouper_key, grouper_value = each_eye_css.split(":")[0], each_eye_css.split(":")[-1]
                if grouper_key not in CSSGenerator().first_level_base_class_pseudo:
                    each_eye_css = grouper_value
            if eye_css_dictionary.get(f".{each_eye_css}"):
                # print(f"GENERATE BASE CSS FROM EYE CSS DICTIONARY: {each_eye_css}")
                base_css_dict.update({f".{each_eye_css}": eye_css_dictionary[f".{each_eye_css}"]})
            else:
                base_css_dict.update(self.process_dynamic_base_css_classes([each_eye_css]))
        # print(f"GENERATE PASSED LIST: {eye_css_list}")
        # print(f"BASE CSS DICT: {base_css_dict}", end="\n\n")
        return base_css_dict
        # base_css_classes = {f".{k}": eye_css_dictionary[f'.{k}'] for k in eye_css_list}
        # return base_css_classes

    def group_generated_base_css_classes(self, css_dict: dict):
        _css_list = list()
        for _ in css_dict.values():
            _css_list.extend(_.replace("{", "").replace("}", "").strip(" ").split(";"))
        _css_list.remove("") if "" in _css_list else None
        return ";".join(_css_list)

    # def collect_markup_css_classes_from_files(self):
    #     markup_css_classes_list = []
    #     for each_watched_file in self.files_to_watch:
    #         with open(each_watched_file, "r", encoding="utf-8") as opened_file:
    #             file_string = opened_file.read()
    #             opened_file.close()
    #             attr_class_list = EyeMarkupParser().get_attr_class_list_from_markup(EyeMarkupParser().clean_markup(file_string))
    #             markup_css_classes_list.extend(attr_class_list)
    #     return self.categorize_markup_css_classes_list(markup_css_classes_list)

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
        # print(css_classes_list)
        eye_css_dictionary = CSSGenerator().css_dictionary()
        flat_css_list = self.flatten_list(css_classes_list)
        # print(flat_css_list)
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
                    # print(f"PSEUDO CLASS DYNAMIC LIST: {self.watched_pseudo_classes_dynamic_list}")
            elif EyeMarkupParser().is_pseudo_elements_class(each_css_class):
                reconstructed_base_css_class = f""".{EyeMarkupParser().reconstruct_markup_base_css_class(
                    EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_css_class)
                )}"""
                if reconstructed_base_css_class in eye_css_dictionary.keys():
                    self.watched_pseudo_elements_list.append(each_css_class)
                else:
                    self.watched_pseudo_elements_dynamic_list.append(each_css_class)
            elif EyeMarkupParser().is_pseudo_group_class(each_css_class):
                # print(f"PSEUDO GROUP CLASS: {each_css_class}")
                reconstructed_base_css_class = f""".{EyeMarkupParser().reconstruct_markup_base_css_class(
                    EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_css_class)
                )}"""
                if reconstructed_base_css_class in eye_css_dictionary.keys():
                    self.watched_pseudo_group_list.append(each_css_class)
                else:
                    self.watched_pseudo_group_dynamic_list.append(each_css_class)
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

        pseudo_group_watched_css = {
            f".{EyeMarkupParser().reconstruct_markup_pseudo_group_css_class(each_pseudo_class)}":
                f"{eye_css_dictionary[f'.{EyeMarkupParser().get_base_class_from_pseudo_selector_str(each_pseudo_class)}']}"
            for each_pseudo_class in self.watched_pseudo_group_list
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
        watched_css.update(pseudo_elements_watched_css)
        watched_css.update(pseudo_classes_watched_css)
        watched_css.update(pseudo_group_watched_css)

        watched_css.update(self.process_dynamic_base_css_classes(self.watched_base_classes_dynamic_list))
        watched_css.update(self.process_dynamic_pseudo_class_css_classes(self.watched_pseudo_classes_dynamic_list))
        watched_css.update(self.process_dynamic_pseudo_selector_css_classes(self.watched_pseudo_elements_dynamic_list))
        watched_css.update(self.process_dynamic_pseudo_group_css_classes(self.watched_pseudo_group_dynamic_list))
        # watched_css.update(self.process_dynamic_pseudo_selector_css_classes(self.watched_pseudo_classes_dynamic_list))

        for k, v in self.process_dynamic_base_css_classes(self.watched_media_query_dynamic_list).items():
            media_query_dict[CSSGenerator().default_media_query_dict[k.split(":", 1)[0].strip(".").strip("\\").removeprefix('.')]].update({k: v})

        watched_css.update(CSSGenerator().convert_dict_to_css(media_query_dict, as_dict_str=True))

        return watched_css

    def create_watched_css(self):
        # watched_css_file_name: str = self.watched_css_file_name
        with open(self.watched_css_file_name, "w") as opened_file:
            opened_file.writelines(CSSGenerator().eye_init())
            for _ in self.watched_css_dictionary().items():
                opened_file.writelines(_)
            opened_file.close()

    def process_dynamic_base_css_classes(self, dynamic_css_class_list: list):
        """ A Function to process the dynamic css classes.
        :Date: August 10, 2022.
        """
        dynamic_watched_css_dict = dict()
        # parsable_dynamic_eye_css_classes = sorted(set(dynamic_css_class_list).intersection(set(CSSGenerator().css_templates_dictionary())))
        eye_template_dictionary = CSSGenerator().css_templates_dictionary()

        for each_dynamic_css_class in dynamic_css_class_list:
            # For dynamic Base CSS classes
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
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("em"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}em")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("rem"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}rem")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("pt"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}pt")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("pc"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}pc")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("vw"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}vw")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("vh"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-height").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}vh")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        elif dynamic_css_class_key.startswith("px"):
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}px")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                        else:
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("()", "-width").replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}px")
                            # Added the .strip('.") to the reconstruct_css_class because without it, it generates a
                            # double ".." css class for media queries. - January 7, 2022.
                            dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).strip('.')}": replaced_dynamic_css_dict_value})
                    elif CSSGenerator().is_dimensionless_css_property(dynamic_css_class_key):
                        if "".join(re.findall(r'(\bz\b|opacity\b|scale\b)', each_dynamic_css_class)) == "z":
                            if CSSGenerator().is_zindex_dimension_valid(each_dynamic_base_css_class.rsplit('-', 1)[-1]):
                                replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}")
                                dynamic_watched_css_dict.update({f".{EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class)}": replaced_dynamic_css_dict_value})
                            else:
                                logging.info(f"{dynamic_css_class_key} - {each_dynamic_base_css_class.rsplit('-', 1)[-1]} is not a valid eye.css z_index value")
                        if "".join(re.findall(r'(\bz\b|opacity\b|scale\b)', each_dynamic_css_class)) == "scale":
                            replaced_dynamic_css_dict_value = dynamic_css_dict_value.replace("[]", f"{each_dynamic_base_css_class.rsplit('-', 1)[-1]}")
                            escaped_reconstructed_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace(".", "\.")
                            dynamic_watched_css_dict.update({f".{escaped_reconstructed_css_class}": replaced_dynamic_css_dict_value})
                        if "".join(re.findall(r'(\bz\b|opacity\b|scale\b)', each_dynamic_css_class)) == "opacity":
                            pass
            # using the dynamic_css_class_key below because of pseudo nested classes.
            # elif each_dynamic_css_class.startswith("shadow\:"):
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
            elif dynamic_css_class_key.startswith("border\:"):
                border_style_split = each_dynamic_css_class.split(":")
                _, border_style_definition = border_style_split[0], border_style_split[-1]

                border_style_definition_variant = border_style_definition.split("|")
                border_variant_list = list()
                for each_variant in border_style_definition_variant:
                    each_variant_split = each_variant.split("_")
                    if CSSGenerator().is_color_code(each_variant_split[-1]):
                        each_variant_split[-1] = f"#{each_variant_split[-1]}"
                        each_variant = "_".join(each_variant_split)
                    replaced_each_variant = each_variant.replace("_", " ")
                    border_variant_list.append(replaced_each_variant)
                border_style_value = "".join(border_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{border: {border_style_value};}}"})
            elif dynamic_css_class_key.startswith("outline\:"):
                outline_style_split = each_dynamic_css_class.split(":")
                _, outline_style_definition = outline_style_split[0], outline_style_split[-1]

                outline_style_definition_variant = outline_style_definition.split("|")
                outline_variant_list = list()
                for each_variant in outline_style_definition_variant:
                    replaced_each_variant = each_variant.replace("_", " ")
                    outline_variant_list.append(replaced_each_variant)
                outline_style_value = "".join(outline_variant_list)
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                dynamic_watched_css_dict.update({f""".{reconstructed_dynamic_css_class}""": f"{{outline: {outline_style_value};}}"})
            # elif dynamic_css_class_key.startswith("child"):
            #     child_style_split = each_dynamic_css_class.rsplit(":", 1)
            #     print(child_style_split)
            #     _, child_style_definition = child_style_split[0], child_style_split[-1]
            #     parent_counterpart = f".parent-{_.split('-')[-1]}".replace("\\", "")
            #
            #     style_definition_variant = child_style_definition.split("|")
            #     base_css_classes = {f".{k}": CSSGenerator().css_dictionary()[f'.{k}'] for k in style_definition_variant}
            #     reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
            #     css_result = ";".join([_.replace("{", "").replace("}", "").replace(";", "") for _ in base_css_classes.values()])
            #     print(css_result)
            #     dynamic_watched_css_dict.update({f"{parent_counterpart} .{reconstructed_dynamic_css_class}": f"{{{css_result}}}"})

        return dynamic_watched_css_dict

    @staticmethod
    def process_dynamic_gradients(css_class, dynamic_watched_css_dict, gradient_name="linear"):
        """
        Helper Function to process dynamic gradients
        :Date: August 14, 2022.
        """
        logging.info(f"Dynamic {gradient_name} Gradient class found.")

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

    def process_dynamic_pseudo_selector_css_classes(self, dynamic_css_class_list: list):
        """
        Process dynamic pseudo selector CSS classes
        date: January 28, 2023
        description: e.g., placeholder:font-32|color-brown|font-italic
        """
        dynamic_watched_pseudo_selector_css_dict = dict()
        for each_dynamic_css_class in dynamic_css_class_list:
            if each_dynamic_css_class.startswith("placeholder"):
                placeholder_style_split = each_dynamic_css_class.split(":")
                _, style_definition = placeholder_style_split[0], placeholder_style_split[-1]

                style_definition_variant = style_definition.split("|")
                base_css_classes = {f".{k}": CSSGenerator().css_dictionary()[f'.{k}'] for k in style_definition_variant}
                reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)")
                css_result = ";".join([_.replace("{", "").replace("}", "").replace(";", "") for _ in base_css_classes.values()])
                dynamic_watched_pseudo_selector_css_dict.update({f".{reconstructed_dynamic_css_class}": f"{{{css_result}}}"})

        return dynamic_watched_pseudo_selector_css_dict

    def process_dynamic_pseudo_class_css_classes(self, dynamic_css_class_list: list):
        """
        Process dynamic pseudo class CSS classes
        date: January 27, 2023
        description: e.g., focus:placeholder:font-32|color-gray|font-italic
        """
        dynamic_watched_pseudo_class_css_dict: dict = dict()
        for each_dynamic_css_class in dynamic_css_class_list:
            hover_style_split = each_dynamic_css_class.split(":", 1)
            _pseudo_name, style_definition = hover_style_split[0], hover_style_split[-1]
            # print(f"{_pseudo_name.upper()} SPLIT: {hover_style_split}")
            style_definition_variant = style_definition.split("|")
            base_css_classes = self.generate_base_css_classes(style_definition_variant)
            reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)").replace(f"\.{_pseudo_name}", f".{_pseudo_name}")
            # css_result = ";".join([_.replace("{", "").replace("}", "").replace(";", "") for _ in base_css_classes.values()])
            css_result = self.group_generated_base_css_classes(base_css_classes)
            dynamic_watched_pseudo_class_css_dict.update({f".{reconstructed_dynamic_css_class}": f"{{{css_result}}}"})
            # if each_dynamic_css_class.startswith("hover"):

        return dynamic_watched_pseudo_class_css_dict

    def process_dynamic_pseudo_group_css_classes(self, dynamic_css_class_list: list):
        """
        Process dynamic pseudo group CSS classes
        date: January 29, 2023
        description: e.g., every:placeholder:font-32|color-gray|font-italic
        """
        dynamic_watched_pseudo_class_css_dict: dict = dict()
        for each_dynamic_css_class in dynamic_css_class_list:
            group_style_split = each_dynamic_css_class.split(":", 1)
            _pseudo_name, style_definition = group_style_split[0], group_style_split[-1]
            # print(f"{_pseudo_name.upper()} SPLIT: {group_style_split}")
            style_definition_variant = style_definition.split("|")
            base_css_classes = self.generate_base_css_classes(style_definition_variant)
            # print(base_css_classes)
            reconstructed_dynamic_css_class = EyeMarkupParser().reconstruct_css_class(each_dynamic_css_class).replace("|", "\|").replace(".", "\.").replace("#", "\#").replace("%", "\%").replace("(", "\(").replace(")", "\)").replace(f"\.{_pseudo_name}", f".{_pseudo_name}")
            # css_result = ";".join([_.replace("{", "").replace("}", "").replace(";", "") for _ in base_css_classes.values()])
            css_result = self.group_generated_base_css_classes(base_css_classes)
            dynamic_watched_pseudo_class_css_dict.update({f".{reconstructed_dynamic_css_class}": f"{{{css_result}}}"})
            # if each_dynamic_css_class.startswith("every"):

        return dynamic_watched_pseudo_class_css_dict


class EyeWatcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, Eye.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        # try:
        #     while True:
        #         time.sleep(5)
        #     # while self.observer.is_alive():
        #     #     self.observer.join(1)
        # except RuntimeError as err:
        #     self.observer.stop()
        #     print("Error watching file")
        # self.observer.join()
        try:
            while self.observer.is_alive():
                self.observer.join(1)
        finally:
            self.observer.stop()
            self.observer.join()


class Handler(FileSystemEventHandler):
    FILES_TO_WATCH = []

    def __init__(self):
        directory_to_watch = Eye.DIRECTORY_TO_WATCH
        file_to_watch_extensions = Eye.EXTENSIONS_TO_WATCH
        exact_file_to_watch = Eye.EXACT_FILE
        if exact_file_to_watch != "":
            self.FILES_TO_WATCH.append(exact_file_to_watch) if os.path.isabs(exact_file_to_watch) else self.FILES_TO_WATCH.append(os.path.join(directory_to_watch, exact_file_to_watch))
        elif exact_file_to_watch == "":
            for ext in file_to_watch_extensions:
                self.FILES_TO_WATCH.extend(glob.glob(f"{directory_to_watch}/**/{ext}", recursive=True))

        # Remove all paths in the excluded directory from the list of FILES_TO_WATCH
        for _ in self.FILES_TO_WATCH:
            for each_ignored_directory in Eye.EXCLUDE_DIRECTORY:
                if each_ignored_directory in os.path.dirname(os.path.splitdrive(_)[-1]).split(os.path.sep):
                    self.FILES_TO_WATCH.remove(_)
        print(f"Hello, I am EYE (CSS). \nI am WATCHING: {','.join(self.FILES_TO_WATCH)}")

    def on_any_event(self, event):
        DIRECTORY_TO_IGNORE = Eye.EXCLUDE_DIRECTORY
        FILES_TO_IGNORE = Eye.EXCLUDE_FILES

        if event.src_path not in FILES_TO_IGNORE:
            if event.is_directory:
                return None

            elif event.event_type == 'created':
                # Take any action here when a file is first created.
                logging.info("Received created event - %s." % event.src_path)

            elif event.event_type == 'modified':
                # Take any action here when a file is modified.
                logging.info("Received modified event - %s." % event.src_path)

                if event.src_path in self.FILES_TO_WATCH:
                    EyeWriter().create_watched_css()

    # def on_modified(self, event):
    #     if event.src_path in self.files_to_watch:
    #         EyeWriter().parse_eye_css()


class CSSFinder:
    """
    Class to perform all operations of finding css in files.
    :Date: December 14, 2022.
    :remark: A Future-Feature.
    :description: Will be a class for refactored and re-written EyeMarkupParser methods
        e.g., get_attr_class_data_from_file(), get_attr_class_list_from_markup() etc.
    :tag: TODO
    """
    pass


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
        substring_markup_string = re.sub(r"""\{/\*[<:-|/]*\s*\w*\d*[<:-|/]*\*/}""", "", collapse_markup_string)
        minify_markup_string = re.sub(r""">\s+<""", "><", substring_markup_string)
        cleaned_markup_string = minify_markup_string
        return cleaned_markup_string

    def get_attr_class_data_from_markup(self, markup_string: str) -> list:
        """
        Gets all the class="..." in the markup string.
        :Date: inherit
        """
        cleaned_markup_string = self.clean_markup(markup_string)
        attr_class_data = re.findall(r"""((class\b|className)="([\w*-:|/]\s*)+")""", cleaned_markup_string)

        return attr_class_data

    def get_attr_class_list_from_markup(self, markup_string: str) -> list:
        attr_classes = [
            each_attr[0].split("=")[-1].replace("'", "").replace('"', '').split(" ")
            for each_attr in self.get_attr_class_data_from_markup(markup_string)
        ]
        return attr_classes

    def get_attr_class_data_from_file(self, file_str: str) -> list:
        """
        Function to parse all watched files and get the class attrs from the file
        :param file_str: The file content to parse as a string.
        :return: A list of class attributes from markup files and from scripts.
        :Date: August 13, 2022.
        """
        # js_css_classes_data = re.findall("""(classList.add)\(['"](([\w+-:|#()%]+\s*)+)['"]\)""", file_str, re.MULTILINE)
        """
        # DECEMBER 12, 2022.
        # The above js_css_classes_data action is insufficient when dealing with enterprise programming.
        One limitation experienced with this was when working on Summary.
        The custom methods I wrote to process CSS-class-styles did not work because eye_css could not process those
        custom methods as I have already defined the rule for finding the CSS files from external files aside from
        markup files.
        SOLUTION 1: The Solution found by INSPIRATION is to search through external files for strings that contain "-"
        (dash) between them and use those strings as css files and then process from there.
        SOLUTION 2: Solution 1 will not work because of eye_css pseudo-elements and pseudo-classes. So only contents
        in a string delimiter will be fetched. i.e., strings contained within (', ", `) will be fetched
        """
        js_css_classes_data = re.findall(r"""['\"`](\b[\s\w:.|/-]+\b)[`\"']""", file_str, re.ASCII)
        # print(f"{file_str}:::{js_css_classes_data}")
        # markups_css_classes_data = re.findall(r"""(class\b|className\b)=\"\s*(([\w*-:|#()%/]\s*)+)\"""", file_str)
        # print(markups_css_classes_data)

        # watched_files_css_classes_data = [*markups_css_classes_data, *js_css_classes_data]
        # return watched_files_css_classes_data
        return [*js_css_classes_data]

    def attr_class_list_from_file(self, file_str: str) -> list:
        """
        Function to get the css classes from the attr_class_data as an argument
        :param file_str: The parsed attr class data from the file
        :return: A list of css classes.
        :Date: August 13, 2022.
        """
        # print(self.get_attr_class_data_from_file(file_str))
        # css_classes_list = [
        #     each_css_class[1].split(" ")
        #     for each_css_class in self.get_attr_class_data_from_file(file_str)
        # ]
        css_classes_list = [
            each_css_class.split(" ")
            for each_css_class in self.get_attr_class_data_from_file(file_str)
        ]
        # print(css_classes_list)
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
        pseudo_elements = CSSGenerator().default_pseudo_element_list
        pseudo_group = CSSGenerator().default_pseudo_group_list
        pseudo_classes = CSSGenerator().default_pseudo_class_list
        media_queries = CSSGenerator().default_media_query_list
        if css_class_str.startswith((*pseudo_group, *pseudo_classes, *pseudo_elements, *media_queries)):
            return False
        return True

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
    def is_pseudo_group_class(css_class_str) -> bool:
        """ A Function to check if a css class str is a pseudo group css class
        :param css_class_str: the css class string to check.
        :return: bool.
        :Date: January 28, 2023.
        """
        pseudo_classes = CSSGenerator().default_pseudo_group_list
        if css_class_str.startswith(pseudo_classes):
            return True
        return False

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
    def is_pseudo_theme_class(css_class_str) -> bool:
        """ A Function to check if a css class str is a pseudo theme css class
        :param css_class_str: the css class string to check.
        :return: bool.
        :Date: January 28, 2023.
        """
        pseudo_classes = CSSGenerator().default_pseudo_theme_list
        if css_class_str.startswith(pseudo_classes):
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

        if css_class_str.__contains__(":"):
            if css_class_str.startswith(CSSGenerator().first_level_base_class_pseudo):
                # return css_class_str
                return self.reconstruct_markup_base_css_class(css_class_str)
            natural_base_css_class = css_class_str.rsplit(":", 1)[-1]
            pseudo_css_class = css_class_str.rsplit(":", 1)[0]
            nested_base_css_class_list = list()
            for _ in pseudo_css_class.split(":"):
                if _ in CSSGenerator().first_level_base_class_pseudo:
                    nested_base_css_class_list.append(f"{_}:")
            base_css_class = "".join([*nested_base_css_class_list, *natural_base_css_class])
            # print(f"{css_class_str} :: {base_css_class} :: {pseudo_css_class}")
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
        return True if re.search(
            rf"{css_class_name}*", ",".join(CSSGenerator().css_dictionary().keys())
        ) is not None else False

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
        elif self.is_pseudo_group_class(css_class):
            return self.reconstruct_markup_pseudo_group_css_class(css_class)
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
        # TODO: November 13, 2022. Add :empty selector to padding and margin by default. i.e.,
        # if re.match(r"^pad-*", css_class):
        #   css_class = css_class+":empty"
        return css_class.replace("\:", ":").replace(":", "\:")

    @staticmethod
    def reconstruct_markup_pseudo_group_css_class(css_class: str) -> str:
        """ A Function to reconstruct eye.css pseudo-group from markup file.
        e.g., .every:pct:w-48 ==> .every\:pct\:w-48 {...}
        .sm:every:bg-light ==> @media (max-width) {.every\:bg-light {...}}
        How: ??
        1.  Replace all ":" with "\:"
        2.  Add pseudo group to end of the css class. e.g., .every:bg-lighter => .every\:bg-lighter:every {...}
        :param css_class: the pseudo-css-class to reconstruct
        :return: the reconstructed pseudo_css_class
        :Date: August 5, 2022.
        """
        # Get the pseudo_group from the markup css_classes and perform substitution and addition.
        replaced_css = css_class.replace(":", "\:")
        pseudo_class = css_class.split(":", 1)[0]
        # print(pseudo_class)
        if pseudo_class == "every":
            return f"{replaced_css} > *"
        elif pseudo_class == "all":
            return f"{replaced_css} *"
        elif pseudo_class == "sibling":
            return f"{replaced_css} ~ *"
        return replaced_css

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
        # If the pseudo_class contains a child-, meaning it has a group_selector
        if css_class.__contains__("child-"):
            child_group = re.findall(r"(child-\w+)", css_class)
            child_group_identifier = child_group[0].split("-")[-1]
            pseudo_class = css_class.split(":", 1)[0]
            replaced_css = css_class.replace(':', '\:')
            reconstructed_css = f"parent-{child_group_identifier}:{pseudo_class} .{replaced_css}"
            return reconstructed_css
        # If the pseudo_class contains a sibling-, meaning it has a group_selector
        if css_class.__contains__("sibling-"):
            sibling_group = re.findall(r"(sibling-\w+)", css_class)
            sibling_group_identifier = sibling_group[0].split("-")[-1]
            pseudo_class = css_class.split(":", 1)[0]
            replaced_css = css_class.replace(':', '\:')
            # print(f"{css_class} <> {replaced_css}")
            reconstructed_css = f"sibling-{sibling_group_identifier}:{pseudo_class} ~ .{replaced_css}"
            return reconstructed_css
        # If the pseudo_class contains an all modifier
        if css_class.__contains__("all"):
            replaced_css = css_class.replace(":", "\:")
            pseudo_class = css_class.split(":", 1)[0]
            return f"{replaced_css} *:{pseudo_class}"
        # If the pseudo_class contains an every modifier
        if css_class.__contains__("every"):
            replaced_css = css_class.replace(":", "\:")
            pseudo_class = css_class.split(":", 1)[0]
            return f"{replaced_css} > *:{pseudo_class}"
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
        # pseudo_class = self.get_pseudo_element_from_pseudo_css_str(css_class)
        pseudo_class = css_class.split(":", 1)[0]
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
