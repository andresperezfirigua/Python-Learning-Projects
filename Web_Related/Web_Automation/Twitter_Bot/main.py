from twitterbot import TwitterBot

PROMISED_UP = 200
PROMISED_DOWN = 100

twitterbot = TwitterBot()
twitterbot.get_internet_speed()

if abs(PROMISED_DOWN - twitterbot.down) > 20 or abs(PROMISED_UP - twitterbot.up) > 20:
    twitterbot.tweet_at_provider(PROMISED_DOWN, PROMISED_UP)

twitterbot.driver.quit()
