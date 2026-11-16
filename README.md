# Сборка урезанных шаблонов экспорта Godot для OpenRekall

Здесь только профиль сборки (`openrekall_profile.py`) и сценарий GitHub Actions — ни кода, ни данных игры.
Шаблон для macOS собирается на маке GitHub: Actions → «macOS template» → Run workflow (тег Godot — как у
редактора). Результат — артефакт `macos.zip` (Intel + Apple Silicon); в пресете macOS: Custom Template → Release.
Шаблон для Windows собирается без Mac — см. `_tools/template/README.md` в проекте.
