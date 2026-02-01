from django.db import models
from django.conf import settings

#User (built in)

class Device(models.Model):
    device_uid = models.CharField(max_length=64, unique=True)
    secret_key = models.CharField(max_length=128)
    name = models.CharField(max_length=100, default="Smart Light")
    last_seen_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Schedule(models.Model):
    class Action(models.TextChoices):
        ON = "ON", "On"
        OFF = "OFF", "Off"
        SET_BRIGHTNESS = "BRIGHTNESS", "Set brightness"

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="schedules")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name="created_schedules")
    start_time = models.DateTimeField()
    action_type = models.CharField(max_length=16, choices=Action.choices)
    brightness = models.PositiveSmallIntegerField(null=True, blank=True)
    enabled = models.BooleanField(default=True) #allows for disabling a schedule without deleting it
    executed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["device", "start_time", "enabled"])]

class LogEvent(models.Model):
    class EventType(models.TextChoices):
        CMD_SENT = "cmd_sent", "Command sent"
        CMD_APPLIED = "cmd_applied", "Command applied"
        SCHEDULE_TRIGGERED = "schedule_triggered", "Schedule triggered"
        ERROR = "error", "Error"

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name="log_events")
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="log_events")
    event_type = models.CharField(max_length=32, choices=EventType.choices)
    details = models.JSONField(default=dict, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["device", "timestamp"]),
            models.Index(fields=["event_type", "timestamp"]),
        ]

class PowerReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="power_readings")
    timestamp = models.DateTimeField()

    voltage = models.FloatField(default=120)
    current = models.FloatField()
    power = models.FloatField(null=True, blank=True)
    energy_total = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=["device", "timestamp"])]
        unique_together = [("device", "timestamp")]