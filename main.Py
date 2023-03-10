import locale

from Langues.LangueAnglaise import LangueAnglaise
from Langues.LangueFrancaise import LangueFrancaise
from Langues.LangueLingala import LangueLinagala
from Ohce import Ohce
from PeriodeDeLaJournee import PeriodeDeLaJournee


class SystemLangAdapter():
    def __init__(self):
        langue_systeme = locale.getdefaultlocale()[0]
        self.__langue = LangueAnglaise() \
            if langue_systeme == "en_GB" \
            else LangueFrancaise()
            # else LangueLingala() 
            

if __name__ == '__main__':
    ohce = Ohce(SystemLangAdapter(), PeriodeDeLaJournee.NUIT)