from instagrambot import InstagramBot

account = 'Account'

instaBot = InstagramBot()
instaBot.login()
instaBot.find_followers(account)
instaBot.follow()

instaBot.driver.quit()
