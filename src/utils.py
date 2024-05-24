from datetime import datetime
import pytz
import numpy as np

def simulate_three_phase_pv_value(current_time, duration_hours=24, sample_rate_minutes=1, max_value=200):
    """
    Simulates the value of a three-phase photovoltaic (PV) panel over a 24-hour period from the given current time.

    Args:
    - current_time: Current datetime from which the simulation starts.
    - duration_hours: Total duration of the simulation in hours (default 24 hours).
    - sample_rate_minutes: Time interval between each value sample in minutes (default 1 minute).
    - max_value: Maximum value output of the PV panel during peak sunlight (default 40 volts).

    Returns:
    - values: Dictionary containing value arrays for each phase ('L1', 'L2', 'L3').
    """
    # Number of samples
    num_samples = duration_hours * (60 // sample_rate_minutes)

    # Simulate values as a function of time
    values = {
        'L1': np.zeros(num_samples),
        'L2': np.zeros(num_samples),
        'L3': np.zeros(num_samples)
    }
    
    # Define daylight hours (6 AM to 6 PM) in 24-hour format
    sunrise_hour = 6
    sunset_hour = 18
    daylight_duration = sunset_hour - sunrise_hour

    hour_of_day = current_time.hour + current_time.minute / 60.0
    if sunrise_hour <= hour_of_day <= sunset_hour:
        # Simulate values as sine functions with 120 degree phase shift
        angle_base = (hour_of_day - sunrise_hour) / daylight_duration * np.pi
        values['L1'] = (max_value / 2) * (1 + np.sin(angle_base))  # Shifted to [0, max_voltage]
        values['L2'] = (max_value / 2) * (1 + np.sin(angle_base + 2 * np.pi / 3))  # +120 degrees
        values['L3'] = (max_value / 2) * (1 + np.sin(angle_base - 2 * np.pi / 3))  # -120 degrees
    
    return values



def get_date_time_now():
    # Obtenir la date et l'heure actuelles au format YYYY-MM-DD HH:MM:SS
    europeTz = pytz.timezone("Europe/Zurich") 
    timeNow = datetime.now(europeTz)
    return timeNow.strftime("%Y-%m-%d %H:%M:%S")

def generate_fake_values_v(current_time):
    # Générer des valeurs de tension aléatoires entre 0 et 200V pour chaque phase
    values = simulate_three_phase_pv_value(current_time, duration_hours=24, sample_rate_minutes=1, max_value=200)
    return {'L1': values['L1'], 'L2': values['L2'], 'L3': values['L3']}

def generate_fake_values_a(current_time):
    # Générer des valeurs d'ampérage aléatoires entre 0 et 50A pour chaque phase
    values = simulate_three_phase_pv_value(current_time, duration_hours=24, sample_rate_minutes=1, max_value=50)
    return {'L1': values['L1'], 'L2': values['L2'], 'L3': values['L3']}


def get_values():
    pv_efficiency_percent = 0.9
    europe_tz = pytz.timezone("Europe/Zurich") 
    time_now = datetime.now(europe_tz)

    # Génération de valeurs aléatoires de tension et d'ampérage
    tension_values = generate_fake_values_v(time_now)
    ampere_values = generate_fake_values_a(time_now)

    # Affichage de la date et de l'heure actuelles
    refresh_timer = time_now.strftime("%Y-%m-%d %H:%M:%S")

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
