<img src="assets\EYE_CSS_ICON.png" width="256" height="256" title="Eye CSS icon" alt="This is Eye CSS Official Icon. It is displayed in Eye CSS official github repo."/>

# EYE CSS

Eye css is a **dynamic utility-first css library written in python** which aims to be usable across every design project.
It is similar to tailwind css.

Eye css is a dynamic and powerful css library to create truly dynamic styles while still simple to use and learn.

Eye css is responsive, dynamic, detailed and familiar. Similar to tailwind css in both syntax and operation.

[//]: # (The **utility-first** syntax you are used to is available in eye css with additional features.)

Eye css can be used in small and large web projects. Eye css can be used with your single static html file, to dynamic
large web projects.

[//]: # (Eye css is a truly dynamic css library. With support for almost all tailwind css properties, eye.css gives you extra )

[//]: # (flexibility and dynamism. )

[//]: # (Eye css works similar to tailwind css. Eye css watches your *.html, *.js, *.jsx, *.ts, *.tsx files)

[//]: # (for defined css styles which it creates for you on the fly.)

[//]: # ()

[//]: # (Though Eye css library is written in python, it can work with your existing web projects. Whether Angular, react, vue,)

[//]: # (svelte, etc.)

[//]: # (Once you have a python interpreter, Eye css works.)

[//]: # (Eye css works on all platform, windows, mac, linux.)

Just download Eye css or install Eye css and let **Eye** watch your defined files for defined styles.

It's as simple as that.

## How to use eye css:

### Installation

```commandline
pip install eye-css
```

#### Create an eye_config.yml file and add the following:

```yaml
eye:
  input_directory: "./"
  input_extensions: "*.html"

  exclude_directory: ".git"
  exclude_files: ".gitignore"
```

_**Remember to name the file: eye_config.yml**_

#### To use it with a single javascript file or your favorite javascript library:

```yaml
eye:
  input_directory: "./"
  input_extensions: "*.html,*.js,*.jsx,*.ts,*.tsx"

  exclude_directory: ".git"
  exclude_files: ".gitignore"

  output_name: "watched_eye.css"
```
Note that there is no space when adding file extensions in input_extensions.

Note that there is not space between the file extensions to parse
Next, Add "watched_eye.css" to the head tag of your base html file.

```html
<link rel="stylesheet" href="watched_eye.css"/>
```

Once installed,
run the following command in your terminal

```commandline
python -m eye_css "path to eye_config.yml"
```

Eye css will automatically watch and style your file once you make changes to the defined extensions from
eye_config.yml.

_Note: eye css will not automatically reload your browser or web page on file change,
it leaves that functionality to existing implementation of such. Examples: **htmx, angular, react, vue, svelte and other 
existing web frameworks**._

[//]: # ()

[//]: # ([//]: # &#40;<img alt="Proudly Nigeria" height="24px" src="https://img.shields.io/badge/proudly-Nigerian-008751.svg?style=flat&labelColor=FFFFFF" title="Proudly Nigerian Image" width="auto"/>&#41;)

[//]: # ()

[//]: # ()

[//]: # ([//]: # &#40;HOW EYE CSS WORKS&#41;)

[//]: # (EYE.css parsing follows a defined approach for proper, effective and desirable result.)

[//]: # (The Order of Precedence for declaring inline-css is:)

[//]: # ()

[//]: # (_**`.media-queries:pseudo-classes:pseudo-selectors:bare-css-classes`**_)

[//]: # ()

[//]: # (**Example:**)

[//]: # ()

[//]: # (* **.sm:placeholder:hover:color-blue**)

[//]: # (* **.md:after:hover:bg-light**)

[//]: # (* **.md:placeholder:focus:pct:w-100**)

[//]: # (* **.lg:pct:w-100**)

[//]: # ()

[//]: # ()

[//]: # ([//]: # &#40;JULY 25, 2022.&#41;)

[//]: # ()

[//]: # (## The First Dynamic CSS Framework.)

[//]: # ()

[//]: # (It checks, It Parses, It creates your css files.)

[//]: # ()

[//]: # (Just declare the css-strings. Leave the rest to eye.)

[//]: # ()

[//]: # (How it works.)

[//]: # ()

[//]: # ()

[//]: # (## Understanding when to use pipe in pseudo-base-css-classes.)

[//]: # ([//]: # &#40;- August 16, 2022.&#41;)

[//]: # (To use pipe in pseudo-base-css-classes means a new complete property of the defined style is being parsed.)

[//]: # (e.g., )

[//]: # (1. **transform:translate-x-15px|rotate-z-30deg|perspective-35px**; means translate-x-15px is a complete property of transform pseudo-base-css-class)

[//]: # (2. **shadow:10px-3px-4px-ABCDEB|-15px--3px-8px-2px-yellowgreen|inset-3px--4px-14px-12px-E7E7E7**; means that 10px-3px-4px-ABCDEF is a complete box-shadow property,-15px--3px-8px-2px-yellowgreen is another complete box-shadow property, and so on.)

[//]: # (3. **conic-gradient:red_0deg-_orange_90deg-_yellow_180deg-_green_270deg-_blue_360deg**; means that **red_0deg-_orange_90deg-_yellow_180deg-_green_270deg-_blue_360deg** is a complete conic-gradient property and so on.)

[//]: # (4. **transition:width_2s_linear_1s|height_2s|background-color_4s_ease-in-out_3s** means that width_2s is a complete transition property i.e., **transition: width 2s linear 1s, height 2s, background-color 4s ease-in-out 3s;**)
