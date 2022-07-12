# MAYOWA OBISESAN
# EYE.CSS WATCHER FILE.
# JULY 2, 2022.

# Get a file to watch.
# get all the class or className from the file being watched.
# The class and className represents all the defined inline styles available within an html, jsx or tsx page.

# Have imports here.
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# class EyeWatcher:
#     DIRECTORY_TO_WATCH = os.getcwd()
#
#     def __init__(self):
#         self.files_to_watch = ["main.html"]
#
#         self.files_watched_data = dict()
#
#     def file_os_stats(self, file):
#         if not self.files_watched_data.get("former_modified_time"):
#             self.files_watched_data["former_modified_time"] = os.stat(file).sm_mtime
#         # self.files_watched_data["current_modified_time"] = os.stat(file).sm_mtime
#         return
#
#     def get_files_stats_data(self):
#         for each_file in self.files_to_watch:
#             self.files_watched_data[each_file] = each_file
#
#     def watch(self):
#         current_modified_time = os.path.getmtime(os.path.join(self.DIRECTORY_TO_WATCH, "main.html"))
#         # if current_modified_time > former_modified_time:
#         #     print("File has been modified.")


# TODO: JULY 12, 2022.
# after:[{content: 'This element is empty.'}]:color-green
# Create something like this, for html files which eye will parse into the below:
# Because the class starts with after, split the 'after' class, and continue parsing the other end of the split.
# If the second part of the split begins with a '[', a custom inline-css is defined, so, split the other end of the
# 'after' split with the end of the square bracket ']' which then gives another split.
# Check the square bracket split and see if the second split of the 'square bracket' split contains a colon ':',
# if it does, get the value of the class after the ':' and append to the value inside the square bracket,
# then append inside the after pseudo class and like that to generate an enclosed css-class definition all
# from one html inline-css.
# NOTE: THIS WORKS FOR ONLY PSEUDO-ELEMENT AND NOT ALL CLASSES AND DEFINITELY NOT PSEUDO-CLASSES

class EyeWriter:
    """ Eye.css Watcher script. """

    def __init__(self) -> None:
        self.eye_css_name = "eye_gen.css"
        self.file_to_watch = r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\index.html"
        self.sm_media_query_css_classes_list: list = list()
        self.md_media_query_css_classes_list: list = list()
        self.lg_media_query_css_classes_list: list = list()
        self.xl_media_query_css_classes_list: list = list()
        self.xxl_media_query_css_classes_list: list = list()
        self.css_list: list = list()
        self.css_content_list: list = list()  # made a list so that we can use the writelines file method.
        self.hover_css_classes_list: list = list()
        self.focus_css_classes_list: list = list()
        self.empty_css_classes_list: list = list()
        self.after_css_classes_list: list = list()

    def parse_eye_css(self):
        with open(self.eye_css_name, "r") as opened_file:
            # css_list = opened_file.readlines()
            css_str = opened_file.read()
            opened_file.close()

            print(f"MEDIA QUERY CSS CLASSES LIST: {self.sm_media_query_css_classes_list}")

            # if self.sm_media_query_css_classes_list:
            # print(f"MEDIA QUERY CSS CLASSES LIST: {self.sm_media_query_css_classes_list}")
            self.find_intersection_css_classes(css_str)
            self.find_intersection_css_sm_media_query_classes(css_str)
            self.find_intersection_css_md_media_query_classes(css_str)
            self.find_intersection_css_lg_media_query_classes(css_str)
            self.find_intersection_css_xl_media_query_classes(css_str)
            self.find_intersection_css_xxl_media_query_classes(css_str)

            # Pseudo classes - Intersection
            self.find_intersection_css_hover_classes(css_str)
            self.find_intersection_css_focus_classes(css_str)
            self.find_intersection_css_empty_classes(css_str)

            # Pseudo elements - Intersection
            self.find_intersection_css_after_classes(css_str)
            # self.find_intersection_css_before_classes(css_str)

            self.write_watched_css_file()

    @staticmethod
    def create_sm_media_query(sm_css_classes):
        media_queries_css = ""
        for k, v in sm_css_classes.items():
            # Prepend ".sm" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".sm\:{k.lstrip('.')} {v}"
        sm_media_query_definition = f"@media (max-width: 639px) {{{media_queries_css}}}"
        print(f"SM MEDIA QUERY DEFINITION: {sm_media_query_definition}")
        return sm_media_query_definition

    @staticmethod
    def create_md_media_query(md_css_classes):
        media_queries_css = ""
        for k, v in md_css_classes.items():
            # Prepend ".md" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".md\:{k.lstrip('.')} {v}"
        md_media_query_definition = f"@media (min-width: 768px) {{{media_queries_css}}}"
        print(f"MD MEDIA QUERY DEFINITION: {md_media_query_definition}")
        return md_media_query_definition

    @staticmethod
    def create_lg_media_query(lg_css_classes):
        media_queries_css = ""
        for k, v in lg_css_classes.items():
            # Prepend ".lg" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".lg\:{k.lstrip('.')} {v}"
        lg_media_query_definition = f"@media (min-width: 1024px) {{{media_queries_css}}}"
        print(f"LG MEDIA QUERY DEFINITION: {lg_media_query_definition}")
        return lg_media_query_definition

    @staticmethod
    def create_xl_media_query(xl_css_classes):
        media_queries_css = ""
        for k, v in xl_css_classes.items():
            # Prepend ".xl" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".xl\:{k.lstrip('.')} {v}"
        xl_media_query_definition = f"@media (min-width: 1280px) {{{media_queries_css}}}"
        print(f"XLG MEDIA QUERY DEFINITION: {xl_media_query_definition}")
        return xl_media_query_definition

    @staticmethod
    def create_xxl_media_query(xxl_css_classes):
        media_queries_css = ""
        for k, v in xxl_css_classes.items():
            # Prepend ".xxl" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".xxl\:{k.lstrip('.')} {v}"
        xxl_media_query_definition = f"@media (min-width: 1536px) {{{media_queries_css}}}"
        print(f"XXLG MEDIA QUERY DEFINITION: {xxl_media_query_definition}")
        return xxl_media_query_definition

    @staticmethod
    def create_hover_css(hover_css_classes):
        hover_css_definition = ""
        for k, v in hover_css_classes.items():
            # Prepend ".hover" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            hover_css_definition += f".hover\:{k.lstrip('.')}:hover {v}"
        # hover_css_definition = f"@media (min-width: 768px) {{{hover_css}}}"
        print(f"HOVER CLASS DEFINITION: {hover_css_definition}")
        return hover_css_definition

    @staticmethod
    def create_focus_css(focus_css_classes):
        focus_css_definition = ""
        for k, v in focus_css_classes.items():
            # Prepend ".focus" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            focus_css_definition += f".focus\:{k.lstrip('.')}:focus {v}"
        # focus_css_definition = f"@media (min-width: 768px) {{{focus_css}}}"
        print(f"FOCUS CLASS DEFINITION: {focus_css_definition}")
        return focus_css_definition

    @staticmethod
    def create_empty_css(empty_css_classes):
        empty_css_definition = ""
        for k, v in empty_css_classes.items():
            # Prepend ".empty" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            empty_css_definition += f".empty\:{k.lstrip('.')}:empty {v}"
        # empty_css_definition = f"@media (min-width: 768px) {{{empty_css}}}"
        print(f"EMPTY CLASS DEFINITION: {empty_css_definition}")
        return empty_css_definition

    @staticmethod
    def create_after_css(after_css_classes):
        after_css_definition = ""
        for k, v in after_css_classes.items():
            # Prepend ".after" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            after_css_definition += f".after\:{k.lstrip('.')}::after {v}"
        # after_css_definition = f"@media (min-width: 768px) {{{after_css}}}"
        print(f"AFTER CLASS DEFINITION: {after_css_definition}")
        return after_css_definition

    def find_intersection_css_classes(self, css_str: str = ""):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.collect_html_css_classes()
        # print(f"COLLECTED CSS FROM HTML FILE: {collected_html_classes}")

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        watched_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED CSS CLASSES: {watched_css_classes}")

        # get the values of the watched css classes. use the watched_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_css_classes}
        print(f"RES: {res}")
        # self.write_watched_css_file(res.items())
        self.write_watched_css(res.items())
        # return

    def find_intersection_css_sm_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.sm_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED SM: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED SM MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        sm_media_query = self.create_sm_media_query(res)
        # self.write_watched_css_file(sm_media_query)
        self.write_watched_sm_media_query_css(sm_media_query)
        # return

    def find_intersection_css_md_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.md_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED MD MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        md_media_query = self.create_md_media_query(res)
        # self.write_watched_css_file(sm_media_query)
        self.write_watched_md_media_query_css(md_media_query)
        # return

    def find_intersection_css_lg_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.lg_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED LG MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}

        lg_media_query = self.create_lg_media_query(res)
        self.write_watched_lg_media_query_css(lg_media_query)

    def find_intersection_css_xl_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.xl_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED XL MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}

    def find_intersection_css_xxl_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.xxl_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED XXL MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}

        xxl_media_query = self.create_xxl_media_query(res)
        self.write_watched_xxl_media_query_css(xxl_media_query)

    def find_intersection_css_hover_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.hover_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED HOVER CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        hover_css = self.create_hover_css(res)
        self.write_watched_hover_css(hover_css)

    def find_intersection_css_focus_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.focus_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED FOCUSED CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        focus_css = self.create_focus_css(res)
        self.write_watched_focus_css(focus_css)

    def find_intersection_css_empty_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.empty_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_empty_selector_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED EMPTY CSS CLASSES: {watched_empty_selector_css_classes}")

        # get the values of the watched css classes. use the watched_empty_selector_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_empty_selector_css_classes}
        # print(f"RES: {res}")
        empty_css = self.create_empty_css(res)
        self.write_watched_empty_css(empty_css)

    def find_intersection_css_after_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.after_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        # print(f"SET CSS TO DICT: {set(css_to_dict)}")
        # print(f"COLLECTED MD: HTML CLASSES: {set(collected_html_classes)}")
        watched_after_selector_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED EMPTY CSS CLASSES: {watched_after_selector_css_classes}")

        # get the values of the watched css classes. use the watched_after_selector_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]}}}" for k in watched_after_selector_css_classes}
        # print(f"RES: {res}")
        after_css = self.create_after_css(res)
        self.write_watched_after_css(after_css)

    # def write_watched_css_to_file(self):
    # watched_css_classes = set(self.convert_eye_css_to_dict(css_str)).intersection(
    # set(self.collect_html_css_classes()))

    @classmethod
    def convert_css_to_set(self, css_dict):
        css_set = set()
        print(css_set, end="")

    @classmethod
    def convert_eye_css_to_dict(cls, css_text):
        # import cssutils

        css_dict = dict()
        # css_sheet = cssutils.parseString(css_text)
        # ignored_rules = [cssutils.css.csscomment.CSSComment, cssutils.css.cssfontfacerule.CSSFontFaceRule,
        #                  cssutils.css.cssmediarule.CSSMediaRule, cssutils.css.cssunknownrule.CSSUnknownRule, ]
        # ignored_rules = (cssutils.css.csscomment.CSSComment, cssutils.css.cssfontfacerule.CSSFontFaceRule,
        #                  cssutils.css.cssmediarule.CSSMediaRule, cssutils.css.cssunknownrule.CSSUnknownRule)
        # for rule in css_sheet:
        #     if any((isinstance(rule, rule_type) for rule_type in ignored_rules)): continue
        #     selector = rule.selectorText

        # for rule in css_sheet:
        #     # if (isinstance(rule, rule_type) for rule_type in ignored_rules): continue
        #     # if rule in ignored_rules: continue
        #     # if type(rule) not in ignored_rules:
        #     # if not isinstance(rule, ignored_rules):
        #     if rule.type == rule.STYLE_RULE:
        #         selector = rule.selectorText
        #         styles = rule.style.cssText
        #         css_dict[selector] = styles

        # value = {k: second_dict[k] for k in set(second_dict) - set(first_dict)}

        # parser = cssutils.CSSParser(log=None, loglevel=None, raiseExceptions=False, parseComments=False)
        # # parser.setFetcher(fetcher) # optional
        # sheet = parser.parseString(css_text)
        #
        # for rule in sheet:
        #     if rule.type == rule.STYLE_RULE:
        #         selector = rule.selectorText
        #         styles = rule.style.cssText
        #         css_dict[selector] = styles

        from eye_css_generator import CSSGenerator
        css_list = css_text.rsplit('}')
        for each_css_rule in CSSGenerator.minify_css_list(css_list):
            if each_css_rule not in [None, ""]:
                css_rule_token = each_css_rule.split('{')
                # print(css_rule_token)
                # clean the css_rule_token[1]
                cleaned_css_key = css_rule_token[0].replace(" ", "")
                cleaned_css_values = css_rule_token[1]
                # print(cleaned_css_values)
                css_dict[cleaned_css_key] = cleaned_css_values

        # print(css_dict, end="")
        return css_dict

    @classmethod
    def clean_css_list(cls, uncleaned_list) -> list:
        if uncleaned_list.count(None) > 0:
            for each_item in uncleaned_list:
                if each_item is None:
                    uncleaned_list.remove(None)
            cls.clean_css_list(uncleaned_list)
            # print(f"Cleaned List: {uncleaned_list}")
        return uncleaned_list

    def format_html_css_classes_list(self, res: list) -> list:
        css_classes = []
        for i in res:
            for j in i:
                if j.startswith("pct:"):
                    j = f"pct\:{j.split(':')[-1]}"
                css_classes.append(f".{j}")

                # Test for hover classes.
                if j.startswith("hover:"):
                    # hover_css = f".{j.split(':')[-1]}"
                    hover_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        hover_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        hover_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.hover_css_classes_list.append(hover_css)
                    print(f"HOVER CSS CLASSES LIST: {self.hover_css_classes_list}")

                # Test for focus classes.
                if j.startswith("focus:"):
                    # focus_css = f".{j.split(':')[-1]}"
                    focus_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        focus_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        focus_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.focus_css_classes_list.append(focus_css)
                    print(f"FOCUS CSS CLASSES LIST: {self.focus_css_classes_list}")

                # Test for empty classes.
                if j.startswith("empty:"):
                    # empty_css = f".{j.split(':')[-1]}"
                    empty_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        empty_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        empty_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.empty_css_classes_list.append(empty_css)
                    print(f"EMPTY CSS CLASSES LIST: {self.empty_css_classes_list}")

                # Test for after classes.
                if j.startswith("after:"):
                    # after_css = f".{j.split(':')[-1]}"
                    after_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        after_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        after_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.after_css_classes_list.append(after_css)
                    print(f"AFTER CSS CLASSES LIST: {self.after_css_classes_list}")

                # Test for media queries
                if j.startswith("sm:"):
                    media_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        media_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        media_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.sm_media_query_css_classes_list.append(media_css)
                if j.startswith("md:"):
                    media_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    # print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        media_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        media_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.md_media_query_css_classes_list.append(media_css)
        # print(f"FORMATTED HTML CSS CLASSES LIST: {css_classes}")
        return css_classes

    def collect_html_css_classes(self):
        from bs4 import BeautifulSoup as BSoup
        with open(self.file_to_watch, "r", encoding="utf-8") as opened_file:
            file_string = opened_file.read()
            opened_file.close()
            # print(f"raw html file: {file_string}")
            res = [each.get("class") for each in BSoup(file_string, features="html.parser").find_all()]
            # print(f"css from html file: {res}")
            cleaned_list = self.clean_css_list(res)
            # print(self.format_html_css_classes_list(cleaned_list))
            # print(set(self.format_html_css_classes_list(cleaned_list)))
            # find_all(name=["div", "section"], attrs=["class", "className"])
            # print(res, end="")
            return self.format_html_css_classes_list(cleaned_list)

    # def write_watched_css_file(self, css_list, sm_media_query_css=""):
    # def write_watched_css_file(self, css_text):
    def write_watched_css_file(self):
        # watched_css_file: list = [f"{os.getcwd()}\watched_eye.css", r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\watched_eye.css"]
        watched_css_file_name: str = r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\watched_eye.css"
        self.css_content_list.append("""
            * {
                -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;
                text-rendering: auto;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: antialiased; /* | grayscale*/
                font-family: "system-ui";
                
                transition: all .4s ease-in-out;
            }
            *::-webkit-scrollbar {
                width: 8px;
                height: 100%;
                min-height: 8px;    /* For horizontal scrollbar to display. */
                max-height: 8px;    /* For horizontal scrollbar to display. */
                background-color: #EEEEEE;
            }
            *::-webkit-scrollbar-thumb {
                background-color: #D7D7D7;
            }
            *::-webkit-scrollbar-track {
                background-color: #F3F3F3;
            }
            body {
            }
        """)
        # for _ in watched_css_file:
        with open(watched_css_file_name, "w") as opened_file:
            # opened_file.write("""""")
            # if self.sm_media_query_css_classes_list:
            #     for each_media_style_property in self.sm_media_query_css_classes_list:
            #         pass
            # css_content += (
            #         self.write_watched_sm_media_query_css(opened_file, sm_media_query_css) + self.write_watched_css(
            #     opened_file, css_list))
            #
            # opened_file.write(css_content)

            # match self.hover_css_classes_list:
            #     case list():
            #         pass
            #     case list(str()):
            #         self.write_watched_hover_css(self.hover_css_classes_list)

            for _ in self.css_content_list:
                opened_file.writelines(_)

            # print(f"FINAL CSS CLASSES: {css_list}")
            opened_file.close()

    def write_watched_css(self, css_list):
        self.css_content_list.extend(css_list)
        # print(f"WRITING WATCHED CSS: {self.css_content_list}")
        css_text = ""
        # for each_style_property in css_list:
        # file.writelines(each_style_property)
        # css_text += f"{each_style_property}"
        # return css_text
        # print("Closing eye_final_output.css")

    def write_watched_sm_media_query_css(self, sm_media_query_css):
        self.css_content_list.append(sm_media_query_css)
        # print(f"WRITING WATCHED SM MEDIA QUERY CSS: {self.css_content_list}")
        # if sm_media_query_css != "":
        #     # file.write(sm_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return sm_media_query_css
        # return ""

    def write_watched_md_media_query_css(self, md_media_query_css):
        self.css_content_list.append(md_media_query_css)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if md_media_query_css != "":
        #     # file.write(md_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return md_media_query_css
        # return ""

    def write_watched_lg_media_query_css(self, lg_media_query_css):
        self.css_content_list.append(lg_media_query_css)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if lg_media_query_css != "":
        #     # file.write(lg_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return lg_media_query_css
        # return ""

    def write_watched_xl_media_query_css(self, xl_media_query_css):
        self.css_content_list.append(xl_media_query_css)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if xl_media_query_css != "":
        #     # file.write(xl_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return xl_media_query_css
        # return ""

    def write_watched_xxl_media_query_css(self, xxl_media_query_css):
        self.css_content_list.append(xxl_media_query_css)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if xxl_media_query_css != "":
        #     # file.write(xxl_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return xxl_media_query_css
        # return ""

    def write_watched_hover_css(self, hover_css_list):
        self.css_content_list.extend(hover_css_list)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if md_media_query_css != "":
        #     # file.write(md_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return md_media_query_css
        # return ""

    def write_watched_focus_css(self, focus_css_list):
        self.css_content_list.extend(focus_css_list)
        # print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if md_media_query_css != "":
        #     # file.write(md_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return md_media_query_css
        # return ""

    def write_watched_empty_css(self, empty_css_list):
        self.css_content_list.extend(empty_css_list)

    def write_watched_after_css(self, after_css_list):
        self.css_content_list.extend(after_css_list)

# EyeWatcher().collect_html_css_classes()
# EyeWriter().parse_eye_css()


class EyeWatcher:
    DIRECTORY_TO_WATCH = r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io"

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

    def __init__(self):
        self.files_to_watch = [r"C:\Users\Mayowa Obisesan\Blessed\BMayowa.github.io\index.html"]
        print(f"Hello, I am EYE. \nI am WATCHING: {','.join(self.files_to_watch)}")

    def on_any_event(self, event):
        DIRECTORY_TO_IGNORE = [".git"]
        FILES_TO_EXCLUDE = [".gitignore"]

        if event.src_path not in FILES_TO_EXCLUDE:
            if event.is_directory:
                return None

            elif event.event_type == 'created':
                # Take any action here when a file is first created.
                print("Received created event - %s." % event.src_path)

            elif event.event_type == 'modified':
                # Take any action here when a file is modified.
                print("Received modified event - %s." % event.src_path)

                if event.src_path in self.files_to_watch:
                    EyeWriter().parse_eye_css()

    # def on_modified(self, event):
    #     if event.src_path in self.files_to_watch:
    #         EyeWriter().parse_eye_css()


if __name__ == '__main__':
    w = EyeWatcher()
    w.run()
