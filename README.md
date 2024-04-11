# Everforest Theme

![img](examples/editor%20with%20viewport%20and%20shader.png)

## Full Everforest Theme for Godot Engine

Complete Everforest theme overhaul for the [Godot Game Engine](https://github.com/godotengine) including icons and built in code editor based on the [Everforest theme](https://github.com/sainnhe/everforest-vscode) for VSCode by [sainnhe](https://github.com/sainnhe)

## How to use

The theme has several components. The Godot editor is built with Godot so you can apply normal .res themes to it. The everforest_theme.res file will cover most of the changes needed but isn't capable of handling certain elements such as the icons (which is what the Python script is for) and the code editor (which is what the Everforest-Dark-Medium.tet is for). Due to the way Godot handles the icons you'll have to build the engine from source if you want to use the custom icons but if you don't want to do that you can still use the editor theme and text editor theme.

### Applying the .res theme file

This is the easiest step. Simply click on Editor -> Editor Settings in the file menu then under Interface in the General settings tab click on Theme and at the bottom you'll find a Custom Theme option. Click on the folder icon and navigate to wherever you saved the .res file and click on it and it will apply the theme.
![img](examples/add%20theme.png)

### Applying the text editor theme

For this we'll have to copy the Everforest-Dark-Medium.tet file to the folder Godot keeps the text editor themes in. For Windows this should be C:\Users\YourUserName\AppData\Roaming\Godot\text_editor_themes Once copied there you will go back to Editor -> Editor Settings and scroll down the lefthand menu tree until you find the Theme option under Text Editor in the Genral tab and click it. The first element should be Color Theme and if you click the dropdown for it Everforest-Dark-Medium should show up in the list. Click on it and the theme will be applied.

![img](examples/add%20text%20editor%20theme.png)

### Applying Icons

