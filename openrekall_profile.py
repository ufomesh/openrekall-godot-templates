# OpenRekall: урезанный шаблон экспорта Godot 4.7.2 (только то, что нужно игре)
target = "template_release"
production = "yes"
debug_symbols = "no"
optimize = "size"
deprecated = "no"
minizip = "no"
accesskit = "no"
# рендер: только Compatibility (OpenGL 3.3)
vulkan = "no"
d3d12 = "no"
winrt = "no"
opengl3 = "yes"
# движок: только 2D, без физики, навигации, XR, сложных GUI
disable_3d = "yes"
disable_advanced_gui = "yes"
disable_physics_2d = "yes"
disable_physics_3d = "yes"
disable_navigation_2d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"
# модули: всё выключено, кроме нужных
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"
module_text_server_fb_enabled = "yes"   # текст без ICU (запасной шрифт на экране «нет ROM»)
module_freetype_enabled = "yes"         # запасной шрифт Godot (woff2 → нужен brotli, он по умолчанию включён)
module_webp_enabled = "yes"             # импортированные PNG в .pck хранятся как WebP lossless
