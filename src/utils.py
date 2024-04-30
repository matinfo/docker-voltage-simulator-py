from datetime import datetime
import random
import pytz

def get_date_time_now():
    # Obtenir la date et l'heure actuelles au format YYYY-MM-DD HH:MM:SS
    europeTz = pytz.timezone("Europe/Zurich") 
    timeNow = datetime.now(europeTz)
    return timeNow.strftime("%Y-%m-%d %H:%M:%S")

def generate_fake_values_v():
    # Générer des valeurs de tension aléatoires entre 0 et 200V pour chaque phase
    L1 = random.uniform(0, 200)
    L2 = random.uniform(0, 200)
    L3 = random.uniform(0, 200)
    return {'L1': L1, 'L2': L2, 'L3': L3}

def generate_fake_values_a():
    # Générer des valeurs d'ampérage aléatoires entre 0 et 50A pour chaque phase
    L1 = random.uniform(0, 50)
    L2 = random.uniform(0, 50)
    L3 = random.uniform(0, 50)
    return {'L1': L1, 'L2': L2, 'L3': L3}


def get_values():
  pv_efficiency_percent = 0.9

  # Génération de valeurs aléatoires de tension et d'ampérage
  tension_values = generate_fake_values_v()
  ampere_values = generate_fake_values_a()

  # Affichage de la date et de l'heure actuelles
  refresh_timer = get_date_time_now()

  # Calcul de la puissance actuelle
  power_acw = (tension_values['L1'] * ampere_values['L1'] +
              tension_values['L2'] * ampere_values['L2'] +
              tension_values['L3'] * ampere_values['L3'])

  # Affichage des valeurs pour chaque phase
  # L1
  pw_v1 = tension_values['L1'] / pv_efficiency_percent
  pw_a1 = ampere_values['L1'] / pv_efficiency_percent
  
  output_v1 = tension_values['L1']
  output_w1 = tension_values['L1'] * ampere_values['L1']

  # L2
  pw_v2 = tension_values['L2'] / pv_efficiency_percent
  pw_a2 = ampere_values['L2'] / pv_efficiency_percent
  
  output_v2 = tension_values['L2']
  output_w2 = tension_values['L2'] * ampere_values['L2']

  # L3
  pw_v3 = tension_values['L3'] / pv_efficiency_percent
  pw_a3 = ampere_values['L3'] / pv_efficiency_percent
  
  output_v3 = tension_values['L3']
  output_w3 = tension_values['L3'] * ampere_values['L3']

  return {
      'time': refresh_timer,
      'power': '%.2f' % round(power_acw,2),
      'pw_v1': '%.2f' % round(pw_v1,2),
      'pw_a1': '%.2f' % round(pw_a1,2),
      'output_v1': '%.2f' % round(output_v1,2),
      'output_w1': '%.2f' % round(output_w1,2),
      'pw_v2': '%.2f' % round(pw_v2,2),
      'pw_a2': '%.2f' % round(pw_a2,2),
      'output_v2': '%.2f' % round(output_v2,2),
      'output_w2': '%.2f' % round(output_w2,2),
      'pw_v3': '%.2f' % round(pw_v3,2),
      'pw_a3': '%.2f' % round(pw_a3,2),
      'output_v3': '%.2f' % round(output_v3,2),
      'output_w3': '%.2f' % round(output_w3,2)
  }
