from fastapi import APIRouter
from fastapi import WebSocket

from app.services.notification_service import (
    send_push_notification
)

from datetime import (
    datetime,
    timedelta,
)

import asyncio
import random

router = APIRouter()

# Notification cooldown

notification_cooldowns = {}

# Equipment list

equipment_list = [

    {
        "name": "Tank Engine T9",
        "type": "Tank",
    },

    {
        "name": "Radar RX-7",
        "type": "Radar",
    },

    {
        "name": "Drone Falcon-X",
        "type": "Drone",
    },

    {
        "name": "Generator GX-200",
        "type": "Generator",
    },

    {
        "name": "Weapon System W-99",
        "type": "Weapon System",
    },

    {
        "name": "Communication Hub C1",
        "type": "Communication",
    },

    {
        "name": "Surveillance Camera S-12",
        "type": "Surveillance",
    },
]

# Notification cooldown check

def can_send_notification(

    key: str,

    cooldown_minutes: int = 5,
):

    now = datetime.now()

    if key not in notification_cooldowns:

        notification_cooldowns[key] = now

        return True

    last_sent = notification_cooldowns[key]

    if now - last_sent > timedelta(
        minutes=cooldown_minutes
    ):

        notification_cooldowns[key] = now

        return True

    return False

@router.websocket(
    "/ws/live-monitor/{equipment_type}"
)
async def websocket_endpoint(

    websocket: WebSocket,

    equipment_type: str,
):

    await websocket.accept()
    
    print("TEST NOTIFICATION TRIGGERED")

    send_push_notification(

    title="SENTINELOPS TEST",

    body="Push notification working",
)

    health = 100

    battery_level = 100

    equipment = next(

        (
            item for item in equipment_list

            if item["type"] ==
               equipment_type
        ),

        equipment_list[0],
    )

    while True:

        metrics = {}

        # Tank metrics

        if equipment_type == "Tank":

            metrics = {

                "Engine Temperature":
                    f"{random.randint(75, 100)} °C",

                "Fuel Pressure":
                    f"{random.randint(50, 80)} PSI",

                "RPM":
                    f"{random.randint(2500, 4500)}",

                "Vibration":
                    f"{round(random.uniform(4, 8), 2)}",
            }

        # Radar metrics

        elif equipment_type == "Radar":

            metrics = {

                "Signal Strength":
                    f"{random.randint(60, 100)} %",

                "Heat Level":
                    f"{random.randint(40, 65)} °C",

                "Rotation Speed":
                    f"{random.randint(1000, 3000)} RPM",

                "Voltage":
                    f"{random.randint(210, 240)} V",
            }

        # Drone metrics

        elif equipment_type == "Drone":

            battery_level -= random.uniform(
                0.5,
                3,
            )

            if battery_level < 5:

                battery_level = 100

            metrics = {

                "Battery Level":
                    f"{round(battery_level, 1)} %",

                "Motor Vibration":
                    f"{round(random.uniform(2, 5), 2)}",

                "GPS Signal":
                    random.choice([

                        "Strong",

                        "Medium",

                        "Weak",
                    ]),

                "Altitude Stability":
                    random.choice([

                        "Stable",

                        "Medium",

                        "Unstable",
                    ]),
            }

        # Generator metrics

        elif equipment_type == "Generator":

            metrics = {

                "Output Voltage":
                    f"{random.randint(220, 260)} V",

                "Engine Heat":
                    f"{random.randint(75, 105)} °C",

                "Fuel Level":
                    f"{random.randint(20, 100)} %",

                "Load Capacity":
                    f"{random.randint(40, 100)} %",
            }

        # Weapon system metrics

        elif equipment_type == "Weapon System":

            metrics = {

                "Barrel Temperature":
                    f"{random.randint(80, 110)} °C",

                "Fire Readiness":
                    random.choice([

                        "Ready",

                        "Standby",

                        "Reloading",
                    ]),

                "Recoil Vibration":
                    f"{round(random.uniform(5, 9), 2)}",

                "Power Consumption":
                    f"{random.randint(230, 280)} V",
            }

        # Communication metrics

        elif equipment_type == "Communication":

            metrics = {

                "Network Strength":
                    f"{random.randint(50, 100)} %",

                "CPU Usage":
                    f"{random.randint(20, 95)} %",

                "Temperature":
                    f"{random.randint(45, 95)} °C",

                "Signal Delay":
                    f"{random.randint(1, 10)} ms",
            }

        # Surveillance metrics
        elif equipment_type == "Surveillance":

            metrics = {

              "Camera Temperature":
                 f"{random.randint(55, 110)} °C",

               "Storage Usage":
                 f"{random.randint(50, 100)} %",

               "Motor Vibration":
                 f"{round(random.uniform(3, 9), 2)}",

                "Power Load":
                 f"{random.randint(80, 160)} V",

                "Lens Status":
                 random.choice([

                "Clear",

                "Dust Detected",

                "Blurred",
                 ]),
              }

        health -= random.uniform(
            0.5,
            2,
        )

        if health < 0:

            health = 100

        status = "Healthy"

        if health < 70:

            status = "Warning"

        if health < 40:

            status = "Critical"

        # Push alert logic

        try:

            # Tank alerts

            if equipment_type == "Tank":

                temperature = int(

                    metrics[
                        "Engine Temperature"
                    ].replace(
                        " °C",
                        "",
                    )
                )

                vibration = float(

                    metrics[
                        "Vibration"
                    ]
                )

                pressure = int(

                    metrics[
                        "Fuel Pressure"
                    ].replace(
                        " PSI",
                        "",
                    )
                )

                if (

                    temperature >= 95

                    and can_send_notification(
                        "tank_overheat"
                    )
                ):

                    send_push_notification(

                        title=
                        "Critical Tank Alert",

                        body=
                        f"{equipment['name']} overheating detected",
                    )

                elif (

                    vibration >= 7

                    and can_send_notification(
                        "tank_vibration"
                    )
                ):

                    send_push_notification(

                        title=
                        "Tank Vibration Warning",

                        body=
                        f"{equipment['name']} abnormal vibration detected",
                    )

                elif (

                    pressure <= 55

                    and can_send_notification(
                        "tank_pressure"
                    )
                ):

                    send_push_notification(

                        title=
                        "Fuel Pressure Alert",

                        body=
                        f"{equipment['name']} fuel pressure dropping",
                    )

            # Radar alerts

            elif equipment_type == "Radar":

                heat = int(

                    metrics[
                        "Heat Level"
                    ].replace(
                        " °C",
                        "",
                    )
                )

                voltage = int(

                    metrics[
                        "Voltage"
                    ].replace(
                        " V",
                        "",
                    )
                )

                if (

                    heat >= 60

                    and can_send_notification(
                        "radar_heat"
                    )
                ):

                    send_push_notification(

                        title=
                        "Radar Heat Warning",

                        body=
                        f"{equipment['name']} heat level critical",
                    )

                elif (

                    voltage <= 215

                    and can_send_notification(
                        "radar_voltage"
                    )
                ):

                    send_push_notification(

                        title=
                        "Radar Voltage Alert",

                        body=
                        f"{equipment['name']} voltage instability detected",
                    )

            # Drone alerts

            elif equipment_type == "Drone":

                battery = float(

                    metrics[
                        "Battery Level"
                    ].replace(
                        " %",
                        "",
                    )
                )

                vibration = float(

                    metrics[
                        "Motor Vibration"
                    ]
                )

                if (

                    battery <= 20

                    and can_send_notification(
                        "drone_battery"
                    )
                ):

                    send_push_notification(

                        title=
                        "Drone Battery Critical",

                        body=
                        f"{equipment['name']} battery extremely low",
                    )

                elif (

                    vibration >= 4.5

                    and can_send_notification(
                        "drone_vibration"
                    )
                ):

                    send_push_notification(

                        title=
                        "Drone Vibration Alert",

                        body=
                        f"{equipment['name']} motor instability detected",
                    )

        except Exception as e:

            print(
                "Push Notification Error:",
                e,
            )

        # Final websocket response

        data = {

            "equipment":
                equipment["name"],

            "category":
                equipment["type"],

            "metrics":
                metrics,

            "health_score":
                round(health, 1),

            "status":
                status,
        }

        try:

            await websocket.send_json(
                    data
                )

        except Exception as e:

            print(
        "WebSocket send error:",
        str(e)
            )

            break

        await asyncio.sleep(2)