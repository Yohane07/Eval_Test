from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee

class Francaise:
    def dire_bonjour(self, periodeDelajournee):
        match periodeDelajournee:
            case PeriodeDeLaJournee.MATIN:
                return Constantes.Francais.BONJOUR
            case PeriodeDeLaJournee.APRES_MIDI:
                return Constantes.Francais.BON_APREM
            case PeriodeDeLaJournee.SOIR:
                return Constantes.Francais.BONSOIR
            case PeriodeDeLaJournee.NUIT:
                return Constantes.Francais.BONNE_NUIT
            
        return Constantes.Francais.SALUT
    
    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT
    