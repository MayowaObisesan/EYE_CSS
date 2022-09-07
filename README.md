# EYE_CSS
For design Perfectionist.
#### Hi, This is Eye CSS Official Repository.


Eye.css is a utility-first css library which aims to be usable across every design project.
It is similar to tailwind in its approach.

Eye.css is responsive, dynamic, detailed and makes available every utility-style approach you are used to and even more.
Eye.css needs no npm to work, and certainly needs no external library.
Once you have a python interpreter, eye.css works.

Just download eye package and let **Eye** watch your defined files for defined styles.

It's as simple as that.



[//]: # (<img alt="Proudly Nigeria" height="24px" src="https://img.shields.io/badge/proudly-Nigerian-008751.svg?style=flat&labelColor=FFFFFF" title="Proudly Nigerian Image" width="auto"/>)


[//]: # (HOW EYE CSS WORKS)
EYE.css parsing follows a defined approach for proper, effective and desirable result.
The Order of Precedence for declaring inline-css is:

_**`.media-queries:pseudo-classes:pseudo-selectors:bare-css-classes`**_

**Example:**

* **.sm:placeholder:hover:color-blue**
* **.md:after:hover:bg-light**
* **.md:placeholder:focus:pct:w-100**
* **.lg:pct:w-100**


[//]: # (JULY 25, 2022.)

## The First Dynamic CSS Framework.

It checks, It Parses, It creates your css files.

Just declare the css-strings. Leave the rest to eye.

How it works.


## Understanding when to use pipe in pseudo-base-css-classes.
[//]: # (- August 16, 2022.)
To use pipe in pseudo-base-css-classes means a new complete property of the defined style is being parsed.
e.g., 
1. **transform:translate-x-15px|rotate-z-30deg|perspective-35px**; means translate-x-15px is a complete property of transform pseudo-base-css-class
2. **shadow:10px-3px-4px-ABCDEB|-15px--3px-8px-2px-yellowgreen|inset-3px--4px-14px-12px-E7E7E7**; means that 10px-3px-4px-ABCDEF is a complete box-shadow property,-15px--3px-8px-2px-yellowgreen is another complete box-shadow property, and so on.
3. **conic-gradient:red_0deg-_orange_90deg-_yellow_180deg-_green_270deg-_blue_360deg**; means that **red_0deg-_orange_90deg-_yellow_180deg-_green_270deg-_blue_360deg** is a complete conic-gradient property and so on.
4. **transition:width_2s_linear_1s|height_2s|background-color_4s_ease-in-out_3s** means that width_2s is a complete transition property i.e., **transition: width 2s linear 1s, height 2s, background-color 4s ease-in-out 3s;**