from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee

class Linagala:
    def dire_bonjour(self, periodeDelajournee):
        match periodeDelajournee:
            case PeriodeDeLaJournee.MATIN:
                return Constantes.Lingala.TONGO_MALAMU
            case PeriodeDeLaJournee.APRES_MIDI:
                return Constantes.Lingala.MOYI_MALAMU
            case PeriodeDeLaJournee.SOIR:
                return Constantes.Lingala.POKWA_MALAMU
            case PeriodeDeLaJournee.NUIT:
                return Constantes.Lingala.BOUTOU_MALAMU
            
        return Constantes.Lingala.MBOTE
    
    def bien_dit(self):
        return Constantes.Lingala.OBETI_MALAMU
    