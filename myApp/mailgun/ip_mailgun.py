import requests

# Sending e-mail
def send_email():
    return requests.post(
            "https://api.mailgun.net/v3/sandboxd13de7857b744ce1872cea0b767eeb12.mailgun.org/messages",
            auth=("api", "key-3d3d6b97bec40a2d401864e20179a949"),
            data={
                "from": "Raspberry Pi <disk012@ajou.ac.kr>",
                "to": ["dis012@ajou.ac.kr"],
                "subject": "[Announcement] Raspberry Pi IP Address",
                "text": "test"
                }
            )

if __name__ == "__main__":
    send_email()

