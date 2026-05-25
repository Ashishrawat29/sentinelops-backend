import threading

import firebase_admin

from firebase_admin import (
    credentials,
    messaging,
    exceptions as fb_exceptions,
)

from google.cloud import firestore

# INITIALIZE FIREBASE

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase/serviceAccountKey.json"
    )

    firebase_admin.initialize_app(
        cred
    )

db = firestore.Client.from_service_account_json(
    "firebase/serviceAccountKey.json"
)


def send_push_notification(

    title: str,

    body: str,
):

    def send():

        try:

            tokens_ref = db.collection(
                "device_tokens"
            ).stream()

            for token_doc in tokens_ref:

                token_data = token_doc.to_dict()

                token = token_data.get(
                    "token"
                )

                if not token:

                    continue

                try:

                    message = messaging.Message(

                        notification=
                        messaging.Notification(

                            title=title,

                            body=body,
                        ),

                        token=token,
                    )

                    response = messaging.send(
                        message
                    )

                    print(
                        "Notification sent:",
                        response
                    )

                except (
                    messaging.UnregisteredError,
                    fb_exceptions.NotFoundError,
                ):

                    # Stale token — remove from Firestore so we stop retrying it.
                    try:

                        token_doc.reference.delete()

                        print(
                            "Removed stale token:",
                            token_doc.id,
                        )

                    except Exception as delete_error:

                        print(
                            "Failed to remove stale token:",
                            str(delete_error),
                        )

                except Exception as token_error:

                    print(
                        "Token send error:",
                        str(token_error),
                    )

        except Exception as e:

            print(
                "FCM ERROR:",
                str(e),
            )

    threading.Thread(
        target=send
    ).start()
