import emails
from emails.template import JinjaTemplate
from typing import Dict, Any
from pathlib import Path
import config


def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = "",
    environment: Dict[str, Any] = {},
) -> None:
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=(config.EMAILS_FROM_NAME, config.EMAILS_FROM_EMAIL),
    )
    environment["email"] = config.SMTP_USER
    smtp_options = {
        "host": config.SMTP_HOST,
        "port": config.SMTP_PORT,
        "ssl": config.SMTP_SSL,
        "user": config.SMTP_USER,
        "password": config.SMTP_PASSWORD
    }
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    print(f"status_code: {response.status_code}")


def send_magic_login_email(email_to: str, token: str) -> None:
    project_name = config.PROJECT_NAME
    subject = f"Вход в аккаунт"
    with open(Path(config.EMAIL_TEMPLATES_DIR) / "auth_template.html", encoding="utf-8") as f:
        template_str = f.read()
    server_host = config.SERVER_HOST
    link = f"{server_host}?magic={token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": config.PROJECT_NAME,
            "valid_minutes": int(config.ACCESS_TOKEN_EXPIRE_SECONDS / 60),
            "link": link,
        },
    )
