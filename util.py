TWITTER_BASE_URL = "https://twitter.com/"

# define if there is one element in list that contain input
def is_element_list_in_input(input, list):
  elem = input.lower()
  for str in list:
    if str in elem:
      return True
  return False

# join elements in list into a single string
def str_list_to_join_string(list):
  if len(list) == 0:
    return ""
  separator = '/'
  return separator.join(list)

# get string users account message
def get_string_user_accounts(user_accounts):
  message = ""
  for user_account in user_accounts:
    message = message + get_string_user_account(user_account)
  return message

def get_string_user_account(user_account):
  message = ''
  username = user_account.user_name
  message = message + "User: " + username + "\n"
  message = message + "Twitter Profile Link: " + TWITTER_BASE_URL + username + "\n"

  # adding website url if not empty
  website = user_account.url
  if "" != website:
    message = message + "Website: " + website + "\n"

  # adding keywords of tweets if not empty
  if len(user_account.keywords) > 0:
    message = message + "Keywords: " + str_list_to_join_string(user_account.keywords) + "\n"

  message = message + "Last Tweet \n" + user_account.last_tweet + "\n"
  message = message + "\n"
  return message

# get the usernames from tweet list without duplicate
def get_filtered_usernames_by_tweet_list(tweets, screen_name_must_contain):
  username_list = []
  for tweet in tweets:
    user_name = tweet.user.screen_name
    if is_element_list_in_input(user_name, screen_name_must_contain) and user_name not in username_list:
      username_list.append(user_name)
  return username_list

# define if a user is eligible for retrieving by his timeline
def is_user_eligible_for_retrieving(user_timeline, max_nb_retrieve):
  if len(user_timeline) > 0:
    nb_tweet = user_timeline[0].user.statuses_count
    return nb_tweet <= max_nb_retrieve
  return False
