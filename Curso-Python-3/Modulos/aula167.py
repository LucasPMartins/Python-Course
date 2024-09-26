# locale pra internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/
# international/get-winsystemlocale?view=windowsserver2022
# -ps&viewFallbackFrom=win10-p
import calendar
import locale

# locale.setlocale(locale.LC_ALL, '') #locale do sistema do OS
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') #locale do Brasil com utf8

print(calendar.calendar(2024))
print(locale.getlocale())