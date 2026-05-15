import firebase_admin

from firebase_admin import (
    credentials,
    messaging,
)

# INITIALIZE FIREBASE

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase/serviceAccountKey.json"
    )

    firebase_admin.initialize_app(
        cred
    )


def send_push_notification(

    title: str,

    body: str,
):

    message = messaging.Message(

        notification=
        messaging.Notification(

            title=title,

            body=body,
        ),

        topic="sentinelops_alerts",
    )

    response = messaging.send(
        message
    )

    print(
        "Notification sent:",
        response
    )