from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField


class TimerSettingsForm(FlaskForm):
    bounty_warn = BooleanField('Bounty Rune', default=False)
    bounty_pre_time = IntegerField(default=0)
    bounty_sound = BooleanField(default=False)
    power_rune_warn = BooleanField(default=False)
    power_rune_pre_time = IntegerField(default=0)
    power_rune_sound = BooleanField(default=False)
    double_power_rune_warn = BooleanField(default=False)
    double_power_rune_pre_time = IntegerField(default=0)
    double_power_rune_sound = BooleanField(default=False)
    day_night_warn = BooleanField(default=False)
    day_night_pre_time = IntegerField(default=0)
    day_night_sound = BooleanField(default=False)
    catapult_wave_warn = BooleanField(default=False)
    catapult_wave_pre_time = IntegerField(default=0)
    catapult_wave_sound = BooleanField(default=False)
    creep_wave_number_warn = BooleanField(default=False)
    creep_wave_number_pre_time = IntegerField(default=0)
    creep_wave_number_sound = BooleanField(default=False)
    creep_wave_power_warn = BooleanField(default=False)
    creep_wave_power_pre_time = IntegerField(default=0)
    creep_wave_power_sound = BooleanField(default=False)
    submit = SubmitField('Apply')
