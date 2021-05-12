from util import get_string_user_account
from discord_webhook import DiscordWebhook

def send_webhooks(config, user_accounts):
  for url_webhook in config['webhooks_urls']:
    for user_account in user_accounts:
      message = get_string_user_account(user_account)
      webhook = DiscordWebhook(url=url_webhook, content=message)
      webhook.execute()
