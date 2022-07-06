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

    def parse_eye_css(self):
        with open(self.eye_css_name, "r") as opened_file:
            # css_list = opened_file.readlines()
            css_str = opened_file.read()
            opened_file.close()

            # Attach the method to a class to avoid a continuous function re-run
            css_to_dict = self.convert_eye_css_to_dict(css_str)
            collected_html_classes = self.collect_html_css_classes()

            # print(set(css_to_dict).intersection(set(collected_html_classes)))
            # print("CONVERT")
            watched_css_classes = sorted(set(css_to_dict).intersection(set(collected_html_classes)))
            print(watched_css_classes)

            # get the values of the watched css classes. use the watched_css_classes as keys for the eye_css_dict.
            res = {k: f"{{{css_to_dict[k]};}}" for k in watched_css_classes}
            # print(f"RES: {res}")
            self.write_watched_css_file(res.items())

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

    @classmethod
    def format_css_classes_list(cls, res: list) -> list:
        css_classes = []
        for i in res:
            for j in i:
                if j.startswith("pct"):
                    j = f"pct\:{j.split(':')[-1]}"
                css_classes.append(f".{j}")
        return css_classes

    @classmethod
    def collect_html_css_classes(cls):
        from bs4 import BeautifulSoup as BSoup
        with open("main.html", "r") as opened_file:
            file_string = opened_file.read()
            opened_file.close()
            # print(file_string)
            res = [each.get("class") for each in BSoup(file_string, features="html.parser").find_all()]
            cleaned_list = cls.clean_css_list(res)
            print(cls.format_css_classes_list(cleaned_list))
            # print(set(cls.format_css_classes_list(cleaned_list)))
            # find_all(name=["div", "section"], attrs=["class", "className"])
            # print(res, end="")
            return cls.format_css_classes_list(cleaned_list)

    @classmethod
    def write_watched_css_file(cls, res):
        watched_css_file_name: str = "watched_eye.css"
        with open(watched_css_file_name, "w+") as opened_file:
            opened_file.write("""
            * {
                --webkit-box-sizing: border-box; --moz-box-sizing: border-box; box-sizing: border-box;
                text-rendering: auto;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: antialiased; /* | grayscale*/
            }
            """)
            for each_style_property in res:
                opened_file.writelines(each_style_property)
            opened_file.close()


EyeWatcher.collect_html_css_classes()
EyeWatcher().parse_eye_css()
