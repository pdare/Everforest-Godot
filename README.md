# :point_right: Everforest Theme :point_left:

![img](examples/editor%20with%20viewport%20and%20shader.png)
![img](examples/editor%20with%20text%20editor%20and%20output%20panel.png)

## Full Everforest Theme for Godot Engine

Complete Everforest theme overhaul for the [Godot Game Engine](https://github.com/godotengine) including icons and built in code editor based on the [Everforest theme](https://github.com/sainnhe/everforest-vscode) for VSCode by [sainnhe](https://github.com/sainnhe)

This is for Godot 4.x and will not work for 3.x versions and you will have to build the engine from source to utilize all theme colors

## How to use

The theme has several components. The Godot editor is built with Godot so you can apply normal `.res` themes to it. The `everforest_theme.res` file will cover most of the changes needed but isn't capable of handling certain elements such as the icons (which is what the Python script is for) and the code editor (which is what the `Everforest-Dark-Medium.tet` is for). Due to the way Godot handles the icons you'll have to build the engine from source if you want to use the custom icons but if you don't want to do that you can still use the editor theme and text editor theme.

### Applying the .tres theme file

This is the easiest step. Simply click on `Editor -> Editor Settings` in the file menu then under `Interface` in the `General` settings tab click on `Theme` and at the bottom you'll find a `Custom Theme` option. Click on the folder icon and navigate to wherever you saved the `.tres` file and click on it and it will apply the theme. You'll also have to change the `Base Color` to `7fbbb3` and `Accent Color` to `7fbbb3`. 
![img](examples/add%20theme.png)

### Applying the text editor theme

For this we'll have to copy the `Everforest-Dark-Medium.tet` file to the folder Godot keeps the text editor themes in, these folders are: 
- On Linux: `~/.config/godot/text_editor_themes/`
- On macOS: `~/Library/Application Support/Godot/text_editor_themes/`
- On Windows: `%APPDATA%\Godot\text_editor_themes\`
- If you installed Godot with Steam `steamapps/common/Godot Engine/editor_data/text_editor_themes/`
in your Steam installation folder.

Once copied there you will go back to `Editor -> Editor Settings` and scroll down the lefthand menu tree until you find the `Theme` option under `Text Editor` in the `Genral` tab and click it. The first element should be `Color Theme` and if you click the dropdown for it `Everforest-Dark-Medium` should show up in the list. Click on it and the theme will be applied.

If you need more help applying the text editor theme you can find the official Godot documentation on installing text editor themes [here](https://github.com/godotengine/godot-syntax-themes/tree/master)

![img](examples/add%20text%20editor%20theme.png)

### Applying Icons

To be able to do these steps you'll have to compile Godot from source as the icons are built into the executable at compile time. If you need help building from source the Godot project has a guide [here](https://docs.godotengine.org/en/stable/contributing/development/compiling/index.html) so I won't go over how to do this here.

Run SVGRecolor and enter the filepath to your Godot source directory. After this finishes running you'll have to recompile Godot and the new icon colors should be applied. If you'd rather not use the executable you can run main.py but you'll have to install the svg Python package for it to work.
**YOU MUST REBUILD AFTER RUNNING THE SCRIPT OR YOUR ICONS WILL NOT CHANGE.**

Thanks for using my theme conversion, hope you like it :grin::two_hearts::revolving_hearts::v: