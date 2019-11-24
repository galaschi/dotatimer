from flask import render_template, url_for, redirect
from datetime import datetime, timedelta
from timerapp.forms import TimerSettingsForm
from timerapp import app


seconds = [item for item in range(0, 7201)]


class TimerOptions:
    rules = {}
    message = []
    bounty_warn = [False, 0, False]
    power_rune_warn = [False, 0, False]
    double_power_rune_warn = [False, 0, False]
    day_night_warn = [False, 0, False]
    catapult_wave_warn = [False, 0, False]
    creep_wave_number_warn = [False, 0, False]
    creep_wave_power_warn = [False, 0, False]


@app.route("/")
def timer_page():
    get_rules()
    return render_template('timer.html', TimerOptions=TimerOptions)


@app.route("/settings", methods=['GET', 'POST'])
def timer_settings_page():
    form = TimerSettingsForm()
    if form.validate_on_submit():
        TimerOptions.bounty_warn = [form.bounty_warn.data, form.bounty_pre_time.data, form.bounty_sound.data]
        TimerOptions.power_rune_warn = [form.power_rune_warn.data, form.power_rune_pre_time.data, form.power_rune_sound.data]
        TimerOptions.double_power_rune_warn = [form.double_power_rune_warn.data, form.double_power_rune_pre_time.data, form.double_power_rune_sound.data]
        TimerOptions.day_night_warn = [form.day_night_warn.data, form.day_night_pre_time.data, form.day_night_sound.data]
        TimerOptions.catapult_wave_warn = [form.catapult_wave_warn.data, form.catapult_wave_pre_time.data, form.catapult_wave_sound.data]
        TimerOptions.creep_wave_number_warn = [form.creep_wave_number_warn.data, form.creep_wave_number_pre_time.data, form.creep_wave_number_sound.data]
        TimerOptions.creep_wave_power_warn = [form.creep_wave_power_warn.data, form.creep_wave_power_pre_time.data, form.creep_wave_power_sound.data]
        return redirect(url_for('timer_page'))
    return render_template('timer_settings.html', form=form, TimerOptions=TimerOptions)


def get_rules():
    check_bounty_rune(TimerOptions.bounty_warn)
    check_power_rune(TimerOptions.power_rune_warn)
    check_double_power_rune(TimerOptions.power_rune_warn)
    check_day_night(TimerOptions.day_night_warn)
    check_catapult_wave(TimerOptions.catapult_wave_warn)
    check_creep_wave_number(TimerOptions.creep_wave_number_warn)
    check_creep_wave_power(TimerOptions.creep_wave_power_warn)
    TimerOptions.rules['rules'] = TimerOptions.message


def check_bounty_rune(options):
    if options[0]:
        for sec in seconds:
            if sec % 300 == 0:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "A bounty is about to spawn"})
                TimerOptions.message.append({"time": sec, "message": "A bounty rune has spawned, it worths "+str((40+(sec/60)*2))})


def check_power_rune(options):
    if options[0]:
        for sec in seconds:
            if sec % 120 == 0 and sec >= 120:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "A power rune is about to spawn"})
                TimerOptions.message.append({"time": sec, "message": "A power rune has spawned"})


def check_double_power_rune(options):
    if options[0]:
        if options[1]:
            TimerOptions.message.append({"time": str(2400-options[1]), "message": "Now runes are spawning either TOP and BOT"})
        TimerOptions.message.append({"time": 2400, "message": "Now runes are spawning either TOP and BOT"})


def check_day_night(options):
    if options[0]:
        for sec in seconds:
            if sec % 300 == 0 and sec >= 300:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "The Day/Night is about to change"})
                TimerOptions.message.append({"time": sec, "message": "The Day/Night has changed"})


def check_catapult_wave(options):
    if options[0]:
        for sec in seconds:
            if sec % 300 == 0 and 300 <= sec < 2100:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "A siege creep is about to spawn"})
                TimerOptions.message.append({"time": sec, "message": "A siege creep has spawned"})
            if sec % 300 == 0 and sec >= 2100:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Two siege creeps are about to spawn"})
                TimerOptions.message.append({"time": sec, "message": "Two siege creeps has spawned"})


def check_creep_wave_number(options):
    if options[0]:
        for sec in seconds:
            if sec == 900:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Total number of creeps per wave is about to get increased"})
                TimerOptions.message.append({"time": sec, "message": "Now all lanes get +1 melee creep, total count of melee creeps is now 4 for all lanes."})
            if sec == 1800:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Total number of creeps per wave is about to get increased"})
                TimerOptions.message.append({"time": sec, "message": "Now all lanes get +1 melee creep. total count of melee creeps is now 5 for all lanes."})
            if sec == 2100:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Total number of creeps per wave is about to get increased"})
                TimerOptions.message.append({"time": sec, "message": "Now all lanes get +1 siege creep. total count of siege creeps is now 2 for all lanes."})
            if sec == 2400:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Total number of creeps per wave is about to get increased"})
                TimerOptions.message.append({"time": sec, "message": "Now all lanes get +1 ranged creep. Total count of ranged creeps is now 2 for all lanes."})
            if sec == 2700:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Total number of creeps per wave is about to get increased"})
                TimerOptions.message.append({"time": sec, "message": "Now all lanes get +1 melee creep. Total count of melee creeps is now 6 for all lanes."})


def check_creep_wave_power(options):
    if options[0]:
        for sec in seconds:
            if sec % 450 == 0 and sec >= 450:
                if options[1] > 0:
                    TimerOptions.message.append({"time": sec - options[1], "message": "Wave creeps are about to get stronger"})
                TimerOptions.message.append({"time": sec, "message": "Now every wave creep is stronger (Dmg and HP)"})


def check_roshan_spawn(roshan_spawn_warn, time):
    roshan_death_time = datetime.strptime('00:00', '%M:%S')
    if roshan_spawn_warn:
        if roshan_death_time > (time.minute == 0 and time.second == 0):
            aegis_claim_time = roshan_death_time + timedelta(minutes=5)
            return "Aegis will be claimed at:" + str(aegis_claim_time)


def check_aegis_claim(aegis_claim_warn, time):
    roshan_death_time = datetime.strptime('00:00', '%M:%S')
    if aegis_claim_warn:
        if roshan_death_time > (time.minute == 0 and time.second == 0):
            roshan_initial_spawn = roshan_death_time + timedelta(minutes=8)
            roshan_last_spawn = roshan_death_time + timedelta(minutes=11)
            return "Roshan will spawn between" + str(roshan_initial_spawn) + "and" + str(roshan_last_spawn)









