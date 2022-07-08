# MAYOWA OBISESAN
# EYE.CSS WATCHER FILE.
# JULY 2, 2022.

# Get a file to watch.
# get all the class or className from the file being watched.
# The class and className represents all the defined inline styles available within an html, jsx or tsx page.


class EyeWatcher:
    """ Eye.css Watcher script. """

    def __init__(self) -> None:
        self.eye_css_name = "eye_gen.css"
        self.sm_media_query_css_classes_list: list = list()
        self.md_media_query_css_classes_list: list = list()
        self.lg_media_query_css_classes_list: list = list()
        self.xl_media_query_css_classes_list: list = list()
        self.xxl_media_query_css_classes_list: list = list()
        self.css_list: list = list()
        self.css_content_list: list = list()  # made a list so that we can use the writelines file method.

    @staticmethod
    def create_sm_media_query(sm_css_classes):
        media_queries_css = ""
        for k, v in sm_css_classes.items():
            # Prepend ".sm" to the media_query css class key and strip the "." existing before any existing class e.g., .pct
            media_queries_css += f".sm\:{k.lstrip('.')} {v}"
        sm_media_query_definition = f"@media (min-width: 640px) {{{media_queries_css}}}"
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

            self.write_watched_css_file()

    def find_intersection_css_classes(self, css_str: str = ""):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.collect_html_css_classes()
        print(f"COLLECTED CSS FROM HTML FILE: {collected_html_classes}")

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        watched_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED CSS CLASSES: {watched_css_classes}")

        # get the values of the watched css classes. use the watched_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]};}}" for k in watched_css_classes}
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
        print(f"SET CSS TO DICT: {set(css_to_dict)}")
        print(f"COLLECTED HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]};}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        sm_media_query = self.create_sm_media_query(res)
        md_media_query = self.create_md_media_query(res)
        # self.write_watched_css_file(sm_media_query)
        self.write_watched_sm_media_query_css(sm_media_query)
        self.write_watched_md_media_query_css(md_media_query)
        # return

    def find_intersection_css_md_media_query_classes(self, css_str):
        # Attach the method to a class to avoid a continuous function re-run
        css_to_dict = self.convert_eye_css_to_dict(css_str)
        collected_html_classes = self.md_media_query_css_classes_list

        # print(set(css_to_dict).intersection(set(collected_html_classes)))
        # print("CONVERT")
        print(f"SET CSS TO DICT: {set(css_to_dict)}")
        print(f"COLLECTED HTML CLASSES: {set(collected_html_classes)}")
        watched_media_query_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
        print(f"WATCHED MEDIA CSS CLASSES: {watched_media_query_css_classes}")

        # get the values of the watched css classes. use the watched_media_query_css_classes as keys for the eye_css_dict.
        res = {k: f"{{{css_to_dict[k]};}}" for k in watched_media_query_css_classes}
        # print(f"RES: {res}")
        md_media_query = self.create_md_media_query(res)
        # self.write_watched_css_file(sm_media_query)
        self.write_watched_md_media_query_css(md_media_query)
        # return

    # def write_watched_css_to_file(self):
    # watched_css_classes = set(self.convert_eye_css_to_dict(css_str)).intersection(
    # set(self.collect_html_css_classes()))

    @classmethod
    def convert_css_to_set(self, css_dict):
        css_set = set()
        print(css_set, end="")

    @classmethod
    def convert_eye_css_to_dict(cls, css_text):
        import cssutils

        css_dict = dict()
        css_sheet = cssutils.parseString(css_text)

        # ignored_rules = [cssutils.css.csscomment.CSSComment, cssutils.css.cssfontfacerule.CSSFontFaceRule,
        #                  cssutils.css.cssmediarule.CSSMediaRule, cssutils.css.cssunknownrule.CSSUnknownRule, ]
        ignored_rules = (cssutils.css.csscomment.CSSComment, cssutils.css.cssfontfacerule.CSSFontFaceRule,
                         cssutils.css.cssmediarule.CSSMediaRule, cssutils.css.cssunknownrule.CSSUnknownRule)
        # for rule in css_sheet:
        #     if any((isinstance(rule, rule_type) for rule_type in ignored_rules)): continue
        #     selector = rule.selectorText

        for rule in css_sheet:
            # if (isinstance(rule, rule_type) for rule_type in ignored_rules): continue
            # if rule in ignored_rules: continue
            # if type(rule) not in ignored_rules:
            # if not isinstance(rule, ignored_rules):
            if rule.type == rule.STYLE_RULE:
                selector = rule.selectorText
                styles = rule.style.cssText
                css_dict[selector] = styles

        # value = {k: second_dict[k] for k in set(second_dict) - set(first_dict)}
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
                if j.startswith("sm:"):
                    media_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        media_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        media_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.sm_media_query_css_classes_list.append(media_css)
                if j.startswith("md:"):
                    media_css = j.split(':', 1)[-1]
                    j_conv = j.split(':')[1:]
                    print(f"J CONV : {j_conv}")
                    if len(j_conv) == 1:
                        media_css = f".{j_conv[-1]}"
                    elif len(j_conv) > 1:
                        j_conv[0] = f"{j_conv[0]}"
                        media_css = f".{j_conv[0]}\:{j_conv[-1]}"
                    self.sm_media_query_css_classes_list.append(media_css)
        # print(f"FORMATTED HTML CSS CLASSES LIST: {css_classes}")
        return css_classes

    def collect_html_css_classes(self):
        from bs4 import BeautifulSoup as BSoup
        with open("main.html", "r") as opened_file:
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
        watched_css_file_name: str = "watched_eye.css"
        self.css_content_list.append("""
            * {
                --webkit-box-sizing: border-box; --moz-box-sizing: border-box; box-sizing: border-box;
            text-rendering: auto;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: antialiased; /* | grayscale*/
            }
        """)
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
            for _ in self.css_content_list:
                opened_file.writelines(_)

            # print(f"FINAL CSS CLASSES: {css_list}")
            opened_file.close()

    def write_watched_css(self, css_list):
        self.css_content_list.extend(css_list)
        print(f"WRITING WATCHED CSS: {self.css_content_list}")
        css_text = ""
        # for each_style_property in css_list:
        # file.writelines(each_style_property)
        # css_text += f"{each_style_property}"
        # return css_text
        # print("Closing eye_final_output.css")

    def write_watched_sm_media_query_css(self, sm_media_query_css):
        self.css_content_list.append(sm_media_query_css)
        print(f"WRITING WATCHED SM MEDIA QUERY CSS: {self.css_content_list}")
        # if sm_media_query_css != "":
        #     # file.write(sm_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return sm_media_query_css
        # return ""

    def write_watched_md_media_query_css(self, md_media_query_css):
        self.css_content_list.append(md_media_query_css)
        print(f"WRITING WATCHED MD MEDIA QUERY CSS: {self.css_content_list}")
        # if md_media_query_css != "":
        #     # file.write(md_media_query_css)
        #     # return the css_text instead of writing to the file from here.
        #     return md_media_query_css
        # return ""


# EyeWatcher().collect_html_css_classes()
EyeWatcher().parse_eye_css()
